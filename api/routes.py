from controllers.employeeController import EmployeesController,EmployeeController
from controllers.homeController import HomeController
def initialize_routes(api):
    # --------- HomeController --------

    api.add_resource(HomeController,'/')

    
    api.add_resource(EmployeesController,'/api/employees')
    api.add_resource(EmployeeController,'/api/employee')