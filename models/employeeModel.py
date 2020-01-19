from config.configDB import db
from datetime import datetime
from utils.createID import encodedID
import json 

# Định nghĩa đối tượng collection trong MongoDB 
class Employee(db.Document):
    employee_id = db.StringField(required=True, unique=True)
    employee_name = db.StringField(max_length=255, required=True)
    employee_gender = db.BooleanField(required=True)
    employee_birthday = db.DateTimeField(required=True)
    employee_avatar = db.StringField()
    def json(self):
        employee_dict = {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "employee_gender": self.employee_gender,
            "employee_birthday": self.employee_birthday,
            "employee_avatar": self.employee_avatar,

        }
        return json.dumps(employee_dict)
    def get_id(self):
        return unicode(self.employee_id)
    
def createEmloyee(payload):
    newEmployee = Employee(
        employee_id=encodedID(payload["employee_name"]),
        employee_name=payload["employee_name"],
        employee_gender=payload["employee_gender"],
        employee_birthday=payload["employee_birthday"],
        employee_avatar=payload["employee_avatar"],
    )
    newEmployee.save()


# Sau khi đã có đối tượng, ta sẽ thao tác với đối tượng đó 
def getEmployees():
    return Employee.objects().to_json()

# def updateEmployee(self,payload):
#     pass #
def deleteEmployee(payload):
    id_ =  Employee.objects.get(employee_id = payload['id']).delete()
    return id_ 
def getDetailEmployee(payload):
    result = Employee.objects.get(employee_id = payload['id']).to_json()
    return result
def updateEmployee(payload): 
    result = Employee.objects.get(employee_id = payload["id"]).update(**payload["data"])
    return result