from flask import Response, request
from models.memberModel import *
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

import json
from mongoengine.errors import *

from utils.error import errors



class MemberRegisterController(Resource):
    def post(self):
        try:
            payload = request.get_json()
            result = register(payload)
            
            return Response(
                json.dumps({"code" : 200,"status" :"Create member sucesss"}), 
                mimetype="application/json", 
                status=200)
        except(NotUniqueError):
            return Response(
                json.dumps(errors['MemberAlreadyExistsError']), 
                mimetype="application/json", 
                status=errors['MemberAlreadyExistsError']['status'])
        except(ValidationError):
            return Response(
                json.dumps(errors['ValidationError']),
                mimetype="application/json",
                status=errors['ValidationError']['status']
            )

class MemberLoginController(Resource):
    def post(self):
        try: 
            payload = request.get_json()
            result = login(payload)
     
            if result:
                return Response(json.dumps({"code" : 200,"token":result['token'],"data":result['data']}), 
                mimetype="application/json",
                status=200,
                headers={"token":result})
            else:
                return Response(
                    json.dumps(errors['UnauthorizedError']),
                    mimetype="application/json",
                    status=errors['UnauthorizedError']['status']
                )
        except(DoesNotExist):
            return Response(
                json.dumps(errors['MemberNotExistsError']),
                mimetype="application/json",
                status=errors['MemberNotExistsError']['status']
            )
        
class MemberLogoutController(Resource):
    @jwt_required
    def delete(self):
        logout()
        return Response(
            json.dumps({"code" :200,"status" :"logout success"}), 
            mimetype="application/json",
            status=200)


# class EmployeeController(Resource):
#     def post(self):
#         payload = request.get_json()
#         createEmloyee(payload)
#         return Response(json.dumps({"code" : 200,"status" :"insert employee sucesss"}),mimetype="application/json",status=200)
#     def put(self):
#         payload = request.get_json()
#         updateEmployee(payload)
#         return Response(json.dumps({"code" : 200,"status" :"update employee sucesss"}),mimetype="application/json",status=200)
#     def delete(self):
#         payload = request.get_json()
#         deleteEmployee(payload)
#         return Response(json.dumps({"code" : 200,"status" :"delete employee sucesss"}),mimetype="application/json",status=200)

#     def get(self):
#         payload = request.get_json()
#         result  = getDetailEmployee(payload)
#         return Response(result, mimetype="application/json", status=200)