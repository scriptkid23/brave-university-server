from utils.extensions import *
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect,send

def initialize_socketio(socketio):
    
    @socketio.on('connect')
    def on_connect():
        print('user connected')

    
    @socketio.on('disconnect')
    def on_disconnect():
        print('user disconnected')


    chat_store = []
    @socketio.on('my_event')
    def my_event(data):
        ExportMessage(chat_store,data)
        print(chat_store)
        emit('my_response',json.dumps(chat_store),broadcast=True)