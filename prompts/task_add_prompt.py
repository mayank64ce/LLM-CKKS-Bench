task_add = """
Task: Homomorphically add two fixed-length vectors under CKKS using OpenFHE.
Inputs: Read two lines from stdin, each containing 5 space-separated doubles. No extra prompts to the user.
Output: Decrypt and print the resulting 5-element vector to stdout, space-separated. No extra ouput messages.
Constraints:
  - Use OpenFHE’s CKKS API.
  - Vector length is always 5; values ∈ [0,10].
Example:
  Input:
    1.0 2.0 3.0 4.0 5.0
    5.0 4.0 3.0 2.0 1.0
  Expected Output:
    6.0 6.0 6.0 6.0 6.0
""".strip()