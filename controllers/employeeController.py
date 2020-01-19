from flask import Response, request
from models.employeeModel import *
from flask_restful import Resource
import json
class EmployeesController(Resource):
    def get(self):
        payload = getEmployees()
        return Response(payload, mimetype="application/json", status=200)

      
class EmployeeController(Resource):
    def post(self):
        payload = request.get_json()
        createEmloyee(payload)
        return Response(json.dumps({"code" : 200,"status" :"insert employee sucesss"}),mimetype="application/json",status=200)
    def put(self):
        payload = request.get_json()
        updateEmployee(payload)
        return Response(json.dumps({"code" : 200,"status" :"update employee sucesss"}),mimetype="application/json",status=200)
    def delete(self):
        payload = request.get_json()
        deleteEmployee(payload)
        return Response(json.dumps({"code" : 200,"status" :"delete employee sucesss"}),mimetype="application/json",status=200)

    def get(self):
        payload = request.get_json()
        result  = getDetailEmployee(payload)
        return Response(result, mimetype="application/json", status=200)