from .base_model import BaseModel


class Place(BaseModel):
    """Represents a place in the HBnB application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.city = kwargs.get("city", "")
        self.price_per_night = kwargs.get("price_per_night", 0)
        self.owner_id = kwargs.get("owner_id")  # Link to User.id
        self.amenities = kwargs.get("amenities", [])  # List of Amenity IDs

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "price_per_night": self.price_per_night,
            "owner_id": self.owner_id,
            "amenities": self.amenities,
        })
        return data
