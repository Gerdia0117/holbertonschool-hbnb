class InMemoryRepository:
    """Simple in-memory storage for models."""

    def __init__(self):
        # storage = { "User": {id1: obj1, id2: obj2}, "Place": {...}, ... }
        self.storage = {}

    def save(self, obj):
        """Save or update an object."""
        cls_name = obj.__class__.__name__
        self.storage.setdefault(cls_name, {})
        self.storage[cls_name][obj.id] = obj
        return obj

    def get(self, cls_name, obj_id):
        """Retrieve an object by its class and id."""
        return self.storage.get(cls_name, {}).get(obj_id)

    def all(self, cls_name):
        """Return all objects of a given class."""
        return list(self.storage.get(cls_name, {}).values())

    def delete(self, cls_name, obj_id):
        """Delete an object by its id."""
        cls_storage = self.storage.get(cls_name, {})
        return cls_storage.pop(obj_id, None)
