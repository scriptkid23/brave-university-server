from app.app import app

from config.configDB import initialize_db
from flask_restful import Api
from api.routes import initialize_routes
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from config.config import configuration
from flask_jwt_extended import JWTManager
from middleware.security import ConfigurationSecurity

jwt = JWTManager(app)
configuration(app)
ConfigurationSecurity(jwt)
cors = CORS(app)
api  = Api(app)
initialize_db(app)
initialize_routes(api)


HOST = 'localhost'
app.run(host=HOST,debug=True,port=5000)
