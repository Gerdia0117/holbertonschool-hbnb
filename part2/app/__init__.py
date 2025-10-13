from flask import Flask
from flask_restx import Api

def create_app():
    """Factory function for Flask app"""
    app = Flask(__name__)

    # Initialize Flask-RESTx API
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Business Logic & API Endpoints",
    )

    # Register namespaces later (e.g., from app.api.users)
    # from app.api.users import ns as users_ns
    # api.add_namespace(users_ns)

    return app
