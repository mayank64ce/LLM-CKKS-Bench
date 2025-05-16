class BaseLLM:
    def __init__(self, model_name, model_type, args, temperature=0.7, max_new_tokens=150):
        self.model_name = model_name.split("/")[-1]
        self.model_type = model_type
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.args = args
        
    def generate(self, prompt):
        """
        Generate a response based on the provided prompt.
        This method should be overridden by subclasses to implement specific generation logic.
        """
        raise NotImplementedError("Subclasses should implement this method.")
    
    def __call__(self, prompt):
        """
        Call the generate method with the provided prompt.
        """
        return self.generate(prompt)