from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description, place_id, id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
        self.name = name
        self.description = description
        self.place_id = place_id
