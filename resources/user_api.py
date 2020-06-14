from flask_restful import Resource
from models.user import User

class UserAPI(Resource):
    def post(self):
        return(User.add_user("awalia", "a","Ashm Walia"))
