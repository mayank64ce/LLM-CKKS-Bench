class BasePrompt:
    def __init__(self, messages,args=None):
        self.messages = messages
        self.args = args
    
    def add_message(self, role="assistant", content=""):
        """
        Add a message to the prompt.
        Args:
            role (str): The role of the message sender (e.g., "user", "assistant").
            content (str): The content of the message.
        """
        self.messages.append({"role": role, "content": content})