"""
Base model defining shared attributes and methods.
"""
from datetime import datetime, timezone
import uuid

class BaseModel:
    """Common base model for all entities."""

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.now(timezone.utc))
        self.updated_at = kwargs.get("updated_at", datetime.now(timezone.utc))

    def to_dict(self):
        """Convert instance to dictionary."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def update(self, **kwargs):
        """Update attributes and refresh timestamp."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
