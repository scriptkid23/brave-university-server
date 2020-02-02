from flask import Flask
from config.configDB import initialize_db
from flask_restful import Api
from api.routes import initialize_routes
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv 
import os 
from utils.blacklist import *
APP_ROOT = os.path.join(os.path.dirname(__file__),'.')
DOTENV_PATH = os.path.join(APP_ROOT,'.env')
load_dotenv(DOTENV_PATH) 

app  = Flask(__name__)

cors = CORS(app)
api  = Api(app)
jwt  = JWTManager(app)



@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/braveDB'
}
initialize_db(app)
initialize_routes(api)

HOST = '192.168.0.117'
app.run(host=HOST,debug=True)