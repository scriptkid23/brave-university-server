from flask import Response, request
from models.roleModel import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
# from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError
import json
from utils.error import errors 
# Lấy ra tất cả danh sách nhân viên 
class RolesController(Resource): 
    @jwt_required
    def get(self):

        payload = getEmployees()
        # print(get_jwt_identity()) // lấy employee_id 
        return Response(payload, mimetype="application/json", status=200)

      
class RoleController(Resource):
    # Tạo 1 nhân viên 
    @jwt_required
    def post(self):
        try:
            payload = request.get_json()
            createRole(payload)
            return Response(json.dumps({"code" : 200,"status" :"insert role sucesss"}),mimetype="application/json",status=200)
        except(DuplicateKeyError):
            return Response(
                json.dumps(errors['DuplicateRole']),
                mimetype='application/json',
                status = 400
            )
    # cập nhật thông tin của một nhân viên 
    # @jwt_required
    # def put(self):
    #     payload = request.get_json()
    #     updateEmployee(payload)
    #     return Response(json.dumps({"code" : 200,"status" :"update employee sucesss"}),mimetype="application/json",status=200)
    
    # # Xoá một nhân viên 
    # @jwt_required
    # def delete(self):
    #     payload = request.get_json()
    #     deleteEmployee(payload)
    #     return Response(json.dumps({"code" : 200,"status" :"delete employee sucesss"}),mimetype="application/json",status=200)
    
    # # Lấy ra thông tin chi tiết của một nhân viên 
    # @jwt_required
    # def get(self):
    #     payload = request.get_json()
    #     result  = getDetailEmployee(payload)
    #     return Response(result, mimetype="application/json", status=200)