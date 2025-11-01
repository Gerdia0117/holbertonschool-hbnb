from .base_model import BaseModel
from app.extensions import db

# Association table for many-to-many relationship between Place and Amenity
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel):
    """Represents a place in the HBnB application."""
    
    __tablename__ = 'places'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    city = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    
    # Foreign key to User
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    owner = db.relationship('User', backref='places')
    reviews = db.relationship('Review', backref='place', cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenity, backref='places')

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
