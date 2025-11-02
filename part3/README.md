# HBnB Evolution - Part 3: Authentication, Authorization & Database Persistence

## 📋 Table of Contents
- [Overview](#overview)
- [Features Implemented](#features-implemented)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Authentication & Authorization](#authentication--authorization)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Architecture](#architecture)
- [SQL Scripts](#sql-scripts)
- [Testing](#testing)
- [Project Structure](#project-structure)

---

## Overview

Part 3 transforms the HBnB API into a production-ready application with:
- **Secure Authentication** using JWT tokens
- **Role-Based Access Control** (admin vs regular users)
- **Database Persistence** with SQLAlchemy ORM
- **Password Security** with bcrypt hashing
- **Ownership-Based Authorization** for resources
- **Raw SQL Scripts** for schema and data management

---

## Features Implemented

### ✅ Task 0: Application Factory & Configuration
- Implemented Flask Application Factory pattern
- Configuration system with development/testing/production environments
- Environment-based settings (SECRET_KEY, DATABASE_URI, JWT config)

### ✅ Task 1: Password Hashing (Bcrypt)
- User model with secure password storage
- Bcrypt integration for password hashing
- `hash_password()` and `verify_password()` methods
- Passwords excluded from API responses

### ✅ Task 2: JWT Authentication
- Login endpoint (`POST /api/v1/auth/login`)
- JWT token generation with user claims (user_id, is_admin)
- Protected endpoints using `@jwt_required()` decorator
- Token expiration (1 hour)

### ✅ Task 3: Authenticated User Access
- Place creation/update requires authentication and ownership
- Review creation/update/delete requires authentication and ownership
- User profile updates require authentication (self-only)
- Ownership validation and restrictions
- Prevention of self-reviews and duplicate reviews

### ✅ Task 4: Administrator Access
- Admin-only endpoints for amenity management
- Admins can bypass ownership restrictions
- Admins can manage any user (email, password, is_admin status)
- Role-based authorization with `@admin_required()` decorator

### ✅ Task 5: SQLAlchemy Repository Implementation
- Repository pattern with factory
- Generic `SQLAlchemyRepository` base class
- Entity-specific repositories (User, Place, Review, Amenity)
- Database configuration and initialization

### ✅ Task 6: User Entity Mapping
- User model mapped to SQLAlchemy
- `UserRepository` with email lookup
- Password hashing integrated with ORM
- Database initialization script

### ✅ Task 7: Place, Review, Amenity Mapping
- All entities mapped to SQLAlchemy models
- Specific repositories for each entity
- CRUD operations via repositories
- Facade updated to use repositories

### ✅ Task 8: Entity Relationships
- User ↔ Place (one-to-many)
- User ↔ Review (one-to-many)
- Place ↔ Review (one-to-many with cascade delete)
- Place ↔ Amenity (many-to-many via association table)
- Foreign key constraints with CASCADE

### ✅ Task 9: SQL Scripts
- `schema.sql` - Complete database schema
- `seed.sql` - Initial data (admin user, amenities)
- `data.sql` - Sample test data
- Comprehensive SQL documentation

---

## Getting Started

### Prerequisites
- Python 3.12+
- pip
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/holbertonschool-hbnb.git
cd holbertonschool-hbnb/part3

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python3 init_db.py
```

### Running the Application

```bash
# Development mode
export FLASK_ENV=development
python3 run.py

# The API will be available at http://localhost:5000
```

---

## Configuration

Configuration is managed in `config.py` with environment-specific settings:

### Development Config
- `DEBUG = True`
- SQLite database: `sqlite:///hbnb_dev.db`

### Testing Config
- `TESTING = True`
- In-memory database: `sqlite:///:memory:`

### Production Config
- `DEBUG = False`
- Database from environment variable

### Key Settings
- `SECRET_KEY` - Flask secret key
- `JWT_SECRET_KEY` - JWT signing key
- `JWT_ACCESS_TOKEN_EXPIRES` - Token lifetime (3600s = 1 hour)
- `SQLALCHEMY_DATABASE_URI` - Database connection string
- `SQLALCHEMY_TRACK_MODIFICATIONS = False`

---

## Authentication & Authorization

### Login Flow
1. User registers via `POST /api/v1/users/`
2. User logs in via `POST /api/v1/auth/login`
3. Server returns JWT token with claims
4. Client includes token in subsequent requests: `Authorization: Bearer <token>`

### JWT Claims
- `identity` - User ID
- `is_admin` - Boolean admin flag

### Access Levels

| Action | Public | Authenticated | Owner | Admin |
|--------|--------|---------------|-------|-------|
| View users/places/reviews | ✅ | ✅ | ✅ | ✅ |
| Create user | ✅ | ✅ | ✅ | ✅ |
| Create place | ❌ | ✅ | ✅ | ✅ |
| Update own place | ❌ | ❌ | ✅ | ✅ |
| Update any place | ❌ | ❌ | ❌ | ✅ |
| Create review | ❌ | ✅ | ✅ | ✅ |
| Update own review | ❌ | ❌ | ✅ | ✅ |
| Update any review | ❌ | ❌ | ❌ | ✅ |
| Create amenity | ❌ | ❌ | ❌ | ✅ |
| Update amenity | ❌ | ❌ | ❌ | ✅ |

---

## API Endpoints

### Authentication
```
POST   /api/v1/auth/login          Login and get JWT token
```

### Users
```
GET    /api/v1/users/              List all users (public)
POST   /api/v1/users/              Create user (public)
GET    /api/v1/users/<id>          Get user details (public)
PUT    /api/v1/users/<id>          Update user (auth: self or admin)
```

### Places
```
GET    /api/v1/places/             List all places (public)
POST   /api/v1/places/             Create place (auth required)
GET    /api/v1/places/<id>         Get place details (public)
PUT    /api/v1/places/<id>         Update place (auth: owner or admin)
```

### Reviews
```
GET    /api/v1/reviews/            List all reviews (public)
POST   /api/v1/reviews/            Create review (auth required)
GET    /api/v1/reviews/<id>        Get review details (public)
PUT    /api/v1/reviews/<id>        Update review (auth: author or admin)
DELETE /api/v1/reviews/<id>        Delete review (auth: author or admin)
GET    /api/v1/reviews/place/<id>  Get reviews for place (public)
```

### Amenities
```
GET    /api/v1/amenities/          List all amenities (public)
POST   /api/v1/amenities/          Create amenity (admin only)
GET    /api/v1/amenities/<id>      Get amenity details (public)
PUT    /api/v1/amenities/<id>      Update amenity (admin only)
```

### Protected Examples
```
GET    /api/v1/protected/test      Test protected endpoint (auth required)
GET    /api/v1/protected/admin-only Test admin endpoint (admin only)
```

---

## Database

### Models

#### BaseModel (Abstract)
- `id` (UUID, Primary Key)
- `created_at` (DateTime)
- `updated_at` (DateTime)

#### User
- `first_name` (String 50)
- `last_name` (String 50)
- `email` (String 120, Unique)
- `password` (String 255, Hashed)
- `is_admin` (Boolean)

#### Place
- `name` (String 100)
- `description` (String 500)
- `city` (String 50)
- `price` (Float)
- `latitude` (Float)
- `longitude` (Float)
- `owner_id` (Foreign Key → User)

#### Review
- `text` (String 500)
- `rating` (Integer)
- `user_id` (Foreign Key → User)
- `place_id` (Foreign Key → Place)

#### Amenity
- `name` (String 50, Unique)

### Relationships

```
User ──1:N──→ Place          (User.places ↔ Place.owner)
User ──1:N──→ Review         (User.reviews ↔ Review.user)
Place ──1:N──→ Review        (Place.reviews ↔ Review.place)
Place ──M:N──→ Amenity       (via place_amenity table)
```

### Database Initialization

```bash
# Using Python script (recommended)
python3 init_db.py

# Using SQL scripts (alternative)
cd sql/
sqlite3 hbnb.db < schema.sql
sqlite3 hbnb.db < seed.sql
sqlite3 hbnb.db < data.sql  # Optional sample data
```

---

## Architecture

### Repository Pattern
```
┌─────────────────┐
│   API Layer     │  Flask-RESTX endpoints
└────────┬────────┘
         │
┌────────▼────────┐
│     Facade      │  Business logic orchestration
└────────┬────────┘
         │
┌────────▼────────┐
│  Repositories   │  Data access layer
└────────┬────────┘
         │
┌────────▼────────┐
│  SQLAlchemy     │  ORM & Database
└─────────────────┘
```

### Key Components

- **Extensions** (`app/extensions.py`) - Flask extensions (bcrypt, jwt, db)
- **Models** (`app/models/`) - SQLAlchemy ORM models
- **Repositories** (`app/persistence/`) - Data access layer
- **Facade** (`app/business/facade.py`) - Business logic
- **API** (`app/api/`) - REST endpoints
- **Utils** (`app/utils/auth.py`) - Authorization helpers

---

## SQL Scripts

Located in `sql/` directory:

### schema.sql
Creates complete database schema:
- All tables with proper data types
- Foreign key constraints
- Indexes for performance
- CASCADE delete rules

### seed.sql
Initial required data:
- Admin user (`admin@hbnb.com` / `admin123`)
- 10 common amenities
- 1 sample place

### data.sql
Additional sample data:
- 3 test users
- 4 sample places
- Place-amenity associations
- 5 sample reviews

See `sql/SQL_README.md` for detailed usage instructions.

---

## Testing

### Manual Testing Examples

```bash
# 1. Create a user
curl -X POST http://localhost:5000/api/v1/users/ \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"John","last_name":"Doe","email":"john@example.com","password":"secret123"}'

# 2. Login and get token
TOKEN=$(curl -s -X POST http://localhost:5000/api/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@hbnb.com","password":"admin123"}' | \
  python3 -c 'import sys, json; print(json.load(sys.stdin)["access_token"])')

# 3. Create a place (requires auth)
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Beach House","city":"Miami","price":250}'

# 4. Get all places (public)
curl http://localhost:5000/api/v1/places/

# 5. Create amenity (admin only)
curl -X POST http://localhost:5000/api/v1/amenities/ \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Hot Tub"}'
```

### Testing Users

**Admin User:**
- Email: `admin@hbnb.com`
- Password: `admin123`
- Role: Administrator

**Sample Users** (from data.sql):
- Alice: `alice@example.com`
- Bob: `bob@example.com`
- Carol: `carol@example.com`
- Password (all): `admin123`

---

## Project Structure

```
part3/
├── app/
│   ├── __init__.py              # Application factory
│   ├── extensions.py            # Flask extensions (bcrypt, jwt, db)
│   ├── api/                     # REST API endpoints
│   │   ├── user_endpoints.py
│   │   ├── place_endpoints.py
│   │   ├── review_endpoints.py
│   │   ├── amenity_endpoints.py
│   │   ├── auth_endpoints.py
│   │   └── protected_endpoints.py
│   ├── models/                  # SQLAlchemy models
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── persistence/             # Repository layer
│   │   ├── repository_interface.py
│   │   ├── memory_repository.py
│   │   ├── sqlalchemy_repository.py
│   │   ├── user_repository.py
│   │   ├── place_repository.py
│   │   ├── review_repository.py
│   │   ├── amenity_repository.py
│   │   └── repository_factory.py
│   ├── business/                # Business logic
│   │   └── facade.py
│   └── utils/                   # Utilities
│       └── auth.py              # Authorization helpers
├── sql/                         # SQL scripts
│   ├── schema.sql              # Database schema
│   ├── seed.sql                # Initial data
│   ├── data.sql                # Sample data
│   └── SQL_README.md           # SQL documentation
├── tests/
│   └── test_api.py             # API tests
├── config.py                   # Configuration classes
├── run.py                      # Application entry point
├── init_db.py                  # Database initialization
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## Key Technologies

- **Flask** - Web framework
- **Flask-RESTX** - REST API with Swagger documentation
- **Flask-Bcrypt** - Password hashing
- **Flask-JWT-Extended** - JWT authentication
- **Flask-SQLAlchemy** - ORM integration
- **SQLAlchemy** - Database ORM
- **SQLite** - Development database

---

## Security Features

✅ Password hashing with bcrypt  
✅ JWT token-based authentication  
✅ Token expiration (1 hour)  
✅ Passwords never returned in responses  
✅ Email uniqueness validation  
✅ Ownership-based authorization  
✅ Role-based access control (RBAC)  
✅ Foreign key constraints  
✅ SQL injection prevention (via ORM)  

---

## Notes

- Set `USE_DATABASE=True` environment variable to use SQLAlchemy repositories
- Default repository mode is database persistence
- Public GET endpoints remain accessible without authentication
- Admin users can bypass all ownership restrictions
- Review restrictions: cannot review own place, cannot review same place twice
- All timestamps are in UTC
- UUIDs are used for all entity IDs

---

## Credits

Developed as part of the Holberton School HBnB Evolution project.

**Part 3** focuses on authentication, authorization, and database persistence.
