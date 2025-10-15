from flask import Flask
from flask_restx import Api
from app.api.user_endpoints import api as user_ns  # ⬅️ Import your user routes


def create_app():
    """App factory for the HBnB Flask application."""
    app = Flask(__name__)

    # Create the main API object
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Part 2 REST API"
    )

    # Register the user namespace (group of routes)
    # This means all user routes will be under /api/v1/users
    api.add_namespace(user_ns, path="/api/v1/users")

    return app
