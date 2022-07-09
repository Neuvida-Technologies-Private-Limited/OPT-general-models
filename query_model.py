"""
Loading OPT model and its tokenizer.
"""
from transformers import GPT2Tokenizer, OPTForCausalLM

# enter the path to Language model
path =  "./opt-2.7b"

# Loading Language model and its tokenizer

model = OPTForCausalLM.from_pretrained(path)
tokenizer = GPT2Tokenizer.from_pretrained(path)


