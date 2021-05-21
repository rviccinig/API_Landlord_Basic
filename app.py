#Modular Landlord App

import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from flask_jwt import JWT
# Create my App
app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

#Its very important to take the db creation out of the main file to avoid circular import
# We connect the database and the migrate isuing the .init_app method
from db import db,migrate
db.init_app(app)
migrate.init_app(app, db)

# define my app as an API
api = Api(app)

# authentication with jwt
jwt = JWT(app, authenticate, identity)

#RESOURCES
from resources.user import register_user, UserList
from resources.building import create_building,PropertyList,Massive_Upload
from resources.prediction import prediction_regression
from resources.vacant import add_vacancy,Vacancy_List


api.add_resource(register_user, '/register')
api.add_resource(UserList,'/see_all')
api.add_resource(create_building,'/create_building')
api.add_resource(PropertyList,'/property_list')
api.add_resource(Massive_Upload,'/massive_upload')
api.add_resource(prediction_regression,'/prediction_regression')
api.add_resource(add_vacancy,'/create_vacancy')
api.add_resource(Vacancy_List,'/vacancy_list')

#Crate the API
if __name__ == '__main__':
    app.run(debug=True)
