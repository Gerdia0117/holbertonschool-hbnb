# HBnB Evolution - Part 3

This part implements a production-ready API with authentication, authorization, and database persistence using SQLAlchemy, plus raw SQL scripts for schema and seed data.

## What’s Included

- Application Factory with configuration support
- Password hashing with bcrypt
- JWT authentication (login, protected endpoints, claims)
- Role-based access control (admin vs regular user)
- Authenticated access rules (ownership checks, restrictions)
- SQLAlchemy integration (db, models, repositories, relationships)
- Raw SQL scripts (schema.sql, seed.sql)

## Getting Started

### Install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the API
```bash
export FLASK_ENV=development
python3 run.py
```

## Configuration
Defined in `config.py`:
- SECRET_KEY, JWT_SECRET_KEY
- SQLALCHEMY_DATABASE_URI
- SQLALCHEMY_TRACK_MODIFICATIONS

## App Factory
`app/__init__.py` provides `create_app(config_name)` and initializes:
- Flask-RESTX API and namespaces
- Bcrypt, JWTManager, SQLAlchemy

## Authentication & Authorization
- Endpoint: `POST /api/v1/auth/login` returns a JWT token
- JWT includes claim `is_admin`
- Protected endpoints require `Authorization: Bearer <token>`
- Utilities: `app/utils/auth.py`
  - `@admin_required()` decorator
  - `is_admin()` helper

## Users
- Passwords hashed with bcrypt
- Endpoints:
  - `GET /api/v1/users/` (public)
  - `POST /api/v1/users/` (public; returns user without password)
  - `GET /api/v1/users/<id>` (public)
  - `PUT /api/v1/users/<id>` (auth required; self-update; admin can update any user incl. email/password/is_admin)
- Email uniqueness validated

## Places
- Endpoints:
  - `GET /api/v1/places/` (public)
  - `POST /api/v1/places/` (auth; owner set from token)
  - `GET /api/v1/places/<id>` (public)
  - `PUT /api/v1/places/<id>` (auth; owner only; admin bypass)

## Reviews
- Endpoints:
  - `GET /api/v1/reviews/` (public)
  - `POST /api/v1/reviews/` (auth; user set from token; prevent self-review and duplicates)
  - `GET /api/v1/reviews/<id>` (public)
  - `PUT /api/v1/reviews/<id>` (auth; author only; admin bypass)
  - `DELETE /api/v1/reviews/<id>` (auth; author only; admin bypass)
  - `GET /api/v1/reviews/place/<place_id>` (public)

## Amenities
- Endpoints:
  - `GET /api/v1/amenities/` (public)
  - `POST /api/v1/amenities/` (admin only)
  - `GET /api/v1/amenities/<id>` (public)
  - `PUT /api/v1/amenities/<id>` (admin only)

## Database (SQLAlchemy)
### Initialization
`init_db.py` will create tables and seed an admin user:
```bash
python3 init_db.py
```

### Models
- BaseModel: `id`, `created_at`, `updated_at`
- User: `first_name`, `last_name`, `email` (unique), `password` (hashed), `is_admin`
- Place: `name`, `description`, `city`, `price`, `latitude`, `longitude`, `owner_id`
- Review: `text`, `rating`, `user_id`, `place_id`
- Amenity: `name` (unique)

### Relationships
- User 1—* Place (User.places, Place.owner)
- User 1—* Review (User.reviews, Review.user)
- Place 1—* Review (Place.reviews, Review.place; cascade delete-orphan)
- Place *—* Amenity via `place_amenity`

## Persistence Layer (Repositories)
- Generic: `SQLAlchemyRepository`
- Specific:
  - `UserRepository` (email lookup)
  - `PlaceRepository`
  - `ReviewRepository`
  - `AmenityRepository`
- Factory: `app/persistence/repository_factory.py` selects repo per entity
- Facade: `app/business/facade.py` orchestrates business rules and uses specific repos

## Raw SQL Scripts
- `schema.sql`: Creates tables, FKs, indexes
- `seed.sql`: Inserts admin user and common amenities, sample place
- `SQL_README.md`: Instructions for using the SQL scripts (SQLite/MySQL/Python)

## Testing (Manual examples)
```bash
# Create a user
curl -s -X POST http://localhost:5000/api/v1/users/ \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"John","last_name":"Doe","email":"john@example.com","password":"secret"}'

# Login and get token
TOKEN=$(curl -s -X POST http://localhost:5000/api/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@hbnb.com","password":"admin123"}' | \
  python3 -c 'import sys, json; print(json.load(sys.stdin)["access_token"])')

# Create a place as admin
curl -s -X POST http://localhost:5000/api/v1/places/ \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"name":"Beach House","city":"Miami","price":250}'
```

## Notes
- Set `USE_DATABASE=True` to use SQLAlchemy repositories via factory
- Public GET endpoints remain accessible without JWT
- Admins bypass ownership checks
- Passwords are never returned in API responses

## Project Structure (key files)
- `run.py` — app entrypoint
- `app/__init__.py` — factory, API, extensions init
- `app/extensions.py` — bcrypt, jwt, db
- `app/api/*.py` — namespaces and endpoints
- `app/models/*.py` — SQLAlchemy models
- `app/persistence/*.py` — repositories and factory
- `app/business/facade.py` — business logic
- `schema.sql`, `seed.sql` — raw SQL scripts
- `SQL_README.md` — SQL scripts guide
