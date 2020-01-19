from flask_mongoengine import MongoEngine


# db = MongoEngine.connection(db= database.default["DATABASE"],
#                         username=database.default["USERNAME"],
#                         password=database.default["PASSWORD"],
#                         host= database.default["HOST"],
#                         port= database.default["PORT"],
#                         authentication_source=database.default["AUTHENTICATION_SOURCE"],
#                 )
db = MongoEngine() 


def initialize_db(app):
        db.init_app(app)
