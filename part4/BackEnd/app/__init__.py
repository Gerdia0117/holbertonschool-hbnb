from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from app.extensions import bcrypt, jwt, db
from app.api.user_endpoints import api as user_ns
from app.api.amenity_endpoints import api as amenity_ns
from app.api.place_endpoints import api as place_ns
from app.api.review_endpoints import api as review_ns
from app.api.auth_endpoints import api as auth_ns
from app.api.protected_endpoints import api as protected_ns

def create_app(config_name='default'):
    """
    Application Factory pattern.
    
    Args:
        config_name (str): The configuration to use ('development', 'testing', 'production', 'default')
    
    Returns:
        Flask: The configured Flask application instance
    """
    app = Flask(__name__)
    
    # Enable CORS for front-end
    CORS(app)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # create the main API object
    api = Api(app, version="1.0", title="HBnB API",
              description="HBnB RESTful API")

    # register namespaces (not blueprints)
    api.add_namespace(auth_ns, path="/api/v1/auth")
    api.add_namespace(protected_ns, path="/api/v1/protected")
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")

    return app
