task_matmul = """
Task: Homomorphically multiply two fixed-size 2×2 matrices under CKKS using OpenFHE.
Inputs: Read two lines from stdin. Each line contains four space-separated doubles representing a 2×2 matrix flattened in row-major order. Do not print any extra prompts.
Output: Decrypt and print the resulting 2×2 matrix as four space-separated doubles on a single line (flattened in row-major order).
Constraints:
  - Use OpenFHE’s CKKS API for all encryption, evaluation, and decryption steps.
  - Matrix dimensions are always 2×2; input values ∈ [0,10].
Example:
  Input:
    1.0 2.0 3.0 4.0
    5.0 6.0 7.0 8.0
  Expected Output:
    19.0 22.0 43.0 50.0
""".strip()