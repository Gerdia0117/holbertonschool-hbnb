# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.api.user_endpoints import api as user_ns


def create_app():
    """Application factory"""
    app = Flask(__name__)
    api = Api(app, version="1.0", title="HBnB API",
              description="HBnB User Management API")

    # Register namespaces
    api.add_namespace(user_ns, path="/api/v1/users")

    return app
