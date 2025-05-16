task_conv = """
Task: Homomorphically compute the 2D convolution between a 5×5 input matrix and a 3×3 kernel using OpenFHE’s CKKS API.

Inputs:
  - Read two lines from stdin.
    - The first line contains 25 space-separated doubles representing the 5×5 input matrix in row-major flattened format.
    - The second line contains 9 space-separated doubles representing the 3×3 kernel in row-major flattened format.
Output:
  - Decrypt and print the resulting 9-element vector to stdout, in row-major flattened format. No extra output messages.

Constraints:
  - Use OpenFHE’s CKKS API.
  - All values are positive real numbers in the range [1.0, 10.0].
  - Perform a valid convolution (no padding, stride=1).

Example:
  Input:
    7.0 7.0 5.0 10.0 5.0 9.0 8.0 2.0 9.0 10.0 9.0 5.0 4.0 9.0 4.0 7.0 7.0 4.0 4.0 9.0 2.0 9.0 5.0 8.0 10.0
    1.0 5.0 4.0 2.0 4.0 2.0 6.0 10.0 8.0
  Expected Output:
    252.0 256.0 281.0 247.0 212.0 275.0 242.0 267.0 297.0
""".strip()
