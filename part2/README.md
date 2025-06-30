# HBnB Application - Backend System

![Project Architecture](https://i.imgur.com/JK9yX2C.png)

A RESTful API for a vacation rental platform (like Airbnb) built with Python, Flask, and Flask-RESTx.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Core Features](#core-features)
3. [Models](#models)
4. [API Endpoints](#api-endpoints)
5. [Setup Instructions](#setup-instructions)
6. [Testing](#testing)
7. [Future Improvements](#future-improvements)

## Project Structure

## Core Features

- **User Management**: Registration, profiles, authentication
- **Property Listings**: Create/update rental properties with geo-coordinates
- **Amenities**: Manage property features (WiFi, Pool, etc.)
- **Reviews**: Rating system with text comments
- **In-Memory Database**: Temporary storage (will be replaced with SQLAlchemy)

## Models

### Base Model (`base_model.py`)
```python
class BaseModel:
    # Shared attributes:
    # - id (UUID)
    # - created_at (timestamp)
    # - updated_at (timestamp)
    # - save() method

class User(BaseModel):
    # Attributes:
    # - first_name
    # - last_name
    # - email
    # - password (plaintext - will be hashed later)
    # - owned_places (list)

class Property(BaseModel):
    # Attributes:
    # - title
    # - description
    # - price
    # - latitude/longitude
    # - host (User)
    # - amenities (list)
    # - reviews (list)

API Endpoints
Users (/api/v1/users)
Method	Path	Description
GET	/	List all users
POST	/	Create new user
GET	/<user_id>	Get user details
PUT	/<user_id>	Update user
Properties (/api/v1/properties)
Method	Path	Description
GET	/	List all properties
POST	/	Add new property
GET	/<property_id>	Get property details
PUT	/<property_id>	Update property
Amenities (/api/v1/amenities)
Method	Path	Description
GET	/	List all amenities
POST	/	Add new amenity

Setup Instructions

    Install dependencies:
    pip install flask flask-restx

    Run the application:
    export FLASK_APP=app
    flask run

Access the API:
http://localhost:5000/api/v1/users

Testing

Example test cases are included in the endpoint files. To test:

# Sample user creation
curl -X POST http://localhost:5000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John", "last_name":"Doe", "email":"john@example.com"}'

Future Improvements

    Database Integration: Replace in-memory storage with SQLAlchemy

    Authentication: Add JWT token support

    Image Uploads: Property photo management

    Search: Filter properties by location/price

    Pagination: For large result sets

Project Status

✅ Core Models Implemented
✅ Basic API Endpoints
✅ In-Memory Storage
🔜 Database Integration
🔜 User Authentication
