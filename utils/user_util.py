from models.user import User as usr
from werkzeug.security import check_password_hash
import json

def check_valid_user(username, password):
    try:
        login_result = login(username, password)
    except Exception as e:
        return {'is_logged_in':False,'fullname':"none"}

    if login_result['is_logged_in']:
        return login_result
    return {'is_logged_in':False,'fullname':"none"}

def login(username, password):
    try:
        logged_in_user = usr.query.filter_by(username=username).first()
    except Exception as e:
        print("Error occured while trying to login : " + str(e))
        raise e
    return {'is_logged_in': (check_password_hash(logged_in_user.password, password=password)), 'fullname': logged_in_user.fullname}

def load_json(request):
    return json.loads(request.data.decode('utf8').replace("'", '"'))

def add_user(username, password, fullname):
    return (usr.add_user(username, password, fullname))