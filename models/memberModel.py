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
    member_fist_name  = db.StringField(max_length=255, min_length =1)
    member_last_name  = db.StringField(max_length=255, min_length =1)
    member_gender     = db.BooleanField()
    member_email      = db.EmailField()
    member_address    = db.StringField(max_length=255, min_length =1)
    member_about_me   = db.StringField(max_length=255, min_length =1)
    member_avatar     = db.StringField()
    member_role       = db.StringField(max_length=255, min_length =1)
    # def json(self):
    #     member_dict = {
    #        "member_id": self.member_id,
    #        "member_username": self.member_username,
    #        "member_password": self.member_password
    #     }
    #     return json.dumps(member_dict)
    
    def checkPassword(self,password):
        if(self.member_password == password):
            return True
        else:
            return False
    


def register(payload):
        
        newMember= Member(
            member_id        = encodedID(payload['member_username']),
            member_username  = payload["member_username"],
            member_fist_name = payload["member_fist_name"],
            member_last_name = payload["member_last_name"],
            member_password  = payload["member_password"],
            # member_role      = ObjectId(getRoleDefault())
        )
        newMember.save(validate=True)

def login(payload):
    member = Member.objects.get(member_username = payload["member_username"])
    authorized = member.checkPassword(payload["member_password"])
    if not authorized:
        return False
    expires = datetime.timedelta(days = 1)
    access_token = create_access_token(identity=str(member.member_id),expires_delta=expires)

    pipeline = [{
        "$lookup" : {
            "from" : Role._get_collection_name(),
            "localField" : 'member_role',
            "foreignField" : '_id',
            "as" : 'my_role'
        }
    }]

    permission_list = Member.objects(member_id = member['member_id']).aggregate(pipeline)
    result = loads(dumps(list(permission_list)))
    del result[0]['my_role'][0]['_id']

    payload = {
        "access_token" : access_token,
        "permission" : result[0]['my_role'][0]
    }
    # print(decode_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODA3NDAxNzgsIm5iZiI6MTU4MDc0MDE3OCwianRpIjoiYTQ1NDVkMzQtMGNjMS00YWZiLWFiYzgtMjAxODY3ZmM5ZTk2IiwiZXhwIjoxNTgwODI2NTc4LCJpZGVudGl0eSI6Ik1qQXlNQzB5TFRNdE1USXRORFV0TVRndE5EYzFNemt3TFdGa2JXbHUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.9l1HtvKDXChn0aKS4H17Fw7znVwvyU5_d4C8NXVyQTM'))
    return payload

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
