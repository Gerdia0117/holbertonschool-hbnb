from .base_model import BaseModel
from app.extensions import db


class Amenity(BaseModel):
    """Represents an amenity for a place."""
    
    __tablename__ = 'amenities'
    
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        """Convert amenity to dictionary."""
        data = super().to_dict()
        data["name"] = self.name
        return data
