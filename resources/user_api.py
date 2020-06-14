from flask_restful import Resource
from models.user import User
import flask
import json
from utils.login_util import check_valid_user

class UserAPI(Resource):
    def post(self):
        username = flask.request.form.get('usrname', "")
        password = flask.request.form.get('password', "")
        fullname = flask.request.form.get('fullname', "")
        return(User.add_user(username, password,fullname))

class LoginAPI(Resource):
    def post(self):
        params= json.loads(flask.request.data.decode('utf8').replace("'", '"'))
        print(type(params))
        result = check_valid_user(params['username'],params['password'])
        data = flask.jsonify(result)
        if result['is_logged_in']:
            return flask.make_response(data, 200)
        else:
            return flask.make_response(data, 403)
