
from dotenv import load_dotenv
import os
def configuration(app):
    
    APP_ROOT = os.path.join(os.path.dirname(__file__),'.')
    DOTENV_PATH = os.path.join(APP_ROOT,'.env')
    load_dotenv(DOTENV_PATH)

    UPLOAD_FOLDER = os.path.join(APP_ROOT,'upload/image/')


    app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/braveDB'
    }
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
