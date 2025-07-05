from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, rating=1, comment="", user_id=None, place_id=None):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.place_id = place_id
