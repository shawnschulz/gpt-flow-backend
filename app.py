from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from flask import request

app = Flask(__name__)

#app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment on deploy
#api = Api(app)
@app.route('/json', methods=['POST'])
def json():
    request_data = request.get_json()
    nodes = request_data['nodes']
    return '''
              Nodes is {}'''.format(nodes)
# @app.route("/users/<user_id>", defaults={'path':''}, methods = ['GET', 'POST'])
# def user(user_id):
#     if request.method == 'GET':
#         '''
#             perform GET for user_id
#         '''
#     if request.method == 'POST':
#         '''
#             perform POST for user_id
#         '''
#         data = request.form
#     else:
#         # POST Error 405 Method Not Allowed

# def serve(path):
#     return send_from_directory(app.static_folder, 'index.html') #<- p sure this doesn't work for react hookup

# api.add_resource(HelloApiHandler, '/flask/prompts2')

if __name__ == '__main__':
    # run app in debug mode on port 4269 <- may need to change to diff port later
    app.run(debug=True, port=4269)