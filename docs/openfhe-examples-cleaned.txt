Directory structure:
└── anon-openfhe-examples-cleaned/
    ├── README.md
    ├── advanced-ckks-bootstrapping.cpp
    ├── advanced-real-numbers-128.cpp
    ├── advanced-real-numbers.cpp
    ├── ckks-noise-flooding.cpp
    ├── CKKS_NOISE_FLOODING.md
    ├── function-evaluation.cpp
    ├── FUNCTION_EVALUATION.md
    ├── inner-product.cpp
    ├── iterative-ckks-bootstrapping.cpp
    ├── linearwsum-evaluation.cpp
    ├── polynomial-evaluation.cpp
    ├── pre-buffer.cpp
    ├── pre-hra-secure.cpp
    ├── rotation.cpp
    ├── scheme-switching-serial.cpp
    ├── scheme-switching.cpp
    ├── SCHEME_SWITCHING_CAPABILITY.md
    ├── simple-ckks-bootstrapping.cpp
    ├── simple-integers-serial.cpp
    ├── simple-integers.cpp
    ├── simple-real-numbers-serial.cpp
    ├── simple-real-numbers.cpp
    ├── tckks-interactive-mp-bootstrapping-Chebyshev.cpp
    ├── tckks-interactive-mp-bootstrapping.cpp
    ├── threshold-fhe-5p.cpp
    └── threshold-fhe.cpp

================================================
FILE: README.md
================================================
OpenFHE Lattice Cryptography Library - Examples
=============================================

[License Information](License.md)

Document Description
===================
This document describes the examples included with the OpenFHE lattice crypto library.

Examples Directory Description
==========================

Directory Objective
-------------------
This directory contains examples that, when linked with the library, demonstrate the capabilities of the system

File Listing
------------

*Example programs*

- [advanced-ckks-bootstrapping.cpp](advanced-ckks-bootstrapping.cpp): an example showing CKKS bootstrapping for a ciphertext with sparse packing
- [advanced-real-numbers.cpp](advanced-real-numbers.cpp): shows several advanced examples of approximate homomorphic encryption using CKKS
- [advanced-real-numbers-128.cpp](advanced-real-numbers-128.cpp): shows several advanced examples of approximate homomorphic encryption using high-precision CKKS
- [ckks-noise-flooding.cpp](ckks-noise-flooding.cpp): demonstrates use of experimental feature NOISE_FLOODING_DECRYPT mode in CKKS, which enhances security
- [depth-bfvrns.cpp](depth-bfvrns.cpp): demonstrates use of the BFVrns scheme for basic homomorphic encryption
- [depth-bfvrns-behz.cpp](depth-bfvrns-behz.cpp): demonstrates use of the BEHZ BFV variant for basic homomorphic encryption
- [depth-bgvrns.cpp](depth-bgvrns.cpp): demonstrates use of the BGVrns scheme for basic homomorphic encryption
- [iterative-ckks-bootstrapping.cpp](iterative-ckks-bootstrapping.cpp): demonstrates how to run multiple iterations of CKKS bootstrapping to improve precision
- [linearwsum-evaluation.cpp](linearwsum-evaluation.cpp): demonstrates the evaluation of a linear weighted sum using CKKS
- [function-evaluation.cpp](function-evaluation.cpp): demonstrates the evaluation of a non-polynomial function using a Chebyshev approximation using CKKS
- [polynomial-evaluation.cpp](polynomial-evaluation.cpp): demonstrates an evaluation of a polynomial (power series) using CKKS
- [pre-buffer.cpp](pre-buffer.cpp): demonstrates use of OpenFHE for encryption, re-encryption and decryption of packed vector of binary data
- [pre-hra-secure.cpp](pre-hra-secure.cpp): shows examples of HRA-secure PRE based on BGV
- [rotation.cpp](rotation.cpp): demonstrates use of EvalRotate for different schemes
- [scheme-switching.cpp](scheme-switching.cpp): demonstrates several use cases for switching between CKKS and FHEW ciphertexts
- [simple-ckks-bootstrapping.cpp](simple-ckks-bootstrapping.cpp): simple example showing CKKS bootstrapping for a ciphertext with full packing
- [simple-integers.cpp](simple-integers.cpp): simple example showing homomorphic additions, multiplications, and rotations for vectors of integers using BFVrns
- [simple-integers-bgvrns.cpp](simple-integers-bgvrns.cpp): simple example showing homomorphic additions, multiplications, and rotations for vectors of integers using BGVrns
- [simple-integers-serial.cpp](simple-integers-serial.cpp): simple example showing typical serialization/deserialization calls for a prototype computing homomorphic additions, multiplications, and rotations for vectors of integers using BFVrns
- [simple-integers-serial-bgvrns.cpp](simple-integers-serial-bgvrns.cpp): simple example showing typical serialization/deserialization calls for a prototype computing homomorphic additions, multiplications, and rotations for vectors of integers using BGVrns
- [simple-real-numbers.cpp](simple-real-numbers): simple example showing homomorphic additions, multiplications, and rotations for vectors of real numbers using CKKS
- [simple-real-numbers-serial.cpp](simple-real-numbers-serial.cpp): simple example showing typical serialization/deserialization calls for a prototype computing homomorphic additions, multiplications, and rotations for vectors of integers using CKKS
- [threshold-fhe.cpp](threshold-fhe.cpp): shows several examples of threshold FHE in BGVrns, BFVrns, and CKKSrns
- [threshold-fhe-5p.cpp](threshold-fhe-5p.cpp): shows example of threshold FHE with 5 parties in BFVrns

How To Link Your Own Project After Having OpenFHE Installed
===================
1. Check that you do not get error messages at the time of running "make install" for OpenFHE. You may need the admin rights to install.
2. Go to a new directory where you will keep "my_own_project.cpp" file.
3. Copy openfhe-development/CMakeLists.User.txt to the new directory and rename it to CMakeLists.txt.
4. Open CMakeLists.txt for editing and add a line to its end as suggested in the comments in CMakeLists.txt. Something like this:
```
    add_executable( test my_own_project.cpp)
```
5. ... and after that, execute commands that are very similar to the commands to build and run examples in OpenFHE:
```
    mkdir build
    cd build
    cmake ..
    make
    and, finally, run ./my_own_project
```

Generating Cryptocontext using GenCryptoContext()
===================
1. Pick the scheme you want to use. I chose CKKS for our tutorial example.
2. Include openfhe.h\
    **NOTE for OpenFHE contributors**\
    Instead of including openfhe.h, your code should include gen-cryptocontext.h and the header with the scheme-specific context generator (scheme/<scheme>/cryptocontext-<scheme>.h). Example:
```
    #include "scheme/ckks/cryptocontext-ckks.h"
    #include "gen-cryptocontext.h"
```
3. Create a parameter object to be passed to GenCryptoContext(). Its generic form would look like this: CCParams<GeneratorName> parameters where GeneratorName is the name of the class defined in cryptocontext-<scheme>.h. In our case it is CryptoContextCKKS and the line to add is
```
    CCParams<CryptoContextCKKS<Element>> parameters;
    // std::cout << parameters << std::endl;  // prints all parameter values
```
4. Adjust the parameters' values with set functions for CCParams<CryptoContextCKKS> as the object is created using default values from scheme/cryptocontextparams-defaults.h. The set functions can be found in scheme/cryptocontextparams-base.h. For example, we can set the multiplicative depth to be 1 as shown below.
```
    parameters.SetMultiplicativeDepth(1);
```
5. Call GenCryptoContext() to generate the cryptocontext.
```
    auto cryptoContext = GenCryptoContext(parameters);
```
6. Enable the features that we want to use. For example, if we want to perform an encrypted rotation, then we need encryption, key switching, and leveled somewhat homomorphic encryption (SHE) operations.
```
    cryptoContext->Enable(ENCRYPTION);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
```

Now your code should look like this:
```
    #include "openfhe.h
    ...........................................
    CCParams<CryptoContextCKKS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(8);
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(16);

    auto cryptoContext = GenCryptoContext(parameters);

    cryptoContext->Enable(ENCRYPTION);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    ...........................................
```

## Description of the CryptoContext parameters and their restrictions
Choosing the CryptoContext parameters is important for obtaining the best performance for your encrypted application, while maintaining the desired level of security. We strongly recommend that you specify the security level and have OpenFHE automatically select the other parameters, unless you are an expert in homomorphic encryption. If you would like to modify the parameters to understand how they affect noise growth and performance, we provide descriptions below.

The default values for all the parameters can be found in [gen-cryptocontext-params-defaults.h](../include/scheme/gen-cryptocontext-params-defaults.h)

If the set function is called for a parameter which is not available for the given scheme, then an exception will be thrown at run-time.

**PlaintextModulus ptModulus (BGV/BFV only)** - impacts noise growth and has to be set by user as it can not be zero.

**uint32_t digitSize** - used in digit decomposition and impacts noise growth.

**float standardDeviation** - error distribution parameter (recommended for advanced users), used for Gaussian error generation.

**SecretKeyDist secretKeyDist** - secret key distribution: GAUSSIAN, UNIFORM_TERNARY, etc.

**uint32_t maxRelinSkDeg** - max relinearization degree of secret key polynomial (used for lazy relinearization).

**KeySwitchTechnique ksTech**:  BV or HYBRID currently
- For BV we do not have extra modulus, so the security depends on ciphertext modulus Q
- For BV we need digitSize - digit size in digit decomposition
- For HYBRID we do have an extra modulus P, so the security depends on modulus P*Q
- For HYBRID we need numLargeDigits - number of digits in digit decomposition

**ScalingTechnique scalTech (CKKS/BGV only)** - rescaling/modulus switching technique: FIXEDMANUAL, FIXEDAUTO, FLEXIBLEAUTO, FLEXIBLEAUTOEXT. NORESCALE is not allowed (used for BFV internally). see https://eprint.iacr.org/2022/915 for additional details.

**uint32_t batchSize** - max batch size of messages to be packed in encoding (number of slots).

**ProxyReEncryptionMode PREMode** - PRE security mode IND-CPA, FIXED_NOISE_HRA. NOISE_FLOODING_HRA supported only in BGV for scaleTech=FIXEDMANUAL.

**MultipartyMode multipartyMode (BFV/BGV only)** - multiparty security mode. The NOISE_FLOODING_MULTIPARTY mode adds extra noise and gives enhanced security compared to the FIXED_NOISE_MULTIPARTY mode. Not available for CKKS, but FIXED_NOISE_MULTIPARTY is used for CKKS internally

**DecryptionNoiseMode decryptionNoiseMode (CKKS only)** - NOISE_FLOODING_DECRYPT mode is more secure (provable secure) than FIXED_NOISE_DECRYPT, but it requires executing all computations twice.

**ExecutionMode executionMode (CKKS only)** - The execution mode is only used in NOISE_FLOODING_DECRYPT mode:
- EXEC_NOISE_ESTIMATION - we estimate the noise we need to add to the actual computation to guarantee good security.
- EXEC_EVALUATION - we input our noise estimate and perform the desired secure encrypted computation.
- Although not available for BGV/BFV, EXEC_EVALUATION is used for these schemes internally.

**double noiseEstimate (CKKS only)** - This estimate is obtained from running the computation in EXEC_NOISE_ESTIMATION mode. It is only used in the NOISE_FLOODING_DECRYPT mode.

**double desiredPrecision (CKKS only)** - desired precision for 128-bit CKKS. We use this value in NOISE_FLOODING_DECRYPT mode to determine the scaling factor.

**uint32_t statisticalSecurity (BGV/CKKS only)** - statistical security of CKKS in NOISE_FLOODING_DECRYPT mode. This is the bound on the probability of success that any adversary can have. Specifically, they have a probability of success of at most 2^(-statisticalSecurity). Used for BGV when PREMode=NOISE_FLOODING_HRA and for CKKS when multipartyMode=NOISE_FLOODING_MULTIPARTY.

**uint32_t numAdversarialQueries (BGV/CKKS only)** - this is the number of adversarial queries a user is expecting for their application, which we use to ensure security of CKKS in NOISE_FLOODING_DECRYPT mode. Used for BGV when PREMode=NOISE_FLOODING_HRA and for CKKS when multipartyMode=NOISE_FLOODING_MULTIPARTY.

**uint32_t thresholdNumOfParties (BGV/BFV only)** - number of parties in a threshold application, which is used for the bound on the joint secret key.

**uint32_t firstModSize (CKKS/BGV only) and uint32_t scalingModSize** - are used to calculate ciphertext modulus. The ciphertext modulus should be seen as: Q = q_0 * q_1 * ... * q_n * q':
- q_0 is first prime, and it's number of bits is firstModSize
- q_i have same number of bits and is equal to scalingModSize
- the prime q' is not explicitly given, but it is used internally in CKKS and BGV schemes (in *EXT scaling methods)
- **firstModSize** is allowed for BGV with **scalTech = FIXEDMANUAL** only
- **scalingModSize** is allowed for BGV with **scalTech = FIXEDMANUAL** and **scalingModSize** must be < 60 for CKKS and NATIVEINT=64
- **firstModSize and scalingModSize** are not available for BGV if PREMode=NOISE_FLOODING_HRA.

**uint32_t numLargeDigits** - number of digits in HYBRID key switching (see KeySwitchTechnique).

**uint32_t multiplicativeDepth** - the maximum number of multiplications (in a binary tree manner) we can perform before bootstrapping. Must be 0 for BGV if PREMode=NOISE_FLOODING_HRA.

**SecurityLevel securityLevel** - We use the values from the security standard at http://homomorphicencryption.org/wp-content/uploads/2018/11/HomomorphicEncryptionStandardv1.1.pdf. Given the ring dimension and security level, we have upper bound of possible highest modulus (Q for BV or P*Q for HYBRID).

**uint32_t ringDim** - ring dimension N of the scheme : the ring is Z_Q[x] / (X^N+1). Must be > 0 for BGV if PREMode=NOISE_FLOODING_HRA.

**uint32_t evalAddCount (BGV/BFV only)** - maximum number of additions (used for setting noise). In BGV, it is the maximum number of additions at any level.

**EncryptionTechnique encryptionTechnique (BFV only)** - STANDARD or EXTENDED mode for BFV encryption; EXTENDED slightly reduces the size of Q (by few bits) but makes encryption somewhat slower (see https://eprint.iacr.org/2022/915 for details). Although not available for CKKS/BGV, STANDARD is used for these 2 schemes internally

**MultiplicationTechnique multiplicationTechnique (BFV only)** - multiplication method in BFV: BEHZ, HPS, HPSPOVERQ, HPSPOVERLEVELED (see https://eprint.iacr.org/2022/915 for details).

**uint32_t keySwitchCount (BGV/BFV only)** - maximum number of key switching operations (used for setting noise).

**uint32_t PRENumHops (BGV only)** - number of hops supported for PRE in the provable HRA setting:
- used only with multipartyMode=NOISE_FLOODING_MULTIPARTY
- if PREMode=NOISE_FLOODING_HRA, then **PRENumHops** must be > 0

**COMPRESSION_LEVEL interactiveBootCompressionLevel (CKKS only)** - interactive multi-party bootstrapping parameter which sets the compression
level in ciphertext to SLACK (has weaker security assumption, thus less efficient) or COMPACT (has stronger security assumption, thus more efficient)



================================================
FILE: advanced-ckks-bootstrapping.cpp
================================================
/*

Example for CKKS bootstrapping with sparse packing

*/

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

void BootstrapExample(uint32_t numSlots);

int main(int argc, char* argv[]) {
    // We run the example with 8 slots and ring dimension 4096 to illustrate how to run bootstrapping with a sparse plaintext.
    // Using a sparse plaintext and specifying the smaller number of slots gives a performance improvement (typically up to 3x).
    BootstrapExample(8);
}

void BootstrapExample(uint32_t numSlots) {
    // Step 1: Set CryptoContext
    CCParams<CryptoContextCKKSRNS> parameters;

    // A. Specify main parameters
    /*  A1) Secret key distribution
    * The secret key distribution for CKKS should either be SPARSE_TERNARY or UNIFORM_TERNARY.
    * The SPARSE_TERNARY distribution was used in the original CKKS paper,
    * but in this example, we use UNIFORM_TERNARY because this is included in the homomorphic
    * encryption standard.
    */
    SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
    parameters.SetSecretKeyDist(secretKeyDist);

    /*  A2) Desired security level based on FHE standards.
    * In this example, we use the "NotSet" option, so the example can run more quickly with
    * a smaller ring dimension. Note that this should be used only in
    * non-production environments, or by experts who understand the security
    * implications of their choices. In production-like environments, we recommend using
    * HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
    * or 256-bit security, respectively. If you choose one of these as your security level,
    * you do not need to set the ring dimension.
    */
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 12);

    /*  A3) Key switching parameters.
    * By default, we use HYBRID key switching with a digit size of 3.
    * Choosing a larger digit size can reduce complexity, but the size of keys will increase.
    * Note that you can leave these lines of code out completely, since these are the default values.
    */
    parameters.SetNumLargeDigits(3);
    parameters.SetKeySwitchTechnique(HYBRID);

    /*  A4) Scaling parameters.
    * By default, we set the modulus sizes and rescaling technique to the following values
    * to obtain a good precision and performance tradeoff. We recommend keeping the parameters
    * below unless you are an FHE expert.
    */
#if NATIVEINT == 128 && !defined(__EMSCRIPTEN__)
    // Currently, only FIXEDMANUAL and FIXEDAUTO modes are supported for 128-bit CKKS bootstrapping.
    ScalingTechnique rescaleTech = FIXEDAUTO;
    usint dcrtBits               = 78;
    usint firstMod               = 89;
#else
    // All modes are supported for 64-bit CKKS bootstrapping.
    ScalingTechnique rescaleTech = FLEXIBLEAUTO;
    usint dcrtBits               = 59;
    usint firstMod               = 60;
#endif

    parameters.SetScalingModSize(dcrtBits);
    parameters.SetScalingTechnique(rescaleTech);
    parameters.SetFirstModSize(firstMod);

    /*  A4) Bootstrapping parameters.
    * We set a budget for the number of levels we can consume in bootstrapping for encoding and decoding, respectively.
    * Using larger numbers of levels reduces the complexity and number of rotation keys,
    * but increases the depth required for bootstrapping.
	* We must choose values smaller than ceil(log2(slots)). A level budget of {4, 4} is good for higher ring
    * dimensions (65536 and higher).
    */
    std::vector<uint32_t> levelBudget = {3, 3};

    /* We give the user the option of configuring values for an optimization algorithm in bootstrapping.
    * Here, we specify the giant step for the baby-step-giant-step algorithm in linear transforms
    * for encoding and decoding, respectively. Either choose this to be a power of 2
    * or an exact divisor of the number of slots. Setting it to have the default value of {0, 0} allows OpenFHE to choose
    * the values automatically.
    */
    std::vector<uint32_t> bsgsDim = {0, 0};

    /*  A5) Multiplicative depth.
    * The goal of bootstrapping is to increase the number of available levels we have, or in other words,
    * to dynamically increase the multiplicative depth. However, the bootstrapping procedure itself
    * needs to consume a few levels to run. We compute the number of bootstrapping levels required
    * using GetBootstrapDepth, and add it to levelsAvailableAfterBootstrap to set our initial multiplicative
    * depth.
    */
    uint32_t levelsAvailableAfterBootstrap = 10;
    usint depth = levelsAvailableAfterBootstrap + FHECKKSRNS::GetBootstrapDepth(levelBudget, secretKeyDist);
    parameters.SetMultiplicativeDepth(depth);

    // Generate crypto context.
    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    // Enable features that you wish to use. Note, we must enable FHE to use bootstrapping.
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    cryptoContext->Enable(ADVANCEDSHE);
    cryptoContext->Enable(FHE);

    usint ringDim = cryptoContext->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << ringDim << std::endl << std::endl;

    // Step 2: Precomputations for bootstrapping
    cryptoContext->EvalBootstrapSetup(levelBudget, bsgsDim, numSlots);

    // Step 3: Key Generation
    auto keyPair = cryptoContext->KeyGen();
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);
    // Generate bootstrapping keys.
    cryptoContext->EvalBootstrapKeyGen(keyPair.secretKey, numSlots);

    // Step 4: Encoding and encryption of inputs
    // Generate random input
    std::vector<double> x;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    for (size_t i = 0; i < numSlots; i++) {
        x.push_back(dis(gen));
    }

    // Encoding as plaintexts
    // We specify the number of slots as numSlots to achieve a performance improvement.
    // We use the other default values of depth 1, levels 0, and no params.
    // Alternatively, you can also set batch size as a parameter in the CryptoContext as follows:
    // parameters.SetBatchSize(numSlots);
    // Here, we assume all ciphertexts in the cryptoContext will have numSlots slots.
    // We start with a depleted ciphertext that has used up all of its levels.
    Plaintext ptxt = cryptoContext->MakeCKKSPackedPlaintext(x, 1, depth - 1, nullptr, numSlots);
    ptxt->SetLength(numSlots);
    std::cout << "Input: " << ptxt << std::endl;

    // Encrypt the encoded vectors
    Ciphertext<DCRTPoly> ciph = cryptoContext->Encrypt(keyPair.publicKey, ptxt);

    std::cout << "Initial number of levels remaining: " << depth - ciph->GetLevel() << std::endl;

    // Step 5: Perform the bootstrapping operation. The goal is to increase the number of levels remaining
    // for HE computation.
    auto ciphertextAfter = cryptoContext->EvalBootstrap(ciph);

    std::cout << "Number of levels remaining after bootstrapping: " << depth - ciphertextAfter->GetLevel() << std::endl
              << std::endl;

    // Step 7: Decryption and output
    Plaintext result;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextAfter, &result);
    result->SetLength(numSlots);
    std::cout << "Output after bootstrapping \n\t" << result << std::endl;
}



================================================
FILE: advanced-real-numbers-128.cpp
================================================
/*
  Advanced examples for 128-bit implementation of CKKS
 */

// Define PROFILE to enable TIC-TOC timing measurements
#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

void AutomaticRescaleDemo(ScalingTechnique scalTech);
void ManualRescaleDemo(ScalingTechnique scalTech);
void HybridKeySwitchingDemo1();
void HybridKeySwitchingDemo2();
void FastRotationsDemo1();
void FastRotationsDemo2();

int main(int argc, char* argv[]) {
    /*
   * Our 128-bit implementation of CKKS includes two variants called
   * "FIXEDMANUAL" and "FIXEDAUTO", respectively.  Note that 128-bit
   * CKKS supports does not support the FLEXIBLEAUTO mode.
   *
   * To turn on the 128-bit mode, run "cmake -DNATIVE_SIZE=128 .."
   *
   * Before we start, we need to say a few words about the rescale
   * operation, which is central in CKKS. Whenever we multiply two
   * ciphertexts c1 and c2 which encrypt numbers m1*D and m2*D
   * respectively, we get a result that looks like m1*m2*D^2. Since the
   * scaling factor of this number is D^2, we say that the result is of
   * depth 2. It is clear that a ciphertext of depth 2 cannot be added
   * to ciphertexts of depth 1, because their scaling factors are
   * different. Rescaling takes a ciphertext of depth 2, and makes it of
   * depth 1 by an operation that looks a lot like dividing by D=2^p.
   *
   * For efficiency reasons, our implementation of CKKS works in the
   * RNS space, which means that we avoid working with big numbers and
   * we only work with native integers. One complication that arises
   * from this is that we can only rescale by dividing by certain prime
   * numbers and not D=2^p.
   *
   * There are two ways to deal with this. The first is to choose prime
   * numbers as close to 2^p as possible, and assume that the scaling
   * factor remains the same. This inevitably incurs some approximation
   * error, and this is why we refer to it as the FIXEDMANUAL variant.
   * The second way of dealing with this is to track how the scaling
   * factor changes and try to adjust for it. This is what we call the
   * FLEXIBLEAUTO variant of CKKS. Only the approximate approach is supported
   * for 128-bit CKKS. We also include FIXEDAUTO, which is an automated
   * version of FIXEDMANUAL that does all rescaling automatically.
   *
   * We have designed FIXEDAUTO so it hides all the nuances of
   * tracking the depth of ciphertexts and having to call the rescale
   * operation. Therefore, FIXEDAUTO is more appropriate for users
   * who do not want to get into the details of the underlying crypto
   * and math, or who want to put together a quick prototype. On the
   * contrary, FIXEDMANUAL is more appropriate for production
   * applications that have been optimized by experts.
   *
   * The first two parts of this demo introduce the two variants, by
   * implementing the same computation, using both FIXEDAUTO and FIXEDMANUAL.
   *
   */

#if NATIVEINT == 128 && !defined(__EMSCRIPTEN__)
    AutomaticRescaleDemo(FIXEDAUTO);
    // Note that FLEXIBLEAUTO is not supported for 128-bit CKKS

    ManualRescaleDemo(FIXEDMANUAL);

    /*
   * Our implementation of CKKS supports two different algorithms
   * for key switching, namely BV and HYBRID. BV corresponds to
   * a technique also known as digit decomposition (both RNS and based
   * on a digit size). GHS (not implemented separately anymore) corresponds to ciphertext
   * modulus doubling. HYBRID combines the characteristics of both
   * BV and GHS. Please refer to the documentation of KeySwitchBVGen,
   * KeySwitchGHSGen, and KeySwitchHybridGen in keyswitch-bv.h/cpp and keyswitch-hybrid.h/cpp for more
   * details about the different key switch techniques.
   *
   * For most cases, HYBRID will be the most appropriate and efficient
   * key switching technique, and this is why we devote the third and
   * fourth part of this demo to HYBRID key switching.
   */
    HybridKeySwitchingDemo1();
    HybridKeySwitchingDemo2();

    /*
   * The final parts of this demo showcase our implementation of an
   * optimization technique called hoisting. The idea is simple - when
   * we want to perform multiple different rotations to the same
   * ciphertext, we can compute one part of the rotation algorithm once,
   * and reuse it multiple times. Please refer to the documentation of
   * EvalFastRotationPrecompute in keyswitch-bv.h/cpp and keyswitch-hybrid.h/cpp
   * for more details on hoisting in BV and HYBRID key switching.
   */
    FastRotationsDemo1();
    FastRotationsDemo2();
#else
    std::cout << "This demo only runs for 128-bit CKKS." << std::endl;
#endif

    return 0;
}

void AutomaticRescaleDemo(ScalingTechnique scalTech) {
    /* Please read comments in main() for an introduction to what the
   * rescale operation is. Knowing about Rescale() is not necessary
   * to use the FIXEDAUTO CKKS variant, it is however needed to
   * understand what's happening underneath.
   *
   * FIXEDAUTO is a variant of CKKS that automatically
   *    performs rescaling before every multiplication.
   *    This is done to make it easier for users to write FHE
   *    computations without worrying about the depth of ciphertexts
   *    or rescaling.
   */
    if (scalTech == FIXEDAUTO) {
        std::cout << "\n\n\n ===== FixedAutoDemo ============= " << std::endl;
    }

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(6);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);

    // Input
    std::vector<double> x = {1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    /* Computing f(x) = c*x^18 + c*x^9 + d
   *
   * In the following we compute f(x) with a computation
   * that has a multiplicative depth of 5 or 6.
   *
   * The result is correct, even though there is no call to
   * the Rescale() operation.
   */
    auto c2    = cc->EvalMult(c, c);                       // x^2
    auto c4    = cc->EvalMult(c2, c2);                     // x^4
    auto c8    = cc->EvalMult(c4, c4);                     // x^8
    auto c16   = cc->EvalMult(c8, c8);                     // x^16
    auto c9    = cc->EvalMult(c8, c);                      // x^9
    auto c18   = cc->EvalMult(c16, c2);                    // x^18
    auto cRes1 = cc->EvalAdd(cc->EvalAdd(c18, c9), 1.0);   // Final result 1
    auto cRes2 = cc->EvalSub(cc->EvalAdd(c18, c9), 1.0);   // Final result 2
    auto cRes3 = cc->EvalMult(cc->EvalAdd(c18, c9), 0.5);  // Final result 3

    Plaintext result1, result2, result3;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRes1, &result1);
    result1->SetLength(batchSize);
    std::cout << "x^18 + x^9 + 1 = " << result1 << std::endl;

    cc->Decrypt(keys.secretKey, cRes2, &result2);
    result2->SetLength(batchSize);
    std::cout << "x^18 + x^9 - 1 = " << result2 << std::endl;

    cc->Decrypt(keys.secretKey, cRes3, &result3);
    result3->SetLength(batchSize);
    std::cout << "0.5*x^18 + 0.5*x^9 = " << result3 << std::endl;
}

void ManualRescaleDemo(ScalingTechnique scalTech) {
    /* Please read comments in main() for an introduction to what the
   * rescale operation is, and what's the FIXEDMANUAL variant of CKKS.
   *
   * Even though FIXEDMANUAL does not implement automatic rescaling
   * as FIXEDAUTO does, this does not mean that it does not abstract
   * away some of the nitty-gritty details of using CKKS.
   *
   * In CKKS, ciphertexts are defined versus a large ciphertext modulus Q.
   * Whenever we rescale a ciphertext, its ciphertext modulus becomes
   * smaller too. All homomorphic operations require that their inputs are
   * defined over the same ciphertext modulus, and therefore, we need to
   * adjust one of them if their ciphertext moduli do not match. The way
   * this is done in the original CKKS paper is through an operation called
   * Modulus Switch. In our implementation, we call this operation
   * LevelReduce, and both FIXEDMANUAL and FIXEDAUTO do it automatically.
   * As far as we know, automatic level reduce does not incur any performance
   * penalty and this is why it is performed in both FIXEDMANUAL and
   * FIXEDAUTO.
   *
   * Overall, we believe that automatic modulus switching and rescaling make
   * CKKS much easier to use, at least for non-expert users.
   */
    std::cout << "\n\n\n ===== FixedManualDemo ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl << std::endl;

    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);

    // Input
    std::vector<double> x = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    /* Computing f(x) = x^18 + x^9 + 1
   *
   * Compare the following with the corresponding code
   * for FIXEDAUTO. Here we need to track the depth of ciphertexts
   * and call Rescale() whenever needed. In this instance it's still
   * not hard to do so, but this can be quite tedious in other
   * complicated computations (e.g., in bootstrapping).
   *
   */
    // x^2
    auto c2_depth2 = cc->EvalMult(c, c);
    auto c2_depth1 = cc->Rescale(c2_depth2);
    // x^4
    auto c4_depth2 = cc->EvalMult(c2_depth1, c2_depth1);
    auto c4_depth1 = cc->Rescale(c4_depth2);
    // x^8
    auto c8_depth2 = cc->EvalMult(c4_depth1, c4_depth1);
    auto c8_depth1 = cc->Rescale(c8_depth2);
    // x^16
    auto c16_depth2 = cc->EvalMult(c8_depth1, c8_depth1);
    auto c16_depth1 = cc->Rescale(c16_depth2);
    // x^9
    auto c9_depth2 = cc->EvalMult(c8_depth1, c);
    // x^18
    auto c18_depth2 = cc->EvalMult(c16_depth1, c2_depth1);
    // Final result
    auto cRes_depth2 = cc->EvalAdd(cc->EvalAdd(c18_depth2, c9_depth2), 1.0);
    auto cRes_depth1 = cc->Rescale(cRes_depth2);

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRes_depth1, &result);
    result->SetLength(batchSize);
    std::cout << "x^18 + x^9 + 1 = " << result << std::endl;
}

void HybridKeySwitchingDemo1() {
    /*
   * Please refer to comments in the demo-simple_real_number.cpp
   * for a brief introduction on what key switching is and to
   * find reference for HYBRID key switching.
   *
   * In this demo, we focus on how to choose the number of digits
   * in HYBRID key switching, and how that affects the usage and
   * efficiency of the CKKS scheme.
   *
   */

    std::cout << "\n\n\n ===== HybridKeySwitchingDemo1 ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FIXEDAUTO);
    // uint32_t ringDimension = 0;  // 0 means the library will choose it based on securityLevel
    /*
   * dnum is the number of large digits in HYBRID decomposition
   *
   * If not supplied (or value 0 is supplied), the default value is
   * set as follows:
   * - If multiplicative depth is > 3, then dnum = 3 digits are used.
   * - If multiplicative depth is 3, then dnum = 2 digits are used.
   * - If multiplicative depth is < 3, then dnum is set to be equal to
   * multDepth+1
   */

    uint32_t dnum = 2;
    /* To understand the effects of changing dnum, it is important to
   * understand how the ciphertext modulus size changes during key
   * switching.
   *
   * In our RNS implementation of CKKS, every ciphertext corresponds
   * to a large number (which is represented as small integers in RNS)
   * modulo a ciphertext modulus Q, which is defined as the product of
   * (multDepth+1) prime numbers: Q = q0 * q1 * ... * qL. Each qi is
   * selected to be close to the scaling factor D=2^p, hence the total
   * size of Q is approximately:
   *
   * sizeof(Q) = (multDepth+1)*scaleModSize.
   *
   * HYBRID key switching takes a number d that's defined modulo Q,
   * and performs 4 steps:
   * 1 - Digit decomposition:
   *     Split d into dnum digits - the size of each digit is roughly
   *     ceil(sizeof(Q)/dnum)
   * 2 - Extend ciphertext modulus from Q to Q*P
   *     Here P is a product of special primes
   * 3 - Multiply extended component with key switching key
   * 4 - Decrease the ciphertext modulus back down to Q
   *
   * It's not necessary to understand how all these stages work, as
   * long as it's clear that the size of the ciphertext modulus is
   * increased from sizeof(Q) to sizeof(Q)+sizeof(P) in stage 2. P
   * is always set to be as small as possible, as long as sizeof(P)
   * is larger than the size of the largest digit, i.e., than
   * ceil(sizeof(Q)/dnum). Therefore, the size of P is inversely
   * related to the number of digits, so the more digits we have, the
   * smaller P has to be.
   *
   * The tradeoff here is that more digits means that the digit
   * decomposition stage becomes more expensive, but the maximum
   * size of the ciphertext modulus Q*P becomes smaller. Since
   * the size of Q*P determines the necessary ring dimension to
   * achieve a certain security level, more digits can in some
   * cases mean that we can use smaller ring dimension and get
   * better performance overall.
   *
   * We show this effect with demos HybridKeySwitchingDemo1 and
   * HybridKeySwitchingDemo2.
   *
   */
    parameters.SetNumLargeDigits(dnum);
    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl;

    std::cout << "- Using HYBRID key switching with " << dnum << " digits" << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Input
    std::vector<double> x = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    TimeVar t;
    TIC(t);
    auto cRot1         = cc->EvalRotate(c, 1);
    auto cRot2         = cc->EvalRotate(cRot1, -2);
    double time2digits = TOC(t);
    // Take note and compare the runtime to the runtime
    // of the same computation in the next demo.

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRot2, &result);
    result->SetLength(batchSize);
    std::cout << "x rotate by -1 = " << result << std::endl;
    std::cout << " - 2 rotations with HYBRID (2 digits) took " << time2digits << "ms" << std::endl;

    /* Interested users may set the following if to 1
   * to observe the prime numbers comprising Q and P,
   * and how these change with the number of digits
   * dnum.
   */
#if 0
  const auto cryptoParamsCKKS =
      std::dynamic_pointer_cast<CryptoParametersCKKSRNS>(
          cc->GetCryptoParameters());

  auto paramsQ = cc->GetElementParams()->GetParams();
  std::cout << "\nModuli in Q:" << std::endl;
  for (uint32_t i = 0; i < paramsQ.size(); i++) {
    // q0 is a bit larger because its default size is 60 bits.
    // One can change this by supplying the firstModSize argument
    // in genCryptoContextCKKS.
    std::cout << "q" << i << ": " << paramsQ[i]->GetModulus() << std::endl;
  }
  auto paramsQP = cryptoParamsCKKS->GetParamsQP();
  std::cout << "Moduli in P: " << std::endl;
  BigInteger P = BigInteger(1);
  for (uint32_t i = 0; i < paramsQP->GetParams().size(); i++) {
    if (i > paramsQ.size()) {
      P = P * BigInteger(paramsQP->GetParams()[i]->GetModulus());
      std::cout << "p" << i - paramsQ.size() << ": "
                << paramsQP->GetParams()[i]->GetModulus() << std::endl;
    }
  }
  auto QBitLength = cc->GetModulus().GetLengthForBase(2);
  auto PBitLength = P.GetLengthForBase(2);
  std::cout << "\nQ = " << cc->GetModulus() << " (bit length: " << QBitLength
            << ")" << std::endl;
  std::cout << "P = " << P << " (bit length: " << PBitLength << ")"
            << std::endl;
  std::cout << "Total bit-length of ciphertext modulus: "
            << QBitLength + PBitLength << std::endl;
  std::cout << "Given this ciphertext modulus, a ring dimension of "
            << cc->GetRingDimension() << " gives us 128-bit security."
            << std::endl;
#endif
}

void HybridKeySwitchingDemo2() {
    /*
   * Please refer to comments in HybridKeySwitchingDemo1.
   *
   */

    std::cout << "\n\n\n ===== HybridKeySwitchingDemo2 ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FIXEDAUTO);

    // uint32_t ringDimension = 0;  // 0 means the library will choose it based on securityLevel
    /*
   * Here we use dnum = 3 digits. Even though 3 digits are
   * more than the two digits in the previous demo and the
   * cost of digit decomposition is higher, the increase in
   * digits means that individual digits are smaller, and we
   * can perform key switching by using only one special
   * prime in P (instead of two in the previous demo).
   *
   * This also means that the maximum size of ciphertext
   * modulus in key switching is smaller by 60 bits, and it
   * turns out that this decrease is adequate to warrant a
   * smaller ring dimension to achieve the same security
   * level (128-bits).
   *
   */
    uint32_t dnum = 3;

    parameters.SetNumLargeDigits(dnum);
    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Compare the ring dimension in this demo to the one in
    // the previous.
    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl;

    std::cout << "- Using HYBRID key switching with " << dnum << " digits" << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Input
    std::vector<double> x = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    TimeVar t;
    TIC(t);
    auto cRot1 = cc->EvalRotate(c, 1);
    auto cRot2 = cc->EvalRotate(cRot1, -2);
    // The runtime here is smaller than in the previous demo.
    double time3digits = TOC(t);

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRot2, &result);
    result->SetLength(batchSize);
    std::cout << "x rotate by -1 = " << result << std::endl;
    std::cout << " - 2 rotations with HYBRID (3 digits) took " << time3digits << "ms" << std::endl;

    /* Interested users may set the following if to 1
   * to observe the prime numbers comprising Q and P,
   * and how these change with the number of digits
   * dnum.
   */
#if 0
  const auto cryptoParamsCKKS =
      std::dynamic_pointer_cast<CryptoParametersCKKSRNS>(
          cc->GetCryptoParameters());

  auto paramsQ = cc->GetElementParams()->GetParams();
  std::cout << "\nModuli in Q:" << std::endl;
  for (uint32_t i = 0; i < paramsQ.size(); i++) {
    // q0 is a bit larger because its default size is 60 bits.
    // One can change this by supplying the firstModSize argument
    // in genCryptoContextCKKS.
    std::cout << "q" << i << ": " << paramsQ[i]->GetModulus() << std::endl;
  }
  auto paramsQP = cryptoParamsCKKS->GetParamsQP();
  std::cout << "Moduli in P: " << std::endl;
  BigInteger P = BigInteger(1);
  for (uint32_t i = 0; i < paramsQP->GetParams().size(); i++) {
    if (i > paramsQ.size()) {
      P = P * BigInteger(paramsQP->GetParams()[i]->GetModulus());
      std::cout << "p" << i - paramsQ.size() << ": "
                << paramsQP->GetParams()[i]->GetModulus() << std::endl;
    }
  }
  auto QBitLength = cc->GetModulus().GetLengthForBase(2);
  auto PBitLength = P.GetLengthForBase(2);
  std::cout << "\nQ = " << cc->GetModulus() << " (bit length: " << QBitLength
            << ")" << std::endl;
  std::cout << "P = " << P << " (bit length: " << PBitLength << ")"
            << std::endl;
  std::cout << "Given this ciphertext modulus, a ring dimension of "
            << cc->GetRingDimension() << " gives us 128-bit security."
            << std::endl;
#endif
}

void FastRotationsDemo1() {
    /*
   * In CKKS, whenever someone applies a rotation R() to a ciphertext
   * encrypted with key s, we get a result which is not valid under
   * key s, but under the same rotation R(s) of s. Therefore, after
   * every rotation we need to perform key switching, making them as
   * expensive as multiplications.
   *
   * As mentioned earlier (in comments of HybridKeySwitchingDemo1),
   * key switching involves the following steps:
   * 1 - Digit decomposition
   * 2 - Extend ciphertext modulus from Q to Q*P
   * 3 - Multiply extended component with key switching key
   * 4 - Decrease the ciphertext modulus back down to Q
   *
   * A useful observation is that the first two steps are independent
   * of the particular rotation we want to perform. Steps 3-4 on the
   * other hand depend on the specific rotation we have at hand,
   * because each rotation index has a different key switch key.
   *
   * This observation means that, if we want to perform multiple
   * different rotations to the same ciphertext, we can perform
   * the first two steps once, and then only perform steps 3-4 for
   * each rotation. This technique is called hoisting, and we have
   * implemented it for all three key switching techniques (BV, GHS,
   * HYBRID) in OpenFHE.
   *
   * The benefits expected by this technique differ depending on the
   * key switching algorithms we're using. BV is the technique that
   * gets the greatest benefits, because the digit decomposition is
   * the most expensive part. However, HYBRID also benefits from
   * hoisting, and we show this in this part of the demo.
   *
   */

    std::cout << "\n\n\n ===== FastRotationsDemo1 ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    uint32_t N = cc->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << N << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, 2, 3, 4, 5, 6, 7});

    // Input
    std::vector<double> x = {0, 0, 0, 0, 0, 0, 0, 1};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    Ciphertext<DCRTPoly> cRot1, cRot2, cRot3, cRot4, cRot5, cRot6, cRot7;

    // First, we perform 7 regular (non-hoisted) rotations
    // and measure the runtime.
    TimeVar t;
    TIC(t);
    cRot1                 = cc->EvalRotate(c, 1);
    cRot2                 = cc->EvalRotate(c, 2);
    cRot3                 = cc->EvalRotate(c, 3);
    cRot4                 = cc->EvalRotate(c, 4);
    cRot5                 = cc->EvalRotate(c, 5);
    cRot6                 = cc->EvalRotate(c, 6);
    cRot7                 = cc->EvalRotate(c, 7);
    double timeNoHoisting = TOC(t);

    auto cResNoHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    // M is the cyclotomic order and we need it to call EvalFastRotation
    uint32_t M = 2 * N;

    // Then, we perform 7 rotations with hoisting.
    TIC(t);
    auto cPrecomp       = cc->EvalFastRotationPrecompute(c);
    cRot1               = cc->EvalFastRotation(c, 1, M, cPrecomp);
    cRot2               = cc->EvalFastRotation(c, 2, M, cPrecomp);
    cRot3               = cc->EvalFastRotation(c, 3, M, cPrecomp);
    cRot4               = cc->EvalFastRotation(c, 4, M, cPrecomp);
    cRot5               = cc->EvalFastRotation(c, 5, M, cPrecomp);
    cRot6               = cc->EvalFastRotation(c, 6, M, cPrecomp);
    cRot7               = cc->EvalFastRotation(c, 7, M, cPrecomp);
    double timeHoisting = TOC(t);
    // The time with hoisting should be faster than without hoisting.

    auto cResHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cResNoHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result without hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x without hoisting took " << timeNoHoisting << "ms" << std::endl;

    cc->Decrypt(keys.secretKey, cResHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result with hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x with hoisting took " << timeHoisting << "ms" << std::endl;
}

void FastRotationsDemo2() {
    /*
   * This demo is identical to the previous one, with the exception
   * that we use BV key switching instead of HYBRID.
   *
   * The benefits expected by hoisting differ depending on the
   * key switching algorithms we're using. BV is the technique that
   * gets the greatest benefits, because the digit decomposition is
   * the most expensive part. However, HYBRID also benefits from
   * hoisting, and we show this in this part of the demo.
   *
   */

    std::cout << "\n\n\n ===== FastRotationsDemo2 ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(90);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FIXEDAUTO);
    parameters.SetKeySwitchTechnique(BV);
    /*
   * This controls how many multiplications are possible without rescaling.
   * The number of multiplications (maxRelinSkDeg) is maxDepth - 1.
   * This is useful for an optimization technique called lazy
   * re-linearization (only applicable in FIXEDMANUAL, as
   * FIXEDAUTO implements automatic rescaling).
   */
    // This is the size of the first modulus
    // by default, firstModSize is set to 105
    uint32_t firstModSize = 100;
    /*
   * The digit size is only used in BV key switching and
   * it allows us to perform digit decomposition at a finer granularity.
   * Under normal circumstances, digit decomposition is what we call
   * RNS decomposition, i.e., each digit is roughly the size of the
   * qi's that comprise the ciphertext modulus Q. When using BV, in
   * certain cases like having to perform rotations without any
   * preceding multiplication, we need to have smaller digits to prevent
   * noise from corrupting the result. In this case, using digitSize = 10
   * does the trick. Users are encouraged to set this to 0 (i.e., RNS
   * decomposition) and see how the results are incorrect.
   */
    uint32_t digitSize = 10;

    parameters.SetFirstModSize(firstModSize);
    parameters.SetDigitSize(digitSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    uint32_t N = cc->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << N << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, 2, 3, 4, 5, 6, 7});

    // Input
    std::vector<double> x = {0, 0, 0, 0, 0, 0, 0, 1};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    Ciphertext<DCRTPoly> cRot1, cRot2, cRot3, cRot4, cRot5, cRot6, cRot7;

    // First, we perform 7 regular (non-hoisted) rotations
    // and measure the runtime.
    TimeVar t;
    TIC(t);
    cRot1                 = cc->EvalRotate(c, 1);
    cRot2                 = cc->EvalRotate(c, 2);
    cRot3                 = cc->EvalRotate(c, 3);
    cRot4                 = cc->EvalRotate(c, 4);
    cRot5                 = cc->EvalRotate(c, 5);
    cRot6                 = cc->EvalRotate(c, 6);
    cRot7                 = cc->EvalRotate(c, 7);
    double timeNoHoisting = TOC(t);

    auto cResNoHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    // M is the cyclotomic order and we need it to call EvalFastRotation
    uint32_t M = 2 * N;

    // Then, we perform 7 rotations with hoisting.
    TIC(t);
    auto cPrecomp       = cc->EvalFastRotationPrecompute(c);
    cRot1               = cc->EvalFastRotation(c, 1, M, cPrecomp);
    cRot2               = cc->EvalFastRotation(c, 2, M, cPrecomp);
    cRot3               = cc->EvalFastRotation(c, 3, M, cPrecomp);
    cRot4               = cc->EvalFastRotation(c, 4, M, cPrecomp);
    cRot5               = cc->EvalFastRotation(c, 5, M, cPrecomp);
    cRot6               = cc->EvalFastRotation(c, 6, M, cPrecomp);
    cRot7               = cc->EvalFastRotation(c, 7, M, cPrecomp);
    double timeHoisting = TOC(t);
    /* The time with hoisting should be faster than without hoisting.
   * Also, the benefits from hoisting should be more pronounced in this
   * case because we're using BV. Of course, we also observe less
   * accurate results than when using HYBRID, because of using
   * digitSize = 10 (Users can decrease digitSize to see the accuracy
   * increase, and performance decrease).
   */

    auto cResHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cResNoHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result without hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x without hoisting took " << timeNoHoisting << "ms" << std::endl;

    cc->Decrypt(keys.secretKey, cResHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result with hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x with hoisting took " << timeHoisting << "ms" << std::endl;
}



================================================
FILE: advanced-real-numbers.cpp
================================================
/*
  Advanced examples CKKS
 */

// Define PROFILE to enable TIC-TOC timing measurements
#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

void AutomaticRescaleDemo(ScalingTechnique scalTech);
void ManualRescaleDemo(ScalingTechnique scalTech);
void HybridKeySwitchingDemo1();
void HybridKeySwitchingDemo2();
void FastRotationsDemo1();
void FastRotationsDemo2();

int main(int argc, char* argv[]) {
    /*
   * Our implementation of CKKS includes four rescaling methods called
   * "FIXEDMANUAL*, *FIXEDAUTO*, "FLEXIBLEAUTO", and "FLEXIBLEAUTOEXT".
   * THese rescaling methods are explained in the CKKS section of
   * https://eprint.iacr.org/2022/915.
   *
   * Before we start, we need to say a few words about the rescale
   * operation, which is central in CKKS. Whenever we multiply two
   * ciphertexts c1 and c2 which encrypt numbers m1*D and m2*D
   * respectively, we get a result that looks like m1*m2*D^2. Since the
   * scaling factor of this number is D^2, we say that the result is of
   * depth 2. It is clear that a ciphertext of depth 2 cannot be added
   * to ciphertexts of depth 1, because their scaling factors are
   * different. Rescaling takes a ciphertext of depth 2, and makes it of
   * depth 1 by an operation that looks a lot like dividing by D=2^p.
   *
   * For efficiency reasons, our implementation of CKKS works in the
   * RNS space, which means that we avoid working with big numbers and
   * we only work with native integers. One complication that arises
   * from this is that we can only rescale by dividing by certain prime
   * numbers and not D=2^p.
   *
   * There are two ways to deal with this. The first is to choose prime
   * numbers as close to 2^p as possible, and assume that the scaling
   * factor remains the same. This inevitably incurs some approximation
   * error, and there are two variants for this scenario: FLEXIBLEAUTO
   * and FLEXIBLEAUTOEXT.
   *
   * The second way of dealing with this is to track how the scaling
   * factor changes and try to adjust for it. This is what we do for the
   * FLEXIBLEAUTO and FLEXIBALEAUTOEXT variants of CKKS. The tradeoff is
   * that FLEXIBLEAUTO*    * computations are typically somewhat slower (based on our experience
   * the slowdown is around 5-35% depending on the complexity of the
   * computation), because of the adjustment of values that need to
   * take place.
   *
   * We have designed FLEXIBLEAUTO(EXT) so it hides all the nuances of
   * tracking the depth of ciphertexts and having to call the rescale
   * operation. Therefore, FLEXIBLEAUTO(EXT) is more appropriate for users
   * who do not want to get into the details of the underlying crypto
   * and math, or who want to put together a quick prototype. On the
   * contrary, FIXEDMANUAL is more appropriate for production
   * applications that have been optimized by experts.
   *
   * The first two parts of this demo implement the same computation, i.e, the function
   * f(x) = x^18 + x^9 + 1, using all four methods.
   *
   */
    AutomaticRescaleDemo(FLEXIBLEAUTO);
    // default
    AutomaticRescaleDemo(FLEXIBLEAUTOEXT);
    AutomaticRescaleDemo(FIXEDAUTO);
    ManualRescaleDemo(FIXEDMANUAL);

    /*
   * Our implementation of CKKS supports two different algorithms
   * for key switching, namely BV and HYBRID. BV corresponds to
   * a technique also known as digit decomposition (both RNS and based
   * on a digit size). GHS (not implemented separately anymore) corresponds to ciphertext
   * modulus doubling, and HYBRID combines the characteristics of both
   * BV and GHS. Please refer to the documentation of KeySwitchGen in
   * keyswitch-bv.h/cpp and keyswitch-hybrid.h/cpp for more
   * details about the different key switch techniques.
   *
   * For most cases, HYBRID will be the most appropriate and efficient
   * key switching technique, and this is why we devote the third and
   * fourth part of this demo to HYBRID key switching.
   */
    HybridKeySwitchingDemo1();
    HybridKeySwitchingDemo2();

    /*
   * The final parts of this demo showcase our implementation of an
   * optimization technique called hoisting. The idea is simple - when
   * we want to perform multiple different rotations to the same
   * ciphertext, we can compute one part of the rotation algorithm once,
   * and reuse it multiple times. Please refer to the documentation of
   * EvalFastRotationPrecompute in keyswitch-bv.h/cpp and keyswitch-hybrid.h/cpp
   * for more details on hoisting in BV and HYBRID key switching.
   */
    FastRotationsDemo1();
    FastRotationsDemo2();

    return 0;
}

void AutomaticRescaleDemo(ScalingTechnique scalTech) {
    /* Please read comments in main() for an introduction to what the
   * rescale operation is. Knowing about Rescale() is not necessary
   * to use the FLEXIBLEAUTO CKKS variant, it is however needed to
   * understand what's happening underneath.
   *
   * FLEXIBLEAUTO is a variant of CKKS that has two main features:
   * 1 - It automatically performs rescaling before every multiplication.
   *    This is done to make it easier for users to write FHE
   *    computations without worrying about the depth of ciphertexts
   *    or rescaling.
   * 2 - It tracks the exact scaling factor of all ciphertexts.
   *    This means that computations in FLEXIBLEAUTO will be more
   *    accurate than the same computations in FIXEDMANUAL. Keep
   *    in mind that this difference only becomes apparent when
   *    dealing with computations of large multiplicative depth; this
   *    is because a large multiplicative depth means we need to find
   *    more prime numbers sufficiently close to D=2^p, and this
   *    becomes harder and harder as the multiplicative depth
   *    increases.
   */
    if (scalTech == FLEXIBLEAUTO) {
        std::cout << std::endl << std::endl << std::endl << " ===== FlexibleAutoDemo ============= " << std::endl;
    }
    else if (scalTech == FLEXIBLEAUTOEXT) {
        std::cout << std::endl << std::endl << std::endl << " ===== FlexibleAutoExtDemo ============= " << std::endl;
    }
    else {
        std::cout << std::endl << std::endl << std::endl << " ===== FixedAutoDemo ============= " << std::endl;
    }

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(50);
    parameters.SetScalingTechnique(scalTech);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);

    // Input
    std::vector<double> x = {1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(ptxt, keys.publicKey);

    /* Computing f(x) = x^18 + x^9 + 1
   *
   * In the following we compute f(x) with a computation
   * that has a multiplicative depth of 5.
   *
   * The result is correct, even though there is no call to
   * the Rescale() operation.
   */
    auto c2   = cc->EvalMult(c, c);                      // x^2
    auto c4   = cc->EvalMult(c2, c2);                    // x^4
    auto c8   = cc->EvalMult(c4, c4);                    // x^8
    auto c16  = cc->EvalMult(c8, c8);                    // x^16
    auto c9   = cc->EvalMult(c8, c);                     // x^9
    auto c18  = cc->EvalMult(c16, c2);                   // x^18
    auto cRes = cc->EvalAdd(cc->EvalAdd(c18, c9), 1.0);  // Final result

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(cRes, keys.secretKey, &result);
    result->SetLength(batchSize);
    std::cout << "x^18 + x^9 + 1 = " << result << std::endl;
}

void ManualRescaleDemo(ScalingTechnique scalTech) {
    /* Please read comments in main() for an introduction to what the
   * rescale operation is, and what's the FIXEDMANUAL variant of CKKS.
   *
   * Even though FIXEDMANUAL does not implement automatic rescaling
   * as FLEXIBLEAUTO does, this does not mean that it does not abstract
   * away some of the nitty-gritty details of using CKKS.
   *
   * In CKKS, ciphertexts are defined versus a large ciphertext modulus Q.
   * Whenever we rescale a ciphertext, its ciphertext modulus becomes
   * smaller too. All homomorphic operations require that their inputs are
   * defined over the same ciphertext modulus, and therefore, we need to
   * adjust one of them if their ciphertext moduli do not match. The way
   * this is done in the original CKKS paper is through an operation called
   * Modulus Switch. In our implementation, we call this operation
   * LevelReduce, and both FIXEDMANUAL and FLEXIBLEAUTO do it automatically.
   * As far as we know, automatic level reduce does not incur any performance
   * penalty and this is why it is performed in both FIXEDMANUAL and
   * FLEXIBLEAUTO.
   *
   * Overall, we believe that automatic modulus switching and rescaling make
   * CKKS much easier to use, at least for non-expert users.
   */
    std::cout << "\n\n\n ===== FixedManualDemo ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);

    // Input
    std::vector<double> x = {1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    /* Computing f(x) = x^18 + x^9 + 1
   *
   * Compare the following with the corresponding code
   * for FLEXIBLEAUTO. Here we need to track the depth of ciphertexts
   * and call Rescale() whenever needed. In this instance it's still
   * not hard to do so, but this can be quite tedious in other
   * complicated computations (e.g., in bootstrapping).
   *
   */
    // x^2
    auto c2_depth2 = cc->EvalMult(c, c);
    auto c2_depth1 = cc->Rescale(c2_depth2);
    // x^4
    auto c4_depth2 = cc->EvalMult(c2_depth1, c2_depth1);
    auto c4_depth1 = cc->Rescale(c4_depth2);
    // x^8
    auto c8_depth2 = cc->EvalMult(c4_depth1, c4_depth1);
    auto c8_depth1 = cc->Rescale(c8_depth2);
    // x^16
    auto c16_depth2 = cc->EvalMult(c8_depth1, c8_depth1);
    auto c16_depth1 = cc->Rescale(c16_depth2);
    // x^9
    auto c9_depth2 = cc->EvalMult(c8_depth1, c);
    // x^18
    auto c18_depth2 = cc->EvalMult(c16_depth1, c2_depth1);
    // Final result
    auto cRes_depth2 = cc->EvalAdd(cc->EvalAdd(c18_depth2, c9_depth2), 1.0);
    auto cRes_depth1 = cc->Rescale(cRes_depth2);

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRes_depth1, &result);
    result->SetLength(batchSize);
    std::cout << "x^18 + x^9 + 1 = " << result << std::endl;
}

void HybridKeySwitchingDemo1() {
    /*
   * Please refer to comments in the demo-simple_real_number.cpp
   * for a brief introduction on what key switching is and to
   * find reference for HYBRID key switching.
   *
   * In this demo, we focus on how to choose the number of digits
   * in HYBRID key switching, and how that affects the usage and
   * efficiency of the CKKS scheme.
   *
   */

    std::cout << "\n\n\n ===== HybridKeySwitchingDemo1 ============= " << std::endl;
    /*
   * dnum is the number of large digits in HYBRID decomposition
   *
   * If not supplied (or value 0 is supplied), the default value is
   * set as follows:
   * - If multiplicative depth is > 3, then dnum = 3 digits are used.
   * - If multiplicative depth is 3, then dnum = 2 digits are used.
   * - If multiplicative depth is < 3, then dnum is set to be equal to
   * multDepth+1
   */
    uint32_t dnum = 2;
    /* To understand the effects of changing dnum, it is important to
   * understand how the ciphertext modulus size changes during key
   * switching.
   *
   * In our RNS implementation of CKKS, every ciphertext corresponds
   * to a large number (which is represented as small integers in RNS)
   * modulo a ciphertext modulus Q, which is defined as the product of
   * (multDepth+1) prime numbers: Q = q0 * q1 * ... * qL. Each qi is
   * selected to be close to the scaling factor D=2^p, hence the total
   * size of Q is approximately:
   *
   * sizeof(Q) = (multDepth+1)*scaleModSize.
   *
   * HYBRID key switching takes a number d that's defined modulo Q,
   * and performs 4 steps:
   * 1 - Digit decomposition:
   *     Split d into dnum digits - the size of each digit is roughly
   *     ceil(sizeof(Q)/dnum)
   * 2 - Extend ciphertext modulus from Q to Q*P
   *     Here P is a product of special primes
   * 3 - Multiply extended component with key switching key
   * 4 - Decrease the ciphertext modulus back down to Q
   *
   * It's not necessary to understand how all these stages work, as
   * long as it's clear that the size of the ciphertext modulus is
   * increased from sizeof(Q) to sizeof(Q)+sizeof(P) in stage 2. P
   * is always set to be as small as possible, as long as sizeof(P)
   * is larger than the size of the largest digit, i.e., than
   * ceil(sizeof(Q)/dnum). Therefore, the size of P is inversely
   * related to the number of digits, so the more digits we have, the
   * smaller P has to be.
   *
   * The tradeoff here is that more digits means that the digit
   * decomposition stage becomes more expensive, but the maximum
   * size of the ciphertext modulus Q*P becomes smaller. Since
   * the size of Q*P determines the necessary ring dimension to
   * achieve a certain security level, more digits can in some
   * cases mean that we can use smaller ring dimension and get
   * better performance overall.
   *
   * We show this effect with demos HybridKeySwitchingDemo1 and
   * HybridKeySwitchingDemo2.
   *
   */
    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FLEXIBLEAUTO);
    parameters.SetNumLargeDigits(dnum);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl;

    std::cout << "- Using HYBRID key switching with " << dnum << " digits" << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Input
    std::vector<double> x = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    TimeVar t;
    TIC(t);
    auto cRot1         = cc->EvalRotate(c, 1);
    auto cRot2         = cc->EvalRotate(cRot1, -2);
    double time2digits = TOC(t);
    // Take note and compare the runtime to the runtime
    // of the same computation in the next demo.

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRot2, &result);
    result->SetLength(batchSize);
    std::cout << "x rotate by -1 = " << result << std::endl;
    std::cout << " - 2 rotations with HYBRID (2 digits) took " << time2digits << "ms" << std::endl;
}

void HybridKeySwitchingDemo2() {
    /*
   * Please refer to comments in HybridKeySwitchingDemo1.
   *
   */

    std::cout << "\n\n\n ===== HybridKeySwitchingDemo2 ============= " << std::endl;

    /*
   * Here we use dnum = 3 digits. Even though 3 digits are
   * more than the two digits in the previous demo and the
   * cost of digit decomposition is higher, the increase in
   * digits means that individual digits are smaller, and we
   * can perform key switching by using only one special
   * prime in P (instead of two in the previous demo).
   *
   * This also means that the maximum size of ciphertext
   * modulus in key switching is smaller by 60 bits, and it
   * turns out that this decrease is adequate to warrant a
   * smaller ring dimension to achieve the same security
   * level (128-bits).
   *
   */
    uint32_t dnum = 3;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(5);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FLEXIBLEAUTO);
    parameters.SetNumLargeDigits(dnum);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Compare the ring dimension in this demo to the one in
    // the previous.
    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension() << std::endl;

    std::cout << "- Using HYBRID key switching with " << dnum << " digits" << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Input
    std::vector<double> x = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    TimeVar t;
    TIC(t);
    auto cRot1 = cc->EvalRotate(c, 1);
    auto cRot2 = cc->EvalRotate(cRot1, -2);
    // The runtime here is smaller than in the previous demo.
    double time3digits = TOC(t);

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cRot2, &result);
    result->SetLength(batchSize);
    std::cout << "x rotate by -1 = " << result << std::endl;
    std::cout << " - 2 rotations with HYBRID (3 digits) took " << time3digits << "ms" << std::endl;

}

void FastRotationsDemo1() {
    /*
   * In CKKS, whenever someone applies a rotation R() to a ciphertext
   * encrypted with key s, we get a result which is not valid under
   * key s, but under the same rotation R(s) of s. Therefore, after
   * every rotation we need to perform key switching, making them as
   * expensive as multiplications.
   *
   * As mentioned earlier (in comments of HybridKeySwitchingDemo1),
   * key switching involves the following steps:
   * 1 - Digit decomposition
   * 2 - Extend ciphertext modulus from Q to Q*P
   * 3 - Multiply extended component with key switching key
   * 4 - Decrease the ciphertext modulus back down to Q
   *
   * A useful observation is that the first two steps are independent
   * of the particular rotation we want to perform. Steps 3-4 on the
   * other hand depend on the specific rotation we have at hand,
   * because each rotation index has a different key switch key.
   *
   * This observation means that, if we want to perform multiple
   * different rotations to the same ciphertext, we can perform
   * the first two steps once, and then only perform steps 3-4 for
   * each rotation. This technique is called hoisting, and we have
   * implemented it for all three key switching techniques (BV, GHS,
   * HYBRID) in OpenFHE.
   *
   * The benefits expected by this technique differ depending on the
   * key switching algorithms we're using. BV is the technique that
   * gets the greatest benefits, because the digit decomposition is
   * the most expensive part. However, HYBRID also benefits from
   * hoisting, and we show this in this part of the demo.
   *
   */

    std::cout << "\n\n\n ===== FastRotationsDemo1 ============= " << std::endl;

    uint32_t batchSize = 8;
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    uint32_t N = cc->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << N << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, 2, 3, 4, 5, 6, 7});

    // Input
    std::vector<double> x = {0, 0, 0, 0, 0, 0, 0, 1};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    Ciphertext<DCRTPoly> cRot1, cRot2, cRot3, cRot4, cRot5, cRot6, cRot7;

    // First, we perform 7 regular (non-hoisted) rotations
    // and measure the runtime.
    TimeVar t;
    TIC(t);
    cRot1                 = cc->EvalRotate(c, 1);
    cRot2                 = cc->EvalRotate(c, 2);
    cRot3                 = cc->EvalRotate(c, 3);
    cRot4                 = cc->EvalRotate(c, 4);
    cRot5                 = cc->EvalRotate(c, 5);
    cRot6                 = cc->EvalRotate(c, 6);
    cRot7                 = cc->EvalRotate(c, 7);
    double timeNoHoisting = TOC(t);

    auto cResNoHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    // M is the cyclotomic order and we need it to call EvalFastRotation
    uint32_t M = 2 * N;

    // Then, we perform 7 rotations with hoisting.
    TIC(t);
    auto cPrecomp       = cc->EvalFastRotationPrecompute(c);
    cRot1               = cc->EvalFastRotation(c, 1, M, cPrecomp);
    cRot2               = cc->EvalFastRotation(c, 2, M, cPrecomp);
    cRot3               = cc->EvalFastRotation(c, 3, M, cPrecomp);
    cRot4               = cc->EvalFastRotation(c, 4, M, cPrecomp);
    cRot5               = cc->EvalFastRotation(c, 5, M, cPrecomp);
    cRot6               = cc->EvalFastRotation(c, 6, M, cPrecomp);
    cRot7               = cc->EvalFastRotation(c, 7, M, cPrecomp);
    double timeHoisting = TOC(t);
    // The time with hoisting should be faster than without hoisting.

    auto cResHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cResNoHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result without hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x without hoisting took " << timeNoHoisting << "ms" << std::endl;

    cc->Decrypt(keys.secretKey, cResHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result with hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x with hoisting took " << timeHoisting << "ms" << std::endl;
}

void FastRotationsDemo2() {
    /*
   * This demo is identical to the previous one, with the exception
   * that we use BV key switching instead of HYBRID.
   *
   * The benefits expected by hoisting differ depending on the
   * key switching algorithms we're using. BV is the technique that
   * gets the greatest benefits, because the digit decomposition is
   * the most expensive part. However, HYBRID also benefits from
   * hoisting, and we show this in this part of the demo.
   *
   */

    std::cout << "\n\n\n ===== FastRotationsDemo2 ============= " << std::endl;

    // uint32_t dnum = 0;  -already default
    /*
   * This controls how many multiplications are possible without rescaling.
   * The number of multiplications (maxRelinSkDeg) is maxDepth - 1.
   * This is useful for an optimization technique called lazy
   * re-linearization (only applicable in FIXEDMANUAL, as
   * FLEXIBLEAUTO implements automatic rescaling).
   */
    // uint32_t maxDepth (maxRelinSkDeg) = 2; - already default
    /*
   * The digit size is only used in BV key switching and
   * it allows us to perform digit decomposition at a finer granularity.
   * Under normal circumstances, digit decomposition is what we call
   * RNS decomposition, i.e., each digit is roughly the size of the
   * qi's that comprise the ciphertext modulus Q. When using BV, in
   * certain cases like having to perform rotations without any
   * preceding multiplication, we need to have smaller digits to prevent
   * noise from corrupting the result. In this case, using digitSize = 10
   * does the trick. Users are encouraged to set this to 0 (i.e., RNS
   * decomposition) and see how the results are incorrect.
   */
    uint32_t digitSize = 10;
    uint32_t batchSize = 8;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingTechnique(FLEXIBLEAUTO);
    parameters.SetKeySwitchTechnique(BV);
    parameters.SetFirstModSize(60);
    parameters.SetDigitSize(digitSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    uint32_t N = cc->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << N << std::endl << std::endl;

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalRotateKeyGen(keys.secretKey, {1, 2, 3, 4, 5, 6, 7});

    // Input
    std::vector<double> x = {0, 0, 0, 0, 0, 0, 0, 1};
    Plaintext ptxt        = cc->MakeCKKSPackedPlaintext(x);

    std::cout << "Input x: " << ptxt << std::endl;

    auto c = cc->Encrypt(keys.publicKey, ptxt);

    Ciphertext<DCRTPoly> cRot1, cRot2, cRot3, cRot4, cRot5, cRot6, cRot7;

    // First, we perform 7 regular (non-hoisted) rotations
    // and measure the runtime.
    TimeVar t;
    TIC(t);
    cRot1                 = cc->EvalRotate(c, 1);
    cRot2                 = cc->EvalRotate(c, 2);
    cRot3                 = cc->EvalRotate(c, 3);
    cRot4                 = cc->EvalRotate(c, 4);
    cRot5                 = cc->EvalRotate(c, 5);
    cRot6                 = cc->EvalRotate(c, 6);
    cRot7                 = cc->EvalRotate(c, 7);
    double timeNoHoisting = TOC(t);

    auto cResNoHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    // M is the cyclotomic order and we need it to call EvalFastRotation
    uint32_t M = 2 * N;

    // Then, we perform 7 rotations with hoisting.
    TIC(t);
    auto cPrecomp       = cc->EvalFastRotationPrecompute(c);
    cRot1               = cc->EvalFastRotation(c, 1, M, cPrecomp);
    cRot2               = cc->EvalFastRotation(c, 2, M, cPrecomp);
    cRot3               = cc->EvalFastRotation(c, 3, M, cPrecomp);
    cRot4               = cc->EvalFastRotation(c, 4, M, cPrecomp);
    cRot5               = cc->EvalFastRotation(c, 5, M, cPrecomp);
    cRot6               = cc->EvalFastRotation(c, 6, M, cPrecomp);
    cRot7               = cc->EvalFastRotation(c, 7, M, cPrecomp);
    double timeHoisting = TOC(t);
    /* The time with hoisting should be faster than without hoisting.
   * Also, the benefits from hoisting should be more pronounced in this
   * case because we're using BV. Of course, we also observe less
   * accurate results than when using HYBRID, because of using
   * digitSize = 10 (Users can decrease digitSize to see the accuracy
   * increase, and performance decrease).
   */

    auto cResHoist = c + cRot1 + cRot2 + cRot3 + cRot4 + cRot5 + cRot6 + cRot7;

    Plaintext result;
    std::cout.precision(8);

    cc->Decrypt(keys.secretKey, cResNoHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result without hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x without hoisting took " << timeNoHoisting << "ms" << std::endl;

    cc->Decrypt(keys.secretKey, cResHoist, &result);
    result->SetLength(batchSize);
    std::cout << "Result with hoisting = " << result << std::endl;
    std::cout << " - 7 rotations on x with hoisting took " << timeHoisting << "ms" << std::endl;
}



================================================
FILE: ckks-noise-flooding.cpp
================================================
/*
  Please see CKKS_NOISE_FLOODING.md for technical details on CKKS noise flooding for the INDCPA^D scenario.
  
  Example for using CKKS with the experimental NOISE_FLOODING_DECRYPT mode. We do not recommend
  this mode for production yet. This experimental mode gives us equivalent security levels to
  BGV and BFV, but it requires the user to run all encrypted operations twice. The first iteration
  is a preliminary run to measure noise, and the second iteration is the actual run, which
  will input the noise as a parameter. We use the noise to enhance security within decryption.

  Note that a user can choose to run the first computation with NATIVE_SIZE = 64 to estimate noise,
  and the second computation with NATIVE_SIZE = 128, if they wish. This would require a
  different set of binaries: first, with NATIVE_SIZE = 64 and the second one with NATIVE_SIZE = 128.
  It can be considered as an optimization for the case when we need NATIVE_SIZE = 128.

  For NATIVE_SIZE=128, we automatically choose the scaling mod size and first mod size in the second iteration
  based on the input noise estimate. This means that we currently do not support bootstrapping in the
  NOISE_FLOODING_DECRYPT mode, since the scaling mod size and first mod size affect the noise estimate for
  bootstrapping. We plan to add support for bootstrapping in NOISE_FLOODING_DECRYPT mode in a future release.
 */

#include "openfhe.h"

using namespace lbcrypto;

// Demo function for NOISE_FLOODING_DECRYPT mode in CKKS
void CKKSNoiseFloodingDemo();

/**
 * We recommend putting part of the CryptoContext inside a function because
 * you must make sure all parameters are the same, except EXECUTION_MODE and NOISE_ESTIMATE.
 *
 * @param cryptoParams Crypto parameters that already have their execution mode set (and noise estimate, if in EXEC_EVALUATION mode).
 * @return the cryptoContext.
 */
CryptoContext<DCRTPoly> GetCryptoContext(CCParams<CryptoContextCKKSRNS>& cryptoParams);

/**
 * We recommend putting the encrypted computation you wish to perform inside a function because
 * you have to perform it twice. In this example, we perform two multiplications and an addition.
 *
 * @param cryptoContext Crypto context.
 * @param publicKey Public key for encryption.
 * @return the ciphertext result. The first iteration will return a ciphertext that contains a noise measurement.
 * The second iteration will return the actual encrypted computation.
 */
Ciphertext<DCRTPoly> EncryptedComputation(CryptoContext<DCRTPoly>& cryptoContext, PublicKey<DCRTPoly> publicKey);

int main(int argc, char* argv[]) {
    CKKSNoiseFloodingDemo();
    return 0;
}

void CKKSNoiseFloodingDemo() {
    // ----------------------- Setup first CryptoContext -----------------------------
    // Phase 1 will be for noise estimation.
    // -------------------------------------------------------------------------------
    std::cout << "---------------------------------- PHASE 1: NOISE ESTIMATION ----------------------------------"
              << std::endl;
    CCParams<CryptoContextCKKSRNS> parametersNoiseEstimation;
    // EXEC_NOISE_ESTIMATION indicates that the resulting plaintext will estimate the amount of noise in the computation.
    parametersNoiseEstimation.SetExecutionMode(EXEC_NOISE_ESTIMATION);

    auto cryptoContextNoiseEstimation = GetCryptoContext(parametersNoiseEstimation);

    usint ringDim = cryptoContextNoiseEstimation->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << ringDim << std::endl << std::endl;

    // Key Generation
    auto keyPairNoiseEstimation = cryptoContextNoiseEstimation->KeyGen();
    cryptoContextNoiseEstimation->EvalMultKeyGen(keyPairNoiseEstimation.secretKey);

    // We run the encrypted computation the first time.
    auto noiseCiphertext = EncryptedComputation(cryptoContextNoiseEstimation, keyPairNoiseEstimation.publicKey);

    // Decrypt  noise
    Plaintext noisePlaintext;
    cryptoContextNoiseEstimation->Decrypt(keyPairNoiseEstimation.secretKey, noiseCiphertext, &noisePlaintext);
    double noise = noisePlaintext->GetLogError();
    std::cout << "Noise \n\t" << noise << std::endl;

    // ----------------------- Setup second CryptoContext -----------------------------
    // Phase 2 will be for the actual evaluation.
    // IMPORTANT: We must use a different public/private key pair here to achieve the
    // security guarantees for noise flooding.
    // -------------------------------------------------------------------------------
    std::cout << "---------------------------------- PHASE 2: EVALUATION ----------------------------------"
              << std::endl;
    CCParams<CryptoContextCKKSRNS> parametersEvaluation;
    // EXEC_EVALUATION indicates that we are in phase 2 of computation, and wil5 obtain the actual result.
    parametersEvaluation.SetExecutionMode(EXEC_EVALUATION);
    // Here, we set the noise of our previous computation
    parametersEvaluation.SetNoiseEstimate(noise);

    // We can set our desired precision for 128-bit CKKS only. For NATIVE_SIZE=64, we ignore this parameter.
    parametersEvaluation.SetDesiredPrecision(25);

    // We can set the statistical security and number of adversarial queries, but we can also
    // leave these lines out, as we are setting them to the default values here.
    parametersEvaluation.SetStatisticalSecurity(30);
    parametersEvaluation.SetNumAdversarialQueries(1);

    // The remaining parameters must be the same as the first CryptoContext. Note that we can choose to run the
    // first computation with NATIVEINT = 64 to estimate noise, and the second computation with NATIVEINT = 128,
    // or vice versa, if we wish.
    auto cryptoContextEvaluation = GetCryptoContext(parametersEvaluation);

    // IMPORTANT: Generate new keys
    auto keyPairEvaluation = cryptoContextEvaluation->KeyGen();
    cryptoContextEvaluation->EvalMultKeyGen(keyPairEvaluation.secretKey);

    // We run the encrypted computation the second time.
    auto ciphertextResult = EncryptedComputation(cryptoContextEvaluation, keyPairEvaluation.publicKey);

    // Decrypt final result
    Plaintext result;
    cryptoContextEvaluation->Decrypt(keyPairEvaluation.secretKey, ciphertextResult, &result);
    size_t vecSize = 8;
    result->SetLength(vecSize);
    std::cout << "Final output \n\t" << result->GetCKKSPackedValue() << std::endl;

    std::vector<std::complex<double>> expectedResult = {1.01, 1.04, 0, 0, 1.25, 0, 0, 1.64};
    std::cout << "Expected result\n\t " << expectedResult << std::endl;
}

CryptoContext<DCRTPoly> GetCryptoContext(CCParams<CryptoContextCKKSRNS>& parameters) {
    // This demo is to illustrate how to use the security mode NOISE_FLOODING_DECRYPT to achieve enhanced security.
    parameters.SetDecryptionNoiseMode(NOISE_FLOODING_DECRYPT);

    // Specify main parameters
    parameters.SetSecretKeyDist(UNIFORM_TERNARY);

    /* Desired security level based on FHE standards. Note that this is different than NoiseDecryptionMode,
    * which also gives us enhanced security in CKKS when using NOISE_FLOODING_DECRYPT.
    * We must always use the same ring dimension in both iterations, so we set the security level to HEStd_NotSet,
    * and manually set the ring dimension.
    */
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 16);

    ScalingTechnique rescaleTech = FIXEDAUTO;
    usint dcrtBits               = 59;
    usint firstMod               = 60;

    parameters.SetScalingTechnique(rescaleTech);
    parameters.SetScalingModSize(dcrtBits);
    parameters.SetFirstModSize(firstMod);

    // In this example, we perform two multiplications and an addition.
    parameters.SetMultiplicativeDepth(2);

    // Generate crypto context.
    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    // Enable features that you wish to use.
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(LEVELEDSHE);

    return cryptoContext;
}

Ciphertext<DCRTPoly> EncryptedComputation(CryptoContext<DCRTPoly>& cryptoContext, PublicKey<DCRTPoly> publicKey) {
    // Encoding and encryption of inputs
    // Generate random input
    std::vector<double> vec1 = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8};
    std::vector<double> vec2 = {1, 1, 0, 0, 1, 0, 0, 1};

    // Encoding as plaintexts and encrypt
    Plaintext ptxt1            = cryptoContext->MakeCKKSPackedPlaintext(vec1);
    Plaintext ptxt2            = cryptoContext->MakeCKKSPackedPlaintext(vec2);
    Ciphertext<DCRTPoly> ciph1 = cryptoContext->Encrypt(publicKey, ptxt1);
    Ciphertext<DCRTPoly> ciph2 = cryptoContext->Encrypt(publicKey, ptxt2);

    Ciphertext<DCRTPoly> ciphMult   = cryptoContext->EvalMult(ciph1, ciph2);
    Ciphertext<DCRTPoly> ciphMult2  = cryptoContext->EvalMult(ciphMult, ciph1);
    Ciphertext<DCRTPoly> ciphResult = cryptoContext->EvalAdd(ciphMult2, ciph2);

    return ciphResult;
}



================================================
FILE: CKKS_NOISE_FLOODING.md
================================================
# Static Estimation
Here we describe static noise estimation in FHE and how it relates
to noise flooding. We focus on CKKS, but the same applies to
threshold decryption in [threshold FHE](https://link.springer.com/chapter/10.1007/978-3-642-29011-4_29).

# Li and Micciancio's CKKS attack
[Li and Micciancio](https://link.springer.com/chapter/10.1007/978-3-030-77870-5_23) showed that 
approximate FHE schemes (e.g., CKKS) can leak information about the secret key.
In short, CKKS decryptions give
direct access to the secret key given a ciphertext and a decryption
since the user gets $\mathsf{ct} = (as + m + e, -a)$ and its decryption is $m+e$.
Therefore, we can recover the secret $s$ given the above and we should
always think of the RLWE ciphertext error as part of the secret key.

# Solution: Noise Flooding
One solution to the above issue is to change the decryption algorithm
in CKKS to add [additional error to the output](https://link.springer.com/chapter/10.1007/978-3-031-15802-5_20). That is, given a
CKKS ciphertext $\mathsf{ct} = (c_0, c_1)$, decryption is a \emph{randomized}
procedure given as $$\mathsf{Dec}(\mathsf{ct}): \text{ Sample } z \gets D_{R, \sigma}.\text{ Return } c_0 + c_1s + z \pmod q$$
where $D_{R, \sigma}$ is a discrete gaussian over the polynomial ring,
represented in its coefficient form, and 
$\sigma$ is a standard deviation set by a security level
and the noise estimate. If we want $s>0$ bits of statistical
security, then the standard deviation is
$$\sigma = \sqrt{12\tau}2^{s/2}\mathsf{ct}.t$$
where $\tau$ is the number of adversarial queries the application
is expecting and $\mathsf{ct}.t$ is the ciphertext error estimate (described below).
For the statistical security parameter $s$, one would want this to be
at least $30$, which would bound any (potentially inefficient)
adversary's success probability to at most $2^{-30}$, or about one in
a billion [^1].
Note that this is the same as "noise-smudging" in [threshold FHE](https://link.springer.com/chapter/10.1007/978-3-642-29011-4_29) but has a much
tighter analysis.

# Static Noise Estimation
Notice that the number of queries $\tau$ and the statistical security $s$
in the equation for $\sigma$ are determined by the application or user.
However, the ciphertext noise bound is difficult to determine before
the homomorphic computation is performed. This is because CKKS noise
growth depends on the input message as soon as the computation
involves a multiplication.

# Noise Flooding and Static Estimation in OpenFHE
OpenFHE enables the user to do the following for static estimation, i.e. 
determining a good bound for $\mathsf{ct}.t$.
1. It first runs the computation on a fresh secret key-public key
pair, independent of the user's key pair, and a message determined
by the user. Here, the user can use the actual message or a
message picked from a suitable set of messages (representing
real data the homomorphic computation is supposed to be computed on).
2. OpenFHE estimates the error in the computation by measuring
the noise/precision-loss in the imaginary slots of the decrypted
plaintext. [Costache et al.](https://eprint.iacr.org/2022/162) argue that this method accurately estimates noise growth in
FHE according to their heuristics and experiments. It also
has long been used in PALISADE. Note, this means that
OpenFHE only supports real number arithmetic in CKKS.
The parameter $\mathsf{ct}.t$ is now set according to this estimate.
We call this step the
$\mathsf{EXEC}\textunderscore\mathsf{NOISE}\textunderscore\mathsf{ESTIMATION}$ execution mode.
3. Finally, OpenFHE runs the actual computation, with the
users ciphertexts under her secret key, and applies
noise flooding with discrete gaussian noise with
standard deviation $\sigma = \sqrt{12\tau}2^{s/2}\mathsf{ct}.t$.
We call this mode $\mathsf{EXEC}\textunderscore\mathsf{EVALUATION}$.

The code for this procedure is in
  src/examples/pke/ckks-noise-flooding.cpp
in OpenFHE. 
For leveled computations, the code allows for the user to run the 
static estimation using 64-bit CKKS and the actual computation in 128-bit CKKS.

[^1]:The formula for $\sigma$ in Corollary 2 of [the state of the art in noise flooding security](https://link.springer.com/chapter/10.1007/978-3-031-15802-5_20) has an incorrect $\sqrt{2n}$ factor since the indistinguishablility game is played over the coefficient embedding.



================================================
FILE: function-evaluation.cpp
================================================
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



================================================
FILE: FUNCTION_EVALUATION.md
================================================
OpenFHE Lattice Cryptography Library - Arbitrary Smooth Function Evaluation
============================================================================

[License Information](License.md)

Document Description
===================
This document describes how to evaluate an arbitrary smooth function on a ciphertext in CKKS using [Chebyshev approximation](https://www.gnu.org/software/gsl/doc/html/cheb.html). The Chebyshev approximation is a method of approximating a smooth function using polynomials.

Example Description
==========================

The example for this code is located in [function-evaluation.cpp](function-evaluation.cpp). The file gives examples on how to run `EvalLogistic`, the logistic function $\frac{1}{1 + e^{-x}},$ and an arbitrary function using `EvalChebyshevFunction`. We use the square root function in our example for `EvalChebyshevFunction`.

Input Parameters
==========================
- `ciphertext`: This is the ciphertext we wish to operate on.
- `a`: This is the lower bound of underlying plaintext values we could have.
- `b`: This is the upper bound of underlying plaintext values we could have.
- `degree`: This is the polynomial degree of the Chebyshev approximation. A higher degree gives a more precise estimate, but takes longer to run.

How to Choose Multiplicative Depth
====================================
Each run of EvalChebyshevFunction requires a certain number of multiplications which depends on the input polynomial degree. We give a table below to map polynomial degrees to multiplicative depths.

| Degree        | Multiplicative Depth |
| ------------- |:--------------------:|
| 3-5           | 4                    |
| 6-13          | 5                    |
| 14-27         | 6                    |
| 28-59         | 7                    |
| 60-119        | 8                    |
| 120-247       | 9                    |
| 248-495       | 10                   |
| 496-1007      | 11                   |
| 1008-2031     | 12                   |

Note that if we use a range $(a, b) = (-1, 1),$ the multiplicative depth is 1 less than the depths listed in the table.



================================================
FILE: inner-product.cpp
================================================
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



================================================
FILE: iterative-ckks-bootstrapping.cpp
================================================
//==================================================================================
// BSD 2-Clause License
//
// Copyright (c) 2014-2022, NJIT, Duality Technologies Inc. and other contributors
//
// All rights reserved.
//
// Author TPOC: contact@openfhe.org
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//==================================================================================

/*

Example for multiple iterations of CKKS bootstrapping to improve precision. Note that you need to run a
single iteration of bootstrapping first, to measure the precision. Then, you can input the measured
precision as a parameter to EvalBootstrap with multiple iterations. With 2 iterations, you can achieve
double the precision of a single bootstrapping.

* Source: Bae Y., Cheon J., Cho W., Kim J., and Kim T. META-BTS: Bootstrapping Precision
* Beyond the Limit. Cryptology ePrint Archive, Report
* 2022/1167. (https://eprint.iacr.org/2022/1167.pdf)

*/

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

void IterativeBootstrapExample();

int main(int argc, char* argv[]) {
    // We run the example with 8 slots and ring dimension 4096.
    IterativeBootstrapExample();
}

// CalculateApproximationError() calculates the precision number (or approximation error).
// The higher the precision, the less the error.
double CalculateApproximationError(const std::vector<std::complex<double>>& result,
                                   const std::vector<std::complex<double>>& expectedResult) {
    if (result.size() != expectedResult.size())
        OPENFHE_THROW("Cannot compare vectors with different numbers of elements");

    // using the infinity norm
    double maxError = 0;
    for (size_t i = 0; i < result.size(); ++i) {
        double error = std::abs(result[i].real() - expectedResult[i].real());
        if (maxError < error)
            maxError = error;
    }

    return std::abs(std::log2(maxError));
}

void IterativeBootstrapExample() {
    // Step 1: Set CryptoContext
    CCParams<CryptoContextCKKSRNS> parameters;
    SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
    parameters.SetSecretKeyDist(secretKeyDist);
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 12);

#if NATIVEINT == 128 && !defined(__EMSCRIPTEN__)
    // Currently, only FIXEDMANUAL and FIXEDAUTO modes are supported for 128-bit CKKS bootstrapping.
    ScalingTechnique rescaleTech = FIXEDAUTO;
    usint dcrtBits               = 78;
    usint firstMod               = 89;
#else
    // All modes are supported for 64-bit CKKS bootstrapping.
    ScalingTechnique rescaleTech = FLEXIBLEAUTO;
    usint dcrtBits               = 59;
    usint firstMod               = 60;
#endif

    parameters.SetScalingModSize(dcrtBits);
    parameters.SetScalingTechnique(rescaleTech);
    parameters.SetFirstModSize(firstMod);

    // Here, we specify the number of iterations to run bootstrapping. Note that we currently only support 1 or 2 iterations.
    // Two iterations should give us approximately double the precision of one iteration.
    uint32_t numIterations = 2;

    std::vector<uint32_t> levelBudget = {3, 3};
    std::vector<uint32_t> bsgsDim     = {0, 0};

    uint32_t levelsAvailableAfterBootstrap = 10;
    usint depth =
        levelsAvailableAfterBootstrap + FHECKKSRNS::GetBootstrapDepth(levelBudget, secretKeyDist) + (numIterations - 1);
    parameters.SetMultiplicativeDepth(depth);

    // Generate crypto context.
    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    // Enable features that you wish to use. Note, we must enable FHE to use bootstrapping.
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    cryptoContext->Enable(ADVANCEDSHE);
    cryptoContext->Enable(FHE);

    usint ringDim = cryptoContext->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << ringDim << std::endl << std::endl;

    // Step 2: Precomputations for bootstrapping
    // We use a sparse packing.
    uint32_t numSlots = 8;
    cryptoContext->EvalBootstrapSetup(levelBudget, bsgsDim, numSlots);

    // Step 3: Key Generation
    auto keyPair = cryptoContext->KeyGen();
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);
    // Generate bootstrapping keys.
    cryptoContext->EvalBootstrapKeyGen(keyPair.secretKey, numSlots);

    // Step 4: Encoding and encryption of inputs
    // Generate random input
    std::vector<double> x;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    for (size_t i = 0; i < numSlots; i++) {
        x.push_back(dis(gen));
    }

    // Encoding as plaintexts
    // We specify the number of slots as numSlots to achieve a performance improvement.
    // We use the other default values of depth 1, levels 0, and no params.
    // Alternatively, you can also set batch size as a parameter in the CryptoContext as follows:
    // parameters.SetBatchSize(numSlots);
    // Here, we assume all ciphertexts in the cryptoContext will have numSlots slots.
    // We start with a depleted ciphertext that has used up all of its levels.
    Plaintext ptxt = cryptoContext->MakeCKKSPackedPlaintext(x, 1, depth - 1, nullptr, numSlots);
    ptxt->SetLength(numSlots);
    std::cout << "Input: " << ptxt << std::endl;

    // Encrypt the encoded vectors
    Ciphertext<DCRTPoly> ciph = cryptoContext->Encrypt(keyPair.publicKey, ptxt);

    // Step 5: Measure the precision of a single bootstrapping operation.
    auto ciphertextAfter = cryptoContext->EvalBootstrap(ciph);

    Plaintext result;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextAfter, &result);
    result->SetLength(numSlots);
    uint32_t precision =
        std::floor(CalculateApproximationError(result->GetCKKSPackedValue(), ptxt->GetCKKSPackedValue()));
    std::cout << "Bootstrapping precision after 1 iteration: " << precision << std::endl;

    // Set precision equal to empirically measured value after many test runs.
    precision = 17;
    std::cout << "Precision input to algorithm: " << precision << std::endl;

    // Step 6: Run bootstrapping with multiple iterations.
    auto ciphertextTwoIterations = cryptoContext->EvalBootstrap(ciph, numIterations, precision);

    Plaintext resultTwoIterations;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextTwoIterations, &resultTwoIterations);
    result->SetLength(numSlots);
    auto actualResult = resultTwoIterations->GetCKKSPackedValue();

    std::cout << "Output after two iterations of bootstrapping: " << actualResult << std::endl;
    double precisionMultipleIterations = CalculateApproximationError(actualResult, ptxt->GetCKKSPackedValue());

    // Output the precision of bootstrapping after two iterations. It should be approximately double the original precision.
    std::cout << "Bootstrapping precision after 2 iterations: " << precisionMultipleIterations << std::endl;
    std::cout << "Number of levels remaining after 2 bootstrappings: "
              << depth - ciphertextTwoIterations->GetLevel() - (ciphertextTwoIterations->GetNoiseScaleDeg() - 1)
              << std::endl;
}



================================================
FILE: linearwsum-evaluation.cpp
================================================
/*
  Example of polynomial evaluation using CKKS.
 */

#define PROFILE  // turns on the reporting of timing results

#include "openfhe.h"

using namespace lbcrypto;

int main(int argc, char* argv[]) {
    TimeVar t;

    double timeEvalLinearWSum(0.0);

    std::cout << "\n======EXAMPLE FOR EVAL LINEAR WEIGHTED SUM========\n" << std::endl;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(1);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(8);
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(2048);
    parameters.SetScalingTechnique(FLEXIBLEAUTO);
    parameters.SetFirstModSize(60);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);

    std::vector<std::vector<std::complex<double>>> input;

    input.push_back({0.5, 0.7, 0.9, 0.95, 0.93, 1.3});
    input.push_back({1.2, 1.7, -0.9, 0.85, -0.63, 2});
    input.push_back({0.5, 0, 1.9, 2.95, -3.93, 3.3});
    input.push_back({1.5, 0.7, 1.9, 2.95, -3.78, 3.3});
    input.push_back({0.5, 2.7, 1.9, 0.0, -3.43, 1.3});
    input.push_back({0.5, 0.7, -1.9, 2.95, 1.96, 0.0});
    input.push_back({0.0, 0.0, 1.0, 0.0, 0.0, 0.0});

    size_t encodedLength = input.size();

    std::vector<double> coefficients({0.15, 0.75, 1.25, 1, 0, 0.5, 0.5});

    auto keyPair = cc->KeyGen();

    std::cout << "Generating evaluation key for homomorphic multiplication...";
    cc->EvalMultKeyGen(keyPair.secretKey);
    std::cout << "Completed." << std::endl;

    std::vector<ConstCiphertext<DCRTPoly>> ciphertextVec;
    for (usint i = 0; i < encodedLength; ++i) {
        Plaintext plaintext = cc->MakeCKKSPackedPlaintext(input[i]);
        ciphertextVec.push_back(cc->Encrypt(keyPair.publicKey, plaintext));
    }

    TIC(t);

    auto result = cc->EvalLinearWSum(ciphertextVec, coefficients);

    timeEvalLinearWSum = TOC(t);

    std::vector<std::complex<double>> unencIP;
    for (usint i = 0; i < input[0].size(); ++i) {
        std::complex<double> x = 0;
        for (usint j = 0; j < encodedLength; ++j) {
            x += input[j][i] * coefficients[j];
        }
        unencIP.push_back(x);
    }

    Plaintext plaintextDec;

    cc->Decrypt(keyPair.secretKey, result, &plaintextDec);

    plaintextDec->SetLength(encodedLength);

    std::cout << std::setprecision(10) << std::endl;

    std::cout << "\n Result of evaluating a linear weighted sum with coefficients " << coefficients << " \n";
    std::cout << plaintextDec << std::endl;

    std::cout << "\n Expected result: " << unencIP << std::endl;

    std::cout << "\n Evaluation time: " << timeEvalLinearWSum << " ms" << std::endl;

    return 0;
}



================================================
FILE: polynomial-evaluation.cpp
================================================
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



================================================
FILE: pre-buffer.cpp
================================================
/*
  Example of Proxy Re-Encryption on a packed vector.
  Example software for multiparty proxy-reencryption of an integer buffer using BFV rns scheme.
 */

#define PROFILE  // for TIC TOC
#include "openfhe.h"

using namespace lbcrypto;

using CT = Ciphertext<DCRTPoly>;  // ciphertext
using PT = Plaintext;             // plaintext

using vecInt  = std::vector<int64_t>;  // vector of ints
using vecChar = std::vector<char>;     // vector of characters

bool run_demo_pre(void);

int main(int argc, char* argv[]) {
    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    bool passed = run_demo_pre();

    if (!passed) {  // there could be an error
        exit(1);
    }
    exit(0);  // successful return
}

bool run_demo_pre(void) {
    // Generate parameters.
    TimeVar t;  // timer for tic toc
    std::cout << "setting up BFV RNS crypto system" << std::endl;
    TIC(t);
    // int plaintextModulus = 786433; //plaintext prime modulus
    int plaintextModulus = 65537;  // can encode shorts

    CCParams<CryptoContextBFVRNS> parameters;
    parameters.SetPlaintextModulus(plaintextModulus);
    parameters.SetScalingModSize(60);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    std::cout << "\nParam generation time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;
    // Turn on features
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(PRE);

    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;
    std::cout << "r = " << cc->GetCryptoParameters()->GetDigitSize() << std::endl;

    auto ringsize = cc->GetRingDimension();
    std::cout << "Alice can encrypt " << ringsize * 2 << " bytes of data" << std::endl;
    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    // Initialize Key Pair Containers
    KeyPair<DCRTPoly> keyPair1;

    std::cout << "\nRunning Alice key generation (used for source data)..." << std::endl;

    TIC(t);
    keyPair1 = cc->KeyGen();
    std::cout << "Key generation time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    if (!keyPair1.good()) {
        std::cout << "Alice Key generation failed!" << std::endl;
        return (false);
    }

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////

    unsigned int nshort = ringsize;

    vecInt vShorts;

    for (size_t i = 0; i < nshort; i++)
        vShorts.push_back(std::rand() % 65536);

    PT pt = cc->MakePackedPlaintext(vShorts);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////

    TIC(t);
    auto ct1 = cc->Encrypt(keyPair1.publicKey, pt);
    std::cout << "Encryption time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    ////////////////////////////////////////////////////////////
    // Decryption of Ciphertext
    ////////////////////////////////////////////////////////////

    PT ptDec1;

    TIC(t);
    cc->Decrypt(keyPair1.secretKey, ct1, &ptDec1);
    std::cout << "Decryption time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    ptDec1->SetLength(pt->GetLength());

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    // Initialize Key Pair Containers
    KeyPair<DCRTPoly> keyPair2;

    std::cout << "Bob Running key generation ..." << std::endl;

    TIC(t);
    keyPair2 = cc->KeyGen();
    std::cout << "Key generation time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    if (!keyPair2.good()) {
        std::cout << "Bob Key generation failed!" << std::endl;
        return (false);
    }

    ////////////////////////////////////////////////////////////
    // Perform the proxy re-encryption key generation operation.
    // This generates the keys which are used to perform the key switching.
    ////////////////////////////////////////////////////////////

    std::cout << "\n"
              << "Generating proxy re-encryption key..." << std::endl;

    EvalKey<DCRTPoly> reencryptionKey12;

    TIC(t);
    reencryptionKey12 = cc->ReKeyGen(keyPair1.secretKey, keyPair2.publicKey);
    std::cout << "Key generation time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    ////////////////////////////////////////////////////////////
    // Re-Encryption
    ////////////////////////////////////////////////////////////

    TIC(t);
    auto ct2 = cc->ReEncrypt(ct1, reencryptionKey12);
    std::cout << "Re-Encryption time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    ////////////////////////////////////////////////////////////
    // Decryption of Ciphertext
    ////////////////////////////////////////////////////////////

    PT ptDec2;

    TIC(t);
    cc->Decrypt(keyPair2.secretKey, ct2, &ptDec2);
    std::cout << "Decryption time: "
              << "\t" << TOC_MS(t) << " ms" << std::endl;

    ptDec2->SetLength(pt->GetLength());

    auto unpacked0 = pt->GetPackedValue();
    auto unpacked1 = ptDec1->GetPackedValue();
    auto unpacked2 = ptDec2->GetPackedValue();
    bool good      = true;

    // note that OpenFHE assumes that plaintext is in the range of -p/2..p/2
    // to recover 0...q simply add q if the unpacked value is negative
    for (unsigned int j = 0; j < pt->GetLength(); j++) {
        if (unpacked1[j] < 0)
            unpacked1[j] += plaintextModulus;
        if (unpacked2[j] < 0)
            unpacked2[j] += plaintextModulus;
    }

    // compare all the results for correctness
    for (unsigned int j = 0; j < pt->GetLength(); j++) {
        if ((unpacked0[j] != unpacked1[j]) || (unpacked0[j] != unpacked2[j])) {
            std::cout << j << ", " << unpacked0[j] << ", " << unpacked1[j] << ", " << unpacked2[j] << std::endl;
            good = false;
        }
    }
    if (good) {
        std::cout << "PRE passes" << std::endl;
    }
    else {
        std::cout << "PRE fails" << std::endl;
    }

    ////////////////////////////////////////////////////////////
    // Done
    ////////////////////////////////////////////////////////////

    std::cout << "Execution Completed." << std::endl;

    return good;
}



================================================
FILE: pre-hra-secure.cpp
================================================
/*
  Example of HRA-secure Proxy Re-Encryption with 13 hops.
 */

#define PROFILE  // for TIC TOC
#include "openfhe.h"

using namespace lbcrypto;

using CT = Ciphertext<DCRTPoly>;  // ciphertext
using PT = Plaintext;             // plaintext

using vecInt  = std::vector<int64_t>;  // vector of ints
using vecChar = std::vector<char>;     // vector of characters

bool run_demo_pre(void);

int main(int argc, char* argv[]) {
    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    bool passed = run_demo_pre();

    if (!passed) {  // there could be an error
        exit(1);
    }
    exit(0);  // successful return
}

bool run_demo_pre(void) {
    // Generate parameters.
    TimeVar t;  // timer for tic toc
    std::cout << "setting up the HRA-secure BGV PRE cryptosystem" << std::endl;
    TIC(t);

    double t1;

    uint32_t plaintextModulus = 2;  // can encode shorts

    uint32_t numHops = 13;

    CCParams<CryptoContextBGVRNS> parameters;
    parameters.SetPlaintextModulus(plaintextModulus);
    parameters.SetScalingTechnique(FIXEDMANUAL);
    parameters.SetPRENumHops(numHops);
    parameters.SetStatisticalSecurity(40);
    parameters.SetNumAdversarialQueries(1048576);
    parameters.SetRingDim(32768);
    parameters.SetPREMode(NOISE_FLOODING_HRA);
    parameters.SetKeySwitchTechnique(HYBRID);
    parameters.SetMultiplicativeDepth(0);
    // parameters.SetNumLargeDigits(3);
    // parameters.SetKeySwitchTechnique(BV);
    // parameters.SetDigitSize(15);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    std::cout << "\nParam generation time: "
              << "\t" << TOC_US(t) << " ms" << std::endl;
    // Turn on features
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(PRE);

    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;
    // std::cout << "crypto parameters = " << *cc->GetCryptoParameters() << std::endl;
    const auto cryptoParamsBGV = std::dynamic_pointer_cast<CryptoParametersBGVRNS>(cc->GetCryptoParameters());
    std::cout << "log QP = " << cryptoParamsBGV->GetParamsQP()->GetModulus().GetMSB() << std::endl;
    // std::cout << "RNS parameters = " << *cryptoParamsBGV->GetParamsQP() << std::endl;

    auto ringsize = cc->GetRingDimension();
    std::cout << "Alice can encrypt " << ringsize / 8 << " bytes of data" << std::endl;
    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    // Initialize Key Pair Containers
    KeyPair<DCRTPoly> keyPair1;

    std::cout << "\nRunning Alice key generation (used for source data)..." << std::endl;

    TIC(t);
    keyPair1 = cc->KeyGen();
    t1       = TOC_US(t);
    std::cout << "Key generation time: "
              << "\t" << t1 / 1000.0 << " ms" << std::endl;

    if (!keyPair1.good()) {
        std::cout << "Alice Key generation failed!" << std::endl;
        return (false);
    }

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////

    unsigned int nshort = ringsize;

    vecInt vShorts;

    for (size_t i = 0; i < nshort; i++)
        vShorts.push_back(std::rand() % plaintextModulus);

    PT pt = cc->MakeCoefPackedPlaintext(vShorts);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////

    TIC(t);
    auto ct1 = cc->Encrypt(keyPair1.publicKey, pt);
    t1       = TOC_US(t);
    std::cout << "Encryption time: "
              << "\t" << t1 / 1000.0 << " ms" << std::endl;

    ////////////////////////////////////////////////////////////
    // Decryption of Ciphertext
    ////////////////////////////////////////////////////////////

    PT ptDec1;

    TIC(t);
    cc->Decrypt(keyPair1.secretKey, ct1, &ptDec1);
    t1 = TOC_US(t);
    std::cout << "Decryption time: "
              << "\t" << t1 / 1000.0 << " ms" << std::endl;

    ptDec1->SetLength(pt->GetLength());

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    // Initialize Key Pair Containers
    std::vector<KeyPair<DCRTPoly>> keyPairVector(numHops);
    std::vector<EvalKey<DCRTPoly>> reencryptionKeyVector(numHops);

    std::cout << "Generating keys for " << numHops << " parties" << std::endl;

    for (unsigned int i = 0; i < numHops; i++) {
        TIC(t);
        keyPairVector[i] = cc->KeyGen();
        t1               = TOC_US(t);
        if (i == 1)
            std::cout << "Key generation time: "
                      << "\t" << t1 / 1000.0 << " ms" << std::endl;

        if (!keyPairVector[i].good()) {
            std::cout << "Bob Key generation failed!" << std::endl;
            return (false);
        }

        ////////////////////////////////////////////////////////////
        // Perform the proxy re-encryption key generation operation.
        // This generates the keys which are used to perform the key switching.
        ////////////////////////////////////////////////////////////
        if (i == 0) {
            reencryptionKeyVector[i] = cc->ReKeyGen(keyPair1.secretKey, keyPairVector[i].publicKey);
        }
        else {
            TIC(t);
            reencryptionKeyVector[i] = cc->ReKeyGen(keyPairVector[i - 1].secretKey, keyPairVector[i].publicKey);
            t1                       = TOC_US(t);
            if (i == 1)
                std::cout << "Re-encryption key generation time: "
                          << "\t" << t1 / 1000.0 << " ms" << std::endl;
        }
    }

    ////////////////////////////////////////////////////////////
    // Re-Encryption
    ////////////////////////////////////////////////////////////
    bool good = true;
    for (unsigned int i = 0; i < numHops; i++) {
        TIC(t);
        ct1 = cc->ReEncrypt(ct1, reencryptionKeyVector[i]);
        t1  = TOC_US(t);
        std::cout << "Re-Encryption time at hop " << i + 1 << "\t" << t1 / 1000.0 << " ms" << std::endl;

        if (i < numHops - 1)
            cc->ModReduceInPlace(ct1);

        ////////////////////////////////////////////////////////////
        // Decryption of Ciphertext
        ////////////////////////////////////////////////////////////

        PT ptDec2;

        TIC(t);
        cc->Decrypt(keyPairVector[i].secretKey, ct1, &ptDec2);
        t1 = TOC_US(t);
        std::cout << "Decryption time: "
                  << "\t" << t1 / 1000.0 << " ms" << std::endl;

        ptDec2->SetLength(pt->GetLength());

        auto unpacked0 = pt->GetCoefPackedValue();
        auto unpacked1 = ptDec1->GetCoefPackedValue();
        auto unpacked2 = ptDec2->GetCoefPackedValue();

        // note that OpenFHE assumes that plaintext is in the range of -p/2..p/2
        // to recover 0...q simply add q if the unpacked value is negative
        for (unsigned int j = 0; j < pt->GetLength(); j++) {
            if (unpacked1[j] < 0)
                unpacked1[j] += plaintextModulus;
            if (unpacked2[j] < 0)
                unpacked2[j] += plaintextModulus;
        }

        // compare all the results for correctness
        for (unsigned int j = 0; j < pt->GetLength(); j++) {
            if ((unpacked0[j] != unpacked1[j]) || (unpacked0[j] != unpacked2[j])) {
                // std::cout << j << ", " << unpacked0[j] << ", " << unpacked1[j] << ", " << unpacked2[j] << std::endl;
                good = false;
            }
        }
        if (good) {
            std::cout << "PRE passes" << std::endl;
        }
        else {
            std::cout << "PRE fails" << std::endl;
        }
    }

    ////////////////////////////////////////////////////////////
    // Done
    ////////////////////////////////////////////////////////////

    std::cout << "Execution Completed." << std::endl;

    return good;
}



================================================
FILE: rotation.cpp
================================================
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



================================================
FILE: scheme-switching-serial.cpp
================================================
/*
  Real number serialization in a simple context. The goal of this is to show a simple setup for real number
  serialization before progressing into the next logical step - serialization and communication across
  2 separate entities
 */

#include <iomanip>
#include <tuple>
#include <unistd.h>

#include "openfhe.h"
#include "binfhecontext.h"
#include "scheme/ckksrns/schemeswitching-data-serializer.h"

// header files needed for serialization
#include "ciphertext-ser.h"
#include "cryptocontext-ser.h"
#include "key/key-ser.h"
#include "scheme/ckksrns/ckksrns-ser.h"

using namespace lbcrypto;

/////////////////////////////////////////////////////////////////
// NOTE:
// If running locally, you may want to replace the "hardcoded" DATAFOLDER with
// the DATAFOLDER location below which gets the current working directory
/////////////////////////////////////////////////////////////////
// char buff[1024];
// std::string DATAFOLDER = std::string(getcwd(buff, 1024));

// Save-Load locations for keys
const std::string DATAFOLDER      = "demoData";
std::string ccLocation            = "/cryptocontext.txt";     // cc
std::string pubKeyLocation        = "/key_pub.txt";           // Pub key
std::string multKeyLocation       = "/key_mult.txt";          // relinearization key
std::string rotKeyLocation        = "/key_rot.txt";           // automorphism / rotation key
std::string paramssLocation       = "/paramss.txt";           // cc
std::string binccLocation         = "/bincryptocontext.txt";  // binfhe cc
std::string btRkLocation          = "/bt_rk.txt";             // binfhe bootstrapping refreshing key
std::string btSwkLocation         = "/bt_swk.txt";            // binfhe bootstrapping rotation key
std::string FHEWtoCKKSKeyLocation = "/key_swkFC.txt";         // switching key from FHEW to CKKS

// Save-load locations for RAW ciphertexts
std::string cipherLocation = "/ciphertext.txt";

// Save-load locations for evaluated ciphertext
std::string cipherArgminLocation = "/ciphertextArgmin.txt";

/**
 * Demarcate - Visual separator between the sections of code
 * @param msg - string message that you want displayed between blocks of
 * characters
 */
void demarcate(const std::string& msg) {
    std::cout << std::setw(50) << std::setfill('*') << '\n' << std::endl;
    std::cout << msg << std::endl;
    std::cout << std::setw(50) << std::setfill('*') << '\n' << std::endl;
}

/**
 * serverVerification
 *  - deserialize data from the client.
 *  - Verify that the results are as we expect
 * @param cc cryptocontext that was previously generated
 * @param kp keypair that was previously generated
 * @param vectorSize vector size of the vectors supplied
 * @return
 *  5-tuple of the plaintexts of various operations
 */

Plaintext serverVerification(CryptoContext<DCRTPoly>& cc, KeyPair<DCRTPoly>& kp, int vectorSize) {
    Ciphertext<DCRTPoly> serverCiphertextFromClient_Argmin;

    Serial::DeserializeFromFile(DATAFOLDER + cipherArgminLocation, serverCiphertextFromClient_Argmin, SerType::BINARY);
    std::cout << "Deserialized all data from client on server" << '\n' << std::endl;

    demarcate("Part 5: Correctness verification");

    Plaintext serverPlaintextFromClient_Argmin;
    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_Argmin, &serverPlaintextFromClient_Argmin);

    serverPlaintextFromClient_Argmin->SetLength(vectorSize);

    return serverPlaintextFromClient_Argmin;
}

/**
 * serverSetupAndWrite
 *  - simulates a server at startup where we generate a cryptocontext and keys.
 *  - then, we generate some data (akin to loading raw data on an enclave)
 * before encrypting the data
 * @param ringDim - ring dimension
 * @param batchSize - batch size to use
 * @param multDepth - multiplication depth
 * @param logQ_LWE - number of bits of the ciphertext modulus in FHEW
 * @param oneHot - flag to indicate one hot encoding of the result
 * @return Tuple<cryptoContext, keyPair>
 */
std::tuple<CryptoContext<DCRTPoly>, KeyPair<DCRTPoly>, int> serverSetupAndWrite(uint32_t ringDim, uint32_t batchSize,
                                                                                uint32_t multDepth,
                                                                                uint32_t scaleModSize,
                                                                                uint32_t firstModSize,
                                                                                uint32_t logQ_LWE, bool oneHot) {
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(FLEXIBLEAUTO);

    CryptoContext<DCRTPoly> serverCC = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    serverCC->Enable(PKE);
    serverCC->Enable(KEYSWITCH);
    serverCC->Enable(LEVELEDSHE);
    serverCC->Enable(ADVANCEDSHE);
    serverCC->Enable(FHE);
    serverCC->Enable(SCHEMESWITCH);

    std::cout << "Cryptocontext generated" << std::endl;

    KeyPair<DCRTPoly> serverKP = serverCC->KeyGen();
    std::cout << "Keypair generated" << std::endl;

    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_LWE);
    params.SetNumSlotsCKKS(batchSize);
    params.SetNumValues(batchSize);
    params.SetComputeArgmin(true);
    params.SetOneHotEncoding(oneHot);
    auto privateKeyFHEW = serverCC->EvalSchemeSwitchingSetup(params);

    serverCC->EvalSchemeSwitchingKeyGen(serverKP, privateKeyFHEW);

    std::vector<std::complex<double>> vec = {1.0, 2.0, 3.0, 4.0};
    std::cout << "\nDisplaying data vector: ";

    for (auto& v : vec) {
        std::cout << v << ',';
    }

    std::cout << '\n' << std::endl;

    Plaintext serverP = serverCC->MakeCKKSPackedPlaintext(vec);

    std::cout << "Plaintext version of vector: " << serverP << std::endl;

    std::cout << "Plaintexts have been generated from complex-double vectors" << std::endl;

    auto serverC = serverCC->Encrypt(serverKP.publicKey, serverP);

    std::cout << "Ciphertext have been generated from Plaintext" << std::endl;

    /*
   * Part 2:
   * We serialize the following:
   *  Cryptocontext
   *  Public key
   *  relinearization (eval mult keys)
   *  rotation keys
   *  binfhe cryptocontext
   *  binfhe bootstrapping keys
   *  Some of the ciphertext
   *
   *  We serialize all of them to files
   */

    demarcate("Scheme Switching Part 2: Data Serialization (server)");

    SchemeSwitchingDataSerializer serializer(serverCC, serverKP.publicKey, serverC);
    serializer.Serialize();

    return std::make_tuple(serverCC, serverKP, vec.size());
}

/**
 * clientProcess
 *  - deserialize data from a file which simulates receiving data from a server
 * after making a request
 *  - we then process the data
 */

void clientProcess(uint32_t modulus_LWE) {
    CryptoContextImpl<DCRTPoly>::ClearEvalMultKeys();
    CryptoContextImpl<DCRTPoly>::ClearEvalSumKeys();
    CryptoContextImpl<DCRTPoly>::ClearEvalAutomorphismKeys();
    CryptoContextFactory<DCRTPoly>::ReleaseAllContexts();

    SchemeSwitchingDataDeserializer deserializer;
    deserializer.Deserialize();

    CryptoContext<DCRTPoly> clientCC{deserializer.getCryptoContext()};
    PublicKey<DCRTPoly> clientPublicKey{deserializer.getPublicKey()};
    std::shared_ptr<lbcrypto::BinFHEContext> clientBinCC{clientCC->GetBinCCForSchemeSwitch()};
    Ciphertext<DCRTPoly> clientC{deserializer.getRAWCiphertext()};

    // Scale the inputs to ensure their difference is correctly represented after switching to FHEW
    double scaleSign = 512.0;
    auto beta        = clientBinCC->GetBeta().ConvertToInt();
    auto pLWE        = modulus_LWE / (2 * beta);  // Large precision

    clientCC->EvalCompareSwitchPrecompute(pLWE, scaleSign, false);

    std::cout << "Done with precomputations" << '\n' << std::endl;

    // Compute on the ciphertext
    auto clientCiphertextArgmin =
        clientCC->EvalMinSchemeSwitching(clientC, clientPublicKey, clientC->GetSlots(), clientC->GetSlots(), 0, 1);

    std::cout << "Done with argmin computation" << '\n' << std::endl;

    // Now, we want to simulate a client who is encrypting data for the server to
    // decrypt. E.g weights of a machine learning algorithm
    demarcate("Part 3.5: Client Serialization of data that has been operated on");

    Serial::SerializeToFile(DATAFOLDER + cipherArgminLocation, clientCiphertextArgmin[1], SerType::BINARY);

    std::cout << "Serialized ciphertext from client" << '\n' << std::endl;
}

int main() {
    std::cout << "This program requres the subdirectory `" << DATAFOLDER << "' to exist, otherwise you will get "
              << "an error writing serializations." << std::endl;

    // Set main params
    uint32_t ringDim      = 64;
    uint32_t batchSize    = 4;
    uint32_t multDepth    = 13 + static_cast<int>(std::log2(batchSize));
    uint32_t logQ_ccLWE   = 25;
    bool oneHot           = true;
    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;

    const int cryptoContextIdx = 0;
    const int keyPairIdx       = 1;
    const int vectorSizeIdx    = 2;

    demarcate(
        "Scheme switching Part 1: Cryptocontext generation, key generation, data encryption "
        "(server)");

    auto tupleCryptoContext_KeyPair =
        serverSetupAndWrite(ringDim, batchSize, multDepth, scaleModSize, firstModSize, logQ_ccLWE, oneHot);

    auto cc         = std::get<cryptoContextIdx>(tupleCryptoContext_KeyPair);
    auto kp         = std::get<keyPairIdx>(tupleCryptoContext_KeyPair);
    auto vectorSize = std::get<vectorSizeIdx>(tupleCryptoContext_KeyPair);

    demarcate("Scheme switching Part 3: Client deserialize all data");

    clientProcess(1 << logQ_ccLWE);

    demarcate("Scheme switching Part 4: Server deserialization of data from client. ");

    auto ArgminRes = serverVerification(cc, kp, vectorSize);

    // vec1: {1,2,3,4}

    std::cout << ArgminRes << std::endl;  // EXPECT: 1.0, 0.0, 0.0, 0.0
}



================================================
FILE: scheme-switching.cpp
================================================
/*
  Examples for scheme switching between CKKS and FHEW and back, with intermediate computations
 */

#include "openfhe.h"
#include "binfhecontext.h"

using namespace lbcrypto;

void SwitchCKKSToFHEW();
void SwitchFHEWtoCKKS();
void FloorViaSchemeSwitching();
void ComparisonViaSchemeSwitching();
void FuncViaSchemeSwitching();
void PolyViaSchemeSwitching();
void ArgminViaSchemeSwitching();
void ArgminViaSchemeSwitchingAlt();
void ArgminViaSchemeSwitchingUnit();
void ArgminViaSchemeSwitchingAltUnit();
std::vector<int32_t> RotateInt(const std::vector<int32_t>&, int32_t);

int main() {
    SwitchCKKSToFHEW();
    SwitchFHEWtoCKKS();
    FloorViaSchemeSwitching();
    FuncViaSchemeSwitching();
    PolyViaSchemeSwitching();
    ComparisonViaSchemeSwitching();
    ArgminViaSchemeSwitching();
    ArgminViaSchemeSwitchingAlt();
    ArgminViaSchemeSwitchingUnit();
    ArgminViaSchemeSwitchingAltUnit();

    return 0;
}

void SwitchCKKSToFHEW() {
    /*
  Example of switching a packed ciphertext from CKKS to multiple FHEW ciphertexts.
 */

    std::cout << "\n-----SwitchCKKSToFHEW-----\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS

    // Specify main parameters
    uint32_t multDepth    = 3;
    uint32_t firstModSize = 60;
    uint32_t scaleModSize = 50;
    uint32_t ringDim      = 4096;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    // uint32_t slots        = ringDim / 2;  // Uncomment for fully-packed
    uint32_t slots     = 16;  // sparsely-packed
    uint32_t batchSize = slots;

    CCParams<CryptoContextCKKSRNS> parameters;

    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(FLEXIBLEAUTOEXT);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", number of slots " << slots << ", and supports a multiplicative depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    auto privateKeyFHEW = cc->EvalCKKStoFHEWSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();
    cc->EvalCKKStoFHEWKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Compute the scaling factor to decrypt correctly in FHEW; under the hood, the LWE mod switch will performed on the ciphertext at the last level
    auto pLWE1       = ccLWE->GetMaxPlaintextSpace().ConvertToInt();  // Small precision
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE2       = modulus_LWE / (2 * beta);  // Large precision

    double scale1 = 1.0 / pLWE1;
    double scale2 = 1.0 / pLWE2;

    // Perform the precomputation for switching
    cc->EvalCKKStoFHEWPrecompute(scale1);

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1  = {0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    std::vector<double> x2  = {0.0, 271.0, 30000.0, static_cast<double>(pLWE2) - 2};
    uint32_t encodedLength1 = x1.size();
    uint32_t encodedLength2 = x2.size();

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr);
    Plaintext ptxt2 = cc->MakeCKKSPackedPlaintext(x2, 1, 0, nullptr);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);
    auto c2 = cc->Encrypt(keys.publicKey, ptxt2);

    // Step 4: Scheme switching from CKKS to FHEW

    // A: First scheme switching case

    // Transform the ciphertext from CKKS to FHEW
    auto cTemp = cc->EvalCKKStoFHEW(c1, encodedLength1);

    std::cout << "\n---Decrypting switched ciphertext with small precision (plaintext modulus " << NativeInteger(pLWE1)
              << ")---\n"
              << std::endl;

    std::vector<int32_t> x1Int(encodedLength1);
    std::transform(x1.begin(), x1.end(), x1Int.begin(), [&](const double& elem) {
        return static_cast<int32_t>(static_cast<int32_t>(std::round(elem)) % pLWE1);
    });
    ptxt1->SetLength(encodedLength1);
    std::cout << "Input x1: " << ptxt1->GetRealPackedValue() << "; which rounds to: " << x1Int << std::endl;
    std::cout << "FHEW decryption: ";
    LWEPlaintext result;
    for (uint32_t i = 0; i < cTemp.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cTemp[i], &result, pLWE1);
        std::cout << result << " ";
    }
    std::cout << "\n" << std::endl;

    // B: Second scheme switching case

    // Perform the precomputation for switching
    cc->EvalCKKStoFHEWPrecompute(scale2);

    // Transform the ciphertext from CKKS to FHEW (only for the number of inputs given)
    auto cTemp2 = cc->EvalCKKStoFHEW(c2, encodedLength2);

    std::cout << "\n---Decrypting switched ciphertext with large precision (plaintext modulus " << NativeInteger(pLWE2)
              << ")---\n"
              << std::endl;

    ptxt2->SetLength(encodedLength2);
    std::cout << "Input x2: " << ptxt2->GetRealPackedValue() << std::endl;
    std::cout << "FHEW decryption: ";
    for (uint32_t i = 0; i < cTemp2.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cTemp2[i], &result, pLWE2);
        std::cout << result << " ";
    }
    std::cout << "\n" << std::endl;

    // C: Decompose the FHEW ciphertexts in smaller digits
    std::cout << "Decomposed values for digit size of " << NativeInteger(pLWE1) << ": " << std::endl;
    // Generate the bootstrapping keys (refresh and switching keys)
    ccLWE->BTKeyGen(privateKeyFHEW);

    for (uint32_t j = 0; j < cTemp2.size(); j++) {
        // Decompose the large ciphertext into small ciphertexts that fit in q
        auto decomp = ccLWE->EvalDecomp(cTemp2[j]);

        // Decryption
        auto p = ccLWE->GetMaxPlaintextSpace().ConvertToInt();
        LWECiphertext ct;
        for (size_t i = 0; i < decomp.size(); i++) {
            ct = decomp[i];
            LWEPlaintext resultDecomp;
            // The last digit should be up to P / p^floor(log_p(P))
            if (i == decomp.size() - 1) {
                p = pLWE2 / std::pow(static_cast<double>(pLWE1), std::floor(std::log(pLWE2) / std::log(pLWE1)));
            }
            ccLWE->Decrypt(privateKeyFHEW, ct, &resultDecomp, p);
            std::cout << "(" << resultDecomp << " * " << NativeInteger(pLWE1) << "^" << i << ")";
            if (i != decomp.size() - 1) {
                std::cout << " + ";
            }
        }
        std::cout << std::endl;
    }
}

void SwitchFHEWtoCKKS() {
    std::cout << "\n-----SwitchFHEWtoCKKS-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back.\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS to be switched into

    // A. Specify main parameters
    ScalingTechnique scTech = FIXEDAUTO;
    // for r = 3 in FHEWtoCKKS, Chebyshev max depth allowed is 9, 1 more level for postscaling
    uint32_t multDepth = 3 + 9 + 1;
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;
    uint32_t scaleModSize = 50;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;  // If this is not HEStd_NotSet, ensure ringDim is compatible
    uint32_t logQ_ccLWE   = 28;

    // uint32_t slots = ringDim/2; // Uncomment for fully-packed
    uint32_t slots     = 16;  // sparsely-packed
    uint32_t batchSize = slots;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", number of slots " << slots << ", and supports a multiplicative depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    auto ccLWE = std::make_shared<BinFHEContext>();
    ccLWE->BinFHEContext::GenerateBinFHEContext(TOY, false, logQ_ccLWE, 0, GINX, false);

    // LWE private key
    LWEPrivateKey lwesk;
    lwesk = ccLWE->KeyGen();

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Step 3. Precompute the necessary keys and information for switching from FHEW to CKKS
    cc->EvalFHEWtoCKKSSetup(ccLWE, slots, logQ_ccLWE);
    cc->SetBinCCForSchemeSwitch(ccLWE);

    cc->EvalFHEWtoCKKSKeyGen(keys, lwesk);

    // Step 4: Encoding and encryption of inputs
    // For correct CKKS decryption, the messages have to be much smaller than the FHEW plaintext modulus!

    auto pLWE1       = ccLWE->GetMaxPlaintextSpace().ConvertToInt();  // Small precision
    uint32_t pLWE2   = 256;                                           // Medium precision
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE3       = modulus_LWE / (2 * beta);  // Large precision
    // Inputs
    std::vector<int> x1 = {1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0};
    std::vector<int> x2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    if (x1.size() < slots) {
        std::vector<int> zeros(slots - x1.size(), 0);
        x1.insert(x1.end(), zeros.begin(), zeros.end());
        x2.insert(x2.end(), zeros.begin(), zeros.end());
    }

    // Encrypt
    std::vector<LWECiphertext> ctxtsLWE1(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under small plantext modulus p = 4 and ciphertext modulus
        ctxtsLWE1[i] = ccLWE->Encrypt(lwesk, x1[i]);
    }

    std::vector<LWECiphertext> ctxtsLWE2(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under larger plaintext modulus p = 16 but small ciphertext modulus
        ctxtsLWE2[i] = ccLWE->Encrypt(lwesk, x1[i], LARGE_DIM, pLWE1);
    }

    std::vector<LWECiphertext> ctxtsLWE3(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under larger plaintext modulus and large ciphertext modulus
        ctxtsLWE3[i] = ccLWE->Encrypt(lwesk, x2[i], LARGE_DIM, pLWE2, modulus_LWE);
    }

    std::vector<LWECiphertext> ctxtsLWE4(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under large plaintext modulus and large ciphertext modulus
        ctxtsLWE4[i] = ccLWE->Encrypt(lwesk, x2[i], LARGE_DIM, pLWE3, modulus_LWE);
    }

    // Step 5. Perform the scheme switching
    auto cTemp = cc->EvalFHEWtoCKKS(ctxtsLWE1, slots, slots);

    std::cout << "\n---Input x1: " << x1 << " encrypted under p = " << 4 << " and Q = " << ctxtsLWE1[0]->GetModulus()
              << "---" << std::endl;

    // Step 6. Decrypt
    Plaintext plaintextDec;
    cc->Decrypt(keys.secretKey, cTemp, &plaintextDec);
    plaintextDec->SetLength(slots);
    std::cout << "Switched CKKS decryption 1: " << plaintextDec << std::endl;

    // Step 5'. Perform the scheme switching
    cTemp = cc->EvalFHEWtoCKKS(ctxtsLWE2, slots, slots, pLWE1, 0, pLWE1);

    std::cout << "\n---Input x1: " << x1 << " encrypted under p = " << NativeInteger(pLWE1)
              << " and Q = " << ctxtsLWE2[0]->GetModulus() << "---" << std::endl;

    // Step 6'. Decrypt
    cc->Decrypt(keys.secretKey, cTemp, &plaintextDec);
    plaintextDec->SetLength(slots);
    std::cout << "Switched CKKS decryption 2: " << plaintextDec << std::endl;

    // Step 5''. Perform the scheme switching
    cTemp = cc->EvalFHEWtoCKKS(ctxtsLWE3, slots, slots, pLWE2, 0, pLWE2);

    std::cout << "\n---Input x2: " << x2 << " encrypted under p = " << pLWE2
              << " and Q = " << ctxtsLWE3[0]->GetModulus() << "---" << std::endl;

    // Step 6''. Decrypt
    cc->Decrypt(keys.secretKey, cTemp, &plaintextDec);
    plaintextDec->SetLength(slots);
    std::cout << "Switched CKKS decryption 3: " << plaintextDec << std::endl;

    // Step 5'''. Perform the scheme switching
    std::setprecision(logQ_ccLWE + 10);
    auto cTemp2 = cc->EvalFHEWtoCKKS(ctxtsLWE4, slots, slots, pLWE3, 0, pLWE3);

    std::cout << "\n---Input x2: " << x2 << " encrypted under p = " << NativeInteger(pLWE3)
              << " and Q = " << ctxtsLWE4[0]->GetModulus() << "---" << std::endl;

    // Step 6'''. Decrypt
    Plaintext plaintextDec2;
    cc->Decrypt(keys.secretKey, cTemp2, &plaintextDec2);
    plaintextDec2->SetLength(slots);
    std::cout << "Switched CKKS decryption 4: " << plaintextDec2 << std::endl;
}

void FloorViaSchemeSwitching() {
    std::cout << "\n-----FloorViaSchemeSwitching-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back.\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    ScalingTechnique scTech = FLEXIBLEAUTO;

    // for r = 3 in FHEWtoCKKS, Chebyshev max depth allowed is 9, 1 more level for postscaling
    uint32_t multDepth = 3 + 9 + 1;
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;
    uint32_t scaleModSize = 50;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 23;
    uint32_t slots        = 16;  // sparsely-packed
    uint32_t batchSize    = slots;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", number of slots " << slots << ", and supports a multiplicative depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(slots);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    // Generate bootstrapping key for EvalFloor
    ccLWE->BTKeyGen(privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Set the scaling factor to be able to decrypt; under the hood, the LWE mod switch will be performed on the ciphertext at the last level
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE        = modulus_LWE / (2 * beta);  // Large precision
    double scaleCF   = 1.0 / pLWE;

    cc->EvalCKKStoFHEWPrecompute(scaleCF);

    // Step 3: Encoding and encryption of inputs
    // Inputs
    std::vector<double> x1 = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0};

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 4: Scheme switching from CKKS to FHEW
    auto cTemp = cc->EvalCKKStoFHEW(c1);

    // Step 5: Evaluate the floor function
    uint32_t bits = 2;

    std::vector<LWECiphertext> cFloor(cTemp.size());
    for (uint32_t i = 0; i < cTemp.size(); i++) {
        cFloor[i] = ccLWE->EvalFloor(cTemp[i], bits);
    }

    std::cout << "Input x1: " << ptxt1->GetRealPackedValue() << std::endl;
    std::cout << "Expected result for EvalFloor with " << bits << " bits: ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << (static_cast<int>(ptxt1->GetRealPackedValue()[i]) >> bits) << " ";
    }
    LWEPlaintext pFloor;
    std::cout << "\nFHEW decryption p = " << NativeInteger(pLWE)
              << "/(1 << bits) = " << NativeInteger(pLWE) / (1 << bits) << ": ";
    for (uint32_t i = 0; i < cFloor.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cFloor[i], &pFloor, pLWE / (1 << bits));
        std::cout << pFloor << " ";
    }
    std::cout << "\n" << std::endl;

    // Step 6: Scheme switching from FHEW to CKKS
    auto cTemp2 = cc->EvalFHEWtoCKKS(cFloor, slots, slots, pLWE / (1 << bits), 0, pLWE / (1 << bits));

    Plaintext plaintextDec2;
    cc->Decrypt(keys.secretKey, cTemp2, &plaintextDec2);
    plaintextDec2->SetLength(slots);
    std::cout << "Switched floor decryption modulus_LWE mod " << NativeInteger(pLWE) / (1 << bits) << ": "
              << plaintextDec2 << std::endl;
}

void FuncViaSchemeSwitching() {
    std::cout << "\n-----FuncViaSchemeSwitching-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back.\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    // 1 for CKKS to FHEW, 14 for FHEW to CKKS
    uint32_t multDepth    = 9 + 3 + 2;
    uint32_t scaleModSize = 50;
    uint32_t ringDim      = 2048;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    uint32_t slots        = 8;  // sparsely-packed
    uint32_t batchSize    = slots;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(FIXEDAUTO);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", and number of slots " << slots << std::endl << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetArbitraryFunctionEvaluation(true);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(slots);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    // Generate the bootstrapping keys for EvalFunc in FHEW
    ccLWE->BTKeyGen(privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Set the scaling factor to be able to decrypt; under the hood, the LWE mod switch will be performed on the ciphertext at the last level
    auto pLWE =
        ccLWE->GetMaxPlaintextSpace().ConvertToInt();  // Small precision because GenerateLUTviaFunction needs p < q
    double scaleCF = 1.0 / pLWE;

    cc->EvalCKKStoFHEWPrecompute(scaleCF);

    // Step 3: Initialize the function

    // Initialize Function f(x) = x^3 + 2x + 1 % p
    auto fp = [](NativeInteger m, NativeInteger p1) -> NativeInteger {
        if (m < p1)
            return (m * m * m + 2 * m * m + 1) % p1;
        else
            return ((m - p1 / 2) * (m - p1 / 2) * (m - p1 / 2) + 2 * (m - p1 / 2) * (m - p1 / 2) + 1) % p1;
    };

    // Generate LUT from function f(x)
    auto lut = ccLWE->GenerateLUTviaFunction(fp, pLWE);

    // Step 4: Encoding and encryption of inputs
    // Inputs
    std::vector<double> x1 = {0.0, 0.3, 2.0, 4.0, 5.0, 6.0, 7.0, 8.0};

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 5: Scheme switching from CKKS to FHEW
    auto cTemp = cc->EvalCKKStoFHEW(c1);

    std::cout << "Input x1: " << ptxt1->GetRealPackedValue() << std::endl;
    std::cout << "FHEW decryption: ";
    LWEPlaintext result;
    for (uint32_t i = 0; i < cTemp.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cTemp[i], &result, pLWE);
        std::cout << result << " ";
    }

    // Step 6: Evaluate the function
    std::vector<LWECiphertext> cFunc(cTemp.size());
    for (uint32_t i = 0; i < cTemp.size(); i++) {
        cFunc[i] = ccLWE->EvalFunc(cTemp[i], lut);
    }

    std::cout << "\nExpected result x^3 + 2*x + 1 mod p: ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << fp(static_cast<int>(x1[i]) % pLWE, pLWE) << " ";
    }
    LWEPlaintext pFunc;
    std::cout << "\nFHEW decryption mod " << NativeInteger(pLWE) << ": ";
    for (uint32_t i = 0; i < cFunc.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cFunc[i], &pFunc, pLWE);
        std::cout << pFunc << " ";
    }
    std::cout << "\n" << std::endl;

    // Step 7: Scheme switching from FHEW to CKKS
    auto cTemp2 = cc->EvalFHEWtoCKKS(cFunc, slots, slots, pLWE, 0, pLWE);

    Plaintext plaintextDec2;
    cc->Decrypt(keys.secretKey, cTemp2, &plaintextDec2);
    plaintextDec2->SetLength(slots);
    std::cout << "\nSwitched decryption modulus_LWE mod " << NativeInteger(pLWE)
              << " works only for messages << p: " << plaintextDec2 << std::endl;

    // Transform through arcsine
    cTemp2 = cc->EvalFHEWtoCKKS(cFunc, slots, slots, 4, 0, 2);

    cc->Decrypt(keys.secretKey, cTemp2, &plaintextDec2);
    plaintextDec2->SetLength(slots);
    std::cout << "Arcsin(switched result) * p/2pi gives the correct result if messages are < p/4: ";
    for (uint32_t i = 0; i < slots; i++) {
        double x = std::max(std::min(plaintextDec2->GetRealPackedValue()[i], 1.0), -1.0);
        std::cout << std::asin(x) * pLWE / (2 * Pi) << " ";
    }
    std::cout << "\n";
}

void ComparisonViaSchemeSwitching() {
    std::cout << "\n-----ComparisonViaSchemeSwitching-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back.\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    ScalingTechnique scTech = FLEXIBLEAUTO;
    uint32_t multDepth      = 17;
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;

    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    uint32_t slots        = 16;  // sparsely-packed
    uint32_t batchSize    = slots;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);
    parameters.SetSecretKeyDist(UNIFORM_TERNARY);
    parameters.SetKeySwitchTechnique(HYBRID);
    parameters.SetNumLargeDigits(3);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", number of slots " << slots << ", and supports a multiplicative depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(slots);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    ccLWE->BTKeyGen(privateKeyFHEW);
    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Set the scaling factor to be able to decrypt; the LWE mod switch is performed on the ciphertext at the last level
    auto pLWE1           = ccLWE->GetMaxPlaintextSpace().ConvertToInt();  // Small precision
    auto modulus_LWE     = 1 << logQ_ccLWE;
    auto beta            = ccLWE->GetBeta().ConvertToInt();
    auto pLWE2           = modulus_LWE / (2 * beta);  // Large precision
    double scaleSignFHEW = 1.0;
    cc->EvalCompareSwitchPrecompute(pLWE2, scaleSignFHEW);

    // Step 3: Encoding and encryption of inputs
    // Inputs
    std::vector<double> x1 = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0};
    std::vector<double> x2(slots, 5.25);

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr, slots);
    Plaintext ptxt2 = cc->MakeCKKSPackedPlaintext(x2, 1, 0, nullptr, slots);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);
    auto c2 = cc->Encrypt(keys.publicKey, ptxt2);

    // Compute the difference to compare to zero
    auto cDiff = cc->EvalSub(c1, c2);

    // Step 4: CKKS to FHEW switching and sign evaluation to test correctness
    Plaintext pDiff;
    cc->Decrypt(keys.secretKey, cDiff, &pDiff);
    pDiff->SetLength(slots);
    std::cout << "Difference of inputs: ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << pDiff->GetRealPackedValue()[i] << " ";
    }

    const double eps = 0.0001;
    std::cout << "\nExpected sign result from CKKS: ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << int(std::round(pDiff->GetRealPackedValue()[i] / eps) * eps < 0) << " ";
    }
    std::cout << "\n";

    auto LWECiphertexts = cc->EvalCKKStoFHEW(cDiff, slots);

    LWEPlaintext plainLWE;
    std::cout << "\nFHEW decryption with plaintext modulus " << NativeInteger(pLWE2) << ": ";
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, LWECiphertexts[i], &plainLWE, pLWE2);
        std::cout << plainLWE << " ";
    }

    std::cout << "\nExpected sign result in FHEW with plaintext modulus " << NativeInteger(pLWE2) << " and scale "
              << scaleSignFHEW << ": ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << (static_cast<int>(std::round(pDiff->GetRealPackedValue()[i] * scaleSignFHEW)) % pLWE2 -
                          pLWE2 / 2.0 >=
                      0)
                  << " ";
    }
    std::cout << "\n";

    std::cout << "Obtained sign result in FHEW with plaintext modulus " << NativeInteger(pLWE2) << " and scale "
              << scaleSignFHEW << ": ";
    std::vector<LWECiphertext> LWESign(LWECiphertexts.size());
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        LWESign[i] = ccLWE->EvalSign(LWECiphertexts[i]);
        ccLWE->Decrypt(privateKeyFHEW, LWESign[i], &plainLWE, 2);
        std::cout << plainLWE << " ";
    }
    std::cout << "\n";

    // Step 5: Direct comparison via CKKS->FHEW->CKKS
    auto cResult = cc->EvalCompareSchemeSwitching(c1, c2, slots, slots);

    Plaintext plaintextDec3;
    cc->Decrypt(keys.secretKey, cResult, &plaintextDec3);
    plaintextDec3->SetLength(slots);
    std::cout << "Decrypted switched result: " << plaintextDec3 << std::endl;

    // Step 2': Recompute the scaled matrix using a larger scaling
    scaleSignFHEW = 8.0;
    cc->EvalCompareSwitchPrecompute(pLWE2, scaleSignFHEW);

    // Step 4': CKKS to FHEW switching and sign evaluation to test correctness
    LWECiphertexts = cc->EvalCKKStoFHEW(cDiff, slots);

    std::cout << "\nFHEW decryption with plaintext modulus " << NativeInteger(pLWE2) << " and scale " << scaleSignFHEW
              << ": ";
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, LWECiphertexts[i], &plainLWE, pLWE2);
        std::cout << plainLWE << " ";
    }
    std::cout << "\nExpected sign result in FHEW with plaintext modulus " << NativeInteger(pLWE2) << " and scale "
              << scaleSignFHEW << ": ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << (static_cast<int>(std::round(pDiff->GetRealPackedValue()[i] * scaleSignFHEW)) % pLWE2 -
                          pLWE2 / 2.0 >=
                      0)
                  << " ";
    }
    std::cout << "\n";
    std::cout << "Obtained sign result in FHEW with plaintext modulus " << NativeInteger(pLWE2) << " and scale "
              << scaleSignFHEW << ": ";
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        LWESign[i] = ccLWE->EvalSign(LWECiphertexts[i]);
        ccLWE->Decrypt(privateKeyFHEW, LWESign[i], &plainLWE, 2);
        std::cout << plainLWE << " ";
    }
    std::cout << "\n";

    // Step 5': Direct comparison via CKKS->FHEW->CKKS
    cResult = cc->EvalCompareSchemeSwitching(c1, c2, slots, slots);

    cc->Decrypt(keys.secretKey, cResult, &plaintextDec3);
    plaintextDec3->SetLength(slots);
    std::cout << "Decrypted switched result: " << plaintextDec3 << std::endl;

    // Step 2'': Recompute the scaled matrix using other parameters
    std::cout
        << "\nFor very small LWE plaintext modulus and initial fractional inputs, the sign does not always behave properly close to the boundaries at 0 and p/2."
        << std::endl;
    scaleSignFHEW = 1.0;
    cc->EvalCompareSwitchPrecompute(pLWE1, scaleSignFHEW);

    // Step 4'': CKKS to FHEW switching and sign evaluation to test correctness
    LWECiphertexts = cc->EvalCKKStoFHEW(cDiff, slots);

    std::cout << "\nFHEW decryption with plaintext modulus " << NativeInteger(pLWE1) << ": ";
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, LWECiphertexts[i], &plainLWE, pLWE1);
        std::cout << plainLWE << " ";
    }
    std::cout << "\nExpected sign result in FHEW with plaintext modulus " << NativeInteger(pLWE1) << " and scale "
              << scaleSignFHEW << ": ";
    for (uint32_t i = 0; i < slots; ++i) {
        std::cout << (static_cast<int>(std::round(pDiff->GetRealPackedValue()[i] * scaleSignFHEW)) % pLWE1 -
                          pLWE1 / 2.0 >=
                      0)
                  << " ";
    }
    std::cout << "\n";
    std::cout << "Obtained sign result in FHEW with plaintext modulus " << NativeInteger(pLWE1) << " and scale "
              << scaleSignFHEW << ": ";
    for (uint32_t i = 0; i < LWECiphertexts.size(); ++i) {
        LWESign[i] = ccLWE->EvalSign(LWECiphertexts[i]);
        ccLWE->Decrypt(privateKeyFHEW, LWESign[i], &plainLWE, 2);
        std::cout << plainLWE << " ";
    }
    std::cout << "\n";

    // Step 5'': Direct comparison via CKKS->FHEW->CKKS
    cResult = cc->EvalCompareSchemeSwitching(c1, c2, slots, slots, 0, scaleSignFHEW);

    cc->Decrypt(keys.secretKey, cResult, &plaintextDec3);
    plaintextDec3->SetLength(slots);
    std::cout << "Decrypted switched result: " << plaintextDec3 << std::endl;
}

void ArgminViaSchemeSwitching() {
    std::cout << "\n-----ArgminViaSchemeSwitching-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    bool oneHot           = true;  // Change to false if the output should not be one-hot encoded

    uint32_t slots          = 16;  // sparsely-packed
    uint32_t batchSize      = slots;
    uint32_t numValues      = 16;
    ScalingTechnique scTech = FLEXIBLEAUTOEXT;
    // 13 for FHEW to CKKS, log2(numValues) for argmin
    uint32_t multDepth = 9 + 3 + 1 + static_cast<int>(std::log2(numValues));
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", and number of slots " << slots << ", and supports a depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(numValues);
    params.SetComputeArgmin(true);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Scale the inputs to ensure their difference is correctly represented after switching to FHEW
    double scaleSign = 512.0;
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE        = modulus_LWE / (2 * beta);  // Large precision
    // This formulation is for clarity
    cc->EvalCompareSwitchPrecompute(pLWE, scaleSign);
    // But we can also include the scaleSign in pLWE (here we use the fact both pLWE and scaleSign are powers of two)
    // cc->EvalCompareSwitchPrecompute(pLWE / scaleSign, 1);

    // Step 3: Encoding and encryption of inputs
    // Inputs
    std::vector<double> x1 = {-1.125, -1.12, 5.0,  6.0,  -1.0, 2.0,  8.0,   -1.0,
                              9.0,    10.0,  11.0, 12.0, 13.0, 14.0, 15.25, 15.30};
    if (x1.size() < numValues) {
        std::vector<int> zeros(numValues - x1.size(), 0);
        x1.insert(x1.end(), zeros.begin(), zeros.end());
    }

    std::cout << "Expected minimum value " << *(std::min_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::min_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl;
    std::cout << "Expected maximum value " << *(std::max_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::max_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl
              << std::endl;

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);  // Only if we we set batchsize
    // Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr, slots); // If batchsize is not set

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 4: Argmin evaluation
    auto result = cc->EvalMinSchemeSwitching(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMin;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMin);
    ptxtMin->SetLength(1);
    std::cout << "Minimum value: " << ptxtMin << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMin);
    if (oneHot) {
        ptxtMin->SetLength(numValues);
        std::cout << "Argmin indicator vector: " << ptxtMin << std::endl;
    }
    else {
        ptxtMin->SetLength(1);
        std::cout << "Argmin: " << ptxtMin << std::endl;
    }

    result = cc->EvalMaxSchemeSwitching(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMax;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMax);
    ptxtMax->SetLength(1);
    std::cout << "Maximum value: " << ptxtMax << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMax);
    if (oneHot) {
        ptxtMax->SetLength(numValues);
        std::cout << "Argmax indicator vector: " << ptxtMax << std::endl;
    }
    else {
        ptxtMax->SetLength(1);
        std::cout << "Argmax: " << ptxtMax << std::endl;
    }
}

void ArgminViaSchemeSwitchingAlt() {
    std::cout << "\n-----ArgminViaSchemeSwitchingAlt-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    bool oneHot           = true;  // Change to false if the output should not be one-hot encoded

    uint32_t slots          = 16;  // sparsely-packed
    uint32_t batchSize      = slots;
    uint32_t numValues      = 16;
    ScalingTechnique scTech = FLEXIBLEAUTOEXT;
    // 13 for FHEW to CKKS, log2(numValues) for argmin
    uint32_t multDepth = 9 + 3 + 1 + static_cast<int>(std::log2(numValues));
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", and number of slots " << slots << ", and supports a depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(numValues);
    params.SetComputeArgmin(true);
    params.SetUseAltArgmin(true);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Scale the inputs to ensure their difference is correctly represented after switching to FHEW
    double scaleSign = 512.0;
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE        = modulus_LWE / (2 * beta);  // Large precision
    // This formulation is for clarity
    cc->EvalCompareSwitchPrecompute(pLWE, scaleSign);
    // But we can also include the scaleSign in pLWE (here we use the fact both pLWE and scaleSign are powers of two)
    // cc->EvalCompareSwitchPrecompute(pLWE / scaleSign, 1);

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1 = {-1.125, -1.12, 5.0,  6.0,  -1.0, 2.0,  8.0,   -1.0,
                              9.0,    10.0,  11.0, 12.0, 13.0, 14.0, 15.25, 15.30};
    if (x1.size() < numValues) {
        std::vector<int> zeros(numValues - x1.size(), 0);
        x1.insert(x1.end(), zeros.begin(), zeros.end());
    }

    std::cout << "Expected minimum value " << *(std::min_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::min_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl;
    std::cout << "Expected maximum value " << *(std::max_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::max_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl
              << std::endl;

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);  // Only if we we set batchsize
    // Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1, 1, 0, nullptr, slots); // If batchsize is not set

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 4: Argmin evaluation
    auto result = cc->EvalMinSchemeSwitchingAlt(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMin;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMin);
    ptxtMin->SetLength(1);
    std::cout << "Minimum value: " << ptxtMin << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMin);
    if (oneHot) {
        ptxtMin->SetLength(numValues);
        std::cout << "Argmin indicator vector: " << ptxtMin << std::endl;
    }
    else {
        ptxtMin->SetLength(1);
        std::cout << "Argmin: " << ptxtMin << std::endl;
    }

    result = cc->EvalMaxSchemeSwitchingAlt(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMax;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMax);
    ptxtMax->SetLength(1);
    std::cout << "Maximum value: " << ptxtMax << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMax);
    if (oneHot) {
        ptxtMax->SetLength(numValues);
        std::cout << "Argmax indicator vector: " << ptxtMax << std::endl;
    }
    else {
        ptxtMax->SetLength(1);
        std::cout << "Argmax: " << ptxtMax << std::endl;
    }
}

void ArgminViaSchemeSwitchingUnit() {
    std::cout << "\n-----ArgminViaSchemeSwitchingUnit-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    bool oneHot           = true;

    uint32_t slots          = 32;  // sparsely-packed
    uint32_t batchSize      = slots;
    uint32_t numValues      = 32;
    ScalingTechnique scTech = FLEXIBLEAUTO;
    // 1 for CKKS to FHEW, 13 for FHEW to CKKS, log2(numValues) for argmin
    uint32_t multDepth = 9 + 3 + 1 + static_cast<int>(std::log2(numValues));
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);
    cc->Enable(FHE);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", and number of slots " << slots << ", and supports a depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(numValues);
    params.SetComputeArgmin(true);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Here we assume the message does not need scaling, as they are in the unit circle.
    cc->EvalCompareSwitchPrecompute(1, 1);

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1 = {-1.125, -1.12, 5.0,  6.0,  -1.0, 2.0,  8.0,   -1.0,
                              9.0,    10.0,  11.0, 12.0, 13.0, 14.0, 15.25, 15.30};
    if (x1.size() < slots) {
        std::vector<int> zeros(slots - x1.size(), 0);
        x1.insert(x1.end(), zeros.begin(), zeros.end());
    }
    std::cout << "Input: " << x1 << std::endl;

    /* Here we to assume each element of x1 is between (-0.5, 0.5]. The user will use heuristics on the size of the plaintext to achieve this.
     * This will mean that even the difference of the messages will be between (-1,1].
     * However, if a good enough approximation of the maximum is not available and the scaled inputs are too small, the precision of the result
     * might not be good enough.
     */
    double p = 1 << (firstModSize - scaleModSize - 1);
    std::transform(x1.begin(), x1.end(), x1.begin(), [&](const double& elem) { return elem / (2 * p); });

    std::cout << "Input scaled: " << x1 << std::endl;
    std::cout << "Expected minimum value " << *(std::min_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::min_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl;
    std::cout << "Expected maximum value " << *(std::max_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::max_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl
              << std::endl;

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 4: Argmin evaluation
    auto result = cc->EvalMinSchemeSwitching(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMin;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMin);
    ptxtMin->SetLength(1);
    std::cout << "Minimum value: " << ptxtMin << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMin);
    if (oneHot) {
        ptxtMin->SetLength(numValues);
        std::cout << "Argmin indicator vector: " << ptxtMin << std::endl;
    }
    else {
        ptxtMin->SetLength(1);
        std::cout << "Argmin: " << ptxtMin << std::endl;
    }

    result = cc->EvalMaxSchemeSwitching(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMax;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMax);
    ptxtMax->SetLength(1);
    std::cout << "Maximum value: " << ptxtMax << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMax);
    if (oneHot) {
        ptxtMax->SetLength(numValues);
        std::cout << "Argmax indicator vector: " << ptxtMax << std::endl;
    }
    else {
        ptxtMax->SetLength(1);
        std::cout << "Argmax: " << ptxtMax << std::endl;
    }
}

void ArgminViaSchemeSwitchingAltUnit() {
    std::cout << "\n-----ArgminViaSchemeSwitchingAltUnit-----\n" << std::endl;
    std::cout << "Output precision is only wrt the operations in CKKS after switching back\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS
    uint32_t scaleModSize = 50;
    uint32_t firstModSize = 60;
    uint32_t ringDim      = 8192;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;
    bool oneHot           = true;

    uint32_t slots          = 32;  // sparsely-packed
    uint32_t batchSize      = slots;
    uint32_t numValues      = 32;
    ScalingTechnique scTech = FLEXIBLEAUTO;
    // 1 for CKKS to FHEW, 13 for FHEW to CKKS, log2(numValues) for argmin
    uint32_t multDepth = 9 + 3 + 1 + static_cast<int>(std::log2(numValues));
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetFirstModSize(firstModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);
    cc->Enable(FHE);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", and number of slots " << slots << ", and supports a depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(numValues);
    params.SetComputeArgmin(true);
    params.SetUseAltArgmin(true);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    // Here we assume the message does not need scaling, as they are in the unit circle.
    cc->EvalCompareSwitchPrecompute(1, 1);

    // Step 3: Encoding and encryption of inputs

    // Inputs
    std::vector<double> x1 = {-1.125, -1.12, 5.0,  6.0,  -1.0, 2.0,  8.0,   -1.0,
                              9.0,    10.0,  11.0, 12.0, 13.0, 14.0, 15.25, 15.30};
    if (x1.size() < slots) {
        std::vector<int> zeros(slots - x1.size(), 0);
        x1.insert(x1.end(), zeros.begin(), zeros.end());
    }
    std::cout << "Input: " << x1 << std::endl;

    /* Here we to assume each element of x1 is between (-0.5, 0.5]. The user will use heuristics on the size of the plaintext to achieve this.
     * This will mean that even the difference of the messages will be between (-1,1].
     * However, if a good enough approximation of the maximum is not available and the scaled inputs are too small, the precision of the result
     * might not be good enough.
     */
    double p = 1 << (firstModSize - scaleModSize - 1);
    std::transform(x1.begin(), x1.end(), x1.begin(), [&](const double& elem) { return elem / (2 * p); });

    std::cout << "Input scaled: " << x1 << std::endl;
    std::cout << "Expected minimum value " << *(std::min_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::min_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl;
    std::cout << "Expected maximum value " << *(std::max_element(x1.begin(), x1.begin() + numValues)) << " at location "
              << std::max_element(x1.begin(), x1.begin() + numValues) - x1.begin() << std::endl
              << std::endl;

    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);

    // Step 4: Argmin evaluation
    auto result = cc->EvalMinSchemeSwitchingAlt(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMin;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMin);
    ptxtMin->SetLength(1);
    std::cout << "Minimum value: " << ptxtMin << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMin);
    if (oneHot) {
        ptxtMin->SetLength(numValues);
        std::cout << "Argmin indicator vector: " << ptxtMin << std::endl;
    }
    else {
        ptxtMin->SetLength(1);
        std::cout << "Argmin: " << ptxtMin << std::endl;
    }

    result = cc->EvalMaxSchemeSwitchingAlt(c1, keys.publicKey, numValues, slots);

    Plaintext ptxtMax;
    cc->Decrypt(keys.secretKey, result[0], &ptxtMax);
    ptxtMax->SetLength(1);
    std::cout << "Maximum value: " << ptxtMax << std::endl;
    cc->Decrypt(keys.secretKey, result[1], &ptxtMax);
    if (oneHot) {
        ptxtMax->SetLength(numValues);
        std::cout << "Argmax indicator vector: " << ptxtMax << std::endl;
    }
    else {
        ptxtMax->SetLength(1);
        std::cout << "Argmax: " << ptxtMax << std::endl;
    }
}

void PolyViaSchemeSwitching() {
    std::cout << "\n-----PolyViaSchemeSwitching-----\n" << std::endl;

    // Step 1: Setup CryptoContext for CKKS to be switched into

    // A. Specify main parameters
    ScalingTechnique scTech = FIXEDMANUAL;
    // for r = 3 in FHEWtoCKKS, Chebyshev max depth allowed is 9, 1 more level for postscaling, 3 levels for functionality
    uint32_t multDepth = 3 + 9 + 1 + 2;
    if (scTech == FLEXIBLEAUTOEXT)
        multDepth += 1;
    uint32_t scaleModSize = 50;
    uint32_t ringDim      = 2048;
    SecurityLevel sl      = HEStd_NotSet;
    BINFHE_PARAMSET slBin = TOY;
    uint32_t logQ_ccLWE   = 25;

    uint32_t slots     = 16;  // sparsely-packed
    uint32_t batchSize = slots;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(scTech);
    parameters.SetSecurityLevel(sl);
    parameters.SetRingDim(ringDim);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(SCHEMESWITCH);

    std::cout << "CKKS scheme is using ring dimension " << cc->GetRingDimension();
    std::cout << ", number of slots " << slots << ", and supports a multiplicative depth of " << multDepth << std::endl
              << std::endl;

    // Generate encryption keys.
    auto keys = cc->KeyGen();

    // Step 2: Prepare the FHEW cryptocontext and keys for FHEW and scheme switching
    SchSwchParams params;
    params.SetSecurityLevelCKKS(sl);
    params.SetSecurityLevelFHEW(slBin);
    params.SetCtxtModSizeFHEWLargePrec(logQ_ccLWE);
    params.SetNumSlotsCKKS(slots);
    params.SetNumValues(slots);
    auto privateKeyFHEW = cc->EvalSchemeSwitchingSetup(params);
    auto ccLWE          = cc->GetBinCCForSchemeSwitch();

    // Step 3. Precompute the necessary keys and information for switching from FHEW to CKKS and back
    cc->EvalSchemeSwitchingKeyGen(keys, privateKeyFHEW);

    std::cout << "FHEW scheme is using lattice parameter " << ccLWE->GetParams()->GetLWEParams()->Getn();
    std::cout << ", logQ " << logQ_ccLWE;
    std::cout << ", and modulus q " << ccLWE->GetParams()->GetLWEParams()->Getq() << std::endl << std::endl;

    auto pLWE1       = ccLWE->GetMaxPlaintextSpace().ConvertToInt();  // Small precision
    auto modulus_LWE = 1 << logQ_ccLWE;
    auto beta        = ccLWE->GetBeta().ConvertToInt();
    auto pLWE2       = modulus_LWE / (2 * beta);  // Large precision

    double scale1 = 1.0 / pLWE1;
    double scale2 = 1.0 / pLWE2;

    // Generate keys for the CKKS intermediate computation
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalRotateKeyGen(keys.secretKey, {1, 2});

    // Step 4: Encoding and encryption of inputs
    // For correct CKKS decryption, the messages have to be much smaller than the FHEW plaintext modulus!
    // Inputs
    std::vector<int32_t> x1 = {1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0};
    std::vector<int32_t> x2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    std::vector<int32_t> x1Rot(RotateInt(x1, 1));
    std::transform(x1Rot.begin(), x1Rot.end(), x1.begin(), x1Rot.begin(), std::plus<int>());
    std::vector<int32_t> x1Int(slots);
    std::transform(x1Rot.begin(), x1Rot.end(), x1Int.begin(), [&](const int32_t& elem) {
        return static_cast<int32_t>(static_cast<int32_t>(std::round(0.25 * elem * elem)) % pLWE1);
    });

    std::vector<int32_t> x2Rot(RotateInt(x2, 2));
    std::transform(x2Rot.begin(), x2Rot.end(), x2.begin(), x2Rot.begin(), std::plus<int>());
    std::vector<int32_t> x2Int(slots);
    std::transform(x2Rot.begin(), x2Rot.end(), x2Int.begin(), [&](const int32_t& elem) {
        return static_cast<int32_t>(static_cast<int32_t>(std::round(0.25 * elem * elem)) % pLWE2);
    });

    // Encrypt
    std::vector<LWECiphertext> ctxtsLWE1(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under small plantext modulus p = 4 and ciphertext modulus
        ctxtsLWE1[i] = ccLWE->Encrypt(privateKeyFHEW, x1[i]);
    }

    std::vector<LWECiphertext> ctxtsLWE2(slots);
    for (uint32_t i = 0; i < slots; i++) {
        // encrypted under large plaintext modulus and large ciphertext modulus
        ctxtsLWE2[i] = ccLWE->Encrypt(privateKeyFHEW, x2[i], LARGE_DIM, pLWE2, modulus_LWE);
    }

    // Step 5. Perform the scheme switching
    auto cTemp = cc->EvalFHEWtoCKKS(ctxtsLWE1, slots, slots);

    std::cout << "\nInput x1: " << x1 << " encrypted under p = " << 4 << " and Q = " << ctxtsLWE1[0]->GetModulus()
              << std::endl;
    std::cout << "round( 0.5 * (x1 + rot(x1,1) )^2 ): " << x1Int << std::endl;

    // Step 6. Perform the desired computation in CKKS
    auto cPoly = cc->EvalAdd(cTemp, cc->EvalRotate(cTemp, 1));
    cPoly      = cc->EvalMult(cc->EvalMult(cPoly, cPoly), 0.25);

    // Perform the precomputation for switching back to CKKS
    cc->EvalCKKStoFHEWPrecompute(scale1);

    // Transform the ciphertext from CKKS to FHEW
    auto cTemp1 = cc->EvalCKKStoFHEW(cPoly, slots);

    LWEPlaintext result;
    std::cout << "FHEW decryption with plaintext modulus " << NativeInteger(pLWE1) << ": ";
    for (uint32_t i = 0; i < cTemp1.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cTemp1[i], &result, pLWE1);
        std::cout << result << " ";
    }
    std::cout << "\n" << std::endl;

    // Step 5'. Perform the scheme switching
    cTemp = cc->EvalFHEWtoCKKS(ctxtsLWE2, slots, slots, pLWE2, 0, pLWE2);

    std::cout << "\nInput x2: " << x2 << " encrypted under p = " << NativeInteger(pLWE2)
              << " and Q = " << ctxtsLWE2[0]->GetModulus() << std::endl;
    std::cout << "round( 0.5 * (x1 + rot(x2,2) )^2 ): " << x2Int << std::endl;

    // Step 6'. Perform the desired computation in CKKS
    cPoly = cc->EvalAdd(cTemp, cc->EvalRotate(cTemp, 2));
    cPoly = cc->EvalMult(cc->EvalMult(cPoly, cPoly), 0.25);

    // Perform the precomputation for switching back to CKKS
    cc->EvalCKKStoFHEWPrecompute(scale2);

    // Transform the ciphertext from CKKS to FHEW
    auto cTemp2 = cc->EvalCKKStoFHEW(cPoly, slots);

    std::cout << "FHEW decryption with plaintext modulus " << NativeInteger(pLWE2) << ": ";
    for (uint32_t i = 0; i < cTemp2.size(); ++i) {
        ccLWE->Decrypt(privateKeyFHEW, cTemp2[i], &result, pLWE2);
        std::cout << result << " ";
    }
    std::cout << "\n" << std::endl;
}

std::vector<int32_t> RotateInt(const std::vector<int32_t>& a, int32_t index) {
    int32_t slots = a.size();

    std::vector<int32_t> result(slots);

    if (index < 0 || index > slots) {
        index = ReduceRotation(index, slots);
    }

    if (index == 0) {
        result = a;
    }

    else {
        // two cases: i+index <= slots and i+index > slots
        for (int32_t i = 0; i < slots - index; i++) {
            result[i] = a[i + index];
        }
        for (int32_t i = slots - index; i < slots; i++) {
            result[i] = a[i + index - slots];
        }
    }

    return result;
}



================================================
FILE: SCHEME_SWITCHING_CAPABILITY.md
================================================
OpenFHE Lattice Cryptography Library - Scheme switching between CKKS and FHEW experimental capability
=====================================================================================================

[License Information](License.md)

Document Description
====================
This document describes how to use the scheme switching functionality to convert between CKKS and FHEW ciphertexts and perform intermediate
operations.

Example Description
====================

The example for this code is located in [scheme-switching.cpp](scheme-switching.cpp). The file gives examples on how to run:
- `EvalCKKStoFHEW`, which converts a CKKS ciphertext to FHEW ciphertexts;
- `EvalFHEWtoCKKS`, which converts FHEW ciphertexts to a CKKS ciphertext;
- how to combine the two with intermediate operations, for example the floor function or a polynomial;
- `EvalCompareSchemeSwitching `, which returns the result of the comparison between two CKKS ciphertexts via transformation to FHEW ciphertexts
and comparison;
- `EvalMinSchemeSwitching`, `EvalMinSchemeSwitchingAlt` and `EvalMaxSchemeSwitching`, `EvalMaxSchemeSwitchingAlt` respectively, which return
the min and argmin, respectively max and argmax, of a vector of reals packed inside a CKKS ciphertext, via iterated scheme switching.


Functionality
=============

**CKKS->FHEW**
We can transform a CKKS ciphertext (slot-packed and under public key encryption) into FHEW ciphertexts (symmetric key encryption), where
each FHEW ciphertext encrypts a slot of the CKKS ciphertext. The conversion is done by computing the scaled homomorphic decoding (via a
linear transform which can be precomputed), modulus switching, key switching, LWE extraction from RLWE, and another modulus switching.

The features that need to be enabled are PKE, KEYSWITCH, LEVELEDSHE and SCHEMESWITCH.

The user has to generate a CKKS cryptocontext and keys with the desired parameters, as well as to set up the FHEW cryptocontext and
private key through `EvalCKKStoFHEWSetup` and the automorphism keys and key switch hints through `EvalCKKStoFHEWKeyGen`. The setup is
completed by calling `EvalCKKStoFHEWPrecompute` which takes as argument the scale with which to multiply the decoding matrix, which
in most cases should be chosen by the user to be 1 / p, where p is the desired FHEW plaintext modulus; internally, the scale will be
transformed to Q / (scFactor * p), where Q is the CKKS ciphertext modulus on level 0, scFactor is the CKKS scaling factor for that level.
If the scale is left to be the default value of 1, the implicit FHEW plaintext modulus will be Q / scFactor, and the user should take this
into account. Finally, the user can also divide separately the messages by p, and input plaintexts in the unit circle (which translates
to an internal scaling only by Q / scFactor) and recover the initial message in FHEW.

After the setup and precomputation, the user should call `EvalCKKStoFHEW`. The number of slots to be converted is specified by the user,
otherwise it defaults to the number of slots specified in the CKKS scheme. Note that FHEW plaintexts are integers, so the messages from
CKKS will be rounded (and are expected to fit in the FHEW plaintext modulus).

**FHEW->CKKS**
We can transform a number of FHEW ciphertexts (symmetric key encryption) into a CKKS ciphertext (public key encryption) encrypting in
its slots the input messages. The conversion is done by evaluating the FHEW decryption homomorphically (via a linear transform, which
cannot be precomputed because it depends on the ciphertexts), then computing the polynomial interpolation of the modular reduction
function (approximated via the sine function), and finally postprocessing the ciphertext to the appropriate message range.

The features that need to be enabled are PKE, KEYSWITCH, LEVELEDSHE, ADVANCEDSHE and SCHEMESWITCH.

The user has to generate a CKKS cryptocontext and keys with the desired parameters, as well as a FHEW cryptocontext and private key.
The setup also includes precomputing the necessary automorphism keys and CKKS encryption of the FHEW secret key, as well as other
information for switching from FHEW to CKKS, through `EvalFHEWtoCKKSSetup` and `EvalFHEWtoCKKSKeyGen`.

The conversion between FHEW to CKKS is called via `EvalFHEWtoCKKS`, where the user has to specify the number of ciphertexts to
convert into a single CKKS ciphertext, the FHEW plaintext modulus (by default 4), and if the output is not binary, the range for
postprocessing the CKKS ciphertext after the Chebyshev polynomial evaluation. The example `SwitchFHEWtoCKKS()` illustrates this aspect.

Importantly, for correct CKKS decryption, the messages have to be much smaller than the FHEW plaintext modulus used when encrypting in
FHEW. The reason for this is that the modular reduction approximation implemented works well around zero, so m/p should be very small.
(If this does not happen, only small messages will be converted correctly.) Moreover, since the postprocessing implies multiplying
by the FHEW plaintext modulus used, which can be large depending on the target application, some loss of precision is expected when the
message space is large.

**CKKS->FHEW->operation->CKKS**
With the previous two modules in place, we can also work with CKKS ciphertexts, convert them to FHEW, perform operations on them, and
then convert the result back to CKKS.

The user has to generate a CKKS cryptocontext and keys with the desired parameters, then call `EvalSchemeSwitchingSetup` and
`EvalSchemeSwitchingKeyGen`, which combine the setups for both conversions, then the precomputation for the CKKS to FHEW conversion
`EvalCKKStoFHEWPrecompute` as above or `EvalCompareSwitchPrecompute`, and the `BTKeyGen` for the desired intermediate FHEW computations.

After calling `EvalCKKStoFHEW`, the user then applies the desired functions on the FHEW ciphertexts. In the example
`FloorViaSchemeSwitching()` the function is generalized floor/shifted truncation, in the example `ComparisonViaSchemeSwitching()`
the function is comparison between two vectors, and in the example `FuncViaSchemeSwitching()` the function is specified and computed
through `GenerateLUTviaFunction`.

Finally, `EvalFHEWtoCKKS` should be called to switch back to CKKS, where the plaintext modulus of the output of the above function should
be specified (e.g., 4 for the output of comparison).

Recall that FHEW supports integers, while CKKS encodes real values. Therefore, a rounding is done during the conversion. For instance, to
correctly compare numbers that are very close to each other, the user has to scale the inputs with the desired precision. The example
`ComparisonViaSchemeSwitching()` shows how to do this via `EvalCompareSwitchPrecompute`.

Currently, the code does not support an arbitrary function to be applied to the intermediate FHEW ciphertexts if they have to be converted
back to CKKS. The reason is that (1) the current implementation of `GenerateLUTviaFunction` works only for the small decryption ciphertext
modulus q = 2048, which allows a plaintext modulus of at most p = 8 (`GetMaxPlaintextSpace()`) and (2) the current implementation of light
bootstrapping to convert FHEW ciphertexts to a CKKS ciphertext approximates correctly the modular function only arround zero, which requires
the messagee m << p. Instead of specifying directly the larger plaintext modulus in `EvalFHEWtoCKKS`, which is required to postprocess
the ciphertext obtained after the Chebyshev evaluation, one can supply the plaintext modulus as 4, which returns a ciphertext
encrypting $y=sin(2pi*x/p)$. Then, one can apply $arcsin(y)*p/(2pi)$. However, this also does not cover the whole initial message space,
since arcsin has codomain $[-pi/2, pi/2]$. This issue is exemplified in the example `FloorViaSchemeSwitching()`.

**FHEW->CKKS->operation->FHEW**
This functionality is the mirror of the above. The user should call `EvalSchemeSwitchingSetup`, `EvalSchemeSwitchingKeyGen`,
`EvalCKKStoFHEWPrecompute`, and generate the keys which are required for the intermediate CKKS computations. After calling `EvalFHEWtoCKKS`,
the user can then apply the desired functions on the CKKS ciphertext. In the example `PolyViaSchemeSwitching`, this intermediate function
involves rotations, multiplications and additions. Finally, `EvalCKKStoFHEW` should be called to switch back to FHEW (where the plaintext
modulus to be used in decryption was used to compute the scale in `EvalCKKStoFHEWPrecompute`).

**Iterated scheme switching: min/argmin and max/argmax**
We also support repeated scheme switching between CKKS and FHEW with intermediate computations in each scheme. One such example is
computing the minimum and argminimum, respectively the maximum and argmaximum, of a vector encrypted initially in a CKKS ciphertext.

The functionality is computed in a binary tree approach. First, the first half is compared to the second half of the vector: the
difference is computed in CKKS, then switched to FHEW where the signs of the difference are computed, and switched back to CKKS.
Second, using multiplication in CKKS, only half of the slots are selected to update the vector for the next iteration (the ones
corresponding to a negative difference for min and the ones corresponding to a positive difference for max), and the process repeats
until reaching a vector of length of one.

We provide two instantiation of the above intuition, `EvalMinSchemeSwitching` which performs more operations in CKKS and is exemplified
in `ArgminViaSchemeSwitching()`, and `EvalMinSchemeSwitchingAlt` which performs more operations in FHEW and is exemplified in
`ArgminViaSchemeSwitchingAlt()`.

For a good precision of the output, we require a large scaling factor and large first modsize in CKKS, as well as large ciphertext
modulus and plaintext modulus in FHEW. Note that because CKKS is an approximate scheme, performing more operations in CKKS can lead
to a decrease in precision.

The user should call `EvalSchemeSwitchingSetup`, then `EvalSchemeSwitchingKeyGen`, specifying whether the argmin/argmax should have a
one-hot encoding or not, as well as if the alternative computation method mentioned above should be used, then `EvalCompareSwitchPrecompute`
specifying if an additional scaling if desired. As mentioned above, the user can manually scale the inputs to [-0.5, 0.5], (such that
the difference of values is between [-1, 1]) in which case the precomputation does not need to have any scaling, and this is
exemplified in `ArgminViaSchemeSwitchingUnit()` and `ArgminViaSchemeSwitchingUnitAlt()`.

Finally, the user should call `EvalMinSchemeSwitching` or `EvalMinSchemeSwitchingAlt` to obtain the minimum value and the argmin, and
respectively, `EvalMaxSchemeSwitching` or `EvalMaxSchemeSwitchingAlt` to obtain the maximum value and the argmax.

**Current limitations**
- Scheme switching is currently supported only for CKKS and FHEW/TFHE.
- Switching from CKKS to FHEW is only supported for the first consecutive slots in the CKKS ciphertext.
- Switching to CKKS the result of an arbitrary function evaluation in FHEW is not yet supported. Only functions with binary outputs or small outputs with respect to the FHEW plaintext space are supported.
- Computing the min/max via scheme switching is only implemented for vectors of size a power of two.
- Large memory consumption for large number of slots (because of the linear transform required in the switching and that the keys are created with the maximum number of levels)
- Only GINX with uniform ternary secrets is currently supported for scheme switching.



================================================
FILE: simple-ckks-bootstrapping.cpp
================================================
/*

Example for CKKS bootstrapping with full packing

*/

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

void SimpleBootstrapExample();

int main(int argc, char* argv[]) {
    SimpleBootstrapExample();
}

void SimpleBootstrapExample() {
    CCParams<CryptoContextCKKSRNS> parameters;
    // A. Specify main parameters
    /*  A1) Secret key distribution
    * The secret key distribution for CKKS should either be SPARSE_TERNARY or UNIFORM_TERNARY.
    * The SPARSE_TERNARY distribution was used in the original CKKS paper,
    * but in this example, we use UNIFORM_TERNARY because this is included in the homomorphic
    * encryption standard.
    */
    SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
    parameters.SetSecretKeyDist(secretKeyDist);

    /*  A2) Desired security level based on FHE standards.
    * In this example, we use the "NotSet" option, so the example can run more quickly with
    * a smaller ring dimension. Note that this should be used only in
    * non-production environments, or by experts who understand the security
    * implications of their choices. In production-like environments, we recommend using
    * HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
    * or 256-bit security, respectively. If you choose one of these as your security level,
    * you do not need to set the ring dimension.
    */
    parameters.SetSecurityLevel(HEStd_NotSet);
    parameters.SetRingDim(1 << 12);

    /*  A3) Scaling parameters.
    * By default, we set the modulus sizes and rescaling technique to the following values
    * to obtain a good precision and performance tradeoff. We recommend keeping the parameters
    * below unless you are an FHE expert.
    */
#if NATIVEINT == 128 && !defined(__EMSCRIPTEN__)
    ScalingTechnique rescaleTech = FIXEDAUTO;
    usint dcrtBits               = 78;
    usint firstMod               = 89;
#else
    ScalingTechnique rescaleTech = FLEXIBLEAUTO;
    usint dcrtBits               = 59;
    usint firstMod               = 60;
#endif

    parameters.SetScalingModSize(dcrtBits);
    parameters.SetScalingTechnique(rescaleTech);
    parameters.SetFirstModSize(firstMod);

    /*  A4) Multiplicative depth.
    * The goal of bootstrapping is to increase the number of available levels we have, or in other words,
    * to dynamically increase the multiplicative depth. However, the bootstrapping procedure itself
    * needs to consume a few levels to run. We compute the number of bootstrapping levels required
    * using GetBootstrapDepth, and add it to levelsAvailableAfterBootstrap to set our initial multiplicative
    * depth. We recommend using the input parameters below to get started.
    */
    std::vector<uint32_t> levelBudget = {4, 4};

    // Note that the actual number of levels avalailable after bootstrapping before next bootstrapping 
    // will be levelsAvailableAfterBootstrap - 1 because an additional level
    // is used for scaling the ciphertext before next bootstrapping (in 64-bit CKKS bootstrapping)
    uint32_t levelsAvailableAfterBootstrap = 10;
    usint depth = levelsAvailableAfterBootstrap + FHECKKSRNS::GetBootstrapDepth(levelBudget, secretKeyDist);
    parameters.SetMultiplicativeDepth(depth);

    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    cryptoContext->Enable(ADVANCEDSHE);
    cryptoContext->Enable(FHE);

    usint ringDim = cryptoContext->GetRingDimension();
    // This is the maximum number of slots that can be used for full packing.
    usint numSlots = ringDim / 2;
    std::cout << "CKKS scheme is using ring dimension " << ringDim << std::endl << std::endl;

    cryptoContext->EvalBootstrapSetup(levelBudget);

    auto keyPair = cryptoContext->KeyGen();
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);
    cryptoContext->EvalBootstrapKeyGen(keyPair.secretKey, numSlots);

    std::vector<double> x = {0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0};
    size_t encodedLength  = x.size();

    // We start with a depleted ciphertext that has used up all of its levels.
    Plaintext ptxt = cryptoContext->MakeCKKSPackedPlaintext(x, 1, depth - 1);

    ptxt->SetLength(encodedLength);
    std::cout << "Input: " << ptxt << std::endl;

    Ciphertext<DCRTPoly> ciph = cryptoContext->Encrypt(keyPair.publicKey, ptxt);

    std::cout << "Initial number of levels remaining: " << depth - ciph->GetLevel() << std::endl;

    // Perform the bootstrapping operation. The goal is to increase the number of levels remaining
    // for HE computation.
    auto ciphertextAfter = cryptoContext->EvalBootstrap(ciph);

    std::cout << "Number of levels remaining after bootstrapping: "
              << depth - ciphertextAfter->GetLevel() - (ciphertextAfter->GetNoiseScaleDeg() - 1) << std::endl
              << std::endl;

    Plaintext result;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextAfter, &result);
    result->SetLength(encodedLength);
    std::cout << "Output after bootstrapping \n\t" << result << std::endl;
}



================================================
FILE: simple-integers-serial.cpp
================================================
//==================================================================================
// BSD 2-Clause License
//
// Copyright (c) 2014-2022, NJIT, Duality Technologies Inc. and other contributors
//
// All rights reserved.
//
// Author TPOC: contact@openfhe.org
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//==================================================================================

/*
  Simple example for BFVrns (integer arithmetic) with serialization. Refer to the simple-real-numbers-serial file for
  an example of how to use. this in a "client-server" setup
 */

#include "openfhe.h"

// header files needed for serialization
#include "ciphertext-ser.h"
#include "cryptocontext-ser.h"
#include "key/key-ser.h"
#include "scheme/bfvrns/bfvrns-ser.h"

using namespace lbcrypto;

const std::string DATAFOLDER = "demoData";

int main() {
    std::cout << "This program requres the subdirectory `" << DATAFOLDER << "' to exist, otherwise you will get "
              << "an error writing serializations." << std::endl;

    // Sample Program: Step 1: Set CryptoContext
    CCParams<CryptoContextBFVRNS> parameters;
    parameters.SetPlaintextModulus(65537);
    parameters.SetMultiplicativeDepth(2);

    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);
    // Enable features that you wish to use
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);

    std::cout << "\nThe cryptocontext has been generated." << std::endl;

    // Serialize cryptocontext
    if (!Serial::SerializeToFile(DATAFOLDER + "/cryptocontext.txt", cryptoContext, SerType::BINARY)) {
        std::cerr << "Error writing serialization of the crypto context to "
                     "cryptocontext.txt"
                  << std::endl;
        return 1;
    }
    std::cout << "The cryptocontext has been serialized." << std::endl;

    // Sample Program: Step 2: Key Generation

    // Initialize Public Key Containers
    KeyPair<DCRTPoly> keyPair;

    // Generate a public/private key pair
    keyPair = cryptoContext->KeyGen();

    std::cout << "The key pair has been generated." << std::endl;

    // Serialize the public key
    if (!Serial::SerializeToFile(DATAFOLDER + "/key-public.txt", keyPair.publicKey, SerType::BINARY)) {
        std::cerr << "Error writing serialization of public key to key-public.txt" << std::endl;
        return 1;
    }
    std::cout << "The public key has been serialized." << std::endl;

    // Serialize the secret key
    if (!Serial::SerializeToFile(DATAFOLDER + "/key-private.txt", keyPair.secretKey, SerType::BINARY)) {
        std::cerr << "Error writing serialization of private key to key-private.txt" << std::endl;
        return 1;
    }
    std::cout << "The secret key has been serialized." << std::endl;

    // Generate the relinearization key
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);

    std::cout << "The eval mult keys have been generated." << std::endl;

    // Serialize the relinearization (evaluation) key for homomorphic
    // multiplication
    std::ofstream emkeyfile(DATAFOLDER + "/" + "key-eval-mult.txt", std::ios::out | std::ios::binary);
    if (emkeyfile.is_open()) {
        if (cryptoContext->SerializeEvalMultKey(emkeyfile, SerType::BINARY) == false) {
            std::cerr << "Error writing serialization of the eval mult keys to "
                         "key-eval-mult.txt"
                      << std::endl;
            return 1;
        }
        std::cout << "The eval mult keys have been serialized." << std::endl;

        emkeyfile.close();
    }
    else {
        std::cerr << "Error serializing eval mult keys" << std::endl;
        return 1;
    }

    // Generate the rotation evaluation keys
    cryptoContext->EvalRotateKeyGen(keyPair.secretKey, {1, 2, -1, -2});

    std::cout << "The rotation keys have been generated." << std::endl;

    // Serialize the rotation keyhs
    std::ofstream erkeyfile(DATAFOLDER + "/" + "key-eval-rot.txt", std::ios::out | std::ios::binary);
    if (erkeyfile.is_open()) {
        if (cryptoContext->SerializeEvalAutomorphismKey(erkeyfile, SerType::BINARY) == false) {
            std::cerr << "Error writing serialization of the eval rotation keys to "
                         "key-eval-rot.txt"
                      << std::endl;
            return 1;
        }
        std::cout << "The eval rotation keys have been serialized." << std::endl;

        erkeyfile.close();
    }
    else {
        std::cerr << "Error serializing eval rotation keys" << std::endl;
        return 1;
    }

    // Sample Program: Step 3: Encryption

    // First plaintext vector is encoded
    std::vector<int64_t> vectorOfInts1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext1               = cryptoContext->MakePackedPlaintext(vectorOfInts1);
    // Second plaintext vector is encoded
    std::vector<int64_t> vectorOfInts2 = {3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext2               = cryptoContext->MakePackedPlaintext(vectorOfInts2);
    // Third plaintext vector is encoded
    std::vector<int64_t> vectorOfInts3 = {1, 2, 5, 2, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext3               = cryptoContext->MakePackedPlaintext(vectorOfInts3);

    std::cout << "Plaintext #1: " << plaintext1 << std::endl;
    std::cout << "Plaintext #2: " << plaintext2 << std::endl;
    std::cout << "Plaintext #3: " << plaintext3 << std::endl;

    // The encoded vectors are encrypted
    auto ciphertext1 = cryptoContext->Encrypt(keyPair.publicKey, plaintext1);
    auto ciphertext2 = cryptoContext->Encrypt(keyPair.publicKey, plaintext2);
    auto ciphertext3 = cryptoContext->Encrypt(keyPair.publicKey, plaintext3);

    std::cout << "The plaintexts have been encrypted." << std::endl;

    if (!Serial::SerializeToFile(DATAFOLDER + "/" + "ciphertext1.txt", ciphertext1, SerType::BINARY)) {
        std::cerr << "Error writing serialization of ciphertext 1 to ciphertext1.txt" << std::endl;
        return 1;
    }
    std::cout << "The first ciphertext has been serialized." << std::endl;

    if (!Serial::SerializeToFile(DATAFOLDER + "/" + "ciphertext2.txt", ciphertext2, SerType::BINARY)) {
        std::cerr << "Error writing serialization of ciphertext 2 to ciphertext2.txt" << std::endl;
        return 1;
    }
    std::cout << "The second ciphertext has been serialized." << std::endl;

    if (!Serial::SerializeToFile(DATAFOLDER + "/" + "ciphertext3.txt", ciphertext3, SerType::BINARY)) {
        std::cerr << "Error writing serialization of ciphertext 3 to ciphertext3.txt" << std::endl;
        return 1;
    }
    std::cout << "The third ciphertext has been serialized." << std::endl;

    // Sample Program: Step 4: Evaluation

    // OpenFHE maintains an internal map of CryptoContext objects which are
    // indexed by a tag and the tag is applied to both the CryptoContext and some
    // of the keys. When deserializing a context, OpenFHE checks for the tag and
    // if it finds it in the CryptoContext map, it will return the stored version.
    // Hence, we need to clear the context and clear the keys.
    cryptoContext->ClearEvalMultKeys();
    cryptoContext->ClearEvalAutomorphismKeys();
    lbcrypto::CryptoContextFactory<lbcrypto::DCRTPoly>::ReleaseAllContexts();

    // Deserialize the crypto context
    CryptoContext<DCRTPoly> cc;
    if (!Serial::DeserializeFromFile(DATAFOLDER + "/cryptocontext.txt", cc, SerType::BINARY)) {
        std::cerr << "I cannot read serialization from " << DATAFOLDER + "/cryptocontext.txt" << std::endl;
        return 1;
    }
    std::cout << "The cryptocontext has been deserialized." << std::endl;

    PublicKey<DCRTPoly> pk;
    if (Serial::DeserializeFromFile(DATAFOLDER + "/key-public.txt", pk, SerType::BINARY) == false) {
        std::cerr << "Could not read public key" << std::endl;
        return 1;
    }
    std::cout << "The public key has been deserialized." << std::endl;

    std::ifstream emkeys(DATAFOLDER + "/key-eval-mult.txt", std::ios::in | std::ios::binary);
    if (!emkeys.is_open()) {
        std::cerr << "I cannot read serialization from " << DATAFOLDER + "/key-eval-mult.txt" << std::endl;
        return 1;
    }
    if (cc->DeserializeEvalMultKey(emkeys, SerType::BINARY) == false) {
        std::cerr << "Could not deserialize the eval mult key file" << std::endl;
        return 1;
    }
    std::cout << "Deserialized the eval mult keys." << std::endl;

    std::ifstream erkeys(DATAFOLDER + "/key-eval-rot.txt", std::ios::in | std::ios::binary);
    if (!erkeys.is_open()) {
        std::cerr << "I cannot read serialization from " << DATAFOLDER + "/key-eval-rot.txt" << std::endl;
        return 1;
    }
    if (cc->DeserializeEvalAutomorphismKey(erkeys, SerType::BINARY) == false) {
        std::cerr << "Could not deserialize the eval rotation key file" << std::endl;
        return 1;
    }
    std::cout << "Deserialized the eval rotation keys." << std::endl;

    Ciphertext<DCRTPoly> ct1;
    if (Serial::DeserializeFromFile(DATAFOLDER + "/ciphertext1.txt", ct1, SerType::BINARY) == false) {
        std::cerr << "Could not read the ciphertext" << std::endl;
        return 1;
    }
    std::cout << "The first ciphertext has been deserialized." << std::endl;

    Ciphertext<DCRTPoly> ct2;
    if (Serial::DeserializeFromFile(DATAFOLDER + "/ciphertext2.txt", ct2, SerType::BINARY) == false) {
        std::cerr << "Could not read the ciphertext" << std::endl;
        return 1;
    }
    std::cout << "The second ciphertext has been deserialized." << std::endl;

    Ciphertext<DCRTPoly> ct3;
    if (Serial::DeserializeFromFile(DATAFOLDER + "/ciphertext3.txt", ct3, SerType::BINARY) == false) {
        std::cerr << "Could not read the ciphertext" << std::endl;
        return 1;
    }
    std::cout << "The third ciphertext has been deserialized." << std::endl;

    // Homomorphic additions
    auto ciphertextAdd12     = cc->EvalAdd(ct1, ct2);              // iphertext2);
    auto ciphertextAddResult = cc->EvalAdd(ciphertextAdd12, ct3);  // iphertext3);

    // Homomorphic multiplications
    auto ciphertextMul12      = cc->EvalMult(ct1, ct2);              // iphertext2);
    auto ciphertextMultResult = cc->EvalMult(ciphertextMul12, ct3);  // iphertext3);

    // Homomorphic rotations
    auto ciphertextRot1 = cc->EvalRotate(ct1, 1);
    auto ciphertextRot2 = cc->EvalRotate(ct1, 2);
    auto ciphertextRot3 = cc->EvalRotate(ct1, -1);
    auto ciphertextRot4 = cc->EvalRotate(ct1, -2);

    // Sample Program: Step 5: Decryption

    PrivateKey<DCRTPoly> sk;
    if (Serial::DeserializeFromFile(DATAFOLDER + "/key-private.txt", sk, SerType::BINARY) == false) {
        std::cerr << "Could not read secret key" << std::endl;
        return 1;
    }
    std::cout << "The secret key has been deserialized." << std::endl;

    // Decrypt the result of additions
    Plaintext plaintextAddResult;
    cc->Decrypt(sk, ciphertextAddResult, &plaintextAddResult);

    // Decrypt the result of multiplications
    Plaintext plaintextMultResult;
    cc->Decrypt(sk, ciphertextMultResult, &plaintextMultResult);

    // Decrypt the result of rotations
    Plaintext plaintextRot1;
    cc->Decrypt(sk, ciphertextRot1, &plaintextRot1);
    Plaintext plaintextRot2;
    cc->Decrypt(sk, ciphertextRot2, &plaintextRot2);
    Plaintext plaintextRot3;
    cc->Decrypt(sk, ciphertextRot3, &plaintextRot3);
    Plaintext plaintextRot4;
    cc->Decrypt(sk, ciphertextRot4, &plaintextRot4);

    // Shows only the same number of elements as in the original plaintext vector
    // By default it will show all coefficients in the BFV-encoded polynomial
    plaintextRot1->SetLength(vectorOfInts1.size());
    plaintextRot2->SetLength(vectorOfInts1.size());
    plaintextRot3->SetLength(vectorOfInts1.size());
    plaintextRot4->SetLength(vectorOfInts1.size());

    // Output results
    std::cout << "\nResults of homomorphic computations" << std::endl;
    std::cout << "#1 + #2 + #3: " << plaintextAddResult << std::endl;
    std::cout << "#1 * #2 * #3: " << plaintextMultResult << std::endl;
    std::cout << "Left rotation of #1 by 1: " << plaintextRot1 << std::endl;
    std::cout << "Left rotation of #1 by 2: " << plaintextRot2 << std::endl;
    std::cout << "Right rotation of #1 by 1: " << plaintextRot3 << std::endl;
    std::cout << "Right rotation of #1 by 2: " << plaintextRot4 << std::endl;
    return 0;
}



================================================
FILE: simple-integers.cpp
================================================
//==================================================================================
// BSD 2-Clause License
//
// Copyright (c) 2014-2022, NJIT, Duality Technologies Inc. and other contributors
//
// All rights reserved.
//
// Author TPOC: contact@openfhe.org
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//==================================================================================

/*
  Simple example for BFVrns (integer arithmetic)
 */

#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Sample Program: Step 1: Set CryptoContext
    CCParams<CryptoContextBFVRNS> parameters;
    parameters.SetPlaintextModulus(65537);
    parameters.SetMultiplicativeDepth(2);

    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);
    // Enable features that you wish to use
    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);

    // Sample Program: Step 2: Key Generation

    // Initialize Public Key Containers
    KeyPair<DCRTPoly> keyPair;

    // Generate a public/private key pair
    keyPair = cryptoContext->KeyGen();

    // Generate the relinearization key
    cryptoContext->EvalMultKeyGen(keyPair.secretKey);

    // Generate the rotation evaluation keys
    cryptoContext->EvalRotateKeyGen(keyPair.secretKey, {1, 2, -1, -2});

    // Sample Program: Step 3: Encryption

    // First plaintext vector is encoded
    std::vector<int64_t> vectorOfInts1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext1               = cryptoContext->MakePackedPlaintext(vectorOfInts1);
    // Second plaintext vector is encoded
    std::vector<int64_t> vectorOfInts2 = {3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext2               = cryptoContext->MakePackedPlaintext(vectorOfInts2);
    // Third plaintext vector is encoded
    std::vector<int64_t> vectorOfInts3 = {1, 2, 5, 2, 5, 6, 7, 8, 9, 10, 11, 12};
    Plaintext plaintext3               = cryptoContext->MakePackedPlaintext(vectorOfInts3);

    // The encoded vectors are encrypted
    auto ciphertext1 = cryptoContext->Encrypt(keyPair.publicKey, plaintext1);
    auto ciphertext2 = cryptoContext->Encrypt(keyPair.publicKey, plaintext2);
    auto ciphertext3 = cryptoContext->Encrypt(keyPair.publicKey, plaintext3);

    // Sample Program: Step 4: Evaluation

    // Homomorphic additions
    auto ciphertextAdd12     = cryptoContext->EvalAdd(ciphertext1, ciphertext2);
    auto ciphertextAddResult = cryptoContext->EvalAdd(ciphertextAdd12, ciphertext3);

    // Homomorphic multiplications
    auto ciphertextMul12      = cryptoContext->EvalMult(ciphertext1, ciphertext2);
    auto ciphertextMultResult = cryptoContext->EvalMult(ciphertextMul12, ciphertext3);

    // Homomorphic rotations
    auto ciphertextRot1 = cryptoContext->EvalRotate(ciphertext1, 1);
    auto ciphertextRot2 = cryptoContext->EvalRotate(ciphertext1, 2);
    auto ciphertextRot3 = cryptoContext->EvalRotate(ciphertext1, -1);
    auto ciphertextRot4 = cryptoContext->EvalRotate(ciphertext1, -2);

    // Sample Program: Step 5: Decryption

    // Decrypt the result of additions
    Plaintext plaintextAddResult;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextAddResult, &plaintextAddResult);

    // Decrypt the result of multiplications
    Plaintext plaintextMultResult;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextMultResult, &plaintextMultResult);

    // Decrypt the result of rotations
    Plaintext plaintextRot1;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextRot1, &plaintextRot1);
    Plaintext plaintextRot2;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextRot2, &plaintextRot2);
    Plaintext plaintextRot3;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextRot3, &plaintextRot3);
    Plaintext plaintextRot4;
    cryptoContext->Decrypt(keyPair.secretKey, ciphertextRot4, &plaintextRot4);

    plaintextRot1->SetLength(vectorOfInts1.size());
    plaintextRot2->SetLength(vectorOfInts1.size());
    plaintextRot3->SetLength(vectorOfInts1.size());
    plaintextRot4->SetLength(vectorOfInts1.size());

    std::cout << "Plaintext #1: " << plaintext1 << std::endl;
    std::cout << "Plaintext #2: " << plaintext2 << std::endl;
    std::cout << "Plaintext #3: " << plaintext3 << std::endl;

    // Output results
    std::cout << "\nResults of homomorphic computations" << std::endl;
    std::cout << "#1 + #2 + #3: " << plaintextAddResult << std::endl;
    std::cout << "#1 * #2 * #3: " << plaintextMultResult << std::endl;
    std::cout << "Left rotation of #1 by 1: " << plaintextRot1 << std::endl;
    std::cout << "Left rotation of #1 by 2: " << plaintextRot2 << std::endl;
    std::cout << "Right rotation of #1 by 1: " << plaintextRot3 << std::endl;
    std::cout << "Right rotation of #1 by 2: " << plaintextRot4 << std::endl;

    return 0;
}



================================================
FILE: simple-real-numbers-serial.cpp
================================================
/*
  Real number serialization in a simple context. The goal of this is to show a simple setup for real number
  serialization before progressing into the next logical step - serialization and communication across
  2 separate entities
 */

#include <iomanip>
#include <tuple>
#include <unistd.h>

#include "openfhe.h"

// header files needed for serialization
#include "ciphertext-ser.h"
#include "cryptocontext-ser.h"
#include "key/key-ser.h"
#include "scheme/ckksrns/ckksrns-ser.h"

using namespace lbcrypto;

/////////////////////////////////////////////////////////////////
// NOTE:
// If running locally, you may want to replace the "hardcoded" DATAFOLDER with
// the DATAFOLDER location below which gets the current working directory
/////////////////////////////////////////////////////////////////
// char buff[1024];
// std::string DATAFOLDER = std::string(getcwd(buff, 1024));

// Save-Load locations for keys
const std::string DATAFOLDER = "demoData";
std::string ccLocation       = "/cryptocontext.txt";
std::string pubKeyLocation   = "/key_pub.txt";   // Pub key
std::string multKeyLocation  = "/key_mult.txt";  // relinearization key
std::string rotKeyLocation   = "/key_rot.txt";   // automorphism / rotation key

// Save-load locations for RAW ciphertexts
std::string cipherOneLocation = "/ciphertext1.txt";
std::string cipherTwoLocation = "/ciphertext2.txt";

// Save-load locations for evaluated ciphertexts
std::string cipherMultLocation   = "/ciphertextMult.txt";
std::string cipherAddLocation    = "/ciphertextAdd.txt";
std::string cipherRotLocation    = "/ciphertextRot.txt";
std::string cipherRotNegLocation = "/ciphertextRotNegLocation.txt";
std::string clientVectorLocation = "/ciphertextVectorFromClient.txt";

/**
 * Demarcate - Visual separator between the sections of code
 * @param msg - string message that you want displayed between blocks of
 * characters
 */
void demarcate(const std::string& msg) {
    std::cout << std::setw(50) << std::setfill('*') << '\n' << std::endl;
    std::cout << msg << std::endl;
    std::cout << std::setw(50) << std::setfill('*') << '\n' << std::endl;
}

/**
 * serverSetupAndWrite
 *  - simulates a server at startup where we generate a cryptocontext and keys.
 *  - then, we generate some data (akin to loading raw data on an enclave)
 * before encrypting the data
 * @param multDepth - multiplication depth
 * @param scaleModSize - number of bits to use in the scale factor (not the
 * scale factor itself)
 * @param batchSize - batch size to use
 * @return Tuple<cryptoContext, keyPair>
 */
std::tuple<CryptoContext<DCRTPoly>, KeyPair<DCRTPoly>, int> serverSetupAndWrite(int multDepth, int scaleModSize,
                                                                                int batchSize) {
    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> serverCC = GenCryptoContext(parameters);

    serverCC->Enable(PKE);
    serverCC->Enable(KEYSWITCH);
    serverCC->Enable(LEVELEDSHE);

    std::cout << "Cryptocontext generated" << std::endl;

    KeyPair<DCRTPoly> serverKP = serverCC->KeyGen();
    std::cout << "Keypair generated" << std::endl;

    serverCC->EvalMultKeyGen(serverKP.secretKey);
    std::cout << "Eval Mult Keys/ Relinearization keys have been generated" << std::endl;

    serverCC->EvalRotateKeyGen(serverKP.secretKey, {1, 2, -1, -2});
    std::cout << "Rotation keys generated" << std::endl;

    std::vector<std::complex<double>> vec1 = {1.0, 2.0, 3.0, 4.0};
    std::vector<std::complex<double>> vec2 = {12.5, 13.5, 14.5, 15.5};
    std::vector<std::complex<double>> vec3 = {10.5, 11.5, 12.5, 13.5};
    std::cout << "\nDisplaying first data vector: ";

    for (auto& v : vec1) {
        std::cout << v << ',';
    }

    std::cout << '\n' << std::endl;

    Plaintext serverP1 = serverCC->MakeCKKSPackedPlaintext(vec1);
    Plaintext serverP2 = serverCC->MakeCKKSPackedPlaintext(vec2);
    Plaintext serverP3 = serverCC->MakeCKKSPackedPlaintext(vec3);

    std::cout << "Plaintext version of first vector: " << serverP1 << std::endl;

    std::cout << "Plaintexts have been generated from complex-double vectors" << std::endl;

    auto serverC1 = serverCC->Encrypt(serverKP.publicKey, serverP1);
    auto serverC2 = serverCC->Encrypt(serverKP.publicKey, serverP2);
    auto serverC3 = serverCC->Encrypt(serverKP.publicKey, serverP3);

    std::cout << "Ciphertexts have been generated from Plaintexts" << std::endl;

    /*
   * Part 2:
   * We serialize the following:
   *  Cryptocontext
   *  Public key
   *  relinearization (eval mult keys)
   *  rotation keys
   *  Some of the ciphertext
   *
   *  We serialize all of them to files
   */

    demarcate("Part 2: Data Serialization (server)");

    if (!Serial::SerializeToFile(DATAFOLDER + ccLocation, serverCC, SerType::BINARY)) {
        std::cerr << "Error writing serialization of the crypto context to "
                     "cryptocontext.txt"
                  << std::endl;
        std::exit(1);
    }

    std::cout << "Cryptocontext serialized" << std::endl;

    if (!Serial::SerializeToFile(DATAFOLDER + pubKeyLocation, serverKP.publicKey, SerType::BINARY)) {
        std::cerr << "Exception writing public key to pubkey.txt" << std::endl;
        std::exit(1);
    }
    std::cout << "Public key serialized" << std::endl;

    std::ofstream multKeyFile(DATAFOLDER + multKeyLocation, std::ios::out | std::ios::binary);
    if (multKeyFile.is_open()) {
        if (!serverCC->SerializeEvalMultKey(multKeyFile, SerType::BINARY)) {
            std::cerr << "Error writing eval mult keys" << std::endl;
            std::exit(1);
        }
        std::cout << "EvalMult/ relinearization keys have been serialized" << std::endl;
        multKeyFile.close();
    }
    else {
        std::cerr << "Error serializing EvalMult keys" << std::endl;
        std::exit(1);
    }

    std::ofstream rotationKeyFile(DATAFOLDER + rotKeyLocation, std::ios::out | std::ios::binary);
    if (rotationKeyFile.is_open()) {
        if (!serverCC->SerializeEvalAutomorphismKey(rotationKeyFile, SerType::BINARY)) {
            std::cerr << "Error writing rotation keys" << std::endl;
            std::exit(1);
        }
        std::cout << "Rotation keys have been serialized" << std::endl;
    }
    else {
        std::cerr << "Error serializing Rotation keys" << std::endl;
        std::exit(1);
    }

    if (!Serial::SerializeToFile(DATAFOLDER + cipherOneLocation, serverC1, SerType::BINARY)) {
        std::cerr << " Error writing ciphertext 1" << std::endl;
    }

    if (!Serial::SerializeToFile(DATAFOLDER + cipherTwoLocation, serverC2, SerType::BINARY)) {
        std::cerr << " Error writing ciphertext 2" << std::endl;
    }

    return std::make_tuple(serverCC, serverKP, vec1.size());
}

/**
 * clientProcess
 *  - deserialize data from a file which simulates receiving data from a server
 * after making a request
 *  - we then process the data by doing operations (multiplication, addition,
 * rotation, etc)
 *  - !! We also create an object and encrypt it in this function before sending
 * it off to the server to be decrypted
 */
void clientProcess() {
    CryptoContext<DCRTPoly> clientCC;
    clientCC->ClearEvalMultKeys();
    clientCC->ClearEvalAutomorphismKeys();
    lbcrypto::CryptoContextFactory<lbcrypto::DCRTPoly>::ReleaseAllContexts();
    if (!Serial::DeserializeFromFile(DATAFOLDER + ccLocation, clientCC, SerType::BINARY)) {
        std::cerr << "I cannot read serialized data from: " << DATAFOLDER << "/cryptocontext.txt" << std::endl;
        std::exit(1);
    }
    std::cout << "Client CC deserialized";

    KeyPair<DCRTPoly> clientKP;  // We do NOT have a secret key. The client
    // should not have access to this
    PublicKey<DCRTPoly> clientPublicKey;
    if (!Serial::DeserializeFromFile(DATAFOLDER + pubKeyLocation, clientPublicKey, SerType::BINARY)) {
        std::cerr << "I cannot read serialized data from: " << DATAFOLDER << "/cryptocontext.txt" << std::endl;
        std::exit(1);
    }
    std::cout << "Client KP deserialized" << '\n' << std::endl;

    std::ifstream multKeyIStream(DATAFOLDER + multKeyLocation, std::ios::in | std::ios::binary);
    if (!multKeyIStream.is_open()) {
        std::cerr << "Cannot read serialization from " << DATAFOLDER + multKeyLocation << std::endl;
        std::exit(1);
    }
    if (!clientCC->DeserializeEvalMultKey(multKeyIStream, SerType::BINARY)) {
        std::cerr << "Could not deserialize eval mult key file" << std::endl;
        std::exit(1);
    }

    std::cout << "Deserialized eval mult keys" << '\n' << std::endl;
    std::ifstream rotKeyIStream(DATAFOLDER + rotKeyLocation, std::ios::in | std::ios::binary);
    if (!rotKeyIStream.is_open()) {
        std::cerr << "Cannot read serialization from " << DATAFOLDER + multKeyLocation << std::endl;
        std::exit(1);
    }
    if (!clientCC->DeserializeEvalAutomorphismKey(rotKeyIStream, SerType::BINARY)) {
        std::cerr << "Could not deserialize eval rot key file" << std::endl;
        std::exit(1);
    }

    Ciphertext<DCRTPoly> clientC1;
    Ciphertext<DCRTPoly> clientC2;
    if (!Serial::DeserializeFromFile(DATAFOLDER + cipherOneLocation, clientC1, SerType::BINARY)) {
        std::cerr << "Cannot read serialization from " << DATAFOLDER + cipherOneLocation << std::endl;
        std::exit(1);
    }
    std::cout << "Deserialized ciphertext1" << '\n' << std::endl;

    if (!Serial::DeserializeFromFile(DATAFOLDER + cipherTwoLocation, clientC2, SerType::BINARY)) {
        std::cerr << "Cannot read serialization from " << DATAFOLDER + cipherTwoLocation << std::endl;
        std::exit(1);
    }

    std::cout << "Deserialized ciphertext1" << '\n' << std::endl;
    auto clientCiphertextMult   = clientCC->EvalMult(clientC1, clientC2);
    auto clientCiphertextAdd    = clientCC->EvalAdd(clientC1, clientC2);
    auto clientCiphertextRot    = clientCC->EvalRotate(clientC1, 1);
    auto clientCiphertextRotNeg = clientCC->EvalRotate(clientC1, -1);

    // Now, we want to simulate a client who is encrypting data for the server to
    // decrypt. E.g weights of a machine learning algorithm
    demarcate("Part 3.5: Client Serialization of data that has been operated on");

    std::vector<std::complex<double>> clientVector1 = {1.0, 2.0, 3.0, 4.0};
    auto clientPlaintext1                           = clientCC->MakeCKKSPackedPlaintext(clientVector1);
    auto clientInitiatedEncryption                  = clientCC->Encrypt(clientPublicKey, clientPlaintext1);
    Serial::SerializeToFile(DATAFOLDER + cipherMultLocation, clientCiphertextMult, SerType::BINARY);
    Serial::SerializeToFile(DATAFOLDER + cipherAddLocation, clientCiphertextAdd, SerType::BINARY);
    Serial::SerializeToFile(DATAFOLDER + cipherRotLocation, clientCiphertextRot, SerType::BINARY);
    Serial::SerializeToFile(DATAFOLDER + cipherRotNegLocation, clientCiphertextRotNeg, SerType::BINARY);
    Serial::SerializeToFile(DATAFOLDER + clientVectorLocation, clientInitiatedEncryption, SerType::BINARY);

    std::cout << "Serialized all ciphertexts from client" << '\n' << std::endl;
}

/**
 * serverVerification
 *  - deserialize data from the client.
 *  - Verify that the results are as we expect
 * @param cc cryptocontext that was previously generated
 * @param kp keypair that was previously generated
 * @param vectorSize vector size of the vectors supplied
 * @return
 *  5-tuple of the plaintexts of various operations
 */

std::tuple<Plaintext, Plaintext, Plaintext, Plaintext, Plaintext> serverVerification(CryptoContext<DCRTPoly>& cc,
                                                                                     KeyPair<DCRTPoly>& kp,
                                                                                     int vectorSize) {
    Ciphertext<DCRTPoly> serverCiphertextFromClient_Mult;
    Ciphertext<DCRTPoly> serverCiphertextFromClient_Add;
    Ciphertext<DCRTPoly> serverCiphertextFromClient_Rot;
    Ciphertext<DCRTPoly> serverCiphertextFromClient_RogNeg;
    Ciphertext<DCRTPoly> serverCiphertextFromClient_Vec;

    Serial::DeserializeFromFile(DATAFOLDER + cipherMultLocation, serverCiphertextFromClient_Mult, SerType::BINARY);
    Serial::DeserializeFromFile(DATAFOLDER + cipherAddLocation, serverCiphertextFromClient_Add, SerType::BINARY);
    Serial::DeserializeFromFile(DATAFOLDER + cipherRotLocation, serverCiphertextFromClient_Rot, SerType::BINARY);
    Serial::DeserializeFromFile(DATAFOLDER + cipherRotNegLocation, serverCiphertextFromClient_RogNeg, SerType::BINARY);
    Serial::DeserializeFromFile(DATAFOLDER + clientVectorLocation, serverCiphertextFromClient_Vec, SerType::BINARY);
    std::cout << "Deserialized all data from client on server" << '\n' << std::endl;

    demarcate("Part 5: Correctness verification");

    Plaintext serverPlaintextFromClient_Mult;
    Plaintext serverPlaintextFromClient_Add;
    Plaintext serverPlaintextFromClient_Rot;
    Plaintext serverPlaintextFromClient_RotNeg;
    Plaintext serverPlaintextFromClient_Vec;

    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_Mult, &serverPlaintextFromClient_Mult);
    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_Add, &serverPlaintextFromClient_Add);
    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_Rot, &serverPlaintextFromClient_Rot);
    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_RogNeg, &serverPlaintextFromClient_RotNeg);
    cc->Decrypt(kp.secretKey, serverCiphertextFromClient_Vec, &serverPlaintextFromClient_Vec);

    serverPlaintextFromClient_Mult->SetLength(vectorSize);
    serverPlaintextFromClient_Add->SetLength(vectorSize);
    serverPlaintextFromClient_Vec->SetLength(vectorSize);
    serverPlaintextFromClient_Rot->SetLength(vectorSize + 1);
    serverPlaintextFromClient_RotNeg->SetLength(vectorSize + 1);

    return std::make_tuple(serverPlaintextFromClient_Mult, serverPlaintextFromClient_Add, serverPlaintextFromClient_Vec,
                           serverPlaintextFromClient_Rot, serverPlaintextFromClient_RotNeg);
}
int main() {
    std::cout << "This program requres the subdirectory `" << DATAFOLDER << "' to exist, otherwise you will get "
              << "an error writing serializations." << std::endl;

    // Set main params
    const int multDepth    = 5;
    const int scaleModSize = 40;
    const usint batchSize  = 32;

    const int cryptoContextIdx = 0;
    const int keyPairIdx       = 1;
    const int vectorSizeIdx    = 2;

    const int cipherMultResIdx   = 0;
    const int cipherAddResIdx    = 1;
    const int cipherVecResIdx    = 2;
    const int cipherRotResIdx    = 3;
    const int cipherRotNegResIdx = 4;

    demarcate(
        "Part 1: Cryptocontext generation, key generation, data encryption "
        "(server)");

    auto tupleCryptoContext_KeyPair = serverSetupAndWrite(multDepth, scaleModSize, batchSize);
    auto cc                         = std::get<cryptoContextIdx>(tupleCryptoContext_KeyPair);
    auto kp                         = std::get<keyPairIdx>(tupleCryptoContext_KeyPair);
    int vectorSize                  = std::get<vectorSizeIdx>(tupleCryptoContext_KeyPair);

    demarcate("Part 3: Client deserialize all data");
    clientProcess();

    demarcate("Part 4: Server deserialization of data from client. ");

    auto tupleRes  = serverVerification(cc, kp, vectorSize);
    auto multRes   = std::get<cipherMultResIdx>(tupleRes);
    auto addRes    = std::get<cipherAddResIdx>(tupleRes);
    auto vecRes    = std::get<cipherVecResIdx>(tupleRes);
    auto rotRes    = std::get<cipherRotResIdx>(tupleRes);
    auto rotNegRes = std::get<cipherRotNegResIdx>(tupleRes);

    // vec1: {1,2,3,4}
    // vec2: {12.5, 13.5, 14.5, 15.5}

    std::cout << multRes << std::endl;  // EXPECT: 12.5, 27.0, 43.5, 62
    std::cout << addRes << std::endl;   // EXPECT: 13.5, 15.5, 17.5, 19.5
    std::cout << vecRes << std::endl;   // EXPECT:  {1,2,3,4}

    std::cout << "Displaying 5 elements of a 4-element vector to illustrate rotation" << '\n';
    std::cout << rotRes << std::endl;     // EXPECT: {2, 3, 4, noise, noise}
    std::cout << rotNegRes << std::endl;  // EXPECT: {noise, 1, 2, 3, 4}
}



================================================
FILE: simple-real-numbers.cpp
================================================
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



================================================
FILE: tckks-interactive-mp-bootstrapping-Chebyshev.cpp
================================================
/*

Demo for Multi-Party Interactive Collective Bootstrapping in Threshold-CKKS (TCKKS).
3 parties want to evaluate a Chebyshev series on their secret input
This protocol is secure against (n-1) collusion among the participating parties, where n is
the number of participating parties.

*/

#define PROFILE

#include "openfhe.h"

using namespace std;
using namespace lbcrypto;

static void checkApproximateEquality(const std::vector<std::complex<double>>& a,
                                     const std::vector<std::complex<double>>& b, int vectorSize, double epsilon) {
    std::vector<std::complex<double>> allTrue(vectorSize);
    std::vector<std::complex<double>> tmp(vectorSize);
    for (int i = 0; i < vectorSize; i++) {
        allTrue[i] = 1;
        tmp[i]     = abs(a[i] - b[i]) <= epsilon;
    }
    if (tmp != allTrue) {
        cerr << __func__ << " - " << __FILE__ << ":" << __LINE__ << " IntMPBoot - Ctxt Chebyshev Failed: " << endl;
        cerr << __func__ << " - " << __FILE__ << ":" << __LINE__ << " - is diff <= eps?: " << tmp << endl;
    }
    else {
        std::cout << "SUCESSFUL Bootstrapping!\n";
    }
}

void TCKKSCollectiveBoot(enum ScalingTechnique scaleTech);

int main(int argc, char* argv[]) {
    std::cout << "Interactive (3P) Bootstrapping Ciphertext [Chebyshev] (TCKKS) started ...\n";

    // Same test with different rescaling techniques in CKKS
    TCKKSCollectiveBoot(ScalingTechnique::FIXEDMANUAL);
    TCKKSCollectiveBoot(ScalingTechnique::FIXEDAUTO);
    TCKKSCollectiveBoot(ScalingTechnique::FLEXIBLEAUTO);
    TCKKSCollectiveBoot(ScalingTechnique::FLEXIBLEAUTOEXT);

    std::cout << "Interactive (3P) Bootstrapping Ciphertext [Chebyshev] (TCKKS) terminated gracefully!\n";

    return 0;
}

// Demonstrate interactive multi-party bootstrapping for 3 parties
// We follow Protocol 5 in https://eprint.iacr.org/2020/304, "Multiparty
// Homomorphic Encryption from Ring-Learning-With-Errors"

void TCKKSCollectiveBoot(enum ScalingTechnique scaleTech) {
    if (scaleTech != ScalingTechnique::FIXEDMANUAL && scaleTech != ScalingTechnique::FIXEDAUTO &&
        scaleTech != ScalingTechnique::FLEXIBLEAUTO && scaleTech != ScalingTechnique::FLEXIBLEAUTOEXT) {
        std::string errMsg = "ERROR: Scaling technique is not supported!";
        OPENFHE_THROW(errMsg);
    }

    CCParams<CryptoContextCKKSRNS> parameters;
    // A. Specify main parameters
    /*  A1) Secret key distribution
	* The secret key distribution for CKKS should either be SPARSE_TERNARY or UNIFORM_TERNARY.
	* The SPARSE_TERNARY distribution was used in the original CKKS paper,
	* but in this example, we use UNIFORM_TERNARY because this is included in the homomorphic
	* encryption standard.
	*/
    SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
    parameters.SetSecretKeyDist(secretKeyDist);

    /*  A2) Desired security level based on FHE standards.
	* In this example, we use the "NotSet" option, so the example can run more quickly with
	* a smaller ring dimension. Note that this should be used only in
	* non-production environments, or by experts who understand the security
	* implications of their choices. In production-like environments, we recommend using
	* HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
	* or 256-bit security, respectively. If you choose one of these as your security level,
	* you do not need to set the ring dimension.
	*/
    parameters.SetSecurityLevel(HEStd_128_classic);

    /*  A3) Scaling parameters.
	* By default, we set the modulus sizes and rescaling technique to the following values
	* to obtain a good precision and performance tradeoff. We recommend keeping the parameters
	* below unless you are an FHE expert.
	*/
    usint dcrtBits = 50;
    usint firstMod = 60;

    parameters.SetScalingModSize(dcrtBits);
    parameters.SetScalingTechnique(scaleTech);
    parameters.SetFirstModSize(firstMod);

    /*  A4) Multiplicative depth.
    * The multiplicative depth detemins the computational capability of the instantiated scheme. It should be set
    * according the following formula:
    * multDepth >= desired_depth + interactive_bootstrapping_depth
    * where,
    *   The desired_depth is the depth of the computation, as chosen by the user.
    *   The interactive_bootstrapping_depth is either 3 or 4, depending on the ciphertext compression mode: COMPACT vs SLACK (see below)
    * Example 1, if you want to perform a computation of depth 24, you can set multDepth to 10, use 6 levels
    * for computation and 4 for interactive bootstrapping. You will need to bootstrap 3 times.
    */
    parameters.SetMultiplicativeDepth(10);
    parameters.SetKeySwitchTechnique(KeySwitchTechnique::HYBRID);

    uint32_t batchSize = 16;
    parameters.SetBatchSize(batchSize);

    /*  Protocol-specific parameters (SLACK or COMPACT)
    * SLACK (default) uses larger masks, which makes it more secure theoretically. However, it is also slightly less efficient.
    * COMPACT uses smaller masks, which makes it more efficient. However, it is relatively less secure theoretically.
    * Both options can be used for practical security.
    * The following table summarizes the differences between SLACK and COMPACT:
    * Parameter	        SLACK	                                        COMPACT
    * Mask size	        Larger	                                        Smaller
    * Security	        More secure	                                    Less secure
    * Efficiency	    Less efficient	                                More efficient
    * Recommended use	For applications where security is paramount	For applications where efficiency is paramount
    */
    auto compressionLevel = COMPRESSION_LEVEL::COMPACT;
    parameters.SetInteractiveBootCompressionLevel(compressionLevel);

    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    cryptoContext->Enable(ADVANCEDSHE);
    cryptoContext->Enable(MULTIPARTY);

    usint ringDim = cryptoContext->GetRingDimension();
    // This is the maximum number of slots that can be used for full packing.
    usint maxNumSlots = ringDim / 2;
    std::cout << "TCKKS scheme is using ring dimension " << ringDim << std::endl;
    std::cout << "TCKKS scheme number of slots         " << batchSize << std::endl;
    std::cout << "TCKKS scheme max number of slots     " << maxNumSlots << std::endl;
    std::cout << "TCKKS example with Scaling Technique " << scaleTech << std::endl;

    const usint numParties = 3;

    std::cout << "\n===========================IntMPBoot protocol parameters===========================\n";
    std::cout << "num of parties: " << numParties << "\n";
    std::cout << "===============================================================\n";

    double eps = 0.0001;

    // Initialize Public Key Containers
    KeyPair<DCRTPoly> kp1;  // Party 1
    KeyPair<DCRTPoly> kp2;  // Party 2
    KeyPair<DCRTPoly> kp3;  // Lead party - who finalizes interactive bootstrapping

    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    // Round 1 (party A)
    kp1 = cryptoContext->KeyGen();

    // Generate evalmult key part for A
    auto evalMultKey = cryptoContext->KeySwitchGen(kp1.secretKey, kp1.secretKey);

    // Generate evalsum key part for A
    cryptoContext->EvalSumKeyGen(kp1.secretKey);
    auto evalSumKeys = std::make_shared<std::map<usint, EvalKey<DCRTPoly>>>(
        cryptoContext->GetEvalSumKeyMap(kp1.secretKey->GetKeyTag()));

    // Round 2 (party B)
    kp2                  = cryptoContext->MultipartyKeyGen(kp1.publicKey);
    auto evalMultKey2    = cryptoContext->MultiKeySwitchGen(kp2.secretKey, kp2.secretKey, evalMultKey);
    auto evalMultAB      = cryptoContext->MultiAddEvalKeys(evalMultKey, evalMultKey2, kp2.publicKey->GetKeyTag());
    auto evalMultBAB     = cryptoContext->MultiMultEvalKey(kp2.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());
    auto evalSumKeysB    = cryptoContext->MultiEvalSumKeyGen(kp2.secretKey, evalSumKeys, kp2.publicKey->GetKeyTag());
    auto evalSumKeysJoin = cryptoContext->MultiAddEvalSumKeys(evalSumKeys, evalSumKeysB, kp2.publicKey->GetKeyTag());
    cryptoContext->InsertEvalSumKey(evalSumKeysJoin);
    auto evalMultAAB   = cryptoContext->MultiMultEvalKey(kp1.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());
    auto evalMultFinal = cryptoContext->MultiAddEvalMultKeys(evalMultAAB, evalMultBAB, evalMultAB->GetKeyTag());
    cryptoContext->InsertEvalMultKey({evalMultFinal});

    /////////////////////
    // Round 3 (party C) - Lead Party (who encrypts and finalizes the bootstrapping protocol)
    kp3                 = cryptoContext->MultipartyKeyGen(kp2.publicKey);
    auto evalMultKey3   = cryptoContext->MultiKeySwitchGen(kp3.secretKey, kp3.secretKey, evalMultKey);
    auto evalMultABC    = cryptoContext->MultiAddEvalKeys(evalMultAB, evalMultKey3, kp3.publicKey->GetKeyTag());
    auto evalMultBABC   = cryptoContext->MultiMultEvalKey(kp2.secretKey, evalMultABC, kp3.publicKey->GetKeyTag());
    auto evalMultAABC   = cryptoContext->MultiMultEvalKey(kp1.secretKey, evalMultABC, kp3.publicKey->GetKeyTag());
    auto evalMultCABC   = cryptoContext->MultiMultEvalKey(kp3.secretKey, evalMultABC, kp3.publicKey->GetKeyTag());
    auto evalMultABABC  = cryptoContext->MultiAddEvalMultKeys(evalMultBABC, evalMultAABC, evalMultBABC->GetKeyTag());
    auto evalMultFinal2 = cryptoContext->MultiAddEvalMultKeys(evalMultABABC, evalMultCABC, evalMultCABC->GetKeyTag());
    cryptoContext->InsertEvalMultKey({evalMultFinal2});

    auto evalSumKeysC = cryptoContext->MultiEvalSumKeyGen(kp3.secretKey, evalSumKeys, kp3.publicKey->GetKeyTag());
    auto evalSumKeysJoin2 =
        cryptoContext->MultiAddEvalSumKeys(evalSumKeysJoin, evalSumKeysC, kp3.publicKey->GetKeyTag());
    cryptoContext->InsertEvalSumKey(evalSumKeysJoin2);

    if (!kp1.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }
    if (!kp2.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }
    if (!kp3.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }

    // END of Key Generation

    std::vector<std::complex<double>> input({-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0});

    // Chebyshev coefficients
    std::vector<double> coefficients({1.0, 0.558971, 0.0, -0.0943712, 0.0, 0.0215023, 0.0, -0.00505348, 0.0, 0.00119324,
                                      0.0, -0.000281928, 0.0, 0.0000664347, 0.0, -0.0000148709});
    // Input range
    double a = -4;
    double b = 4;

    Plaintext pt1       = cryptoContext->MakeCKKSPackedPlaintext(input);
    usint encodedLength = input.size();

    auto ct1 = cryptoContext->Encrypt(kp3.publicKey, pt1);

    ct1 = cryptoContext->EvalChebyshevSeries(ct1, coefficients, a, b);

    // INTERACTIVE BOOTSTRAPPING STARTS

    ct1 = cryptoContext->IntMPBootAdjustScale(ct1);

    // Leading party (party B) generates a Common Random Poly (crp) at max coefficient modulus (QNumPrime).
    // a is sampled at random uniformly from R_{Q}
    auto crp = cryptoContext->IntMPBootRandomElementGen(kp3.publicKey);
    // Each party generates its own shares: maskedDecryptionShare and reEncryptionShare
    // (h_{0,i}, h_{1,i}) = (masked decryption share, re-encryption share)
    // we use a vector inseat of std::pair for Python API compatibility
    vector<Ciphertext<DCRTPoly>> sharesPair0;  // for Party A
    vector<Ciphertext<DCRTPoly>> sharesPair1;  // for Party B
    vector<Ciphertext<DCRTPoly>> sharesPair2;  // for Party C

    // extract c1 - element-wise
    auto c1 = ct1->Clone();
    c1->GetElements().erase(c1->GetElements().begin());
    // masked decryption on the client: c1 = a*s1
    sharesPair0 = cryptoContext->IntMPBootDecrypt(kp1.secretKey, c1, crp);
    sharesPair1 = cryptoContext->IntMPBootDecrypt(kp2.secretKey, c1, crp);
    sharesPair2 = cryptoContext->IntMPBootDecrypt(kp3.secretKey, c1, crp);

    vector<vector<Ciphertext<DCRTPoly>>> sharesPairVec;
    sharesPairVec.push_back(sharesPair0);
    sharesPairVec.push_back(sharesPair1);
    sharesPairVec.push_back(sharesPair2);

    // Party B finalizes the protocol by aggregating the shares and reEncrypting the results
    auto aggregatedSharesPair = cryptoContext->IntMPBootAdd(sharesPairVec);
    auto ciphertextOutput     = cryptoContext->IntMPBootEncrypt(kp3.publicKey, aggregatedSharesPair, crp, ct1);

    // INTERACTIVE BOOTSTRAPPING ENDS

    // distributed decryption

    auto ciphertextPartial1 = cryptoContext->MultipartyDecryptMain({ciphertextOutput}, kp1.secretKey);
    auto ciphertextPartial2 = cryptoContext->MultipartyDecryptMain({ciphertextOutput}, kp2.secretKey);
    auto ciphertextPartial3 = cryptoContext->MultipartyDecryptLead({ciphertextOutput}, kp3.secretKey);
    vector<Ciphertext<DCRTPoly>> partialCiphertextVec;
    partialCiphertextVec.push_back(ciphertextPartial1[0]);
    partialCiphertextVec.push_back(ciphertextPartial2[0]);
    partialCiphertextVec.push_back(ciphertextPartial3[0]);

    Plaintext plaintextMultiparty;
    cryptoContext->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultiparty);
    plaintextMultiparty->SetLength(encodedLength);

    // Ground truth result
    std::vector<std::complex<double>> result(
        {0.0179885, 0.0474289, 0.119205, 0.268936, 0.5, 0.731064, 0.880795, 0.952571, 0.982011});
    Plaintext plaintextResult = cryptoContext->MakeCKKSPackedPlaintext(result);

    std::cout << "Ground Truth: \n\t" << plaintextResult->GetCKKSPackedValue() << std::endl;
    std::cout << "Computed Res: \n\t" << plaintextMultiparty->GetCKKSPackedValue() << std::endl;

    checkApproximateEquality(plaintextResult->GetCKKSPackedValue(), plaintextMultiparty->GetCKKSPackedValue(),
                             encodedLength, eps);

    std::cout << "\n============================ INTERACTIVE DECRYPTION ENDED ============================\n";

    std::cout << "\nTCKKSCollectiveBoot FHE example with rescaling technique: " << scaleTech << " Completed!"
              << std::endl;
}



================================================
FILE: tckks-interactive-mp-bootstrapping.cpp
================================================
//==================================================================================
// BSD 2-Clause License
//
// Copyright (c) 2014-2022, NJIT, Duality Technologies Inc. and other contributors
//
// All rights reserved.
//
// Author TPOC: contact@openfhe.org
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//==================================================================================

/*
 Demo for Multi-Party Interactive Collective Bootstrapping with Threshold-CKKS (TCKKS) for
 a single ciphertext.
 It is a trivial example showing how to encrypt, bootstrap, and decrypt for 3 parties. No
 computation is done here.

 This protocol is secure against (n-1) collusion among the participating parties, where n is
 the number of participating parties.
 */

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;

/*
 * A utility class defining a party that is involved in the collective bootstrapping protocol
 */
struct Party {
public:
    usint id;  // unique party identifier starting from 0

    std::vector<Ciphertext<DCRTPoly>> sharesPair;  // (h_{0,i}, h_{1,i}) = (masked decryption
                                                   // share, re-encryption share)
                                                   // we use a vector inseat of std::pair for Python API compatibility

    KeyPair<DCRTPoly> kpShard;  // key-pair shard (pk, sk_i)
};

void TCKKSCollectiveBoot(enum ScalingTechnique rescaleTech);

int main(int argc, char* argv[]) {
    std::cout << "Interactive Multi-Party Bootstrapping Ciphertext (TCKKS) started ...\n";

    // Same test with different rescaling techniques in CKKS
    TCKKSCollectiveBoot(ScalingTechnique::FIXEDMANUAL);
    TCKKSCollectiveBoot(ScalingTechnique::FIXEDAUTO);
    TCKKSCollectiveBoot(ScalingTechnique::FLEXIBLEAUTO);
    TCKKSCollectiveBoot(ScalingTechnique::FLEXIBLEAUTOEXT);

    std::cout << "Interactive Multi-Party Bootstrapping Ciphertext (TCKKS) terminated gracefully!\n";

    return 0;
}

// Demonstrate interactive multi-party bootstrapping for 3 parties
// We follow Protocol 5 in https://eprint.iacr.org/2020/304, "Multiparty
// Homomorphic Encryption from Ring-Learning-With-Errors"

void TCKKSCollectiveBoot(enum ScalingTechnique scaleTech) {
    if (scaleTech != ScalingTechnique::FIXEDMANUAL && scaleTech != ScalingTechnique::FIXEDAUTO &&
        scaleTech != ScalingTechnique::FLEXIBLEAUTO && scaleTech != ScalingTechnique::FLEXIBLEAUTOEXT) {
        std::string errMsg = "ERROR: Scaling technique is not supported!";
        OPENFHE_THROW(errMsg);
    }

    CCParams<CryptoContextCKKSRNS> parameters;
    // A. Specify main parameters
    /*  A1) Secret key distribution
	* The secret key distribution for CKKS should either be SPARSE_TERNARY or UNIFORM_TERNARY.
	* The SPARSE_TERNARY distribution was used in the original CKKS paper,
	* but in this example, we use UNIFORM_TERNARY because this is included in the homomorphic
	* encryption standard.
	*/
    SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
    parameters.SetSecretKeyDist(secretKeyDist);

    /*  A2) Desired security level based on FHE standards.
	* In this example, we use the "NotSet" option, so the example can run more quickly with
	* a smaller ring dimension. Note that this should be used only in
	* non-production environments, or by experts who understand the security
	* implications of their choices. In production-like environments, we recommend using
	* HEStd_128_classic, HEStd_192_classic, or HEStd_256_classic for 128-bit, 192-bit,
	* or 256-bit security, respectively. If you choose one of these as your security level,
	* you do not need to set the ring dimension.
	*/
    parameters.SetSecurityLevel(HEStd_128_classic);

    /*  A3) Scaling parameters.
	* By default, we set the modulus sizes and rescaling technique to the following values
	* to obtain a good precision and performance tradeoff. We recommend keeping the parameters
	* below unless you are an FHE expert.
	*/
    usint dcrtBits = 50;
    usint firstMod = 60;

    parameters.SetScalingModSize(dcrtBits);
    parameters.SetScalingTechnique(scaleTech);
    parameters.SetFirstModSize(firstMod);

    /*  A4) Multiplicative depth.
    * The multiplicative depth detemins the computational capability of the instantiated scheme. It should be set
    * according the following formula:
    * multDepth >= desired_depth + interactive_bootstrapping_depth
    * where,
    *   The desired_depth is the depth of the computation, as chosen by the user.
    *   The interactive_bootstrapping_depth is either 3 or 4, depending on the ciphertext compression mode: COMPACT vs SLACK (see below)
    * Example 1, if you want to perform a computation of depth 24, you can set multDepth to 10, use 6 levels
    * for computation and 4 for interactive bootstrapping. You will need to bootstrap 3 times.
    */
    uint32_t multiplicativeDepth = 7;
    parameters.SetMultiplicativeDepth(multiplicativeDepth);
    parameters.SetKeySwitchTechnique(KeySwitchTechnique::HYBRID);

    uint32_t batchSize = 4;
    parameters.SetBatchSize(batchSize);

    /*  Protocol-specific parameters (SLACK or COMPACT)
    * SLACK (default) uses larger masks, which makes it more secure theoretically. However, it is also slightly less efficient.
    * COMPACT uses smaller masks, which makes it more efficient. However, it is relatively less secure theoretically.
    * Both options can be used for practical security.
    * The following table summarizes the differences between SLACK and COMPACT:
    * Parameter	        SLACK	                                        COMPACT
    * Mask size	        Larger	                                        Smaller
    * Security	        More secure	                                    Less secure
    * Efficiency	    Less efficient	                                More efficient
    * Recommended use	For applications where security is paramount	For applications where efficiency is paramount
    */
    auto compressionLevel = COMPRESSION_LEVEL::SLACK;
    parameters.SetInteractiveBootCompressionLevel(compressionLevel);

    CryptoContext<DCRTPoly> cryptoContext = GenCryptoContext(parameters);

    cryptoContext->Enable(PKE);
    cryptoContext->Enable(KEYSWITCH);
    cryptoContext->Enable(LEVELEDSHE);
    cryptoContext->Enable(ADVANCEDSHE);
    cryptoContext->Enable(MULTIPARTY);

    usint ringDim = cryptoContext->GetRingDimension();
    // This is the maximum number of slots that can be used for full packing.
    usint maxNumSlots = ringDim / 2;
    std::cout << "TCKKS scheme is using ring dimension " << ringDim << std::endl;
    std::cout << "TCKKS scheme number of slots         " << batchSize << std::endl;
    std::cout << "TCKKS scheme max number of slots     " << maxNumSlots << std::endl;
    std::cout << "TCKKS example with Scaling Technique " << scaleTech << std::endl;

    const usint numParties = 3;  // n: number of parties involved in the interactive protocol

    std::cout << "\n===========================IntMPBoot protocol parameters===========================\n";
    std::cout << "number of parties: " << numParties << "\n";
    std::cout << "===============================================================\n";

    std::vector<Party> parties(numParties);

    // Joint public key
    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    std::cout << "Running key generation (used for source data)..." << std::endl;

    // Initialization - Assuming numParties (n) of parties
    // P0 is the leading party
    for (usint i = 0; i < numParties; i++) {
        parties[i].id = i;
        std::cout << "Party " << parties[i].id << " started.\n";
        if (0 == i)
            parties[i].kpShard = cryptoContext->KeyGen();
        else
            parties[i].kpShard = cryptoContext->MultipartyKeyGen(parties[0].kpShard.publicKey);
        std::cout << "Party " << i << " key generation completed.\n";
    }
    std::cout << "Joint public key for (s_0 + s_1 + ... + s_n) is generated..." << std::endl;

    // Assert everything is good
    for (usint i = 0; i < numParties; i++) {
        if (!parties[i].kpShard.good()) {
            std::cout << "Key generation failed for party " << i << "!" << std::endl;
            exit(1);
        }
    }

    // Generate the collective public key
    std::vector<PrivateKey<DCRTPoly>> secretKeys;
    for (usint i = 0; i < numParties; i++) {
        secretKeys.push_back(parties[i].kpShard.secretKey);
    }
    kpMultiparty = cryptoContext->MultipartyKeyGen(secretKeys);  // This is the same core key generation operation.

    // Prepare input vector
    std::vector<std::complex<double>> msg1({-0.9, -0.8, 0.2, 0.4});
    Plaintext ptxt1 = cryptoContext->MakeCKKSPackedPlaintext(msg1);

    // Encryption
    Ciphertext<DCRTPoly> inCtxt = cryptoContext->Encrypt(kpMultiparty.publicKey, ptxt1);
    DCRTPoly ptxtpoly           = ptxt1->GetElement<DCRTPoly>();

    std::cout << "Compressing ctxt to the smallest possible number of towers!\n";
    inCtxt = cryptoContext->IntMPBootAdjustScale(inCtxt);

    // INTERACTIVE BOOTSTRAPPING STARTS

    std::cout << "\n============================ INTERACTIVE BOOTSTRAPPING STARTS ============================\n";

    // Leading party (P0) generates a Common Random Poly (a) at max coefficient modulus (QNumPrime).
    // a is sampled at random uniformly from R_{Q}
    Ciphertext<DCRTPoly> a = cryptoContext->IntMPBootRandomElementGen(parties[0].kpShard.publicKey);
    std::cout << "Common Random Poly (a) has been generated with coefficient modulus Q\n";

    // Each party generates its own shares: maskedDecryptionShare and reEncryptionShare
    std::vector<std::vector<Ciphertext<DCRTPoly>>> sharesPairVec;

    // Make a copy of input ciphertext and remove the first element (c0), we only
    // c1 for IntMPBootDecrypt
    auto c1 = inCtxt->Clone();
    c1->GetElements().erase(c1->GetElements().begin());
    for (usint i = 0; i < numParties; i++) {
        std::cout << "Party " << i << " started its part in the Collective Bootstrapping Protocol\n";
        parties[i].sharesPair = cryptoContext->IntMPBootDecrypt(parties[i].kpShard.secretKey, c1, a);
        sharesPairVec.push_back(parties[i].sharesPair);
    }

    // P0 finalizes the protocol by aggregating the shares and reEncrypting the results
    auto aggregatedSharesPair = cryptoContext->IntMPBootAdd(sharesPairVec);
    // Make sure you provide the non-striped ciphertext (inCtxt) in IntMPBootEncrypt
    auto outCtxt = cryptoContext->IntMPBootEncrypt(parties[0].kpShard.publicKey, aggregatedSharesPair, a, inCtxt);

    // INTERACTIVE BOOTSTRAPPING ENDS
    std::cout << "\n============================ INTERACTIVE BOOTSTRAPPING ENDED ============================\n";

    // Distributed decryption

    std::cout << "\n============================ INTERACTIVE DECRYPTION STARTED ============================ \n";

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVec;

    std::cout << "Party 0 started its part in the collective decryption protocol\n";
    partialCiphertextVec.push_back(cryptoContext->MultipartyDecryptLead({outCtxt}, parties[0].kpShard.secretKey)[0]);

    for (usint i = 1; i < numParties; i++) {
        std::cout << "Party " << i << " started its part in the collective decryption protocol\n";
        partialCiphertextVec.push_back(
            cryptoContext->MultipartyDecryptMain({outCtxt}, parties[i].kpShard.secretKey)[0]);
    }

    // Checking the results
    std::cout << "MultipartyDecryptFusion ...\n";
    Plaintext plaintextMultiparty;
    cryptoContext->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultiparty);
    plaintextMultiparty->SetLength(msg1.size());

    std::cout << "Original plaintext \n\t" << ptxt1->GetCKKSPackedValue() << std::endl;
    std::cout << "Result after bootstrapping \n\t" << plaintextMultiparty->GetCKKSPackedValue() << std::endl;

    std::cout << "\n============================ INTERACTIVE DECRYPTION ENDED ============================\n";
}



================================================
FILE: threshold-fhe-5p.cpp
================================================
/*
  Examples of threshold FHE for BGVrns, BFVrns and CKKS
 */

#include "openfhe.h"

using namespace lbcrypto;

void RunBFVrns();
void EvalNoiseBFV(PrivateKey<DCRTPoly> privateKey, ConstCiphertext<DCRTPoly> ciphertext, Plaintext ptxt, usint ptm,
                  double& noise, double& logQ, EncryptionTechnique encMethod);

int main(int argc, char* argv[]) {
    std::cout << "\n=================RUNNING FOR BFVrns=====================" << std::endl;

    RunBFVrns();

    return 0;
}

void RunBFVrns() {
    int plaintextModulus                  = 65537;
    double sigma                          = 3.2;
    lbcrypto::SecurityLevel securityLevel = lbcrypto::SecurityLevel::HEStd_128_classic;

    usint batchSize = 16;
    usint multDepth = 4;
    usint digitSize = 30;
    usint dcrtBits  = 60;

    lbcrypto::CCParams<lbcrypto::CryptoContextBFVRNS> parameters;

    parameters.SetPlaintextModulus(plaintextModulus);
    parameters.SetSecurityLevel(securityLevel);
    parameters.SetStandardDeviation(sigma);
    parameters.SetSecretKeyDist(UNIFORM_TERNARY);
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetBatchSize(batchSize);
    parameters.SetDigitSize(digitSize);
    parameters.SetScalingModSize(dcrtBits);
    parameters.SetMultiplicationTechnique(HPSPOVERQLEVELED);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(MULTIPARTY);

    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    // Output the generated parameters
    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;

    // Initialize Public Key Containers for two parties A and B
    KeyPair<DCRTPoly> kp1;
    KeyPair<DCRTPoly> kp2;

    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    std::cout << "Running key generation (used for source data)..." << std::endl;

    // Round 1 (party A)

    std::cout << "Round 1 (party A) started." << std::endl;

    kp1      = cc->KeyGen();
    kp2      = cc->MultipartyKeyGen(kp1.publicKey);
    auto kp3 = cc->MultipartyKeyGen(kp2.publicKey);
    auto kp4 = cc->MultipartyKeyGen(kp3.publicKey);
    auto kp5 = cc->MultipartyKeyGen(kp4.publicKey);

    // Generate evalmult key part for A
    auto evalMultKey = cc->KeySwitchGen(kp1.secretKey, kp1.secretKey);

    auto evalMultKey2 = cc->MultiKeySwitchGen(kp2.secretKey, kp2.secretKey, evalMultKey);

    auto evalMultKey3 = cc->MultiKeySwitchGen(kp3.secretKey, kp3.secretKey, evalMultKey);

    auto evalMultKey4 = cc->MultiKeySwitchGen(kp4.secretKey, kp4.secretKey, evalMultKey);

    auto evalMultKey5 = cc->MultiKeySwitchGen(kp5.secretKey, kp5.secretKey, evalMultKey);

    auto evalMultAB = cc->MultiAddEvalKeys(evalMultKey, evalMultKey2, kp2.publicKey->GetKeyTag());

    auto evalMultABC = cc->MultiAddEvalKeys(evalMultAB, evalMultKey3, kp3.publicKey->GetKeyTag());

    auto evalMultABCD = cc->MultiAddEvalKeys(evalMultABC, evalMultKey4, kp4.publicKey->GetKeyTag());

    auto evalMultABCDE = cc->MultiAddEvalKeys(evalMultABCD, evalMultKey5, kp5.publicKey->GetKeyTag());

    auto evalMultEABCDE = cc->MultiMultEvalKey(kp5.secretKey, evalMultABCDE, kp5.publicKey->GetKeyTag());

    auto evalMultDABCDE = cc->MultiMultEvalKey(kp4.secretKey, evalMultABCDE, kp5.publicKey->GetKeyTag());

    auto evalMultCABCDE = cc->MultiMultEvalKey(kp3.secretKey, evalMultABCDE, kp5.publicKey->GetKeyTag());

    auto evalMultBABCDE = cc->MultiMultEvalKey(kp2.secretKey, evalMultABCDE, kp5.publicKey->GetKeyTag());

    auto evalMultAABCDE = cc->MultiMultEvalKey(kp1.secretKey, evalMultABCDE, kp5.publicKey->GetKeyTag());

    auto evalMultDEABCDE = cc->MultiAddEvalMultKeys(evalMultEABCDE, evalMultDABCDE, evalMultEABCDE->GetKeyTag());

    auto evalMultCDEABCDE = cc->MultiAddEvalMultKeys(evalMultCABCDE, evalMultDEABCDE, evalMultCABCDE->GetKeyTag());

    auto evalMultBCDEABCDE = cc->MultiAddEvalMultKeys(evalMultBABCDE, evalMultCDEABCDE, evalMultBABCDE->GetKeyTag());

    auto evalMultFinal = cc->MultiAddEvalMultKeys(evalMultAABCDE, evalMultBCDEABCDE, kp5.publicKey->GetKeyTag());
    cc->InsertEvalMultKey({evalMultFinal});

    //---------------------------------------------------
    std::cout << "Running evalsum key generation (used for source data)..." << std::endl;
    // Generate evalsum key part for A
    cc->EvalSumKeyGen(kp1.secretKey);
    auto evalSumKeys =
        std::make_shared<std::map<usint, EvalKey<DCRTPoly>>>(cc->GetEvalSumKeyMap(kp1.secretKey->GetKeyTag()));

    auto evalSumKeysB = cc->MultiEvalSumKeyGen(kp2.secretKey, evalSumKeys, kp2.publicKey->GetKeyTag());

    auto evalSumKeysC = cc->MultiEvalSumKeyGen(kp3.secretKey, evalSumKeys, kp3.publicKey->GetKeyTag());

    auto evalSumKeysD = cc->MultiEvalSumKeyGen(kp4.secretKey, evalSumKeys, kp4.publicKey->GetKeyTag());

    auto evalSumKeysE = cc->MultiEvalSumKeyGen(kp5.secretKey, evalSumKeys, kp5.publicKey->GetKeyTag());

    auto evalSumKeysAB = cc->MultiAddEvalSumKeys(evalSumKeys, evalSumKeysB, kp2.publicKey->GetKeyTag());

    auto evalSumKeysABC = cc->MultiAddEvalSumKeys(evalSumKeysC, evalSumKeysAB, kp3.publicKey->GetKeyTag());

    auto evalSumKeysABCD = cc->MultiAddEvalSumKeys(evalSumKeysABC, evalSumKeysD, kp4.publicKey->GetKeyTag());

    auto evalSumKeysJoin = cc->MultiAddEvalSumKeys(evalSumKeysE, evalSumKeysABCD, kp5.publicKey->GetKeyTag());

    cc->InsertEvalSumKey(evalSumKeysJoin);

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////
    std::vector<int64_t> vectorOfInts1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0};
    std::vector<int64_t> vectorOfInts2 = {1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0};
    std::vector<int64_t> vectorOfInts3 = {2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0};

    Plaintext plaintext1 = cc->MakePackedPlaintext(vectorOfInts1);
    Plaintext plaintext2 = cc->MakePackedPlaintext(vectorOfInts2);
    Plaintext plaintext3 = cc->MakePackedPlaintext(vectorOfInts3);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertext1;
    Ciphertext<DCRTPoly> ciphertext2;
    Ciphertext<DCRTPoly> ciphertext3;

    ciphertext1 = cc->Encrypt(kp5.publicKey, plaintext1);
    ciphertext2 = cc->Encrypt(kp5.publicKey, plaintext2);
    ciphertext3 = cc->Encrypt(kp5.publicKey, plaintext3);

    ////////////////////////////////////////////////////////////
    // Homomorphic Operations
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertextAdd12;
    Ciphertext<DCRTPoly> ciphertextAdd123;

    ciphertextAdd12  = cc->EvalAdd(ciphertext1, ciphertext2);
    ciphertextAdd123 = cc->EvalAdd(ciphertextAdd12, ciphertext3);

    auto ciphertextMult1 = cc->EvalMult(ciphertext1, ciphertext1);
    auto ciphertextMult2 = cc->EvalMult(ciphertextMult1, ciphertext1);
    auto ciphertextMult3 = cc->EvalMult(ciphertextMult2, ciphertext1);
    auto ciphertextMult  = cc->EvalMult(ciphertextMult3, ciphertext1);

    auto ciphertextEvalSum = cc->EvalSum(ciphertext3, batchSize);

    ////////////////////////////////////////////////////////////
    // Decryption after Accumulation Operation on Encrypted Data with Multiparty
    ////////////////////////////////////////////////////////////

    Plaintext plaintextAddNew1;
    Plaintext plaintextAddNew2;
    Plaintext plaintextAddNew3;

    DCRTPoly partialPlaintext1;
    DCRTPoly partialPlaintext2;
    DCRTPoly partialPlaintext3;

    Plaintext plaintextMultipartyNew;

    const std::shared_ptr<CryptoParametersBase<DCRTPoly>> cryptoParams = kp1.secretKey->GetCryptoParameters();
    const std::shared_ptr<typename DCRTPoly::Params> elementParams     = cryptoParams->GetElementParams();

    // Distributed decryption
    // partial decryption by party A
    auto ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextAdd123}, kp1.secretKey);

    // partial decryption by party B
    auto ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp2.secretKey);

    // partial decryption by party C
    auto ciphertextPartial3 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp3.secretKey);

    // partial decryption by party D
    auto ciphertextPartial4 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp4.secretKey);

    // partial decryption by party E
    auto ciphertextPartial5 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp5.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVec;
    partialCiphertextVec.push_back(ciphertextPartial1[0]);
    partialCiphertextVec.push_back(ciphertextPartial2[0]);
    partialCiphertextVec.push_back(ciphertextPartial3[0]);
    partialCiphertextVec.push_back(ciphertextPartial4[0]);
    partialCiphertextVec.push_back(ciphertextPartial5[0]);

    // Two partial decryptions are combined
    cc->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultipartyNew);

    std::cout << "\n Original Plaintext: \n" << std::endl;
    std::cout << plaintext1 << std::endl;
    std::cout << plaintext2 << std::endl;
    std::cout << plaintext3 << std::endl;

    plaintextMultipartyNew->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext: \n" << std::endl;
    std::cout << plaintextMultipartyNew << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyMult;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextMult}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextMult}, kp2.secretKey);

    // partial decryption by party C
    ciphertextPartial3 = cc->MultipartyDecryptMain({ciphertextMult}, kp3.secretKey);

    // partial decryption by party D
    ciphertextPartial4 = cc->MultipartyDecryptMain({ciphertextMult}, kp4.secretKey);

    // partial decryption by party E
    ciphertextPartial5 = cc->MultipartyDecryptMain({ciphertextMult}, kp5.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecMult;
    partialCiphertextVecMult.push_back(ciphertextPartial1[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial2[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial3[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial4[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial5[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecMult, &plaintextMultipartyMult);

    plaintextMultipartyMult->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext after Multiplication of plaintexts 1 "
                 "and 3: \n"
              << std::endl;
    std::cout << plaintextMultipartyMult << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyEvalSum;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextEvalSum}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp2.secretKey);

    ciphertextPartial3 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp3.secretKey);

    ciphertextPartial4 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp4.secretKey);

    ciphertextPartial5 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp5.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecEvalSum;
    partialCiphertextVecEvalSum.push_back(ciphertextPartial1[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial2[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial3[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial4[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial5[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecEvalSum, &plaintextMultipartyEvalSum);

    plaintextMultipartyEvalSum->SetLength(plaintext1->GetLength());

    std::cout << "\n Fused result after summation of ciphertext 3: \n" << std::endl;
    std::cout << plaintextMultipartyEvalSum << std::endl;
}



================================================
FILE: threshold-fhe.cpp
================================================
/*
  Examples of threshold FHE for BGVrns, BFVrns and CKKS
 */

#include "openfhe.h"

using namespace lbcrypto;

void RunBGVrnsAdditive();
void RunBFVrns();
void RunCKKS();

int main(int argc, char* argv[]) {
    std::cout << "\n=================RUNNING FOR BGVrns - Additive "
                 "====================="
              << std::endl;

    RunBGVrnsAdditive();

    std::cout << "\n=================RUNNING FOR BFVrns=====================" << std::endl;

    RunBFVrns();

    std::cout << "\n=================RUNNING FOR CKKS=====================" << std::endl;

    RunCKKS();

    return 0;
}

void RunBGVrnsAdditive() {
    CCParams<CryptoContextBGVRNS> parameters;
    parameters.SetPlaintextModulus(65537);

    // NOISE_FLOODING_MULTIPARTY adds extra noise to the ciphertext before decrypting
    // and is most secure mode of threshold FHE for BFV and BGV.
    parameters.SetMultipartyMode(NOISE_FLOODING_MULTIPARTY);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // Enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(MULTIPARTY);

    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    // Print out the parameters
    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;

    // Initialize Public Key Containers for 3 parties
    KeyPair<DCRTPoly> kp1;
    KeyPair<DCRTPoly> kp2;
    KeyPair<DCRTPoly> kp3;

    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    std::cout << "Running key generation (used for source data)..." << std::endl;

    // generate the public key for first share
    kp1 = cc->KeyGen();
    // generate the public key for two shares
    kp2 = cc->MultipartyKeyGen(kp1.publicKey);
    // generate the public key for all three secret shares
    kp3 = cc->MultipartyKeyGen(kp2.publicKey);

    if (!kp1.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }
    if (!kp2.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }
    if (!kp3.good()) {
        std::cout << "Key generation failed!" << std::endl;
        exit(1);
    }

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////
    std::vector<int64_t> vectorOfInts1 = {1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0};
    std::vector<int64_t> vectorOfInts2 = {1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0};
    std::vector<int64_t> vectorOfInts3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0};

    Plaintext plaintext1 = cc->MakePackedPlaintext(vectorOfInts1);
    Plaintext plaintext2 = cc->MakePackedPlaintext(vectorOfInts2);
    Plaintext plaintext3 = cc->MakePackedPlaintext(vectorOfInts3);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////
    Ciphertext<DCRTPoly> ciphertext1;
    Ciphertext<DCRTPoly> ciphertext2;
    Ciphertext<DCRTPoly> ciphertext3;

    ciphertext1 = cc->Encrypt(kp3.publicKey, plaintext1);
    ciphertext2 = cc->Encrypt(kp3.publicKey, plaintext2);
    ciphertext3 = cc->Encrypt(kp3.publicKey, plaintext3);

    ////////////////////////////////////////////////////////////
    // EvalAdd Operation on Re-Encrypted Data
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertextAdd12;
    Ciphertext<DCRTPoly> ciphertextAdd123;

    ciphertextAdd12  = cc->EvalAdd(ciphertext1, ciphertext2);
    ciphertextAdd123 = cc->EvalAdd(ciphertextAdd12, ciphertext3);

    ////////////////////////////////////////////////////////////
    // Decryption after Accumulation Operation on Encrypted Data with Multiparty
    ////////////////////////////////////////////////////////////

    Plaintext plaintextAddNew1;
    Plaintext plaintextAddNew2;
    Plaintext plaintextAddNew3;

    DCRTPoly partialPlaintext1;
    DCRTPoly partialPlaintext2;
    DCRTPoly partialPlaintext3;

    Plaintext plaintextMultipartyNew;

    const std::shared_ptr<CryptoParametersBase<DCRTPoly>> cryptoParams = kp1.secretKey->GetCryptoParameters();
    const std::shared_ptr<typename DCRTPoly::Params> elementParams     = cryptoParams->GetElementParams();

    // partial decryption by first party
    auto ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextAdd123}, kp1.secretKey);

    // partial decryption by second party
    auto ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp2.secretKey);

    // partial decryption by third party
    auto ciphertextPartial3 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp3.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVec;
    partialCiphertextVec.push_back(ciphertextPartial1[0]);
    partialCiphertextVec.push_back(ciphertextPartial2[0]);
    partialCiphertextVec.push_back(ciphertextPartial3[0]);

    // partial decryptions are combined together
    cc->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultipartyNew);

    std::cout << "\n Original Plaintext: \n" << std::endl;
    std::cout << plaintext1 << std::endl;
    std::cout << plaintext2 << std::endl;
    std::cout << plaintext3 << std::endl;

    plaintextMultipartyNew->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext adding 3 ciphertexts: \n" << std::endl;
    std::cout << plaintextMultipartyNew << std::endl;

    std::cout << "\n";
}

void RunBFVrns() {
    usint batchSize = 16;

    CCParams<CryptoContextBFVRNS> parameters;
    parameters.SetPlaintextModulus(65537);
    parameters.SetBatchSize(batchSize);
    parameters.SetMultiplicativeDepth(2);
    // NOISE_FLOODING_MULTIPARTY adds extra noise to the ciphertext before decrypting
    // and is most secure mode of threshold FHE for BFV and BGV.
    parameters.SetMultipartyMode(NOISE_FLOODING_MULTIPARTY);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(MULTIPARTY);

    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    // Output the generated parameters
    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;

    // Initialize Public Key Containers for two parties A and B
    KeyPair<DCRTPoly> kp1;
    KeyPair<DCRTPoly> kp2;

    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    std::cout << "Running key generation (used for source data)..." << std::endl;

    // Round 1 (party A)

    std::cout << "Round 1 (party A) started." << std::endl;

    kp1 = cc->KeyGen();

    // Generate evalmult key part for A
    auto evalMultKey = cc->KeySwitchGen(kp1.secretKey, kp1.secretKey);

    // Generate evalsum key part for A
    cc->EvalSumKeyGen(kp1.secretKey);
    auto evalSumKeys =
        std::make_shared<std::map<usint, EvalKey<DCRTPoly>>>(cc->GetEvalSumKeyMap(kp1.secretKey->GetKeyTag()));

    std::cout << "Round 1 of key generation completed." << std::endl;

    // Round 2 (party B)

    std::cout << "Round 2 (party B) started." << std::endl;

    std::cout << "Joint public key for (s_a + s_b) is generated..." << std::endl;
    kp2 = cc->MultipartyKeyGen(kp1.publicKey);

    auto evalMultKey2 = cc->MultiKeySwitchGen(kp2.secretKey, kp2.secretKey, evalMultKey);

    std::cout << "Joint evaluation multiplication key for (s_a + s_b) is generated..." << std::endl;
    auto evalMultAB = cc->MultiAddEvalKeys(evalMultKey, evalMultKey2, kp2.publicKey->GetKeyTag());

    std::cout << "Joint evaluation multiplication key (s_a + s_b) is transformed "
                 "into s_b*(s_a + s_b)..."
              << std::endl;
    auto evalMultBAB = cc->MultiMultEvalKey(kp2.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());

    auto evalSumKeysB = cc->MultiEvalSumKeyGen(kp2.secretKey, evalSumKeys, kp2.publicKey->GetKeyTag());

    std::cout << "Joint evaluation summation key for (s_a + s_b) is generated..." << std::endl;
    auto evalSumKeysJoin = cc->MultiAddEvalSumKeys(evalSumKeys, evalSumKeysB, kp2.publicKey->GetKeyTag());

    cc->InsertEvalSumKey(evalSumKeysJoin);

    std::cout << "Round 2 of key generation completed." << std::endl;

    std::cout << "Round 3 (party A) started." << std::endl;

    std::cout << "Joint key (s_a + s_b) is transformed into s_a*(s_a + s_b)..." << std::endl;
    auto evalMultAAB = cc->MultiMultEvalKey(kp1.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());

    std::cout << "Computing the final evaluation multiplication key for (s_a + "
                 "s_b)*(s_a + s_b)..."
              << std::endl;
    auto evalMultFinal = cc->MultiAddEvalMultKeys(evalMultAAB, evalMultBAB, evalMultAB->GetKeyTag());

    cc->InsertEvalMultKey({evalMultFinal});

    std::cout << "Round 3 of key generation completed." << std::endl;

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////
    std::vector<int64_t> vectorOfInts1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0};
    std::vector<int64_t> vectorOfInts2 = {1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0};
    std::vector<int64_t> vectorOfInts3 = {2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0};

    Plaintext plaintext1 = cc->MakePackedPlaintext(vectorOfInts1);
    Plaintext plaintext2 = cc->MakePackedPlaintext(vectorOfInts2);
    Plaintext plaintext3 = cc->MakePackedPlaintext(vectorOfInts3);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertext1;
    Ciphertext<DCRTPoly> ciphertext2;
    Ciphertext<DCRTPoly> ciphertext3;

    ciphertext1 = cc->Encrypt(kp2.publicKey, plaintext1);
    ciphertext2 = cc->Encrypt(kp2.publicKey, plaintext2);
    ciphertext3 = cc->Encrypt(kp2.publicKey, plaintext3);

    ////////////////////////////////////////////////////////////
    // Homomorphic Operations
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertextAdd12;
    Ciphertext<DCRTPoly> ciphertextAdd123;

    ciphertextAdd12  = cc->EvalAdd(ciphertext1, ciphertext2);
    ciphertextAdd123 = cc->EvalAdd(ciphertextAdd12, ciphertext3);

    auto ciphertextMult    = cc->EvalMult(ciphertext1, ciphertext3);
    auto ciphertextEvalSum = cc->EvalSum(ciphertext3, batchSize);

    ////////////////////////////////////////////////////////////
    // Decryption after Accumulation Operation on Encrypted Data with Multiparty
    ////////////////////////////////////////////////////////////

    Plaintext plaintextAddNew1;
    Plaintext plaintextAddNew2;
    Plaintext plaintextAddNew3;

    DCRTPoly partialPlaintext1;
    DCRTPoly partialPlaintext2;
    DCRTPoly partialPlaintext3;

    Plaintext plaintextMultipartyNew;

    const std::shared_ptr<CryptoParametersBase<DCRTPoly>> cryptoParams = kp1.secretKey->GetCryptoParameters();
    const std::shared_ptr<typename DCRTPoly::Params> elementParams     = cryptoParams->GetElementParams();

    // Distributed decryption

    // partial decryption by party A
    auto ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextAdd123}, kp1.secretKey);

    // partial decryption by party B
    auto ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVec;
    partialCiphertextVec.push_back(ciphertextPartial1[0]);
    partialCiphertextVec.push_back(ciphertextPartial2[0]);

    // Two partial decryptions are combined
    cc->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultipartyNew);

    std::cout << "\n Original Plaintext: \n" << std::endl;
    std::cout << plaintext1 << std::endl;
    std::cout << plaintext2 << std::endl;
    std::cout << plaintext3 << std::endl;

    plaintextMultipartyNew->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext: \n" << std::endl;
    std::cout << plaintextMultipartyNew << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyMult;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextMult}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextMult}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecMult;
    partialCiphertextVecMult.push_back(ciphertextPartial1[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial2[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecMult, &plaintextMultipartyMult);

    plaintextMultipartyMult->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext after Multiplication of plaintexts 1 "
                 "and 3: \n"
              << std::endl;
    std::cout << plaintextMultipartyMult << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyEvalSum;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextEvalSum}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecEvalSum;
    partialCiphertextVecEvalSum.push_back(ciphertextPartial1[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial2[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecEvalSum, &plaintextMultipartyEvalSum);

    plaintextMultipartyEvalSum->SetLength(plaintext1->GetLength());

    std::cout << "\n Fused result after summation of ciphertext 3: \n" << std::endl;
    std::cout << plaintextMultipartyEvalSum << std::endl;
}

void RunCKKS() {
    usint batchSize = 16;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(3);
    parameters.SetScalingModSize(50);
    parameters.SetBatchSize(batchSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // enable features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(MULTIPARTY);

    ////////////////////////////////////////////////////////////
    // Set-up of parameters
    ////////////////////////////////////////////////////////////

    // Output the generated parameters
    std::cout << "p = " << cc->GetCryptoParameters()->GetPlaintextModulus() << std::endl;
    std::cout << "n = " << cc->GetCryptoParameters()->GetElementParams()->GetCyclotomicOrder() / 2 << std::endl;
    std::cout << "log2 q = " << log2(cc->GetCryptoParameters()->GetElementParams()->GetModulus().ConvertToDouble())
              << std::endl;

    // Initialize Public Key Containers
    KeyPair<DCRTPoly> kp1;
    KeyPair<DCRTPoly> kp2;

    KeyPair<DCRTPoly> kpMultiparty;

    ////////////////////////////////////////////////////////////
    // Perform Key Generation Operation
    ////////////////////////////////////////////////////////////

    std::cout << "Running key generation (used for source data)..." << std::endl;

    // Round 1 (party A)

    std::cout << "Round 1 (party A) started." << std::endl;

    kp1 = cc->KeyGen();

    // Generate evalmult key part for A
    auto evalMultKey = cc->KeySwitchGen(kp1.secretKey, kp1.secretKey);

    // Generate evalsum key part for A
    cc->EvalSumKeyGen(kp1.secretKey);
    auto evalSumKeys =
        std::make_shared<std::map<usint, EvalKey<DCRTPoly>>>(cc->GetEvalSumKeyMap(kp1.secretKey->GetKeyTag()));

    std::cout << "Round 1 of key generation completed." << std::endl;

    // Round 2 (party B)

    std::cout << "Round 2 (party B) started." << std::endl;

    std::cout << "Joint public key for (s_a + s_b) is generated..." << std::endl;
    kp2 = cc->MultipartyKeyGen(kp1.publicKey);

    auto evalMultKey2 = cc->MultiKeySwitchGen(kp2.secretKey, kp2.secretKey, evalMultKey);

    std::cout << "Joint evaluation multiplication key for (s_a + s_b) is generated..." << std::endl;
    auto evalMultAB = cc->MultiAddEvalKeys(evalMultKey, evalMultKey2, kp2.publicKey->GetKeyTag());

    std::cout << "Joint evaluation multiplication key (s_a + s_b) is transformed "
                 "into s_b*(s_a + s_b)..."
              << std::endl;
    auto evalMultBAB = cc->MultiMultEvalKey(kp2.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());

    auto evalSumKeysB = cc->MultiEvalSumKeyGen(kp2.secretKey, evalSumKeys, kp2.publicKey->GetKeyTag());

    std::cout << "Joint evaluation summation key for (s_a + s_b) is generated..." << std::endl;
    auto evalSumKeysJoin = cc->MultiAddEvalSumKeys(evalSumKeys, evalSumKeysB, kp2.publicKey->GetKeyTag());

    cc->InsertEvalSumKey(evalSumKeysJoin);

    std::cout << "Round 2 of key generation completed." << std::endl;

    std::cout << "Round 3 (party A) started." << std::endl;

    std::cout << "Joint key (s_a + s_b) is transformed into s_a*(s_a + s_b)..." << std::endl;
    auto evalMultAAB = cc->MultiMultEvalKey(kp1.secretKey, evalMultAB, kp2.publicKey->GetKeyTag());

    std::cout << "Computing the final evaluation multiplication key for (s_a + "
                 "s_b)*(s_a + s_b)..."
              << std::endl;
    auto evalMultFinal = cc->MultiAddEvalMultKeys(evalMultAAB, evalMultBAB, evalMultAB->GetKeyTag());

    cc->InsertEvalMultKey({evalMultFinal});

    std::cout << "Round 3 of key generation completed." << std::endl;

    ////////////////////////////////////////////////////////////
    // Encode source data
    ////////////////////////////////////////////////////////////
    std::vector<double> vectorOfInts1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0};
    std::vector<double> vectorOfInts2 = {1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0};
    std::vector<double> vectorOfInts3 = {2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0};

    Plaintext plaintext1 = cc->MakeCKKSPackedPlaintext(vectorOfInts1);
    Plaintext plaintext2 = cc->MakeCKKSPackedPlaintext(vectorOfInts2);
    Plaintext plaintext3 = cc->MakeCKKSPackedPlaintext(vectorOfInts3);

    ////////////////////////////////////////////////////////////
    // Encryption
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertext1;
    Ciphertext<DCRTPoly> ciphertext2;
    Ciphertext<DCRTPoly> ciphertext3;

    ciphertext1 = cc->Encrypt(kp2.publicKey, plaintext1);
    ciphertext2 = cc->Encrypt(kp2.publicKey, plaintext2);
    ciphertext3 = cc->Encrypt(kp2.publicKey, plaintext3);

    ////////////////////////////////////////////////////////////
    // EvalAdd Operation on Re-Encrypted Data
    ////////////////////////////////////////////////////////////

    Ciphertext<DCRTPoly> ciphertextAdd12;
    Ciphertext<DCRTPoly> ciphertextAdd123;

    ciphertextAdd12  = cc->EvalAdd(ciphertext1, ciphertext2);
    ciphertextAdd123 = cc->EvalAdd(ciphertextAdd12, ciphertext3);

    auto ciphertextMultTemp = cc->EvalMult(ciphertext1, ciphertext3);
    auto ciphertextMult     = cc->ModReduce(ciphertextMultTemp);
    auto ciphertextEvalSum  = cc->EvalSum(ciphertext3, batchSize);

    ////////////////////////////////////////////////////////////
    // Decryption after Accumulation Operation on Encrypted Data with Multiparty
    ////////////////////////////////////////////////////////////

    Plaintext plaintextAddNew1;
    Plaintext plaintextAddNew2;
    Plaintext plaintextAddNew3;

    DCRTPoly partialPlaintext1;
    DCRTPoly partialPlaintext2;
    DCRTPoly partialPlaintext3;

    Plaintext plaintextMultipartyNew;

    const std::shared_ptr<CryptoParametersBase<DCRTPoly>> cryptoParams = kp1.secretKey->GetCryptoParameters();
    const std::shared_ptr<typename DCRTPoly::Params> elementParams     = cryptoParams->GetElementParams();

    // distributed decryption

    auto ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextAdd123}, kp1.secretKey);

    auto ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextAdd123}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVec;
    partialCiphertextVec.push_back(ciphertextPartial1[0]);
    partialCiphertextVec.push_back(ciphertextPartial2[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVec, &plaintextMultipartyNew);

    std::cout << "\n Original Plaintext: \n" << std::endl;
    std::cout << plaintext1 << std::endl;
    std::cout << plaintext2 << std::endl;
    std::cout << plaintext3 << std::endl;

    plaintextMultipartyNew->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext: \n" << std::endl;
    std::cout << plaintextMultipartyNew << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyMult;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextMult}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextMult}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecMult;
    partialCiphertextVecMult.push_back(ciphertextPartial1[0]);
    partialCiphertextVecMult.push_back(ciphertextPartial2[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecMult, &plaintextMultipartyMult);

    plaintextMultipartyMult->SetLength(plaintext1->GetLength());

    std::cout << "\n Resulting Fused Plaintext after Multiplication of plaintexts 1 "
                 "and 3: \n"
              << std::endl;
    std::cout << plaintextMultipartyMult << std::endl;

    std::cout << "\n";

    Plaintext plaintextMultipartyEvalSum;

    ciphertextPartial1 = cc->MultipartyDecryptLead({ciphertextEvalSum}, kp1.secretKey);

    ciphertextPartial2 = cc->MultipartyDecryptMain({ciphertextEvalSum}, kp2.secretKey);

    std::vector<Ciphertext<DCRTPoly>> partialCiphertextVecEvalSum;
    partialCiphertextVecEvalSum.push_back(ciphertextPartial1[0]);
    partialCiphertextVecEvalSum.push_back(ciphertextPartial2[0]);

    cc->MultipartyDecryptFusion(partialCiphertextVecEvalSum, &plaintextMultipartyEvalSum);

    plaintextMultipartyEvalSum->SetLength(plaintext1->GetLength());

    std::cout << "\n Fused result after the Summation of ciphertext 3: "
                 "\n"
              << std::endl;
    std::cout << plaintextMultipartyEvalSum << std::endl;
}


