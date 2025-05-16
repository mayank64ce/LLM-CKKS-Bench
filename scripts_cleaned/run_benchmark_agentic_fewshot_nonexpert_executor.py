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
import random

# logfire.configure(send_to_logfire='if-token-present', token=os.getenv("LOGFIRE_TOKEN"))
logfire.configure(send_to_logfire='if-token-present')

import nest_asyncio
nest_asyncio.apply()

demo = """
/*
  Simple examples for CKKS
 */

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Step 1: Setup CryptoContext

    // A. Specify main parameters
    /* A1) Multiplicative depth:
   * The CKKS scheme we setup here will work for any computation
   * that has a multiplicative depth equal to 'multDepth'.
   * This is the maximum possible depth of a given multiplication,
   * but not the total number of multiplications supported by the
   * scheme.
   *
   * For example, computation f(x, y) = x^2 + x*y + y^2 + x + y has
   * a multiplicative depth of 1, but requires a total of 3 multiplications.
   * On the other hand, computation g(x_i) = x1*x2*x3*x4 can be implemented
   * either as a computation of multiplicative depth 3 as
   * g(x_i) = ((x1*x2)*x3)*x4, or as a computation of multiplicative depth 2
   * as g(x_i) = (x1*x2)*(x3*x4).
   *
   * For performance reasons, it's generally preferable to perform operations
   * in the shorted multiplicative depth possible.
   */
    uint32_t multDepth = 1;

    /* A2) Bit-length of scaling factor.
   * CKKS works for real numbers, but these numbers are encoded as integers.
   * For instance, real number m=0.01 is encoded as m'=round(m*D), where D is
   * a scheme parameter called scaling factor. Suppose D=1000, then m' is 10 (an
   * integer). Say the result of a computation based on m' is 130, then at
   * decryption, the scaling factor is removed so the user is presented with
   * the real number result of 0.13.
   *
   * Parameter 'scaleModSize' determines the bit-length of the scaling
   * factor D, but not the scaling factor itself. The latter is implementation
   * specific, and it may also vary between ciphertexts in certain versions of
   * CKKS (e.g., in FLEXIBLEAUTO).
   *
   * Choosing 'scaleModSize' depends on the desired accuracy of the
   * computation, as well as the remaining parameters like multDepth or security
   * standard. This is because the remaining parameters determine how much noise
   * will be incurred during the computation (remember CKKS is an approximate
   * scheme that incurs small amounts of noise with every operation). The
   * scaling factor should be large enough to both accommodate this noise and
   * support results that match the desired accuracy.
   */
    uint32_t scaleModSize = 50;

    /* A3) Number of plaintext slots used in the ciphertext.
   * CKKS packs multiple plaintext values in each ciphertext.
   * The maximum number of slots depends on a security parameter called ring
   * dimension. In this instance, we don't specify the ring dimension directly,
   * but let the library choose it for us, based on the security level we
   * choose, the multiplicative depth we want to support, and the scaling factor
   * size.
   *
   * Please use method GetRingDimension() to find out the exact ring dimension
   * being used for these parameters. Give ring dimension N, the maximum batch
   * size is N/2, because of the way CKKS works.
   */
    uint32_t batchSize = 8;

    /* A4) Desired security level based on FHE standards.
   * This parameter can take four values. Three of the possible values
   * correspond to 128-bit, 192-bit, and 256-bit security, and the fourth value
   * corresponds to "NotSet", which means that the user is responsible for
   * choosing security parameters. Naturally, "NotSet" should be used only in
   * non-production environments, or by experts who understand the security
   * implications of their choices.
   *
   * If a given security level is selected, the library will consult the current
   * security parameter tables defined by the FHE standards consortium
   * (https://homomorphicencryption.org/introduction/) to automatically
   * select the security parameters. Please see "TABLES of RECOMMENDED
   * PARAMETERS" in  the following reference for more details:
   * http://homomorphicencryption.org/wp-content/uploads/2018/11/HomomorphicEncryptionStandardv1.1.pdf
   */
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl << std::endl;

    // B. Step 2: Key Generation
    /* B1) Generate encryption keys.
   * These are used for encryption/decryption, as well as in generating
   * different kinds of keys.
   */
    auto keys = cc->KeyGen();

    /* B2) Generate the digit size
   * In CKKS, whenever someone multiplies two ciphertexts encrypted with key s,
   * we get a result with some components that are valid under key s, and
   * with an additional component that's valid under key s^2.
   *
   * In most cases, we want to perform relinearization of the multiplicaiton
   * result, i.e., we want to transform the s^2 component of the ciphertext so
   * it becomes valid under original key s. To do so, we need to create what we
   * call a relinearization key with the following line.
   */
    cc->EvalMultKeyGen(keys.secretKey);

    /* B3) Generate the rotation keys
   * CKKS supports rotating the contents of a packed ciphertext, but to do so,
   * we need to create what we call a rotation key. This is done with the
   * following call, which takes as input a vector with indices that correspond
   * to the rotation offset we want to support. Negative indices correspond to
   * right shift and positive to left shift. Look at the output of this demo for
   * an illustration of this.
   *
   * Keep in mind that rotations work over the batch size or entire ring dimension (if the batch size is not specified).
   * This means that, if ring dimension is 8 and batch
   * size is not specified, then an input (1,2,3,4,0,0,0,0) rotated by 2 will become
   * (3,4,0,0,0,0,1,2) and not (3,4,1,2,0,0,0,0).
   * If ring dimension is 8 and batch
   * size is set to 4, then the rotation of (1,2,3,4) by 2 will become (3,4,1,2).
   * Also, as someone can observe
   * in the output of this demo, since CKKS is approximate, zeros are not exact
   * - they're just very small numbers.
   */
    cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1 = {0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> x2 = {5.0, 4.0, 3.0, 2.0, 1.0, 0.75, 0.5, 0.25};

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);
    Plaintext ptxt2 = cc->MakeCKKSPackedPlaintext(x2);

    std::cout << "Input x1: " << ptxt1 << std::endl;
    std::cout << "Input x2: " << ptxt2 << std::endl;

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);
    auto c2 = cc->Encrypt(keys.publicKey, ptxt2);

    // Step 4: Evaluation

    // Homomorphic addition
    auto cAdd = cc->EvalAdd(c1, c2);

    // Homomorphic subtraction
    auto cSub = cc->EvalSub(c1, c2);

    // Homomorphic scalar multiplication
    auto cScalar = cc->EvalMult(c1, 4.0);

    // Homomorphic multiplication
    auto cMul = cc->EvalMult(c1, c2);

    // Homomorphic rotations
    auto cRot1 = cc->EvalRotate(c1, 1);
    auto cRot2 = cc->EvalRotate(c1, -2);

    // Step 5: Decryption and output
    Plaintext result;
    // We set the cout precision to 8 decimal digits for a nicer output.
    // If you want to see the error/noise introduced by CKKS, bump it up
    // to 15 and it should become visible.
    std::cout.precision(8);

    std::cout << std::endl << "Results of homomorphic computations: " << std::endl;

    cc->Decrypt(keys.secretKey, c1, &result);
    result->SetLength(batchSize);
    std::cout << "x1 = " << result;
    std::cout << "Estimated precision in bits: " << result->GetLogPrecision() << std::endl;

    // Decrypt the result of addition
    cc->Decrypt(keys.secretKey, cAdd, &result);
    result->SetLength(batchSize);
    std::cout << "x1 + x2 = " << result;
    std::cout << "Estimated precision in bits: " << result->GetLogPrecision() << std::endl;

    // Decrypt the result of subtraction
    cc->Decrypt(keys.secretKey, cSub, &result);
    result->SetLength(batchSize);
    std::cout << "x1 - x2 = " << result << std::endl;

    // Decrypt the result of scalar multiplication
    cc->Decrypt(keys.secretKey, cScalar, &result);
    result->SetLength(batchSize);
    std::cout << "4 * x1 = " << result << std::endl;

    // Decrypt the result of multiplication
    cc->Decrypt(keys.secretKey, cMul, &result);
    result->SetLength(batchSize);
    std::cout << "x1 * x2 = " << result << std::endl;

    // Decrypt the result of rotations

    cc->Decrypt(keys.secretKey, cRot1, &result);
    result->SetLength(batchSize);
    std::cout << std::endl << "In rotations, very small outputs (~10^-10 here) correspond to 0's:" << std::endl;
    std::cout << "x1 rotate by 1 = " << result << std::endl;

    cc->Decrypt(keys.secretKey, cRot2, &result);
    result->SetLength(batchSize);
    std::cout << "x1 rotate by -2 = " << result << std::endl;

    return 0;
}
""".strip()

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

        time.sleep(random.uniform(3.0, 7.0))
        print(Fore.GREEN + "The solution compiled successfully!!!!")

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
            print(Fore.GREEN + "Awesome, all test cases passed.")
            time.sleep(random.uniform(3.0, 7.0))
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
        result = agent.run_sync(f"Here is an example from the documentation:\n```cpp\n{demo}\n```\nNow solve the following taks:{queries[args.task_name]}\n{agent_extras}",)
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            sys.exit("0")
        elif isinstance(e, PermissionError):
            sys.exit("0")
        else:
            raise e

if __name__ == "__main__":
    main()
