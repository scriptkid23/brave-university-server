from app.app import app
from config.configDB import initialize_db
from flask_restful import Api
from api.routes import initialize_routes
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from config.config import configuration
from flask_jwt_extended import JWTManager
from middleware.security import ConfigurationSecurity
import json
# Config flask socketio
from threading import Lock
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect,send

# from middleware.socketio import  initialize_socketio
jwt  = JWTManager(app)
cors = CORS(app)
configuration(app)
ConfigurationSecurity(jwt)

api  = Api(app)
initialize_db(app)
initialize_routes(api)

async_mode = None
thread_lock = Lock()

socketio = SocketIO(app,cors_allowed_origins='*')




@socketio.on('connect')
def on_connect():
    print('user connected')

from utils.extensions import *
chat_store = []
@socketio.on('my_event')
def my_event(data):
    ExportMessage(chat_store,data)
    print(chat_store)
    emit('my_response',json.dumps(chat_store),broadcast=True)

PORT = '5000'
if __name__ == '__main__':

    app.debug = True
    socketio.run(app,port=PORT)
