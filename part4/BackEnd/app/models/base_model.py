"""
Base model defining shared attributes and methods.
"""
from datetime import datetime, timezone
import uuid
from app.extensions import db


class BaseModel(db.Model):
    """Common base model for all entities."""
    
    __abstract__ = True  # This makes it an abstract base class
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

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
