from app.app import app 
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
from utils.blacklist import *

jwt = JWTManager()
def initialize_Security(app):
    jwt.init_app(app)
    
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}
    
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username

# Logout 
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
