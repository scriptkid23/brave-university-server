from flask import Response, request
from models.bookingRoomModel import *
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
from datetime import date
import json
from mongoengine.errors import *

from utils.error import *


class BookingRoomController(Resource):
    @jwt_required
    def post(self):
        try:
            payload = request.get_json()
            payload["booking_by_member"] = get_jwt_identity()
            payload["booking_by_member_role"] = get_jwt_claims()["roles"]
            payload["booking_current_date"] = date.today().strftime("%d-%m-%Y")
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
        except LimitedError:
            return Response(
                json.dumps({"status": 400, "message": "Booking Limited"}),
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
