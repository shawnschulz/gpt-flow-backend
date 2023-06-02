from flask import Flask
from flask_restful import Api, Resource, reqparse
from api.HelloApiHandler import HelloApiHandler

api = Flask(__name__)

@api.route('/output')
def get_output():
    output = False #insert way to get the output here later
    return output

class HelloApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': 'Api Handler Sends their regards >:)'
        }
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)
        args = parser.parse_args()
        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')
        request_type = args['type']
        resuest_json = args['message']
        ret_status = request_type
        ret_msg = request_json
        
        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"
        
        final_ret = {"status": "Success", "message": message}
        
        return final_ret