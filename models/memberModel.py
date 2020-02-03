from config.configDB import db
import datetime
from flask_jwt_extended import create_access_token,get_raw_jwt
from utils.createID import encodedID
from utils.blacklist import * 
import json 
from bson.objectid import ObjectId
from models.roleModel import *
# from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError,NotUniqueError

# # Initialize Validation 
# def checkFieldUsername(self):
#         if(len(self.member_username) == 0):
#             raise ValidationError('Username Field not null ')

class Member(db.Document):

    member_id = db.StringField(required=True, unique=True)
    member_username = db.StringField(max_length=255, min_length = 1,  required=True,unique=True)
    member_password = db.StringField(max_length=255, min_length = 6,  required=True)
    member_role     = db.ObjectIdField(required=True,default=ObjectId)
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
            member_id       = encodedID(payload['member_username']),
            member_username = payload["member_username"],
            member_password = payload["member_password"],
            member_role     = ObjectId(getRoleDefault())
        )
        newMember.save(validate=True)

def login(payload):
    member = Member.objects.get(member_username = payload["member_username"])
    authorized = member.checkPassword(payload["member_password"])
    if not authorized:
        return False
    expires = datetime.timedelta(days = 1)
    access_token = create_access_token(identity=str(member.member_id),expires_delta=expires)
    return access_token

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
