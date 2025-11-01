#!/usr/bin/env python3
"""
Database initialization script.
Creates all database tables based on SQLAlchemy models.
"""
from app import create_app
from app.extensions import db
# Import all models to ensure they're registered
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def init_database():
    """Initialize the database and create all tables."""
    app = create_app()
    
    with app.app_context():
        # Drop all tables (use with caution in production!)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Optional: Create an admin user for testing
        admin = User.query.filter_by(email='admin@hbnb.com').first()
        if not admin:
            admin = User(
                first_name='Admin',
                last_name='User',
                email='admin@hbnb.com',
                is_admin=True
            )
            admin.hash_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print(f"Admin user created: {admin.email}")
        else:
            print("Admin user already exists")

if __name__ == '__main__':
    init_database()
