/*
  Example of vector rotation.
  This code shows how the EvalRotate and EvalMerge operations work
 */

#include <fstream>
#include <iostream>
#include <iterator>
#include <random>

#include "openfhe.h"
#include "math/math-hal.h"

using namespace lbcrypto;

void BFVrnsEvalRotate2n();
void CKKSEvalRotate2n();
void BFVrnsEvalMerge2n();

int main() {
    std::cout << "\nThis code shows how the EvalRotate and EvalMerge operations work "
                 "for different cyclotomic rings (both power-of-two and cyclic).\n"
              << std::endl;

    std::cout << "\n========== BFVrns.EvalRotate - Power-of-Two Cyclotomics "
                 "==========="
              << std::endl;

    BFVrnsEvalRotate2n();

    std::cout << "\n========== CKKS.EvalRotate - Power-of-Two Cyclotomics ===========" << std::endl;

    CKKSEvalRotate2n();

    std::cout << "\n========== BFVrns.EvalMerge - Power-of-Two Cyclotomics ===========" << std::endl;

    BFVrnsEvalMerge2n();

    return 0;
}

void BFVrnsEvalRotate2n() {
    CCParams<CryptoContextBFVRNS> parameters;

    parameters.SetPlaintextModulus(65537);
    parameters.SetMaxRelinSkDeg(3);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    int32_t n = cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2;

    // Initialize the public key containers.
    KeyPair<DCRTPoly> kp = cc->KeyGen();

    std::vector<int32_t> indexList = {2, 3, 4, 5, 6, 7, 8, 9, 10, -n + 2, -n + 3, n - 1, n - 2, -1, -2, -3, -4, -5};

    cc->EvalRotateKeyGen(kp.secretKey, indexList);

    std::vector<int64_t> vectorOfInts = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vectorOfInts.resize(n);
    vectorOfInts[n - 1] = n;
    vectorOfInts[n - 2] = n - 1;
    vectorOfInts[n - 3] = n - 2;

    Plaintext intArray = cc->MakePackedPlaintext(vectorOfInts);

    auto ciphertext = cc->Encrypt(kp.publicKey, intArray);

    for (size_t i = 0; i < 18; i++) {
        auto permutedCiphertext = cc->EvalRotate(ciphertext, indexList[i]);

        Plaintext intArrayNew;

        cc->Decrypt(kp.secretKey, permutedCiphertext, &intArrayNew);

        intArrayNew->SetLength(10);

        std::cout << "Automorphed array - at index " << indexList[i] << ": " << *intArrayNew << std::endl;
    }
}

void CKKSEvalRotate2n() {
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(2);
    parameters.SetScalingModSize(40);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    usint cyclOrder = cc->GetCyclotomicOrder();

    // Initialize the public key containers.
    KeyPair<DCRTPoly> kp = cc->KeyGen();

    int32_t n                      = cyclOrder / 4;
    std::vector<int32_t> indexList = {2, 3, 4, 5, 6, 7, 8, 9, 10, -n + 2, -n + 3, n - 1, n - 2, -1, -2, -3, -4, -5};

    cc->EvalRotateKeyGen(kp.secretKey, indexList);

    std::vector<std::complex<double>> vectorOfInts = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vectorOfInts.resize(n);
    vectorOfInts[n - 1] = n;
    vectorOfInts[n - 2] = n - 1;
    vectorOfInts[n - 3] = n - 2;

    Plaintext intArray = cc->MakeCKKSPackedPlaintext(vectorOfInts);

    auto ciphertext = cc->Encrypt(kp.publicKey, intArray);

    for (size_t i = 0; i < 18; i++) {
        auto permutedCiphertext = cc->EvalRotate(ciphertext, indexList[i]);

        Plaintext intArrayNew;

        cc->Decrypt(kp.secretKey, permutedCiphertext, &intArrayNew);

        intArrayNew->SetLength(10);

        std::cout << "Automorphed array - at index " << indexList[i] << ": " << *intArrayNew << std::endl;
    }
}

void BFVrnsEvalMerge2n() {
    CCParams<CryptoContextBFVRNS> parameters;

    parameters.SetPlaintextModulus(65537);
    parameters.SetMultiplicativeDepth(2);
    parameters.SetMaxRelinSkDeg(3);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);

    // Initialize the public key containers.
    KeyPair<DCRTPoly> kp = cc->KeyGen();

    std::vector<int32_t> indexList = {-1, -2, -3, -4, -5};

    cc->EvalRotateKeyGen(kp.secretKey, indexList);

    std::vector<Ciphertext<DCRTPoly>> ciphertexts;

    std::vector<int64_t> vectorOfInts1 = {32, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Plaintext intArray1                = cc->MakePackedPlaintext(vectorOfInts1);
    ciphertexts.push_back(cc->Encrypt(kp.publicKey, intArray1));

    std::vector<int64_t> vectorOfInts2 = {2, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Plaintext intArray2                = cc->MakePackedPlaintext(vectorOfInts2);
    ciphertexts.push_back(cc->Encrypt(kp.publicKey, intArray2));

    std::vector<int64_t> vectorOfInts3 = {4, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Plaintext intArray3                = cc->MakePackedPlaintext(vectorOfInts3);
    ciphertexts.push_back(cc->Encrypt(kp.publicKey, intArray3));

    std::vector<int64_t> vectorOfInts4 = {8, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Plaintext intArray4                = cc->MakePackedPlaintext(vectorOfInts4);
    ciphertexts.push_back(cc->Encrypt(kp.publicKey, intArray4));

    std::vector<int64_t> vectorOfInts5 = {16, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Plaintext intArray5                = cc->MakePackedPlaintext(vectorOfInts5);
    ciphertexts.push_back(cc->Encrypt(kp.publicKey, intArray5));

    std::cout << "Input ciphertext " << *intArray1 << std::endl;
    std::cout << "Input ciphertext " << *intArray2 << std::endl;
    std::cout << "Input ciphertext " << *intArray3 << std::endl;
    std::cout << "Input ciphertext " << *intArray4 << std::endl;
    std::cout << "Input ciphertext " << *intArray5 << std::endl;

    auto mergedCiphertext = cc->EvalMerge(ciphertexts);

    Plaintext intArrayNew;

    cc->Decrypt(kp.secretKey, mergedCiphertext, &intArrayNew);

    intArrayNew->SetLength(10);

    std::cout << "\nMerged ciphertext " << *intArrayNew << std::endl;
}
