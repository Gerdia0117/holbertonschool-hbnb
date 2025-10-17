"""
Facade for managing communication between the business
logic layer and persistence layer.
"""
from app.persistence.memory_repository import InMemoryRepository
from app.models.amenity import Amenity  # ✅ Add this

class HBnBFacade:
    """High-level interface for the business logic."""

    def __init__(self):
        self.repo = InMemoryRepository()

    # -------------------------------
    # Generic operations
    # -------------------------------
    def create(self, obj):
        """Create a new object in storage."""
        return self.repo.save(obj)

    def get(self, obj_type, obj_id):
        """Get an object by type and ID."""
        return self.repo.get(obj_type, obj_id)

    def delete(self, obj_type, obj_id):
        """Delete an object by type and ID."""
        return self.repo.delete(obj_type, obj_id)

    def list_all(self, obj_type):
        """List all objects of a given type."""
        return self.repo.all(obj_type)

    # -------------------------------
    # Amenity-specific methods
    # -------------------------------
    def create_amenity(self, data):
        """Create a new Amenity."""
        amenity = Amenity(name=data.get("name"))
        return self.repo.save(amenity)

    def get_amenity(self, amenity_id):
        """Retrieve a single Amenity by ID."""
        return self.repo.get("Amenity", amenity_id)

    def get_all_amenities(self):
        """Retrieve all Amenities."""
        return self.repo.all("Amenity")

    def update_amenity(self, amenity_id, data):
        """Update an existing Amenity."""
        amenity = self.repo.get("Amenity", amenity_id)
        if amenity:
            amenity.name = data.get("name", amenity.name)
            self.repo.save(amenity)
        return amenity
