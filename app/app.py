from flask import Flask
from dotenv import load_dotenv
import os

app  = Flask(__name__)

APP_ROOT        = os.path.join(os.path.dirname(__file__),'.')
DOTENV_PATH     = os.path.join(APP_ROOT,'.env')
UPLOAD_FOLDER   = os.path.join(APP_ROOT,'upload/image/')

load_dotenv(DOTENV_PATH)

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://braveDB:whoami@cluster0-4jdjf.mongodb.net/braveDB?retryWrites=true&w=majority'
    
    }

app.config.update(DEBUG = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
