#include <iostream>
#include <vector>
#include <string>
#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Set up crypto parameters
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(3);  // Depth needed for convolution operations
    parameters.SetScalingModSize(50);      // Scaling factor bit size
    parameters.SetBatchSize(256);           // Batching size (power of 2, large enough for our data)
    parameters.SetSecurityLevel(HEStd_128_classic);
    
    // Generate crypto context
    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    
    // std::cout << "CKKS scheme is using ring dimension " << cryptoContext->GetRingDimension() << std::endl;
    
    // Generate keypair
    KeyPair<DCRTPoly> keyPair = cryptoContext->KeyGen();
    
    // Generate multiplication keys
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);
    
    // Matrix input (5x5 flattened)
    std::vector<double> input_matrix = {
        7.0, 7.0, 5.0, 10.0, 5.0,
        9.0, 8.0, 2.0, 9.0, 10.0,
        9.0, 5.0, 4.0, 9.0, 4.0,
        7.0, 7.0, 4.0, 4.0, 9.0,
        2.0, 9.0, 5.0, 8.0, 10.0
    };
    
    // Kernel (3x3 flattened)
    std::vector<double> kernel = {
        1.0, 5.0, 4.0,
        2.0, 4.0, 2.0,
        6.0, 10.0, 8.0
    };
    
    // Encrypt the input matrix
    Plaintext plainMatrix = cryptoContext->MakeCKKSPackedPlaintext(input_matrix);
    auto cipherMatrix = cryptoContext->Encrypt(keyPair.publicKey, plainMatrix);
    
    // In practical application, the kernel might be encrypted as well
    // Here we use it as plaintext for simplicity
    
    // Resulting matrix will be 3x3 (flattened to size 9)
    std::vector<double> result(9, 0);
    
    // Perform convolution
    // For each position in the output matrix
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            // Create a mask for this convolution position
            std::vector<double> mask(input_matrix.size(), 0);
            
            // Place the kernel at the right position in the mask
            for (int ki = 0; ki < 3; ki++) {
                for (int kj = 0; kj < 3; kj++) {
                    int input_idx = (i + ki) * 5 + (j + kj);  // Position in input
                    int kernel_idx = ki * 3 + kj;             // Position in kernel
                    mask[input_idx] = kernel[kernel_idx];
                }
            }
            
            // Encrypt the mask
            Plaintext plainMask = cryptoContext->MakeCKKSPackedPlaintext(mask);
            
            // Calculate the dot product for this position
            auto dotProduct = cryptoContext->EvalMult(cipherMatrix, plainMask);
            
            // We need to sum all elements in the dot product to get the convolution value
            // In CKKS, we use a rotation and addition approach
            Ciphertext<DCRTPoly> sum = dotProduct;
            
            // Sum all elements (naive approach for simplicity)
            for (int k = 1; k < int(input_matrix.size()); k++) {
                cryptoContext->EvalRotateKeyGen(keyPair.secretKey, {k});
                auto rotated = cryptoContext->EvalRotate(dotProduct, k);
                sum = cryptoContext->EvalAdd(sum, rotated);
            }
            
            // Decrypt the sum
            Plaintext plainResult;
            cryptoContext->Decrypt(keyPair.secretKey, sum, &plainResult);
            
            // The first element of the result will be the sum (others are rotations)
            double convolutionValue = plainResult->GetRealPackedValue()[0] / input_matrix.size();
            
            // Store in result array
            result[i * 3 + j] = convolutionValue;
        }
    }
    
    // Print the result
    // std::cout << "Convolution result (3x3):" << std::endl;
    for (int i = 0; i < 9; i++) {
        std::cout << result[i] << " ";
    }
    
    return 0;
}