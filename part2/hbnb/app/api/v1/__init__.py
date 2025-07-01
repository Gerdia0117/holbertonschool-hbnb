from flask_restx import Api
from flask import Blueprint

from .users import api as users_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, version='1.0', title='HBnB API',
    description='API for HBnB app')

from .amenities import api as amenities_ns
api.add_namespace(amenities_ns, path='/amenities')

# Register namespaces
api.add_namespace(users_ns, path='/users')
