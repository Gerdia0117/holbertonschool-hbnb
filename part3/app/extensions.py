"""
Flask extensions module.
This module initializes Flask extensions to avoid circular imports.
"""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
