"""
Flask extensions module.
This module initializes Flask extensions to avoid circular imports.
"""
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()
