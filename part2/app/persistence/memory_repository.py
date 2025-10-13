"""
In-memory implementation of the repository.
"""
from app.persistence.repository_interface import RepositoryInterface
import uuid

class InMemoryRepository(RepositoryInterface):
    """Simple in-memory repository."""

    def __init__(self):
        self.storage = {}

    def save(self, obj):
        """Save or update an object."""
        obj_type = type(obj).__name__
        if obj_type not in self.storage:
            self.storage[obj_type] = {}

        if not getattr(obj, "id", None):
            obj.id = str(uuid.uuid4())

        self.storage[obj_type][obj.id] = obj
        return obj

    def get(self, obj_type, obj_id):
        """Retrieve an object by type and ID."""
        return self.storage.get(obj_type, {}).get(obj_id)

    def delete(self, obj_type, obj_id):
        """Delete an object by ID."""
        if obj_type in self.storage and obj_id in self.storage[obj_type]:
            del self.storage[obj_type][obj_id]
            return True
        return False

    def all(self, obj_type):
        """Return all objects of a given type."""
        return list(self.storage.get(obj_type, {}).values())
