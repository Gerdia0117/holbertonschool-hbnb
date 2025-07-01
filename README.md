# HolbertonSchool HBNB - Airbnb Clone Project

## Project Overview

This project is a comprehensive implementation of an Airbnb-like application, developed as part of the Holberton School curriculum. The project demonstrates the complete development lifecycle from basic console application to a full-stack web application with RESTful API, database integration, and web interface.

## Project Structure

The project is organized into multiple parts, each building upon the previous:

- **Part 1**: Basic console application with object-oriented programming
- **Part 2**: RESTful API development with Flask and advanced features
- **Part 3**: Database integration and data persistence
- **Part 4**: Authentication and authorization
- **Part 5**: Web interface development

## Repository Structure

```
holbertonschool-hbnb/
├── part1/              # Console application and basic models
├── part2/              # RESTful API implementation
├── part3/              # Database integration
├── part4/              # Authentication and authorization
├── part5/              # Web interface
├── app/                # Main application code
│   ├── api/            # API endpoints and routes
│   ├── models/         # Data models and business logic
│   ├── persistence/    # Data persistence layer
│   └── services/       # Business logic services
├── config.py           # Application configuration
├── run.py              # Application entry point
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Features

### Core Models
- **User**: User management and authentication
- **Place**: Property listings and management
- **Review**: User reviews and ratings
- **Amenity**: Property amenities and features

### API Endpoints
- RESTful API with full CRUD operations
- User authentication and authorization
- Place management and search functionality
- Review system with ratings
- Amenity management

### Technical Features
- Object-oriented design with proper inheritance
- RESTful API architecture
- Database integration with SQLAlchemy
- Authentication and session management
- Input validation and error handling
- Comprehensive testing suite

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/holbertonschool/holbertonschool-hbnb.git
   cd holbertonschool-hbnb
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development  # For development
   ```

## Usage

### Running the Application

**Start the Flask development server**:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

### API Usage

The API provides the following main endpoints:

- **Users**: `/api/v1/users/`
- **Places**: `/api/v1/places/`
- **Reviews**: `/api/v1/reviews/`
- **Amenities**: `/api/v1/amenities/`

#### Example API Calls

**Get all users**:
```bash
curl -X GET http://localhost:5000/api/v1/users/
```

**Create a new place**:
```bash
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Cozy Apartment", "description": "A nice place to stay"}'
```

## Development

### Project Parts

#### Part 1: Console Application
- Basic object-oriented models
- Command-line interface for data management
- File-based data persistence
- Unit testing framework

#### Part 2: RESTful API
- Flask web framework implementation
- RESTful API design and endpoints
- JSON serialization and deserialization
- Advanced error handling and validation

#### Part 3: Database Integration
- SQLAlchemy ORM integration
- Database schema design
- Migration management
- Query optimization

#### Part 4: Authentication & Authorization
- User authentication system
- Session management
- Role-based access control
- Security best practices

#### Part 5: Web Interface
- Frontend web application
- Dynamic content rendering
- User interface design
- Full-stack integration

### Code Quality
- PEP 8 compliant code style
- Comprehensive documentation
- Unit and integration testing
- Error handling and logging

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

Run tests with coverage:
```bash
python -m pytest --cov=app tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Learning Objectives

This project covers:
- Object-oriented programming in Python
- Web development with Flask
- RESTful API design and implementation
- Database design and management
- Authentication and security
- Testing and debugging
- Version control with Git
- Project documentation and maintenance

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite (development), PostgreSQL (production)
- **Testing**: pytest, unittest
- **Documentation**: Markdown, docstrings
- **Version Control**: Git

## Project Timeline

This is a multi-part project developed incrementally:
- **Part 1**: Foundation and console application
- **Part 2**: API development and advanced features
- **Part 3**: Database integration
- **Part 4**: Authentication and security
- **Part 5**: Web interface completion

## License

This project is part of the Holberton School curriculum and is for educational purposes.

## Authors

Holberton School Students - Software Engineering Program

---

*This project is part of the Holberton School curriculum and demonstrates full-stack web development skills including backend API development, database management, and frontend web development.*
