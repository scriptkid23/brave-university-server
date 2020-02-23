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
        payload = request.get_json()
        create(payload)
        return Response(
                json.dumps({"code" : 200,"status" :"Create booking sucesss"}),
                mimetype="application/json",
                status=200)