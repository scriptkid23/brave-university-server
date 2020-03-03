from config.configDB import db
import datetime
from flask_jwt_extended import create_access_token, get_raw_jwt, decode_token
from utils.error import LimitedError
from utils.createID import encodedID
from utils.blacklist import *
import json
from bson.objectid import ObjectId
from bson import ObjectId as ObI
from bson.json_util import loads, dumps
# from utils.constant import *
from datetime import datetime
from models.roleModel import *
# from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError,NotUniqueError

# # Initialize Validation
# def checkFieldUsername(self):
#         if(len(self.member_username) == 0):
#             raise ValidationError('Username Field not null ')
SHIFT = (1, 2, 3, 4, 5)
STATUS = ('Pending', 'Success', 'Denial')


class BookingRoom(db.Document):

    booking_by = db.StringField(required=True, min_length=1)
    booking_student_code = db.IntField(required=True, min_value=1)
    booking_class_wildcard = db.StringField(required=True, min_length=1)
    booking_student_number = db.IntField(required=True, min_value=1)
    booking_purpose = db.StringField(required=True, min_length=1)
    booking_lecturer = db.StringField(required=True, min_length=1)
    booking_using_time = db.DateTimeField(required=True)
    booking_start_shift = db.IntField(required=True, choices=SHIFT)
    booking_end_shift = db.IntField(required=True)
    booking_note = db.StringField()
    booking_status = db.StringField(required=True, choices=STATUS, default="Pending")
    booking_room_name = db.StringField(required=True, min_length = 1, default= "None")
    booking_is_submit = db.IntField(required=True, default= 0)
    booking_by_member  = db.StringField(required=True)
    booking_by_member_role    = db.StringField(required=True)
    booking_current_date = db.StringField(required= True)

def counterBooking(payload):
    pipeline = [
        {
            '$match': {
                'booking_by_member': payload['booking_by_member'], 
                'booking_current_date': payload['booking_current_date']
            }
        }, {
            '$group': {
                '_id': '$booking_by_member', 
                'count': {
                    '$sum': 1
                }
            }
        }
    ]
    result = list(BookingRoom.objects.aggregate(pipeline))
    if(len(result) == 0):
        return 0
    else:
        return list(BookingRoom.objects.aggregate(pipeline))[0]["count"]

def create(payload):
    count = counterBooking(payload)
    
    if(payload["booking_by_member_role"] == "student" and count < 1):
        newBooking = BookingRoom(
            booking_by=payload['booking_by'],
            booking_student_code=payload['booking_student_code'],
            booking_class_wildcard=payload['booking_class_wildcard'],
            booking_student_number=payload['booking_student_number'],
            booking_purpose=payload['booking_purpose'],
            booking_lecturer=payload['booking_lecturer'],
            booking_using_time=payload['booking_using_time'],
            booking_start_shift=payload['booking_start_shift'],
            booking_end_shift=payload['booking_end_shift'],
            booking_note=payload['booking_note'],
            booking_by_member = payload['booking_by_member'],
            booking_by_member_role = payload['booking_by_member_role'],
            booking_current_date = payload['booking_current_date']
        )
        newBooking.save(validate=True)
    else:
        raise LimitedError

def getListBookingRoom(payload):
    if payload['booking_id'] == "":
        booking_list = BookingRoom.objects._collection.find(
            {},
            {
                "_id": True,
                "booking_by": True,
                "booking_student_code": True,
                "booking_class_wildcard": True,
                "booking_student_number": True,
                "booking_purpose": True,
                "booking_lecturer": True,
                "booking_using_time": True,
                "booking_start_shift": True,
                "booking_end_shift": True,
                "booking_note": True,
                "booking_status" : True,
                "booking_room_name" : True,
                "booking_is_submit" : True,

            })
        result = loads(dumps(list(booking_list)))
        booking = []
        for i in result:
            temp = {
                "booking_id": str(i['_id']),
                "booking_by": i['booking_by'],
                "booking_student_code": i['booking_student_code'],
                "booking_class_wildcard": i['booking_class_wildcard'],
                "booking_student_number": i['booking_student_number'],
                "booking_purpose": i['booking_purpose'],
                "booking_lecturer": i['booking_lecturer'],
                "booking_using_time":i['booking_using_time'].isoformat(),
                "booking_start_shift": i['booking_start_shift'],
                "booking_end_shift": i['booking_end_shift'],
                "booking_note": i['booking_note'],
                "booking_status" : i['booking_status'],
                "booking_room_name" : i['booking_room_name'],
                "booking_is_submit" :i['booking_is_submit']
            }
            booking.append(temp)
        print(booking)
        return booking
    else:
        print(repr(ObjectId(payload['booking_id'])))
        booking_list = BookingRoom.objects._collection.find(
            {"_id" : ObjectId(payload['booking_id'])},
            {
                "_id": True,
                "booking_by": True,
                "booking_student_code": True,
                "booking_class_wildcard": True,
                "booking_student_number": True,
                "booking_purpose": True,
                "booking_lecturer": True,
                "booking_using_time": True,
                "booking_start_shift": True,
                "booking_end_shift": True,
                "booking_note": True,
                "booking_status" : True,
                "booking_room_name" : True,
                "booking_is_submit" : True

            })
        result = loads(dumps(list(booking_list)))
        booking = []
        for i in result:
            temp = {
                "booking_id": str(i['_id']),
                "booking_by": i['booking_by'],
                "booking_student_code": i['booking_student_code'],
                "booking_class_wildcard": i['booking_class_wildcard'],
                "booking_student_number": i['booking_student_number'],
                "booking_purpose": i['booking_purpose'],
                "booking_lecturer": i['booking_lecturer'],
                "booking_using_time":i['booking_using_time'].isoformat(),
                "booking_start_shift": i['booking_start_shift'],
                "booking_end_shift": i['booking_end_shift'],
                "booking_note": i['booking_note'],
                "booking_status" : i['booking_status'],
                "booking_room_name" : i['booking_room_name'],
                "booking_is_submit" :i['booking_is_submit']
            }
            booking.append(temp)
        print(booking)
        return booking


def update(payload):
    param = payload['booking_id']
    obj = {
        "booking_status" : payload['booking_status'],
        "booking_room_name" : payload['booking_room_name'],
        "booking_is_submit" : 1,
    }
    result = BookingRoom.objects.get(pk= ObjectId(payload['booking_id'])).update(**obj)
