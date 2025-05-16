#include "openfhe.h"
#include <vector>
#include <typeinfo>
#include <cmath>

using namespace lbcrypto;

Ciphertext<DCRTPoly> generateColumnMask(
    const CryptoContext<DCRTPoly>& cc,
    const PublicKey<DCRTPoly>& pk,
    size_t d,
    size_t colIndex
) {
    // 1) build a flat mask of size d*d
    std::vector<double> maskFlat(d * d, 0.0);
    for (size_t i = 0; i < d; ++i) {
        maskFlat[i * d + colIndex] = 1.0;
    }

    // 2) make a CKKS plaintext with exactly d*d slots
    auto ptxtMask = cc->MakeCKKSPackedPlaintext(maskFlat);

    // 3) encrypt under the public key
    auto ctxtMask = cc->Encrypt(pk, ptxtMask);

    return ctxtMask;
}


Ciphertext<DCRTPoly> generateRowMask(
    const CryptoContext<DCRTPoly>& cc,
    const PublicKey<DCRTPoly>& pk,
    size_t d,
    size_t rowIndex
) {
    // 1) build a flat mask of size d*d
    //    slots [rowIndex*d + j] = 1 for j=0..d-1
    std::vector<double> maskFlat(d * d, 0.0);
    for (size_t j = 0; j < d; ++j) {
        maskFlat[rowIndex * d + j] = 1.0;
    }

    // 2) make a CKKS plaintext with those d*d slots
    auto ptxtMask = cc->MakeCKKSPackedPlaintext(maskFlat);

    // 3) encrypt under the public key
    auto ctxtMask = cc->Encrypt(pk, ptxtMask);

    return ctxtMask;
}




int main() {
    // Step 1: Setup CryptoContext
    uint32_t multDepth = 2;
    uint32_t scaleModSize = 50;
    uint32_t batchSize = 4096;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    // Step 2: Key Generation
    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalRotateKeyGen(keys.secretKey, {1, -1, 2, -2, 3, -3, 4, -4, 5, -5});

    // Step 3: Encoding and encryption of inputs

    // Inputs
    int n = 2; // matrix size
    // int n_log=6;

    std::vector<std::vector<double> > x1(n, std::vector<double>(n, 1));
    std::vector<std::vector<double> > x2(n, std::vector<double>(n, 2));

    for(int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> x1[i][j];
        }
    }

    for(int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> x2[i][j];
        }
    }

    std::vector<double> x1_flat(n * n);
    std::vector<double> x2_flat(n * n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            x1_flat[i * n + j] = x1[i][j];
            x2_flat[i * n + j] = x2[i][j];
        }
    }

    // Encoding as plaintexts
    Plaintext matrix_A = cc->MakeCKKSPackedPlaintext(x1_flat);
    Plaintext matrix_B = cc->MakeCKKSPackedPlaintext(x2_flat);

    // Encrypt the encoded vectors
    auto matrixA_enc = cc->Encrypt(keys.publicKey, matrix_A);
    auto matrixB_enc = cc->Encrypt(keys.publicKey, matrix_B);

    std::vector<double> matrix_C = std::vector<double>(n * n, 0.0);

    auto ptxtC = cc->MakeCKKSPackedPlaintext(matrix_C);
    auto matrixC_enc = cc->Encrypt(keys.publicKey, ptxtC);

    // Preprocessing A

    std::vector<Ciphertext<DCRTPoly> > A_tilde;

    // std::cout << "A_tilde" << std::endl;

    for(int j=0;j<n;j++){
        auto ctxtMask = generateColumnMask(cc, keys.publicKey, n, j);
        auto Aj = cc->EvalMult(matrixA_enc, ctxtMask);
        if(j!=0){
            Aj = cc->EvalRotate(Aj, j);
        }
        for(int i=0;i<std::log2(n);++i){
            // std::cout << "rot = " << (1<<i) << std::endl;
            Aj += cc->EvalRotate(Aj, -(1<<i));
        }
        A_tilde.push_back(Aj);
    }

    // Preprocessing B

    std::vector<Ciphertext<DCRTPoly> > B_tilde;
    // std::cout << "B_tilde" << std::endl;
    for(int j=0;j<n;j++){
        auto ctxtMask = generateRowMask(cc, keys.publicKey, n, j);
        auto Bj = cc->EvalMult(matrixB_enc, ctxtMask);
        if(j!=0){
            Bj = cc->EvalRotate(Bj, j*n);
        }
        
        for(int i=0;i<std::log2(n);++i){
            // std::cout << "rot = " << (1<<i)*n << std::endl;
            Bj += cc->EvalRotate(Bj, -(1<<i)*n);
        }
        B_tilde.push_back(Bj);
    }

    for(int i = 0; i < n; ++i) {
        matrixC_enc += cc->EvalMult(A_tilde[i], B_tilde[i]);
    }

    // Step 5: Decryption and output
    Plaintext result;
    std::cout.precision(8);
    // Decrypt the result of multiplication
    cc->Decrypt(keys.secretKey, matrixC_enc, &result);
    result->SetLength(n * n);
    auto cMult = result->GetCKKSPackedValue();
    std::cout << "Result: " << std::endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << cMult[i * n + j].real() << " ";
        }
        std::cout << std::endl;
    }

    // for(int i=0;i<n*n;i++){
    //     std::cout << cMult[i].real() << " ";
    // }

    return 0;
}