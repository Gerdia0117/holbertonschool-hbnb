from .base_model import BaseModel


class Place(BaseModel):
    """Represents a place in the HBnB application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.city = kwargs.get("city", "")
        self.price = kwargs.get("price", 0)
        self.latitude = kwargs.get("latitude", 0.0)
        self.longitude = kwargs.get("longitude", 0.0)
        self.owner_id = kwargs.get("owner_id")  # Link to User.id
        self.amenities = kwargs.get("amenities", [])  # List of Amenity IDs

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": self.amenities,
        })
        return data
