import sys
sys.path.append('..')
from .base import BaseLLM
from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts.prompts import BasePrompt
import time
import random

class Llama3_3_70b(BaseLLM):
    def __init__(self, model_name="meta-llama/llama-3.3-70b-instruct", model_type='openrouter', args=None, tempurature=0.7, max_new_tokens=150):
        super().__init__(model_name, model_type, args, tempurature, max_new_tokens)
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is not set.")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
    
    def generate(self, prompt):
        messages = prompt.messages
        # Sleep for a random interval between 1 and 10 seconds to avoid rate limit errors
        time.sleep(random.uniform(1, 10))
        completion = self.client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=messages,
            max_tokens=self.max_new_tokens,
            temperature=self.temperature,
            seed=self.args.run_id,
        )

        response = completion.choices[0].message.content

        return response

class Args:
    def __init__(self, seed=42):
        self.seed = seed
    def get(self, key, default=None):
        return getattr(self, key, default)

if __name__ == "__main__":
    system_prompt = "You are an helpful assistant."
    user_prompt = "Write a C++ hello world."

    args = Args(seed=1)

    prompt = BasePrompt([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ])

    llm = Llama3_3_70b(args=args)
    print(llm.generate(prompt))
