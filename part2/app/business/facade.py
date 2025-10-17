from app.persistence.memory_repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review  # <-- add this import

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
    # Place-specific methods
    # -------------------------------
    def create_place(self, data):
        owner_id = data.get("owner_id")
        name = data.get("name")
        price = data.get("price", 0)
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if not name:
            raise ValueError("Place name is required.")
        if owner_id and not self.repo.get("User", owner_id):
            raise ValueError("Invalid owner ID.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if latitude and not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if longitude and not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

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
        """Create a new Review linked to a User and Place."""
        user_id = data.get("user_id")
        place_id = data.get("place_id")
        text = data.get("text", "")

        if not user_id or not self.repo.get("User", user_id):
            raise ValueError("Invalid user ID.")
        if not place_id or not self.repo.get("Place", place_id):
            raise ValueError("Invalid place ID.")
        if not text:
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
        """Get all reviews for a specific place."""
        return [
            r for r in self.repo.all("Review")
            if getattr(r, "place_id", None) == place_id
        ]
