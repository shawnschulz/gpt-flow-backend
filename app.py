from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from flask import request
#from chatbot_controller import *
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
    #it's working!
    print("testing testing")
    print(promptData)
    #all we really need to do next is run this through the python script already made, then somehow send it back to
    #the react server to display with a GET method. i'm thinking we just include aspects of the schema script in the
    #api backend. we should write the outputs of the schema to somewhere in the url, and have the front end send
    #get requests to those URLs, check some variable signifying whether the output is ready or not

##This was my attempt at doing a json database earlier lol, just ignore this for now
#    Path('./json_database/temp_schema.json').touch()
#    with open('./json_database/temp_schema.json', "w") as outfile:
#        js.dump(promptData, outfile)
    return runSchema(promptData)
@app.route('/<user_id>/chatbot/response', methods=['POST'])


## Desktop model path
#path_to_model= "/home/shawn/Programming/ai_stuff/llama.cpp/models/30B/ggml-model-q4_0.bin" 

## Laptop model path

#path_to_model= "/Users/shawnschulz/Programming/llama.cpp/models/7B/ggml-model-q4_0.bin"


def ask_alpaca(prompt, model_path="/Users/shawnschulz/Programming/llama.cpp/models/7B/ggml-model-f16.bin" ):
    llm = Llama(model_path=model_path)
    prompt_string = prompt["Instruction"]
#   contextual_prompt = contents + "\n The previous text was just context and is your memory, do not answer anything enclosed in []. Please answer the following question only Q: " + prompt           
    output = llm("Q: " + prompt_string + " A:", max_tokens=1, stop=["Q:", "\n"], echo=True)
    #save additional context
    #save the model again (this could either be extremely important or useless idk lol)
    #f2 = open(memory_dir + 'dataset.json', 'r+b')
    #f2.write(bytes(str(output), 'utf-8'))
    print(output) 
    return_text = output["choices"][0]["text"].split("A: ",1)[1]
    print(return_text)
    return_dict = {}
    return_dict["Response"] = return_text
    return(output)

def chatbot_post():
    if flask.request.method == 'POST':
        chatbot_prompt = request.args.get('chatbot_prompt')
        return(ask_lora(chatbot_prompt))


if __name__ == '__main__':
    # run app in debug mode on port 4269 <- may need to change to diff port later
    app.run(debug=True, port=4269)
