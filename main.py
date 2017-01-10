from flask import Flask
from flask_restful import Api

from controllers.autenthication import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users','/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)