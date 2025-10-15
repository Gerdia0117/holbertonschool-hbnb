from .base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity for a place."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")

    def to_dict(self):
        data = super().to_dict()
        data["name"] = self.name
        return data
