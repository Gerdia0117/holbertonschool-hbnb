from app.persistence.repository_factory import get_repository
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review


class HBnBFacade:
    
    
    _instance = None
    _user_repo = None
    _place_repo = None
    _review_repo = None
    _amenity_repo = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Use repository factory to get appropriate repositories
            cls._user_repo = get_repository('user')
            cls._place_repo = get_repository('place')
            cls._review_repo = get_repository('review')
            cls._amenity_repo = get_repository('amenity')
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'user_repo'):
            self.user_repo = self._user_repo
            self.place_repo = self._place_repo
            self.review_repo = self._review_repo
            self.amenity_repo = self._amenity_repo

    # -------------------------------
    # User methods
    # -------------------------------
    def create_user(self, data):
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")
        email = data.get("email")
        password = data.get("password", "")
        is_admin = data.get("is_admin", False)

        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        
        # Check if email already exists
        if self.get_user_by_email(email):
            raise ValueError("Email already in use")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_admin=is_admin
        )
        # Hash the password before saving
        user.hash_password(password)
        return self.user_repo.save(user)

    def get_user(self, user_id):
        return self.user_repo.get("User", user_id)

    def get_all_users(self):
        return self.user_repo.all("User")
    
    def get_user_by_email(self, email):
        """Get a user by email address."""
        # Use repository's get_by_email method if available (SQLAlchemy)
        if hasattr(self.user_repo, 'get_by_email'):
            return self.user_repo.get_by_email(email)
        # Fallback for InMemoryRepository
        users = self.user_repo.all("User")
        for user in users:
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, data):
        user = self.user_repo.get("User", user_id)
        if not user:
            return None
        
        # Check if email is being updated and if it's unique
        if 'email' in data and data['email'] != user.email:
            if self.get_user_by_email(data['email']):
                raise ValueError("Email already in use")
        
        # Handle password update separately
        if 'password' in data:
            user.hash_password(data['password'])
            data = {k: v for k, v in data.items() if k != 'password'}
        
        for key, value in data.items():
            if hasattr(user, key) and key != 'password':
                setattr(user, key, value)
        self.user_repo.save(user)
        return user

    def delete_user(self, user_id):
        return self.user_repo.delete("User", user_id)

    # -------------------------------
    # Amenity methods
    # -------------------------------
    def create_amenity(self, data):
        if not data.get("name"):
            raise ValueError("Amenity name is required")
        amenity = Amenity(**data)
        return self.amenity_repo.save(amenity)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get("Amenity", amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.all("Amenity")

    def update_amenity(self, amenity_id, data):
        amenity = self.amenity_repo.get("Amenity", amenity_id)
        if not amenity:
            return None
        if "name" in data:
            amenity.name = data["name"]
        self.amenity_repo.save(amenity)
        return amenity

    def delete_amenity(self, amenity_id):
        return self.amenity_repo.delete("Amenity", amenity_id)

    # -------------------------------
    # Place methods
    # -------------------------------
    def create_place(self, data):
        if not data.get("name"):
            raise ValueError("Place name is required")

        owner_id = data.get("owner_id")
        if not owner_id or not self.user_repo.get("User", owner_id):
            raise ValueError("Valid owner_id is required")

        data.setdefault("price", 0)
        data.setdefault("latitude", 0.0)
        data.setdefault("longitude", 0.0)

        place = Place(**data)
        return self.place_repo.save(place)

    def get_place(self, place_id):
        return self.place_repo.get("Place", place_id)

    def get_all_places(self):
        return self.place_repo.all("Place")

    def update_place(self, place_id, data):
        place = self.place_repo.get("Place", place_id)
        if not place:
            return None
        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        self.place_repo.save(place)
        return place

    def delete_place(self, place_id):
        return self.place_repo.delete("Place", place_id)

    # -------------------------------
    # Review methods
    # -------------------------------
    def create_review(self, data):
        user_id = data.get("user_id")
        place_id = data.get("place_id")
        text = data.get("text")

        if not user_id or not self.user_repo.get("User", user_id):
            raise ValueError("Valid user_id is required")
        if not place_id or not self.place_repo.get("Place", place_id):
            raise ValueError("Valid place_id is required")
        if not text:
            raise ValueError("Review text is required")
        
        # Prevent users from reviewing their own places
        if self.is_place_owner(place_id, user_id):
            raise ValueError("You cannot review your own place")
        
        # Prevent duplicate reviews
        if self.has_user_reviewed_place(user_id, place_id):
            raise ValueError("You have already reviewed this place")

        review = Review(**data)
        return self.review_repo.save(review)

    def get_review(self, review_id):
        return self.review_repo.get("Review", review_id)

    def get_all_reviews(self):
        return self.review_repo.all("Review")

    def update_review(self, review_id, data):
        review = self.review_repo.get("Review", review_id)
        if not review:
            return None
        if "text" in data:
            review.text = data["text"]
        self.review_repo.save(review)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete("Review", review_id)

    def get_reviews_by_place(self, place_id):
        return [
            r for r in self.review_repo.all("Review")
            if getattr(r, "place_id", None) == place_id
        ]
    
    # -------------------------------
    # Authorization helper methods
    # -------------------------------
    def is_place_owner(self, place_id, user_id):
        """Check if a user owns a specific place."""
        place = self.place_repo.get("Place", place_id)
        return place and getattr(place, 'owner_id', None) == user_id
    
    def is_review_author(self, review_id, user_id):
        """Check if a user is the author of a specific review."""
        review = self.review_repo.get("Review", review_id)
        return review and getattr(review, 'user_id', None) == user_id
    
    def has_user_reviewed_place(self, user_id, place_id):
        """Check if a user has already reviewed a specific place."""
        reviews = self.review_repo.all("Review")
        for review in reviews:
            if (getattr(review, 'user_id', None) == user_id and 
                getattr(review, 'place_id', None) == place_id):
                return True
        return False
