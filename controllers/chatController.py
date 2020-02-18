from flask_restful import Resource
from flask import Response, request
from models.chatRoomModel   import *
import json

class ChatController(Resource):
    def get(self):
        
        return Response(json.dumps({"code":200}),mimetype="application/json", status=200)