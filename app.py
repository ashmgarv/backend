from flask import Flask
from flask_restful import Api
from dynaconf import settings
from db import db
import os
from flask_migrate import Migrate
from resources import user_api as user



app = Flask(__name__)
api = Api(app)

#Apis
api.add_resource(user.UserAPI, '/user_api')
api.add_resource(user.UserAPI, '/login_api')

#Setup database
app.secret_key = '8a610d19-d675-4eb4-ad96-8fc603821e02'
db_connection_pattern = "mysql://{uname}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_pattern.format(uname=os.environ[settings.ENV_DBUNAME],password=os.environ[settings.ENV_DBPWD],host=os.environ[settings.ENV_DBHOST],port=os.environ[settings.ENV_DBPORT],db_name=os.environ[settings.ENV_DBNAME])
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
