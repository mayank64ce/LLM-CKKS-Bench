"""
Here we take 3 arguments:
1. Model name
2. Task name
3. using fewshot argument
4. using rag argument
"""

import argparse
import sys
sys.path.append(".")
from models import CodeLlama7B, DeepseekCoder, Llama3_3_70b, GPT_4o, Claude_3_5_Haiku, DeepseekChatV3
import logging
from transformers import set_seed
from utils.utils import parse_cpp_from_response, save_file_to_disk
from tools.compiler import Compiler
from tools.executor import Executor
import os
from prompts.prompts import BasePrompt
from pathlib import Path
from prompts import queries
from prompts.system_prompts import system_prompt_simple as system_prompt

class ExperimentWrapper():
    def __init__(self, llm, compiler, executor, run_id=0,args=None):
        self.args = args
        self.llm = llm # Set the LLM here
        self.run_id = run_id
        self.compiler = compiler # Setting the compiler here
        self.executor = executor
        self.max_steps = 10 if args is None else args.max_steps
        self.save_path = f"{args.save_dir}/{args.task_name}/{llm.model_name}/{self.run_id}"
        # breakpoint()
        self.compiler.set_directory(source_dir=self.save_path)

        # set path in executor
        self.executor.set_executable_path(executable=f"{self.save_path}/build/test")
        os.makedirs(self.save_path, exist_ok=True)

        self.success = False
        self.setup_logging()
    
    def setup_logging(self):
        # Set up logging configuration
        logging.basicConfig(
            filename=os.path.join(self.save_path, 'result.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"Starting task {self.args.task_name} with model {self.llm.model_name} started.")

    def run_expr(self, prompt):
        for i in range(1, self.max_steps + 1):
            logging.info(f"Step {i}: Generating code...")
            # y = LLM(Q)
            response = self.llm(prompt)
            code = parse_cpp_from_response(response)

            # check if code was generated ?

            if len(code) == 0:
                logging.info(f"No code generated in step {i}.")
                continue

            # save the output
            new_save_path = os.path.join(self.save_path, "solution.cpp")
            save_file_to_disk(new_save_path, code)
            
            # feedback from compiler
            result = self.compiler.compile()

            # check if solved
            if result.returncode == 0:
                # compiled successfully, now exit
                # self.success = True # this is not success anymore
                # now we run the executor
                passed, total, results = self.executor.run_all() 

                if passed == 5:
                    self.success = True
                    break

                # at lease 1 result was incorrect
                # so feedback will be from the executor
                # BUILD EXECUTOR FEEDBACK HERE

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
                feedback = "\n".join(feedback_lines)
            else:
                # did not compile successfully
                # so feeback will be from the compiler
                # BUILD COMPILER FEEDBACK HERE
                feedback = f"Attempt: {i} The code you suggested caused the following compile error, please update it and give the full revised code: {result.stderr}"
                pass
                
            # attach feedback to the prompt
            prompt.add_message(role="assistant", content=code)
            prompt.add_message(role="user", content=feedback)
            
        if self.success:
            logging.info(f"Model was able to generate functional output in {i} steps.")
        else:
            logging.info(f"Model failed to generate compilable output in {self.max_steps} steps.")
        return code, response
    


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

    set_seed(args.run_id)

    if args.model_name == "CodeLlama-7B":
        llm = CodeLlama7B(max_new_tokens=1024)
    elif args.model_name == "Deepseek-Coder":
        llm = DeepseekCoder(max_new_tokens=1024)
    elif args.model_name == "Llama3-3-70b":
        llm = Llama3_3_70b(max_new_tokens=1024, args=args)
    elif args.model_name == "GPT-4o":
        llm = GPT_4o(max_new_tokens=1024, args=args)
    elif args.model_name == "Deepseek-Chat":
        llm = DeepseekChatV3(max_new_tokens=1024, args=args)
    elif args.model_name == "Claude-3-5-Haiku":
        llm = Claude_3_5_Haiku(max_new_tokens=1024, args=args)
    else:
        raise ValueError(f"Model {args.model_name} not supported.")
    
    # build the initial prompt here

    prompt = BasePrompt([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": queries[args.task_name]}
    ], args)
    
    compiler = Compiler(args=args)                         # here we have the compiler
    executor = Executor(args=args, tests_root=Path("./tests"))
    experiment = ExperimentWrapper(llm, compiler, executor, args.run_id, args) # here is the Experiment Wrapper
    logging.info(f"🚀 Running benchmark: Model={args.model_name}, Task={args.task_name}, Run={args.run_id}")
    code, _ = experiment.run_expr(prompt=prompt)

    logging.info(f"📊 Benchmark Complete | Model: {args.model_name} | Task: {args.task_name} | Run ID: {args.run_id}")

if __name__ == "__main__":
    main()

# debug example: python scripts/run_benchmark.py --model_name=CodeLlama-7B --task_name=task_not --run_id=50 --use_rag --debug
