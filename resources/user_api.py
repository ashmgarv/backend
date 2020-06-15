from flask_restful import Resource
from models.user import User
import flask
from utils.user_util import check_valid_user, load_json, add_user

class UserAPI(Resource):
    def post(self):
        params = load_json(flask.request)
        username = params['username']
        password = params['password']
        fullname = params['fullname']
        return add_user(username, password, fullname)

class LoginAPI(Resource):
    def post(self):
        params = load_json(flask.request)
        result = check_valid_user(params['username'],params['password'])
        data = flask.jsonify(result)
        if result['is_logged_in']:
            return flask.make_response(data, 200)
        else:
            return flask.make_response(data, 403)
