#!/usr/bin/python3
"""
Entry point for the HBnB Flask application.
"""
from app import create_app
import os

# Get configuration from environment variable, default to 'development'
config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == "__main__":
    app.run(debug=True)
