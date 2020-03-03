# class InternalServerError(Exception):
#     pass

# class SchemaValidationError(Exception):
#     pass

# class MemberAlreadyExistsError(Exception):
#     pass

# class UpdatingMovieError(Exception):
#     pass

# class DeletingMovieError(Exception):
#     pass

# class MovieNotExistsError(Exception):
#     pass

# class EmailAlreadyExistsError(Exception):
#     pass

class LimitedError(Exception):
    pass



errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    
     "ValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "MemberAlreadyExistsError": {
         "message": "Member with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "MemberNotExistsError": {
         "message": "Member with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },

    #  Role 
    "DuplicateRole" : {
        "message" : "Role with given name already exists",
        "status" : 400
    }
}