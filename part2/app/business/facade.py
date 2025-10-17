from app.persistence.memory_repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review

class HBnBFacade:
    """High-level interface for business logic."""

    def __init__(self):
        self.repo = InMemoryRepository()

    # -------------------------------
    # Generic CRUD operations
    # -------------------------------
    def create(self, obj):
        return self.repo.save(obj)

    def get(self, obj_type, obj_id):
        return self.repo.get(obj_type, obj_id)

    def list_all(self, obj_type):
        return self.repo.all(obj_type)

    def delete(self, obj_type, obj_id):
        return self.repo.delete(obj_type, obj_id)

    # -------------------------------
    # User-specific methods
    # -------------------------------
    def create_user(self, data):
        if "first_name" not in data or "last_name" not in data or "email" not in data:
            raise ValueError("Missing required user fields.")
        user = User(**data)
        return self.repo.save(user)

    def get_user(self, user_id):
        return self.repo.get("User", user_id)

    def get_all_users(self):
        return self.repo.all("User")

    def update_user(self, user_id, data):
        user = self.repo.get("User", user_id)
        if not user:
            return None
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        self.repo.save(user)
        return user

    # -------------------------------
    # Amenity-specific methods
    # -------------------------------
    def create_amenity(self, data):
        if "name" not in data or not data["name"]:
            raise ValueError("Amenity name is required.")
        amenity = Amenity(**data)
        return self.repo.save(amenity)

    def get_amenity(self, amenity_id):
        return self.repo.get("Amenity", amenity_id)

    def get_all_amenities(self):
        return self.repo.all("Amenity")

    def update_amenity(self, amenity_id, data):
        amenity = self.repo.get("Amenity", amenity_id)
        if not amenity:
            return None
        if "name" in data:
            amenity.name = data["name"]
        self.repo.save(amenity)
        return amenity

    # -------------------------------
    # Place-specific methods
    # -------------------------------
    def create_place(self, data):
        if "name" not in data or not data["name"]:
            raise ValueError("Place name is required.")
        if "owner_id" not in data or not self.repo.get("User", data["owner_id"]):
            raise ValueError("Valid owner_id is required.")
        # Set default optional fields
        data.setdefault("description", "")
        data.setdefault("price", 0)
        data.setdefault("latitude", None)
        data.setdefault("longitude", None)
        place = Place(**data)
        return self.repo.save(place)

    def get_place(self, place_id):
        return self.repo.get("Place", place_id)

    def get_all_places(self):
        return self.repo.all("Place")

    def update_place(self, place_id, data):
        place = self.repo.get("Place", place_id)
        if not place:
            return None
        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        self.repo.save(place)
        return place

    # -------------------------------
    # Review-specific methods
    # -------------------------------
    def create_review(self, data):
        if "user_id" not in data or not self.repo.get("User", data["user_id"]):
            raise ValueError("Valid user_id is required.")
        if "place_id" not in data or not self.repo.get("Place", data["place_id"]):
            raise ValueError("Valid place_id is required.")
        if "text" not in data or not data["text"]:
            raise ValueError("Review text is required.")
        review = Review(**data)
        return self.repo.save(review)

    def get_review(self, review_id):
        return self.repo.get("Review", review_id)

    def get_all_reviews(self):
        return self.repo.all("Review")

    def update_review(self, review_id, data):
        review = self.repo.get("Review", review_id)
        if not review:
            return None
        if "text" in data:
            review.text = data["text"]
        self.repo.save(review)
        return review

    def delete_review(self, review_id):
        return self.repo.delete("Review", review_id)

    def get_reviews_by_place(self, place_id):
        return [
            r for r in self.repo.all("Review")
            if getattr(r, "place_id", None) == place_id
        ]
