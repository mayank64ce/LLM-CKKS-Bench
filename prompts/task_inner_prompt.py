task_inner = """
Task: Homomorphically compute the inner product of two fixed-length vectors under CKKS using OpenFHE.
Inputs: Read two lines from stdin, each containing 5 space-separated doubles. No extra prompts to the user.
Output: Decrypt and print the resulting scalar to stdout. No extra ouput messages.
Constraints:
  - Use OpenFHE’s CKKS API.
  - Vector length is always 5; values ∈ [0,10].
Example:
  Input:
    1.0 2.0 3.0 4.0 5.0
    5.0 4.0 3.0 2.0 1.0
  Expected Output:
    35.0
""".strip()
