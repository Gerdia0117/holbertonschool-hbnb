from flask import Flask
from flask_restx import Api
from app.api.user_endpoints import api as user_ns
from app.api.amenity_endpoints import api as amenity_ns
from app.api.place_endpoints import api as place_ns
from app.api.review_endpoints import api as review_ns

def create_app(config_name='default'):
    """
    Application Factory pattern.
    
    Args:
        config_name (str): The configuration to use ('development', 'testing', 'production', 'default')
    
    Returns:
        Flask: The configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])

    # create the main API object
    api = Api(app, version="1.0", title="HBnB API",
              description="HBnB RESTful API")

    # register namespaces (not blueprints)
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")

    return app
