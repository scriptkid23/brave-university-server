from controllers.employeeController import EmployeesController,EmployeeController
from controllers.homeController import HomeController
from controllers.authController import *
def initialize_routes(api):
    # --------- HomeController --------

    api.add_resource(HomeController,'/')

    api.add_resource(MemberRegisterController,'/api/auth/register')
    api.add_resource(MemberLoginController,'/api/auth/login')
    api.add_resource(MemberLogoutController,'/api/auth/logout')


    api.add_resource(EmployeesController,'/api/employees')
    api.add_resource(EmployeeController,'/api/employee')