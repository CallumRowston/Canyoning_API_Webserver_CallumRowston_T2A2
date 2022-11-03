from flask import Flask
from init import db, ma, bcrypt, jwt
import os

def create_app():
    #Create Flask object
    app = Flask(__name__)

    #JSON sorting and environment variables
    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    #Initialize instances within the app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    #Home route for testing
    @app.route('/')
    def index():
        return 'Test Test Test'
        
    #Register Blueprints


    #Basic test
    print('Hello Canyon')
    return app
    