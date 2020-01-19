from flask import Response, request
from models.memberModel import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_raw_jwt
import json
class MemberRegisterController(Resource):
    def post(self):
        payload = request.get_json()
        result = register(payload)
        if result:
            return Response(json.dumps({"code" : 400,"status" :"Create member failed"}), mimetype="application/json", status=400)
        else:
            return Response(json.dumps({"code" : 200,"status" :"Create member sucesss"}), mimetype="application/json", status=200)
class MemberLoginController(Resource):
    def post(self):
        payload = request.get_json()
        result = login(payload)
        # print(result)
        if(result):
            return Response(json.dumps({"code" : 200,"token" : result}), mimetype="application/json",status=200)
        else:
            return Response(json.dumps({"code" : 400,"status" :"Login member failed"}), mimetype="application/json",status=400)
class MemberLogoutController(Resource):
    @jwt_required
    def delete(self):
        logout()
        return Response(json.dumps({"code" :200,"status" :"logout success"}), mimetype="application/json",status=200)


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