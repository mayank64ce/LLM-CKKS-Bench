import re

def parse_cpp_from_response(response):
    """
    Parse the C++ code from the response string.
    The function assumes that the C++ code is enclosed within triple backticks (```).
    
    Args:
        response (str): The response string containing C++ code.
        
    Returns:
        str: The extracted C++ code, or an empty string if no code is found.
    """
    # Use regex to find the C++ code block
    pattern = r'```cpp(.*?)```'
    match = re.search(pattern, response, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return ""

def save_file_to_disk(file_path, content):
    """
    Save the given content to a file at the specified path.
    
    Args:
        file_path (str): The path where the file should be saved.
        content (str): The content to be written to the file.
    """
    with open(file_path, 'w') as f:
        f.write(content)