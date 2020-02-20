from app.app import app
from config.configDB import initialize_db

from flask_restful import Api
from api.routes import initialize_routes
from flask_mongoengine import MongoEngine
from flask_cors import CORS

from middleware.security import initialize_Security
from middleware.socketio import initialize_socketio

cors = CORS(app)

initialize_Security(app)
initialize_db(app)

api  = Api(app)
initialize_routes(api)

initialize_socketio(app)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
