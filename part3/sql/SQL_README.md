# HBnB Database SQL Scripts

This directory contains SQL scripts for setting up and populating the HBnB database.

## Files

### schema.sql
Creates the complete database schema including all tables and relationships:
- **users** - User accounts with authentication
- **places** - Property listings
- **reviews** - User reviews for places
- **amenities** - Available amenities
- **place_amenity** - Many-to-many relationship between places and amenities

### seed.sql
Populates the database with initial data:
- Administrator user (email: `admin@hbnb.com`, password: `admin123`)
- 10 common amenities (WiFi, Pool, Parking, etc.)
- Sample place with amenities

### data.sql
Additional sample data for testing and demonstration:
- 3 sample users (Alice, Bob, Carol)
- 4 sample places (Modern Loft, Beach Cottage, Mountain Retreat, City Studio)
- Place-amenity associations
- 5 sample reviews

## Usage

### Using SQLite3
```bash
# Navigate to the sql directory
cd sql/

# Create database and schema
sqlite3 hbnb.db < schema.sql

# Insert initial data
sqlite3 hbnb.db < seed.sql

# Optional: Insert additional sample data
sqlite3 hbnb.db < data.sql
```

### Using MySQL
```bash
# Create database and schema
mysql -u username -p database_name < schema.sql

# Insert initial data
mysql -u username -p database_name < seed.sql
```

### Using Python
```python
import sqlite3

# Create and setup database
conn = sqlite3.connect('hbnb.db')
cursor = conn.cursor()

# Execute schema
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# Execute seed data
with open('seed.sql', 'r') as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
```

## Database Structure

### Tables
- **users**: Stores user information and credentials
- **places**: Property listings with location and pricing
- **reviews**: User reviews with ratings
- **amenities**: Available amenities for properties
- **place_amenity**: Links places to their amenities

### Relationships
- User → Places (one-to-many): A user can own multiple places
- User → Reviews (one-to-many): A user can write multiple reviews
- Place → Reviews (one-to-many): A place can have multiple reviews
- Place ↔ Amenities (many-to-many): Places can have multiple amenities

### Foreign Keys
- `places.owner_id` → `users.id`
- `reviews.user_id` → `users.id`
- `reviews.place_id` → `places.id`
- `place_amenity.place_id` → `places.id`
- `place_amenity.amenity_id` → `amenities.id`

## Initial Data

### Admin User
- Email: `admin@hbnb.com`
- Password: `admin123`
- Role: Administrator

### Amenities
WiFi, Swimming Pool, Parking, Air Conditioning, Kitchen, TV, Gym, Laundry, Pet Friendly, Balcony

## Notes

- All IDs are UUIDs (CHAR(36))
- Passwords are hashed using bcrypt
- Timestamps are automatically managed
- CASCADE deletes are enabled for related records
- Indexes are created for frequently queried columns
