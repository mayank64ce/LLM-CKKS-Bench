#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Step 1: Setup CryptoContext
    uint32_t multDepth = 3;
    uint32_t scaleModSize = 50;
    uint32_t batchSize = 8;

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

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1(5), x2(5);

    for(int i=0;i<5;++i){
        std::cin >> x1[i]; 
    }

    for(int i=0;i<5;++i){
        std::cin >> x2[i]; 
    }

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);
    Plaintext ptxt2 = cc->MakeCKKSPackedPlaintext(x2);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);
    auto c2 = cc->Encrypt(keys.publicKey, ptxt2);

    // Step 4: Evaluation

    // Homomorphic multiplication
    auto cMult = cc->EvalMult(c1, c2);

    // Step 5: Decryption and output
    Plaintext result;
    std::cout.precision(8);

    // Decrypt the result of multiplication
    cc->Decrypt(keys.secretKey, cMult, &result);
    result->SetLength(batchSize);

    for(int i = 0; i < 5; ++i) {
        std::cout << result->GetRealPackedValue()[i] << " ";
    }

    return 0;
}