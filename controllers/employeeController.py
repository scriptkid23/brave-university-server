from flask import Response, request
from models.employeeModel import *
from flask_restful import Resource

class EmployeesController(Resource):
    def get(self):
        payload = getEmployees()
        return Response(payload, mimetype="application/json", status=200)

    # def post(self):
    #     body = request.get_json()
    #     movie =  Movie(**body).save()
    #     id = movie.id
    #     return {'id': str(id)}, 200
        
class EmployeeController(Resource):
    def post(self):
        print(request.get_json())
        return Response("insert employee sucesss",mimetype="application/json",status=200)
#     def put(self, id):
#         body = request.get_json()
#         Movie.objects.get(id=id).update(**body)
#         return '', 200
    
#     def delete(self, id):
#         movie = Movie.objects.get(id=id).delete()
#         return '', 200

#     def get(self, id):
#         movies = Movie.objects.get(id=id).to_json()
#         return Response(movies, mimetype="application/json", status=200)