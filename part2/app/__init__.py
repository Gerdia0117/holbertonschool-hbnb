from flask import Flask
from app.api.user_endpoints import api as user_ns

def create_app():
    app = Flask(__name__)

    # Register API namespaces
    app.register_blueprint(user_ns, url_prefix="/api/v1")

    return app
