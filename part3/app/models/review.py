from .base_model import BaseModel
from app.extensions import db


class Review(BaseModel):
    """Represents a review for a place."""
    
    __tablename__ = 'reviews'
    
    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    
    # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    
    # Relationships (backref already defined in User and Place models)
    user = db.relationship('User', backref='reviews')

    def to_dict(self):
        """Convert review to dictionary."""
        data = super().to_dict()
        data.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
        })
        return data
