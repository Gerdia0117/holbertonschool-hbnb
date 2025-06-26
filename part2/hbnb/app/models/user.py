from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name="", last_name="", email="", password=""):
        super().__init__()
        self.first_name = first_name or ""
        self.last_name = last_name or ""
        self.email = email or ""
        self.password = password or ""
        self.owned_places = []

    def add_place(self, place):
        if place and place.owner == self:
            self.owned_places.append(place)

    def __str__(self):
        return f"User({self.first_name} {self.last_name}, Email: {self.email})"
