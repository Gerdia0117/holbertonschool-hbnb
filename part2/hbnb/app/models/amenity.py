from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description=None, place_id=None, id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
        self.name = name
        self.description = description
        self.place_id = place_id
    
    def to_dict(self):
        """Convert amenity to dictionary representation."""
        data = super().to_dict()
        data.update({
            'name': self.name,
            'description': self.description,
            'place_id': self.place_id
        })
        return data
