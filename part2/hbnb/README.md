# HBnB - Holberton School AirBnB Clone (Part 2)

## Overview

This is Part 2 of the HBnB project - a Flask-based REST API for an AirBnB clone application. The application provides a comprehensive API for managing users, places, amenities, and reviews with full documentation and testing suite.

## Features

- **RESTful API** with Flask and Flask-RestX
- **Interactive API Documentation** with Swagger UI
- **Comprehensive Data Models** (Users, Places, Amenities, Reviews)
- **Input Validation** and error handling
- **Complete Test Suite** with multiple testing approaches
- **Modular Architecture** with clear separation of concerns

## Project Structure

```
hbnb/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── api/
│   │   ├── __init__.py          # API blueprint setup
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py         # Users API endpoints
│   │       ├── amenities.py     # Amenities API endpoints
│   │       ├── places.py        # Places API endpoints
│   │       └── reviews.py       # Reviews API endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py        # Base model class
│   │   ├── user.py              # User model
│   │   ├── amenity.py           # Amenity model
│   │   ├── places.py            # Place model
│   │   └── review.py            # Review model
│   ├── persistence/
│   │   └── repository.py        # Data persistence layer
│   └── services/
│       ├── __init__.py
│       └── facade.py            # Business logic facade
├── tests/                       # Pytest test suite
├── config.py                    # Application configuration
├── run.py                       # Application entry point
├── test_simple.py              # Simple unittest suite
├── test_complete.py            # Comprehensive test suite
└── requirements.txt            # Project dependencies
```

## Quick Start

### 1. Setup Environment

```bash
# Navigate to project directory
cd /home/holberton/holbertonschool-hbnb/part2/hbnb

# Activate virtual environment
source test/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt
```

### 2. Run the Application

```bash
# Start the Flask development server
python3 run.py
```

The application will be available at:
- **API Base URL**: http://localhost:5000/api/v1/
- **Interactive Documentation**: http://localhost:5000/api/v1/
- **API Specification**: http://localhost:5000/api/v1/swagger.json

### 3. API Endpoints

#### Users API
- `GET /api/v1/users/` - List all users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

#### Amenities API
- `GET /api/v1/amenities/` - List all amenities
- `POST /api/v1/amenities/` - Create a new amenity
- `GET /api/v1/amenities/{id}` - Get amenity by ID
- `PUT /api/v1/amenities/{id}` - Update amenity

#### Places API
- `GET /api/v1/places/` - List all places
- `POST /api/v1/places/` - Create a new place
- `GET /api/v1/places/{id}` - Get place by ID
- `PUT /api/v1/places/{id}` - Update place

#### Reviews API
- `GET /api/v1/reviews/` - List all reviews
- `POST /api/v1/reviews/` - Create a new review
- `GET /api/v1/reviews/{id}` - Get review by ID
- `PUT /api/v1/reviews/{id}` - Update review

## API Usage Examples

### Create a User
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword123"
  }'
```

### Create an Amenity
```bash
curl -X POST http://localhost:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "WiFi"
  }'
```

### Get All Users
```bash
curl -X GET http://localhost:5000/api/v1/users/
```

---

# Testing Suite

## Overview

This project includes a comprehensive test suite that verifies all API endpoints, error handling, data validation, and complete workflows. The tests are designed to ensure the reliability and correctness of the HBnB Flask application.

## Test Files

### 1. `test_simple.py` 
- **Purpose**: Basic test suite using Python's built-in `unittest`
- **Dependencies**: None (uses standard library only)
- **Features**: Tests basic functionality and endpoints
- **Best for**: Quick validation and CI/CD pipelines

### 2. `test_complete.py`
- **Purpose**: Comprehensive test suite with detailed output
- **Dependencies**: None (uses standard library only)  
- **Features**: Full API testing with visual progress indicators
- **Best for**: Development and thorough testing

### 3. `tests/test_app.py`
- **Purpose**: Advanced test suite using pytest framework
- **Dependencies**: pytest, pytest-flask (see `requirements-test.txt`)
- **Features**: Advanced testing features and better reporting
- **Best for**: Professional testing environments

## Running Tests

### Quick Test (Simple)
```bash
# Activate virtual environment
source test/bin/activate

# Run basic tests
python3 test_simple.py
```

### Comprehensive Test (Recommended)
```bash
# Activate virtual environment  
source test/bin/activate

# Run comprehensive tests with detailed output
python3 test_complete.py
```

### Advanced Testing with Pytest
```bash
# Activate virtual environment
source test/bin/activate

# Install test dependencies
pip install -r requirements-test.txt

# Run pytest tests
pytest tests/test_app.py -v

# Run with coverage
pytest tests/test_app.py --cov=app --cov-report=html
```

## What Gets Tested

### ✅ App Functionality
- Flask application creation and configuration
- Blueprint registration (API and documentation)
- Route registration and HTTP methods

### ✅ API Endpoints
- **Users API** (`/api/v1/users/`)
  - GET: List all users
  - POST: Create new user (with password validation)
  - GET by ID: Retrieve specific user
  - PUT by ID: Update user
  - DELETE by ID: Remove user

- **Amenities API** (`/api/v1/amenities/`)
  - GET: List all amenities
  - POST: Create new amenity (with name validation)
  - GET by ID: Retrieve specific amenity
  - PUT by ID: Update amenity

### ✅ Documentation
- Swagger UI accessibility (`/api/v1/`)
- Swagger JSON specification (`/api/v1/swagger.json`)
- API documentation completeness

### ✅ Error Handling
- 404 errors for non-existent resources
- 405 errors for unsupported HTTP methods
- 400/422 errors for invalid data
- JSON parsing error handling

### ✅ Data Validation
- Required field validation (password for users, name for amenities)
- Email format validation
- Data type validation

### ✅ Workflows
- Complete user management lifecycle
- API documentation workflow
- Error scenario handling

## Test Results Example

```
🧪 HBnB Flask Application - Comprehensive Test Suite
======================================================================

✅ All tests passed successfully!
📊 Total tests run: 15

🚀 Your HBnB Flask application is working perfectly!

📋 What was tested:
  ✅ Flask app creation and configuration
  ✅ API blueprint registration
  ✅ Swagger UI and documentation
  ✅ Users API endpoints (GET, POST)
  ✅ Amenities API endpoints (GET, POST)
  ✅ Error handling (404, 405, 400)
  ✅ Route registration and HTTP methods
  ✅ Data validation
  ✅ Complete API workflows
```

## Required Data Formats

### Users API
```json
{
  "first_name": "John",
  "last_name": "Doe", 
  "email": "john.doe@example.com",
  "password": "password123"  // Required!
}
```

### Amenities API
```json
{
  "name": "WiFi"  // Required!
}
```

## Expected API Responses

### Success Responses
- **201**: Resource created successfully
- **200**: Request successful
- **200**: List retrieved successfully

### Error Responses  
- **400**: Bad request (missing required fields)
- **404**: Resource not found
- **405**: Method not allowed
- **422**: Unprocessable entity (validation errors)

---

# Development

## Dependencies

### Core Dependencies
- **Flask**: Web framework
- **Flask-RestX**: REST API extension with Swagger integration
- **Werkzeug**: WSGI utility library

### Testing Dependencies
- **pytest**: Advanced testing framework
- **pytest-flask**: Flask-specific testing utilities
- **coverage**: Code coverage reporting

## Architecture

### Design Patterns
- **Factory Pattern**: For Flask app creation
- **Repository Pattern**: For data persistence
- **Facade Pattern**: For business logic encapsulation

### Key Components
- **Models**: Data representation and validation
- **API**: RESTful endpoints with Swagger documentation
- **Services**: Business logic and data processing
- **Persistence**: Data storage and retrieval

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the test suite: `python3 test_complete.py`
5. Ensure all tests pass
6. Submit a pull request

## Troubleshooting

### Common Issues

1. **Virtual Environment Not Found**
   ```bash
   # Make sure you're in the right directory
   cd /home/holberton/holbertonschool-hbnb/part2/hbnb
   
   # Check for virtual environment
   ls -la | grep test
   
   # Activate the correct environment
   source test/bin/activate
   ```

2. **Import Errors**
   ```bash
   # Ensure you're in the project root directory
   pwd
   # Should be: /home/holberton/holbertonschool-hbnb/part2/hbnb
   
   # Check that app module exists
   python3 -c "from app import create_app; print('✅ Import successful')"
   ```

3. **Port Already in Use**
   ```bash
   # Find and kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   
   # Or use a different port
   python3 -c "
   from app import create_app
   app = create_app()
   app.run(host='0.0.0.0', port=5001, debug=True)
   "
   ```

## License

This project is part of the Holberton School curriculum.

## Authors

- Holberton School Student
- Project developed as part of the AirBnB clone series

---

**Happy Coding!** 🚀✨
