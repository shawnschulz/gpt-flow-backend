from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from flask import request
import json as js
from pathlib import Path
from optparse import OptionParser
import sys
import json
from llama_cpp import Llama
from schema_controller import * 

app = Flask(__name__)

CORS(app) #comment on deploy

@app.route('/schema_json_handler', methods=['POST'])
def schema_json_handler():
    request_data = request.json
    print(request_data)
    promptData = request_data
    print("testing testing")
    print(promptData)
    return runSchema(promptData)
@app.route('/<user_id>/chatbot/response', methods=['POST'])

#should handle context jsons also, but i am so lazy lol
@app.route('/message_json_handler', methods=['POST'])
def message_json_handler():
    request_data = request.json
    print(request_data)
    promptData = request_data
    print("testing")
    print(promptData)
    return ask_alpaca(promptData["prompt"])

## Desktop model path
#path_to_model= "/home/shawn/Programming/ai_stuff/llama.cpp/models/30B/ggml-model-q4_0.bin" 

## Laptop model path

#path_to_model= "/Users/shawnschulz/Programming/llama.cpp/models/7B/ggml-model-q4_0.bin"


def ask_alpaca(prompt, model_path="./model/ggml-model-q4_0.bin", context_json="/home/shawn/Programming/backend-gpt-flow/context.json"):
    llm = Llama(model_path=model_path)
    prompt_string = prompt
    context_dict = read_dict_from_json(context_json)
    context_string = json.dumps(context_dict)
    output = llm("Context" + context_string +  " Q: " + prompt_string + " A:", max_tokens=64, stop=["Q:", "\n"], echo=True)
    print(output) 
    return_text = output["choices"][0]["text"].split("A: ",1)[1]
    print(return_text)
    return_dict = {}
    if "listed_context" in context_dict.keys():
        context_dict["listed_context"].append(return_text)
    else:
        context_dict["listed_context"] = []
        context_dict["listed_context"].append(return_text)
    write_dict_to_json(context_dict, context_json)
    return_dict["Response"] = return_text
    return(return_dict)

def chatbot_post():
    if flask.request.method == 'POST':
        chatbot_prompt = request.args.get('chatbot_prompt')
        return(ask_lora(chatbot_prompt))

def read_dict_from_json(file_path): 
    with open(file_path) as json_file:
        data = json.load(json_file)
    return(data)     

def write_dict_to_json(json_dict, file_path):
    print(json_dict)
    print(file_path)
    with open(file_path, 'w') as json_file:
        json.dump(json_dict, json_file)

if __name__ == '__main__':
    # run app in debug mode on port 4269 <- may need to change to diff port later
    app.run(debug=True, port=4269)
