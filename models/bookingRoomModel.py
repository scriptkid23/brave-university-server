from config.configDB import db
import datetime
from flask_jwt_extended import create_access_token,get_raw_jwt, decode_token

from utils.createID import encodedID
from utils.blacklist import *
import json
from bson.objectid import ObjectId
from bson.json_util import loads,dumps
# from utils.constant import *

from models.roleModel import *
# from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError,NotUniqueError

# # Initialize Validation
# def checkFieldUsername(self):
#         if(len(self.member_username) == 0):
#             raise ValidationError('Username Field not null ')
SHIFT = (1,2,3,4,5)
STATUS = ('Pending','Success','Denial')
class BookingRoom(db.Document):
 
    booking_by             = db.StringField(required = True)        
    booking_student_code   = db.IntField(required = True,)
    booking_class_wildcard = db.StringField(required = True)
    booking_student_number = db.IntField(required = True)
    booking_purpose        = db.StringField(required = True)
    booking_lecturer       = db.StringField(required = True)
    booking_using_time     = db.DateTimeField(required=True)
    booking_start_shift    = db.IntField(required=True,choices = SHIFT)
    booking_end_shift      = db.IntField(required=True,choices = SHIFT)
    booking_note           = db.StringField(required=True)
    booking_status         = db.StringField(required=True,choices = STATUS)


    def Validation(self):
        if(self.booking_start_shift >= self.booking_end_shift):
            return true



def create(payload):

        newBooking = BookingRoom(
            booking_by = payload['booking_by'],
            booking_student_code = payload['booking_student_code'],
            booking_class_wildcard = payload['booking_class_wildcard'],
            booking_student_number = payload['booking_student_number'],
            booking_purpose = payload['booking_purpose'],
            booking_lecturer = payload['booking_lecturer'],
            booking_using_time = payload['booking_using_time'],
            booking_start_shift = payload['booking_start_shift'],
            booking_end_shift = payload['booking_end_shift'],
            booking_note = payload['booking_note'],
        )
        newBooking.save(validate=True)


def update(payload):
    member_detail = Member.objects._collection.find(
            {"member_username":payload['member_username']},
            {
                "member_username" : True,
                "_id":False,
                "member_first_name" : True,
                "member_last_name" : True,
                "member_role" : True,
                "member_avatar" : True,
            })
    result = loads(dumps(list(member_detail)))
    return result

