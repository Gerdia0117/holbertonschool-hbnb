from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.places import Property
from app.models.amenity import Amenity
from app.models.review import Review

class RentalServiceFacade:
    def __init__(self):
        self.user_repository = InMemoryRepository()
        self.place_repository = InMemoryRepository()
        self.review_repository = InMemoryRepository()
        self.amenity_repository = InMemoryRepository()

    def create_user(self, first_name, last_name, email, password):
        """Create a new user in the repository."""
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        self.user_repository.add(new_user)
        return new_user

    def get_user_by_id(self, user_id):
        """Retrieve a user using their ID."""
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email_address):
        """Retrieve a user by their email address."""
        users = self.user_repository.get_all()
        for user in users:
            if user.email == email_address:
                return user
        return None

    def get_all_users(self):
        """Get a list of all users."""
        return self.user_repository.get_all()

    def update_user(self, user_id, updated_info):
        """Modify an existing user's details."""
        user = self.user_repository.get(user_id)
        if user:
            self.user_repository.update(user_id, updated_info)
            return user
        return None

    def delete_user(self, user_id):
        """Delete a user from the repository."""
        return self.user_repository.delete(user_id)

    def get_user(self, user_id):
        """Retrieve a user using their ID."""
        return self.user_repository.get(user_id)

    def add_amenity(self, amenity_details):
        """Add a new amenity to the repository."""
        new_amenity = Amenity(**amenity_details)
        self.amenity_repository.add(new_amenity)
        return new_amenity

    def get_amenity_by_id(self, amenity_id):
        """Get an amenity by its ID."""
        return self.amenity_repository.get(amenity_id)

    def list_all_amenities(self):
        """Retrieve a list of all amenities."""
        return self.amenity_repository.get_all()
    
    def get_all_amenities(self):
        """Retrieve a list of all amenities."""
        return self.amenity_repository.get_all()
    
    def get_amenity(self, amenity_id):
        """Get an amenity by its ID."""
        return self.amenity_repository.get(amenity_id)

    def add_place(self, place_details):
        """Add a new place to the repository."""
        owner = self.user_repository.get(place_details['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        amenities = []
        for amenity_id in place_details.get('amenities', []):
            amenity = self.amenity_repository.get(amenity_id)
            if not amenity:
                raise ValueError(f"Amenity {amenity_id} not found")
            amenities.append(amenity)

        new_place = Place(
            name=place_details['title'],
            description=place_details.get('description', ''),
            price=place_details['price'],
            latitude=place_details['latitude'],
            longitude=place_details['longitude'],
            owner=owner
        )

        for amenity in amenities:
            new_place.add_amenity(amenity)

        self.place_repository.add(new_place)
        return new_place

    def get_place_by_id(self, place_id):
        """Retrieve a place by its ID, including owner and amenities."""
        return self.place_repository.get(place_id)

    def update_place(self, place_id, updated_details):
        """Modify the details of an existing place."""
        place = self.place_repository.get(place_id)
        if not place:
            return None

        if 'owner_id' in updated_details:
            owner = self.user_repository.get(updated_details['owner_id'])
            if not owner:
                raise ValueError("Owner not found")
            place.owner = owner

        if 'amenities' in updated_details:
            amenities = []
            for amenity_id in updated_details['amenities']:
                amenity = self.amenity_repository.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity {amenity_id} not found")
                amenities.append(amenity)
            place.amenities = amenities

        if 'title' in updated_details:
            place.name = updated_details['title']
        if 'description' in updated_details:
            place.description = updated_details['description']
        if 'price' in updated_details:
            place.price = updated_details['price']
        if 'latitude' in updated_details:
            place.latitude = updated_details['latitude']
        if 'longitude' in updated_details:
            place.longitude = updated_details['longitude']

        self.place_repository.update(place_id, updated_details)
        return place

    def add_review(self, review_details):
        """Add a new review for a place."""
        user = self.user_repository.get(review_details['user_id'])
        if not user:
            raise ValueError("User not found")

        place = self.place_repository.get(review_details['place_id'])
        if not place:
            raise ValueError("Place not found")

        rating = review_details.get('rating')
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5")

        new_review = Review(
            user=user,
            place=place,
            rating=rating,
            comment=review_details.get('text', '')
        )

        self.review_repository.add(new_review)
        return new_review

    def get_review_by_id(self, review_id):
        """Retrieve a review by its ID."""
        return self.review_repository.get(review_id)

    def list_all_reviews(self):
        """Get a list of all reviews."""
        return self.review_repository.get_all()

    def update_review(self, review_id, updated_info):
        """Modify the details of an existing review."""
        review = self.review_repository.get(review_id)
        if not review:
            return None

        if 'user_id' in updated_info:
            user = self.user_repository.get(updated_info['user_id'])
            if not user:
                raise ValueError("User not found")
            review.user = user

        if 'place_id' in updated_info:
            place = self.place_repository.get(updated_info['place_id'])
            if not place:
                raise ValueError("Place not found")
            review.place = place

        if 'rating' in updated_info:
            rating = updated_info['rating']
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise ValueError("Rating must be an integer between 1 and 5")
            review.rating = rating

        if 'text' in updated_info:
            review.comment = updated_info['text']

        review.save()
        return review

    def delete_review(self, review_id):
        """Remove a review from the repository."""
        self.review_repository.delete(review_id)
