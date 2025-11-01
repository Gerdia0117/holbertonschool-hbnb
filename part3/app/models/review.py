from .base_model import BaseModel
from app.extensions import db


class Review(BaseModel):
    """Represents a review for a place."""
    
    __tablename__ = 'reviews'
    
    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.String(36), nullable=False)  # Foreign key to User (will add relationship later)
    place_id = db.Column(db.String(36), nullable=False)  # Foreign key to Place (will add relationship later)

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
