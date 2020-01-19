from flask import Flask
from config.configDB import initialize_db
from flask_restful import Api
from api.routes import initialize_routes
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/braveDB'
}
initialize_db(app)
initialize_routes(api)

app.run(
    debug=True,
)