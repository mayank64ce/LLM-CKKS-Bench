import sys
sys.path.append('..')
from .base import BaseLLM
from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts.prompts import BasePrompt
import time
import random

class GPT_4o(BaseLLM):
    def __init__(self, model_name="openai/gpt-4o", model_type='openai', args=None, tempurature=0.7, max_new_tokens=150):
        super().__init__(model_name, model_type, args, tempurature, max_new_tokens)
        load_dotenv()
        self.client = OpenAI()
    
    def generate(self, prompt):
        messages = prompt.messages
        # Sleep for a random interval between 1 and 10 seconds to avoid rate limit errors
        time.sleep(random.uniform(1, 10))
        completion = self.client.chat.completions.create(
            model="gpt-4o",
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

    llm = GPT_4o(args=args)
    print(llm.generate(prompt))
