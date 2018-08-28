# %%writefile my_flask_app.py 
from flask import Flask, Response, jsonify 
from flask_restplus import Api, Resource, fields, reqparse 
from flask_cors import CORS, cross_origin import os 
# the app 
app = Flask(__name__) 
CORS(app) 
api = Api(app, version='1.0', title='APIs for Call For Code', validate=False) ns = api.namespace('primality', 'Returns a list of diseases') 
# load the algo 
from main_code import function_run as algo 
''' We import our function `function_run` from the file main_code.py. You create all the classes and functions that you want in that file, and import them into the app. ''' 
# model the input data 
model_input = api.model('Enter the Symtom number :', { "UPPER_BOUND": fields.Integer(maximum=10e16)}) 
# the input data type here is Integer. You can change this to whatever works for your app. 
# On Bluemix, get the port number from the environment variable PORT # When running this app on the local machine, default to 8080 
port = int(os.getenv('PORT', 8080)) 
# The ENDPOINT 
@ns.route('/sieve') 
# the endpoint 
class SIEVE(Resource): 
    @api.response(200, "Success", model_input)   
    @api.expect(model_input)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('UPPER_BOUND', type=int)
        args = parser.parse_args()
        inp = int(args["UPPER_BOUND"]) 
        result = algo(inp) 
        return jsonify({"Possible Diseases": result}) 
# run if __name__ == '__main__': app.run(host='0.0.0.0', port=port, debug=False) # deploy with debug=False