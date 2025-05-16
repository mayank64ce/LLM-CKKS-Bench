/*
  Example of polynomial evaluation using CKKS.
 */

#define PROFILE  // turns on the reporting of timing results

#include "openfhe.h"

using namespace lbcrypto;

int main(int argc, char* argv[]) {
    TimeVar t;

    double timeEvalPoly1(0.0), timeEvalPoly2(0.0);

    std::cout << "\n======EXAMPLE FOR EVALPOLY========\n" << std::endl;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(6);
    parameters.SetScalingModSize(50);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);

    std::vector<std::complex<double>> input({0.5, 0.7, 0.9, 0.95, 0.93});

    size_t encodedLength = input.size();

    std::vector<double> coefficients1({0.15, 0.75, 0, 1.25, 0, 0, 1, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1});
    std::vector<double> coefficients2({1,   2,   3,   4,   5,   -1,   -2,   -3,   -4,   -5,
                                       0.1, 0.2, 0.3, 0.4, 0.5, -0.1, -0.2, -0.3, -0.4, -0.5,
                                       0.1, 0.2, 0.3, 0.4, 0.5, -0.1, -0.2, -0.3, -0.4, -0.5});
    Plaintext plaintext1 = cc->MakeCKKSPackedPlaintext(input);

    auto keyPair = cc->KeyGen();

    std::cout << "Generating evaluation key for homomorphic multiplication...";
    cc->EvalMultKeyGen(keyPair.secretKey);
    std::cout << "Completed." << std::endl;

    auto ciphertext1 = cc->Encrypt(keyPair.publicKey, plaintext1);

    TIC(t);

    auto result = cc->EvalPoly(ciphertext1, coefficients1);

    timeEvalPoly1 = TOC(t);

    TIC(t);

    auto result2 = cc->EvalPoly(ciphertext1, coefficients2);

    timeEvalPoly2 = TOC(t);

    Plaintext plaintextDec;

    cc->Decrypt(keyPair.secretKey, result, &plaintextDec);

    plaintextDec->SetLength(encodedLength);

    Plaintext plaintextDec2;

    cc->Decrypt(keyPair.secretKey, result2, &plaintextDec2);

    plaintextDec2->SetLength(encodedLength);

    std::cout << std::setprecision(15) << std::endl;

    std::cout << "\n Original Plaintext #1: \n";
    std::cout << plaintext1 << std::endl;

    std::cout << "\n Result of evaluating a polynomial with coefficients " << coefficients1 << " \n";
    std::cout << plaintextDec << std::endl;

    std::cout << "\n Expected result: (0.70519107, 1.38285078, 3.97211180, "
                 "5.60215665, 4.86357575) "
              << std::endl;

    std::cout << "\n Evaluation time: " << timeEvalPoly1 << " ms" << std::endl;

    std::cout << "\n Result of evaluating a polynomial with coefficients " << coefficients2 << " \n";
    std::cout << plaintextDec2 << std::endl;

    std::cout << "\n Expected result: (3.4515092326, 5.3752765397, 4.8993108833, "
                 "3.2495023573, 4.0485229982) "
              << std::endl;

    std::cout << "\n Evaluation time: " << timeEvalPoly2 << " ms" << std::endl;

    return 0;
}
