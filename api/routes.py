from controllers.employeeController import EmployeesController,EmployeeController

def initialize_routes(api):
    api.add_resource(EmployeesController,'/api/employees')
    api.add_resource(EmployeeController,'/api/employee')