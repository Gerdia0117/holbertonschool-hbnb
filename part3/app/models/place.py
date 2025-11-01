from .base_model import BaseModel
from app.extensions import db


class Place(BaseModel):
    """Represents a place in the HBnB application."""
    
    __tablename__ = 'places'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    city = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    owner_id = db.Column(db.String(36), nullable=False)  # Foreign key to User (will add relationship later)

    def to_dict(self):
        """Convert place to dictionary."""
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
        })
        return data
