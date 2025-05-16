/**
 * Simple example for BFV and CKKS for inner product.
 */

#include <iostream>
#include "openfhe.h"
#include <vector>

using namespace lbcrypto;

template <class T>
T plainInnerProduct(std::vector<T> vec) {
    T res = 0.0;
    for (auto& el : vec) {
        res += (el * el);
    }
    return res;
}

bool innerProductCKKS(const std::vector<double>& incomingVector) {
    double expectedResult                 = plainInnerProduct(incomingVector);
    lbcrypto::SecurityLevel securityLevel = lbcrypto::HEStd_NotSet;
    uint32_t dcrtBits                     = 59;
    uint32_t ringDim                      = 1 << 8;
    uint32_t batchSize                    = ringDim / 2;
    lbcrypto::CCParams<lbcrypto::CryptoContextCKKSRNS> parameters;
    uint32_t multDepth = 10;

    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(dcrtBits);
    parameters.SetBatchSize(batchSize);
    parameters.SetSecurityLevel(securityLevel);
    parameters.SetRingDim(ringDim);

    lbcrypto::CryptoContext<lbcrypto::DCRTPoly> cc;
    cc = GenCryptoContext(parameters);

    cc->Enable(PKE);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);

    KeyPair keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalSumKeyGen(keys.secretKey);

    Plaintext plaintext1 = cc->MakeCKKSPackedPlaintext(incomingVector);
    auto ct1             = cc->Encrypt(keys.publicKey, plaintext1);
    auto finalResult     = cc->EvalInnerProduct(ct1, ct1, batchSize);
    lbcrypto::Plaintext res;
    cc->Decrypt(keys.secretKey, finalResult, &res);
    res->SetLength(incomingVector.size());
    auto final = res->GetCKKSPackedValue()[0].real();
    std::cout << "Expected Result: " << expectedResult << " Inner Product Result: " << final << std::endl;
    return std::abs(expectedResult - final) <= 0.0001;
}

int main(int argc, char* argv[]) {
    std::vector<int64_t> vec = {1, 2, 3, 4, 5};
    std::vector<double> asDouble(vec.begin(), vec.end());
    for (size_t i = 0; i < asDouble.size(); i++) {
        asDouble[i] += (asDouble[i] / 100.0);
    }
    bool ckksRes = innerProductCKKS(asDouble);
    std::cout << "CKKS Inner Product Correct? " << (ckksRes ? "True" : "False") << std::endl;

    return 0;
}
