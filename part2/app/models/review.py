from .base_model import BaseModel


class Review(BaseModel):
    """Represents a review for a place."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get("text", "")
        self.rating = kwargs.get("rating", 0)
        self.user_id = kwargs.get("user_id")
        self.place_id = kwargs.get("place_id")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
        })
        return data
