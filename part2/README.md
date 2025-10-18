# HBnB Evolution - Part 2: Business Logic and API Implementation

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![Tests](https://img.shields.io/badge/tests-11%2F11%20passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Development](#development)
- [Contributing](#contributing)

## 🏠 Overview

HBnB Evolution Part 2 is a RESTful API application built with Flask and Flask-RESTx that implements the core business logic for a property rental platform similar to Airbnb. This part focuses on implementing the Presentation and Business Logic layers, providing a solid foundation for user, place, amenity, and review management.

### 🎯 Project Objectives

- **Modular Architecture**: Implement a clean separation of concerns across multiple layers
- **RESTful API Design**: Create well-documented, scalable API endpoints using Flask-RESTx
- **Business Logic Implementation**: Translate documented designs into working, maintainable code
- **Data Relationships**: Handle complex entity relationships and data serialization
- **Testing & Validation**: Ensure robust functionality through comprehensive testing

## ✨ Features

### Core Functionality
- 👥 **User Management**: Create, read, and update user profiles
- 🏡 **Place Management**: Full CRUD operations for property listings
- 🎯 **Amenity System**: Manage property amenities and features
- ⭐ **Review System**: Complete review management with CRUD operations
- 🔄 **Entity Relationships**: Seamless handling of related data

### Technical Features
- 🛡️ **Input Validation**: Comprehensive data validation and error handling
- 📚 **API Documentation**: Auto-generated Swagger/OpenAPI documentation
- 🏗️ **Facade Pattern**: Simplified communication between architectural layers
- 💾 **In-Memory Storage**: Efficient temporary data persistence
- 🧪 **Test Coverage**: Complete test suite with 11/11 passing tests

## 🏛️ Architecture

The application follows a layered architecture pattern:

```
┌─────────────────────────────────────┐
│         Presentation Layer          │
│    (Flask-RESTx API Endpoints)      │
├─────────────────────────────────────┤
│        Business Logic Layer        │
│     (Facade + Core Models)          │
├─────────────────────────────────────┤
│        Persistence Layer           │
│     (In-Memory Repository)          │
└─────────────────────────────────────┘
```

### Design Patterns
- **Facade Pattern**: Simplifies complex subsystem interactions
- **Repository Pattern**: Abstracts data access logic
- **Singleton Pattern**: Ensures shared state across API endpoints

## 📁 Project Structure

```
part2/
├── app/
│   ├── __init__.py              # Flask application factory
│   ├── api/                     # Presentation Layer
│   │   ├── __init__.py
│   │   ├── user_endpoints.py     # User API endpoints
│   │   ├── place_endpoints.py    # Place API endpoints
│   │   ├── amenity_endpoints.py  # Amenity API endpoints
│   │   └── review_endpoints.py   # Review API endpoints
│   ├── business/                # Business Logic Layer
│   │   ├── __init__.py
│   │   └── facade.py            # Facade pattern implementation
│   ├── models/                  # Core Business Models
│   │   ├── __init__.py
│   │   ├── base_model.py        # Base model with common attributes
│   │   ├── user.py              # User entity model
│   │   ├── place.py             # Place entity model
│   │   ├── amenity.py           # Amenity entity model
│   │   └── review.py            # Review entity model
│   ├── persistence/             # Persistence Layer
│   │   ├── __init__.py
│   │   ├── repository_interface.py
│   │   └── memory_repository.py  # In-memory data storage
│   └── services/                # Service Layer
│       ├── __init__.py
│       └── storage_service.py
├── tests/
│   └── test_api.py              # Comprehensive API test suite
├── run.py                       # Application entry point
└── README.md                    # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.12+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/holbertonschool/holbertonschool-hbnb.git
   cd holbertonschool-hbnb/part2
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-restx
   ```

4. **Verify installation**
   ```bash
   python3 run.py
   ```

## 💻 Usage

### Starting the Application

```bash
python3 run.py
```

The API will be available at `http://localhost:5000`

### API Documentation

Access the interactive Swagger documentation at:
```
http://localhost:5000
```

### Example API Calls

#### Create a User
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

#### Get All Places
```bash
curl -X GET http://localhost:5000/api/v1/places/
```

#### Create a Review
```bash
curl -X POST http://localhost:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Great place!", "user_id": "user-id", "place_id": "place-id"}'
```

## 🔌 API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/users/` | Create a new user |
| GET | `/api/v1/users/` | Get all users |
| GET | `/api/v1/users/{id}` | Get user by ID |
| PUT | `/api/v1/users/{id}` | Update user |

### Places
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/places/` | Create a new place |
| GET | `/api/v1/places/` | Get all places |
| GET | `/api/v1/places/{id}` | Get place by ID |
| PUT | `/api/v1/places/{id}` | Update place |

### Amenities
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/amenities/` | Create a new amenity |
| GET | `/api/v1/amenities/` | Get all amenities |
| GET | `/api/v1/amenities/{id}` | Get amenity by ID |
| PUT | `/api/v1/amenities/{id}` | Update amenity |

### Reviews
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/reviews/` | Create a new review |
| GET | `/api/v1/reviews/{id}` | Get review by ID |
| PUT | `/api/v1/reviews/{id}` | Update review |
| DELETE | `/api/v1/reviews/{id}` | Delete review |
| GET | `/api/v1/reviews/place/{place_id}` | Get reviews for a place |

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python3 -m unittest tests.test_api -v

# Run specific test
python3 -m unittest tests.test_api.TestHBnBAPI.test_1_create_user -v
```

### Test Coverage
The test suite covers:
- ✅ User creation, retrieval, and updates
- ✅ Place management with owner validation
- ✅ Amenity CRUD operations
- ✅ Review lifecycle including deletion
- ✅ Entity relationships and data integrity
- ✅ Error handling and edge cases

**Current Status: 11/11 tests passing** ✨

### Manual Testing with cURL

Test scripts and examples are available in the `tests/` directory for comprehensive API validation.

## 👨‍💻 Development

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Include docstrings for classes and methods
- Maintain consistent error handling patterns

### Development Workflow
1. Create feature branch from main
2. Implement changes with tests
3. Run full test suite
4. Update documentation as needed
5. Submit pull request

### Key Implementation Details
- **Singleton Facade**: Ensures consistent state across API endpoints
- **Input Validation**: Comprehensive validation in business logic layer
- **Error Handling**: Consistent HTTP status codes and error messages
- **Relationship Management**: Proper handling of entity associations

## 📚 Learning Outcomes

This project demonstrates:
- **Modular Design**: Clean separation of concerns across architectural layers
- **API Development**: RESTful API design with Flask and Flask-RESTx
- **Business Logic Implementation**: Translation of requirements into working code
- **Data Modeling**: Entity relationships and data serialization
- **Testing Practices**: Comprehensive testing strategies and validation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is part of the Holberton School curriculum. All rights reserved.

## 🙏 Acknowledgments

- Holberton School for the project framework and guidance
- Flask and Flask-RESTx communities for excellent documentation
- Contributors and reviewers who helped improve this implementation

---

**Part of the HBnB Evolution Project Series**
- Part 1: UML Design and Documentation
- **Part 2: Business Logic and API Implementation** (Current)
- Part 3: Authentication, Authorization, and Database Integration (Coming Next)
- Part 4: Frontend Integration and Deployment