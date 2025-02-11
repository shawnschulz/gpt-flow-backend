from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from flask import request
import json
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
    return prompt_deepseek(promptData["prompt"])



def chatbot_post():
    if flask.request.method == 'POST':
        chatbot_prompt = request.args.get('chatbot_prompt')
        return(prompt_deepseek(chatbot_prompt))

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
