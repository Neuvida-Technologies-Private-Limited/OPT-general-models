"""
Simple API which queries OPT LM with a prompt and returns 
next set of tokens.
"""
from flask import Flask, request, jsonify
from query_model import model, tokenizer
# using time module
import torch
import time

# ts stores the time in seconds
ts = time.time()

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@app.route('/OPT', methods=["POST"])
def testpost():
     print(ts)
     input_json = request.get_json(force=True) 
     prompt_text = input_json['prompt']
     temp = input_json['temp']
     t_p = input_json['top_p']
     t_k = input_json['top_k']
     print(ts)
     encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
     encoded_prompt = encoded_prompt.to(device)
     model.to(device)
     print(ts)
     outputs = model.generate(encoded_prompt,
                        max_length=64+len(encoded_prompt[0]), 
                        do_sample=True,
                        temperature = temp, 
                        top_p=t_p, 
                        top_k=t_k,
                        repetition_penalty=1.2,
                        #  num_beams=5, 
                        # no_repeat_ngram_size=3, 
                        # num_return_sequences=1, 
                        # early_stopping=True
                         )
     output_seq = tokenizer.decode(outputs[0], skip_special_tokens=True)
     print(ts)
     dictToReturn = {'result':output_seq}

     return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run()
     