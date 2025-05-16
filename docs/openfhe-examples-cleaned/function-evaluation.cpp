/*
  Example of evaluating arbitrary smooth functions with the Chebyshev approximation using CKKS.
 */

#include "openfhe.h"

using namespace lbcrypto;

void EvalLogisticExample();

void EvalFunctionExample();

int main(int argc, char* argv[]) {
    EvalLogisticExample();
    EvalFunctionExample();
    return 0;
}

// In this example, we evaluate the logistic function 1 / (1 + exp(-x)) on an input of doubles
void EvalLogisticExample() {
    std::cout << "--------------------------------- EVAL LOGISTIC FUNCTION ---------------------------------"
              << std::endl;
    CCParams<CryptoContextCKKSRNS> parameters;

    // We set a smaller ring dimension to improve performance for this example.
    // In production environments, the security level should be set to
    // HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
    // or 256-bit security, respectively.
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 10);
#if NATIVEINT == 128
    usint scalingModSize = 78;
    usint firstModSize   = 89;
#else
    usint scalingModSize = 50;
    usint firstModSize   = 60;
#endif
    parameters.SetScalingModSize(scalingModSize);
    parameters.SetFirstModSize(firstModSize);

    // Choosing a higher degree yields better precision, but a longer runtime.
    uint32_t polyDegree = 16;

    // The multiplicative depth depends on the polynomial degree.
    // See the FUNCTION_EVALUATION.md file for a table mapping polynomial degrees to multiplicative depths.
    uint32_t multDepth = 6;

    parameters.SetMultiplicativeDepth(multDepth);
    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    // We need to enable Advanced SHE to use the Chebyshev approximation.
    cc->Enable(ADVANCEDSHE);

    auto keyPair = cc->KeyGen();
    // We need to generate mult keys to run Chebyshev approximations.
    cc->EvalMultKeyGen(keyPair.secretKey);

    std::vector<std::complex<double>> input{-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0};
    size_t encodedLength = input.size();
    Plaintext plaintext  = cc->MakeCKKSPackedPlaintext(input);
    auto ciphertext      = cc->Encrypt(keyPair.publicKey, plaintext);

    double lowerBound = -5;
    double upperBound = 5;
    auto result       = cc->EvalLogistic(ciphertext, lowerBound, upperBound, polyDegree);

    Plaintext plaintextDec;
    cc->Decrypt(keyPair.secretKey, result, &plaintextDec);
    plaintextDec->SetLength(encodedLength);

    std::vector<std::complex<double>> expectedOutput(
        {0.0179885, 0.0474289, 0.119205, 0.268936, 0.5, 0.731064, 0.880795, 0.952571, 0.982011});
    std::cout << "Expected output\n\t" << expectedOutput << std::endl;

    std::vector<std::complex<double>> finalResult = plaintextDec->GetCKKSPackedValue();
    std::cout << "Actual output\n\t" << finalResult << std::endl << std::endl;
}

void EvalFunctionExample() {
    std::cout << "--------------------------------- EVAL SQUARE ROOT FUNCTION ---------------------------------"
              << std::endl;
    CCParams<CryptoContextCKKSRNS> parameters;

    // We set a smaller ring dimension to improve performance for this example.
    // In production environments, the security level should be set to
    // HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
    // or 256-bit security, respectively.
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 10);
#if NATIVEINT == 128
    usint scalingModSize = 78;
    usint firstModSize   = 89;
#else
    usint scalingModSize = 50;
    usint firstModSize   = 60;
#endif
    parameters.SetScalingModSize(scalingModSize);
    parameters.SetFirstModSize(firstModSize);

    // Choosing a higher degree yields better precision, but a longer runtime.
    uint32_t polyDegree = 50;

    // The multiplicative depth depends on the polynomial degree.
    // See the FUNCTION_EVALUATION.md file for a table mapping polynomial degrees to multiplicative depths.
    uint32_t multDepth = 7;

    parameters.SetMultiplicativeDepth(multDepth);
    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    // We need to enable Advanced SHE to use the Chebyshev approximation.
    cc->Enable(ADVANCEDSHE);

    auto keyPair = cc->KeyGen();
    // We need to generate mult keys to run Chebyshev approximations.
    cc->EvalMultKeyGen(keyPair.secretKey);

    std::vector<std::complex<double>> input{1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t encodedLength = input.size();
    Plaintext plaintext  = cc->MakeCKKSPackedPlaintext(input);
    auto ciphertext      = cc->Encrypt(keyPair.publicKey, plaintext);

    double lowerBound = 0;
    double upperBound = 10;

    // We can input any lambda function, which inputs a double and returns a double.
    auto result = cc->EvalChebyshevFunction([](double x) -> double { return std::sqrt(x); }, ciphertext, lowerBound,
                                            upperBound, polyDegree);

    Plaintext plaintextDec;
    cc->Decrypt(keyPair.secretKey, result, &plaintextDec);
    plaintextDec->SetLength(encodedLength);

    std::vector<std::complex<double>> expectedOutput(
        {1, 1.414213, 1.732050, 2, 2.236067, 2.449489, 2.645751, 2.828427, 3});
    std::cout << "Expected output\n\t" << expectedOutput << std::endl;

    std::vector<std::complex<double>> finalResult = plaintextDec->GetCKKSPackedValue();
    std::cout << "Actual output\n\t" << finalResult << std::endl << std::endl;
}
