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
"""

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
        {"role": "user", "content": f"Here is an example from the documentation:\n{demo}\n\nNow, solve the following task:{queries[args.task_name]}"}
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
