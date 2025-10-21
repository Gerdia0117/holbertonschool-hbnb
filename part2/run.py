#!/usr/bin/python3
"""
Entry point for the HBnB Flask application.
"""
from part2.app.services import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
