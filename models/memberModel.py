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

class Member(db.Document):

    member_id         = db.StringField(required=True, unique=True)
    member_username   = db.StringField(max_length=255, min_length = 1,  required=True,unique=True)
    member_password   = db.StringField(max_length=255, min_length = 6,  required=True)
    member_first_name  = db.StringField(max_length=255, min_length =1)
    member_last_name  = db.StringField(max_length=255, min_length =1)
    member_gender     = db.BooleanField()
    member_email      = db.EmailField()
    member_address    = db.StringField(max_length=255, min_length =1)
    member_about_me   = db.StringField(max_length=255, min_length =1)
    member_avatar     = db.StringField()
    member_role       = db.StringField(max_length=255, min_length =1,default="student")
   
    
    def checkPassword(self,password):
        if(self.member_password == password):
            return True
        else:
            return False
    


def register(payload):
        
        newMember= Member(
            member_id        = encodedID(payload['member_username']),
            member_username  = payload["member_username"],
            member_first_name = payload["member_first_name"],
            member_last_name = payload["member_last_name"],
            member_password  = payload["member_password"]
        )
        newMember.save(validate=True)
class UserObject:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles


def login(payload):
    print(payload)
    member = Member.objects.get(member_username = payload["member_username"])
    authorized = member.checkPassword(payload["member_password"])
    if not authorized:
        return False
    expires = datetime.timedelta(days = 1)
    print(member.member_username)
    user = UserObject(username=member.member_username, roles=member.member_role)
    access_token = create_access_token(identity=user,expires_delta=expires)
    
    return {"token":access_token,"data":{"username" :member.member_username,"Role":member.member_role}}


def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)

# def login(payload):
    
# def signout(payload):
# def getEmployees():
#     return Employee.objects().to_json()

# def updateEmployee(self,payload):
#     pass #
# def deleteEmployee(self,payload):
