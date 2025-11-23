#!/usr/bin/env python3
"""
Seed the database with sample data for testing.
"""
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def seed_database():
    """Add sample data to the database."""
    app = create_app()
    
    with app.app_context():
        print("Starting database seeding...")
        
        # Check if admin exists
        admin = User.query.filter_by(email='admin@hbnb.com').first()
        if not admin:
            print("Admin user not found. Creating admin user...")
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
            print(f"Admin user found: {admin.email}")
        
        # Create a regular user for testing reviews
        user = User.query.filter_by(email='user@hbnb.com').first()
        if not user:
            user = User(
                first_name='John',
                last_name='Doe',
                email='user@hbnb.com',
                is_admin=False
            )
            user.hash_password('password123')
            db.session.add(user)
            db.session.commit()
            print(f"Regular user created: {user.email}")
        else:
            print(f"Regular user found: {user.email}")
        
        # Create sample amenities
        amenity_names = ['WiFi', 'Kitchen', 'Air Conditioning', 'Workspace', 'TV', 'Parking']
        amenities = []
        for name in amenity_names:
            amenity = Amenity.query.filter_by(name=name).first()
            if not amenity:
                amenity = Amenity(name=name)
                db.session.add(amenity)
                print(f"Created amenity: {name}")
            amenities.append(amenity)
        
        db.session.commit()
        
        # Create sample places
        places_data = [
            {
                'name': 'Cozy Downtown Apartment',
                'description': 'A beautiful and modern apartment in the heart of the city. Perfect for couples or solo travelers looking for comfort and convenience.',
                'city': 'San Francisco',
                'price': 120.0,
                'latitude': 37.7749,
                'longitude': -122.4194,
                'owner_id': admin.id,
                'amenity_indices': [0, 1, 2, 3]  # WiFi, Kitchen, Air Conditioning, Workspace
            },
            {
                'name': 'Beachfront Villa',
                'description': 'Stunning ocean views with direct beach access. Spacious and luxurious with all modern amenities.',
                'city': 'Miami',
                'price': 250.0,
                'latitude': 25.7617,
                'longitude': -80.1918,
                'owner_id': admin.id,
                'amenity_indices': [0, 1, 2, 4, 5]  # WiFi, Kitchen, Air Conditioning, TV, Parking
            },
            {
                'name': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin nestled in the mountains. Perfect for a quiet getaway surrounded by nature.',
                'city': 'Denver',
                'price': 85.0,
                'latitude': 39.7392,
                'longitude': -104.9903,
                'owner_id': admin.id,
                'amenity_indices': [0, 1, 4]  # WiFi, Kitchen, TV
            }
        ]
        
        created_places = []
        for place_data in places_data:
            # Check if place already exists
            existing_place = Place.query.filter_by(
                name=place_data['name'],
                owner_id=place_data['owner_id']
            ).first()
            
            if not existing_place:
                amenity_indices = place_data.pop('amenity_indices')
                place = Place(**place_data)
                
                # Add amenities
                for idx in amenity_indices:
                    place.amenities.append(amenities[idx])
                
                db.session.add(place)
                created_places.append(place)
                print(f"Created place: {place.name} in {place.city}")
            else:
                created_places.append(existing_place)
                print(f"Place already exists: {existing_place.name}")
        
        db.session.commit()
        
        # Create sample reviews (from regular user)
        if len(created_places) > 0 and user:
            review_texts = [
                "Amazing place! Very clean and the host was super helpful. Would definitely stay here again.",
                "Great location, close to everything. The apartment was exactly as described.",
                "Wonderful experience! The place exceeded my expectations. Highly recommended!"
            ]
            
            for idx, place in enumerate(created_places):
                if idx < len(review_texts):
                    # Check if review already exists
                    existing_review = Review.query.filter_by(
                        user_id=user.id,
                        place_id=place.id
                    ).first()
                    
                    if not existing_review:
                        review = Review(
                            text=review_texts[idx],
                            user_id=user.id,
                            place_id=place.id
                        )
                        db.session.add(review)
                        print(f"Created review for: {place.name}")
                    else:
                        print(f"Review already exists for: {place.name}")
            
            db.session.commit()
        
        print("\n✅ Database seeding completed successfully!")
        print(f"\nCreated:")
        print(f"  - 2 users (admin@hbnb.com / admin123, user@hbnb.com / password123)")
        print(f"  - {len(amenities)} amenities")
        print(f"  - {len(created_places)} places")
        print(f"\nYou can now test the application!")

if __name__ == '__main__':
    seed_database()
