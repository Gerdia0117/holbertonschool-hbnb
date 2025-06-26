from flask_restx import Api
from flask import Blueprint

from .user_namespace import api as user_ns

api_blueprint = Blueprint('v1_api', __name__, url_prefix='/api/v1')
rest_api = Api(api_blueprint,
               version='1.0',
               title='HBnB Application API',
               description='API for managing users, places, reviews, and more for the HBnB platform')

rest_api.add_namespace(user_ns, path='/users')
