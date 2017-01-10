from flask import g, app
from flask import jsonify
from flask import request
from flask_restful import Resource
from flaskext.auth import auth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from database.usersrepository import UserRepository


class User(Resource):

    def generate_auth_token(self, expiration=600):
        s = Serializer(app['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': 123})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired. You could make log here
        except BadSignature:
            return None  # invalid token

        user = UserRepository.get_user(data['id'])
        return jsonify(user)


    def get(self, user_id):
        user = UserRepository.get_user(user_id)
        return jsonify(user)

    def post(self):
        username = request.get_json('username')
        password = request.get_json('password')

       # return jsonify(args)

    @auth.login_required
    def get_auth_token(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token.decode('ascii')})

    @auth.login_required
    def verify_password(username_or_token, password):
        # first try to authenticate by token
        user = User.verify_auth_token(username_or_token)
        if not user:
            # try to authenticate with username/password
            user = UserRepository.get_user(username_or_token)
            if not user or not user.verify_password(password):
                return False
        g.user = user
        return True



class Permission(Resource):
    def get(self):
        return {'saraza': 'uno'}
