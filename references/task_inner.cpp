#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Step 1: Setup CryptoContext
    uint32_t multDepth = 1;
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
    cc->Enable(ADVANCEDSHE);

    // Step 2: Key Generation
    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalSumKeyGen(keys.secretKey);

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

    // Homomorphic inner product
    auto res = cc->EvalInnerProduct(c1, c2, batchSize);

    // Step 5: Decryption and output
    Plaintext result;
    std::cout.precision(8);

    // Decrypt the result of inner product
    cc->Decrypt(keys.secretKey, res, &result);
    result->SetLength(x1.size());

    auto cInner = result->GetCKKSPackedValue()[0].real();

    std::cout << cInner << std::endl;

    return 0;
}