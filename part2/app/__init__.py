from flask import Flask
from flask_restx import Api
from app.api.user_endpoints import api as user_ns
from app.api.amenity_endpoints import api as amenity_ns

def create_app():
    app = Flask(__name__)

    # create the main API object
    api = Api(app, version="1.0", title="HBnB API",
              description="HBnB RESTful API")

    # register namespaces (not blueprints)
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")

    return app
