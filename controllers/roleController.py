from flask import Response, request
from models.roleModel import *
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
# from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError
import json
from utils.error import errors 
# Lấy ra tất cả danh sách nhân viên 
class RoleController(Resource): 
   @jwt_required
   def get(self):
       ret = {
        'current_identity': get_jwt_identity(),  # test
        'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
        }
       if get_jwt_claims()['roles'] == 'admin':
            return Response(json.dumps(ret),mimetype="application/json", status=200)
       else:
           return Response("",mimetype="application/json", status=404)

