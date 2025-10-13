"""
Facade for managing communication between the business
logic layer and persistence layer.
"""
from app.persistence.memory_repository import InMemoryRepository

class HBnBFacade:
    """High-level interface for the business logic."""

    def __init__(self):
        self.repo = InMemoryRepository()

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
