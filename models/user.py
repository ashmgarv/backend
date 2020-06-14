from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, default=None)
    password = db.Column(db.String(255), default=None, nullable=False, unique=False)
    fullname = db.Column(db.String(255), default=None, nullable=False, unique=False)

    @staticmethod
    def add_user(username, password, fullname):
        try:
            user = User(username=username, password=generate_password_hash(password), fullname=fullname)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        return True





