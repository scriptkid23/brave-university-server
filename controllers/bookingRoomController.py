from flask import Response, request
from models.bookingRoomModel import *
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

import json
from mongoengine.errors import *

from utils.error import errors


class BookingRoomController(Resource):
    def post(self):
        try:
            payload = request.get_json()
            print("Payload : ", payload)
            create(payload)
            return Response(
                json.dumps(
                    {"status": 200, "message": "Create booking sucesss"}),
                mimetype="application/json",
                status=200)
        except ValidationError:
            return Response(
                json.dumps({"status": 400, "message": "Validation Error"}),
                mimetype="application/json",
                status=400)

    

class GetListBookingRoomController(Resource):
    def post(self):
        try:   
            payload = request.get_json()
            data = getListBookingRoom(payload)
            return Response(
                json.dumps(
                    {"status": 200, "payload": data}),
                mimetype="application/json",
                status=200)
        except ValidationError:
            return Response(
                json.dumps({"status": 400, "message": "Validation Error"}),
                mimetype="application/json",
                status=400)

class UpdateBookingRoomController(Resource):
    def put(self):
        try:
            payload = request.get_json()
            print("payload:",payload)
            result = update(payload)
            return Response(
                json.dumps(
                    {"status": 200, "message": "Update booking sucesss"}),
                mimetype="application/json",
                status=200)
        except ValidationError:
            return Response(
                json.dumps({"status": 400, "message": "Validation Error"}),
                mimetype="application/json",
                status=400)
