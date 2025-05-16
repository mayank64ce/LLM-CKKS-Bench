class BaseAgent:
    def __init__(self):
        pass

    def step(self):
        raise NotImplementedError("Subclasses should implement this method.")