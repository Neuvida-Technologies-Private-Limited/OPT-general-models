"""
Loading OPT model and its tokenizer.
"""
from transformers import GPT2Tokenizer, OPTForCausalLM

# Loading Language model and its tokenizer

model = OPTForCausalLM.from_pretrained("facebook/opt-2.7b")
tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-2.7b")


