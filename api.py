from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)
port = 5000

class BatResource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'checking docker deployment',
            'res': '13+13=26'
        }

class Resource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'checking docker deployment',
            'res': '10+10 = 20'
        }  


api.add_resource(
    BatResource, # shape of user resource
    '/'
)

api.add_resource(
    Resource, # shape of user resource
    '/cat'
)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)