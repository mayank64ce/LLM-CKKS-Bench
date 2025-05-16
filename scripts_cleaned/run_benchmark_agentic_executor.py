import argparse
import sys
sys.path.append('.')
from models import CodeLlama7B, DeepseekCoder, Llama3_3_70b
import logging
from transformers import set_seed
from utils.utils import parse_cpp_from_response, save_file_to_disk
from tools.compiler import Compiler
from tools.executor import Executor
# from tools.summary_rag import SummaryRetriever
import os
from prompts.prompts import BasePrompt
from pathlib import Path
from prompts.system_prompts import system_prompt_simple as system_prompt
from prompts import queries
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.usage import UsageLimits
from pydantic import BaseModel, Field, validator, model_validator, field_validator
from pydantic_ai import Agent, ModelRetry
from dotenv import load_dotenv
load_dotenv()
from prompts.system_prompts import system_prompt_agent as system_prompt
import logfire
from colorama import Fore
import time

# logfire.configure(send_to_logfire='if-token-present', token=os.getenv("LOGFIRE_TOKEN"))
logfire.configure(send_to_logfire='if-token-present')

import nest_asyncio
import random
nest_asyncio.apply()

agent_extras = """
Note:
1. DO NOT execute the program BEFORE compiling.
2. You will first compile the generated solution using compile_ckks tool.
3. If it compiles successfully, you will execute unit tests on it with the execute_ckks tool.
""".strip()

class CodeGenerationResult(BaseModel):
    code: str = Field(..., description="Final generated code")
    compile_success: bool = Field(False, description="True if code compiled")
    tests_passed: bool = Field(False, description="True if all tests passed")
    compile_errors: str | None = Field(None, description="Compiler errors")
    test_feedback: str | None = Field(None, description="Test failure details")

    # # 1. Ensure tests_passed=True only if compilation succeeded
    # @field_validator('tests_passed')
    # @classmethod
    # def validate_tests_passed(cls, v: bool, values) -> bool:
    #     if v and not values.data.get('compile_success'):
    #         raise ValueError("Tests cannot pass if compilation failed")
    #     return v

    # # 2. Ensure compile_errors exist only if compilation failed
    # @field_validator('compile_errors')
    # @classmethod
    # def validate_compile_errors(cls, v: str | None, values) -> str | None:
    #     if v and values.data.get('compile_success'):
    #         raise ValueError("Compile errors cannot exist if compilation succeeded")
    #     return v

    # 3. Enforce BOTH compilation and tests must pass for success
    @model_validator(mode='after')
    def validate_full_success(self) -> 'CodeGenerationResult':
        if not (self.compile_success and self.tests_passed):
            raise ValueError("Both compilation and tests must pass.")
        return self

def main():
    parser = argparse.ArgumentParser(description="Run TFHEEvaluator benchmark.")
    parser.add_argument("--model_name", type=str, required=True, help="Name of the model to benchmark.")
    parser.add_argument("--task_name", type=str, required=True, help="Name of the task to evaluate.")
    parser.add_argument("--run_id", type=int, required=True, help="Run ID (1-10).")
    parser.add_argument("--few_shot", action="store_true", help="Use few-shot examples.")
    parser.add_argument("--use_rag", action="store_true", help="Use RAG for retrieval.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("--num_keep", type=int, default=100, help="Maximum number of lat solutions to keep in context.") # 100 basically means keep all solutions
    parser.add_argument("--max_steps", type=int, default=10, help="Maximum number of steps to run.")
    parser.add_argument("--save_dir", type=str, default="logs", help="Directory to save results.")

    args = parser.parse_args()

    # here we have to decide the model

    model_settings = ModelSettings(
        temperature=0.7,
        max_tokens=1024,
        seed=args.run_id,
        parallel_tool_calls=False,
    )

    if args.model_name == "GPT-4o":
        model = 'openai:gpt-4o'
    elif args.model_name == "Llama3-3-70b":
        model = OpenAIModel(
        'meta-llama/llama-3.3-70b-instruct',
            provider=OpenAIProvider(
                base_url='https://openrouter.ai/api/v1',
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            # model_seed=args.run_id,
            # temperature=0.7,
            # max_tokens=1024,
        )
    elif args.model_name == "Deepseek-Chat":
        model = OpenAIModel(
        'deepseek/deepseek-chat',
            provider=OpenAIProvider(
                base_url='https://openrouter.ai/api/v1',
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            # model_seed=args.run_id,
            # temperature=0.7,
            # max_tokens=1024,
        )
    elif args.model_name == "Claude-3-5-Haiku":
        model = OpenAIModel(
        'anthropic/claude-3.5-haiku',
            provider=OpenAIProvider(
                base_url='https://openrouter.ai/api/v1',
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            # model_seed=args.run_id,
            # temperature=0.7,
            # max_tokens=1024,
        )
    else:
        raise ValueError(f"Model {args.model_name} not supported.")
    
    agent = Agent(
                model,
                output_type=CodeGenerationResult,
                instrument=True,
                retries=10,
                system_prompt=system_prompt,
                model_settings=model_settings,
                usage_limits=UsageLimits(request_limit=5, total_tokens_limit=26000)
            )

    folder_name = agent.model.model_name.split("/")[-1]

    compiler = Compiler(args=args)                         # here we have the compiler
    compiler.set_directory(f"{args.save_dir}/{args.task_name}/{folder_name}/{args.run_id}")

    tests_root = Path("./tests")
    executor = Executor(args=args, tests_root=tests_root)  # here we have the executor
    executor.set_executable_path(executable=f"{compiler.source_dir}/build/test")

    ########################################## COMPILER TOOL HERE ########################################################

    @agent.tool_plain
    def compile_ckks(code: str) -> tuple[bool, str]:
        """
        Compiles the provided C++ code for CKKS encryption with OpenFHE library.

        The code is saved to ./generated/solution.cpp and compiled.
        
        Args:
            code: The full C++ source code as a string.

        Returns:
            A tuple (success, stderr):
                success (bool): True if compilation succeeded, False otherwise.
                stderr (str): The compiler's error output, if any.
        """
        # Here we need to save this "code" at an appropriate location.
        # in this case the location will be "./generated/solution.cpp"
        # Then we call the compiler on it
        os.makedirs(compiler.source_dir, exist_ok=True)
        
        src_path = os.path.join(compiler.source_dir, "solution.cpp")
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(code) 

        result = compiler.compile()

        if result.returncode != 0:
            print(Fore.RED + "Compilation failed...")
            time.sleep(random.uniform(3.0, 7.0))
            raise ModelRetry(f"The generated solution produced the following compile error, please debug and fix it: {result.stderr}")

        print(Fore.GREEN + "The solution compiled successfully!!!!")
        time.sleep(random.uniform(3.0, 7.0))
        return (result.returncode == 0, result.stderr)
    
    ########################################## EXECUTOR TOOL HERE ########################################################
    @agent.tool_plain
    def execute_ckks():
        """
        Executes all unit tests for the current CKKS-based code using the executor tool.

        Runs the compiled code through a predefined set of unit tests and returns a success message
        if all tests pass. If any test fails, it raises a `ModelRetry` exception with detailed 
        feedback including the expected vs actual outputs and stderr logs for failed tests.

        Returns:
            str: A success message if all tests pass.

        Raises:
            ModelRetry: If one or more tests fail. The exception contains diagnostic feedback
            helpful for prompting an AI model to correct the code.|
        """
        passed, total, results = executor.run_all()

        if passed == total:
            time.sleep(random.uniform(3.0, 7.0))
            print(Fore.GREEN + "Awesome, all test cases passed.")
            return "Awesome, all test cases passed."
                
        feedback_lines = [
                        f"The code compiled but only {passed}/{total} tests passed. Please debug the code and return the corrected code."
        ]
        for idx, r in enumerate(results, start=1):
            if not r.passed:
                feedback_lines.append(
                    f"Test #{idx} failed:\n"
                    f"  Expected stdout: {repr(r.expected_stdout)}\n"
                    f"  Actual   stdout: {repr(r.stdout)}\n"
                    f"  stderr output : {repr(r.stderr)}"
                )
        print(Fore.RED + f"The code compiled but only {passed}/{total} tests passed.")
        feedback = "\n".join(feedback_lines)
        
        time.sleep(random.uniform(3.0, 7.0))
        raise ModelRetry(feedback)
    
    try:
        result = agent.run_sync(f"{queries[args.task_name]}\n{agent_extras}",)
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            sys.exit("0")
        elif isinstance(e, PermissionError):
            sys.exit("0")
        else:
            raise e


if __name__ == "__main__":
    main()
