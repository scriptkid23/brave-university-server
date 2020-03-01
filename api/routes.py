from controllers.employeeController import EmployeesController,EmployeeController
from controllers.homeController import HomeController
from controllers.authController import *
from controllers.roleController import *
from controllers.uploadController import *
from controllers.scoreController import *
from controllers.chatController import *
from controllers.bookingRoomController import *
def initialize_routes(api):
    # --------- HomeController --------

    # api.add_resource(HomeController,'/')

    api.add_resource(MemberRegisterController,'/api/auth/register')
    api.add_resource(MemberLoginController,'/api/auth/login')
    api.add_resource(MemberLogoutController,'/api/auth/logout')

    # Get Member detail

    api.add_resource(MemberGetDetailController,'/api/member/detail')
    api.add_resource(EmployeesController,'/api/employees')
    api.add_resource(EmployeeController,'/api/employee')
    api.add_resource(MemberUpdateProfile,'/api/member/update')

    # Get Role

    api.add_resource(RoleController,'/api/role')

    # Upload file

    api.add_resource(UploadImageController,'/api/upload')

    # Score

    api.add_resource(ScoreController,'/api/score')
    api.add_resource(UploadScoreController,'/api/score/upload')

    api.add_resource(GetListRankController,'/api/rank/list')
    api.add_resource(GetListRankTimeLineController,'/api/rank/time-line')


    # Chat 
    api.add_resource(ChatController,'/api/chat')

    # Booking 
    api.add_resource(BookingRoomController,'/api/booking/create')
    api.add_resource(GetListBookingRoomController,'/api/booking/get')
    api.add_resource(UpdateBookingRoomController,'/api/booking/update')
