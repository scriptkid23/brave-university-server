from flask import Response, request
from models.employeeModel import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

import json
# Lấy ra tất cả danh sách nhân viên 
class EmployeesController(Resource): 
    @jwt_required
    def get(self):

        payload = getEmployees()
        # print(get_jwt_identity()) // lấy employee_id 
        return Response(payload, mimetype="application/json", status=200)

      
class EmployeeController(Resource):
    # Tạo 1 nhân viên 
    @jwt_required
    def post(self):
        payload = request.get_json()
        createEmloyee(payload)
        return Response(json.dumps({"code" : 200,"status" :"insert employee sucesss"}),mimetype="application/json",status=200)
    
    # cập nhật thông tin của một nhân viên 
    @jwt_required
    def put(self):
        payload = request.get_json()
        updateEmployee(payload)
        return Response(json.dumps({"code" : 200,"status" :"update employee sucesss"}),mimetype="application/json",status=200)
    
    # Xoá một nhân viên 
    @jwt_required
    def delete(self):
        payload = request.get_json()
        deleteEmployee(payload)
        return Response(json.dumps({"code" : 200,"status" :"delete employee sucesss"}),mimetype="application/json",status=200)
    
    # Lấy ra thông tin chi tiết của một nhân viên 
    @jwt_required
    def get(self):
        payload = request.get_json()
        result  = getDetailEmployee(payload)
        return Response(result, mimetype="application/json", status=200)