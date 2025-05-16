import sys
sys.path.append("..")
from .base import BaseLLM
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

from prompts.prompts import BasePrompt

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                # Set to True for 4-bit quantization
)

class DeepseekCoder(BaseLLM):
    def __init__(self, model_name="deepseek-ai/deepseek-coder-6.7b-instruct", model_type='hf_local', args=None, temperature=0.7, max_new_tokens=150):
        super().__init__(model_name, model_type, args, temperature, max_new_tokens)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", quantization_config=bnb_config)
        self.model.eval()
        

    def generate(self, prompt):
        messages = prompt.messages
        input_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(input_prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=self.max_new_tokens, temperature=self.temperature, do_sample=True)  
        generated_ids = outputs[0][inputs.input_ids.shape[-1]:]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        return response


if __name__ == "__main__":
    system_prompt = """Answer the following questions as best you can. You have access to the following tools:

convert_time: A function to convert a time string with format H:MM:SS to seconds

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
convert_time: A function to convert a time string with format H:MM:SS to seconds, args: {"time": {"type": "string"}}

The $JSON_BLOB should only contain a SINGLE action and MUST be formatted as markdown, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

```
{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}
```
Make sure to have the $INPUT in the right format for the tool you are using, and do not put variable names as input if you can find the right values.

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:
```
$JSON_BLOB
```
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

Youb must always end your output with the following format:

Thought: I now know the final answer
Final Answer: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `Final Answer:` when you provide a definitive answer. """.strip()
    
    prompt = BasePrompt([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Write a c++ hello world program"}
    ])
    # llm = HFLocalLLM("deepseek-ai/deepseek-coder-6.7b-instruct")
    llm = DeepseekCoder()
    print(llm.generate(prompt))