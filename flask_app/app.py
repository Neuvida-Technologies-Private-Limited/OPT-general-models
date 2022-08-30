"""
Simple API which queries META-OPT LM with a prompt and returns 
next set of tokens.
"""
from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, OPTForCausalLM
# using time module
import torch

app = Flask(__name__)

model = OPTForCausalLM.from_pretrained("facebook/opt-1.3b")
tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-1.3b")

#device = torch.device("cpu")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
curr_device = torch.cuda.current_device()
device_name = torch.cuda.get_device_name(curr_device)

@app.route('/', methods=["GET"])
def testing():
     return "success",200


@app.route('/OPT', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     prompt_text =str(input_json['prompt'])
     temp = float(input_json['temp'])
     t_p = float(input_json['top_p'])
     t_k = int(input_json['top_k'])
     max_len = int(input_json['max_len'])

     length = len(prompt_text)

     torch.cuda.empty_cache()
     encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
     encoded_prompt = encoded_prompt.to(device)
     model.to(device)

     with torch.no_grad():
          
          outputs = model.generate(encoded_prompt,
                        max_length=max_len+len(encoded_prompt[0]),
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

     dictToReturn = {'inference-on':device_name,'result':output_seq[length:]}

     return jsonify(dictToReturn)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
     
