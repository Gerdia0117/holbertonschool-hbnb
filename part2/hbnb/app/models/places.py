from .base_model import BaseModel

class Property(BaseModel):
    """Represents a rental property listing with location details"""

    def __init__(self, title="", details="", nightly_rate=0, lat=0.0, lng=0.0, host=None):
        super().__init__()
        self.title = title
        self.details = details
        self.nightly_rate = nightly_rate
        self.lat = lat
        self.lng = lng
        self.host = host
        self.property_reviews = []
        self.features = []

    def include_review(self, new_review):
        """Adds a review if it belongs to this property"""
        if new_review and getattr(new_review, 'property_obj', None) == self:
            self.property_reviews.append(new_review)
            self.save()

    def add_feature(self, feature_item):
        """Includes an amenity if not already present"""
        if feature_item and feature_item not in self.features:
            self.features.append(feature_item)
            self.save()

    def _validate_coordinates(self):
        """Checks if location values are within valid ranges"""
        if not (-90 <= self.lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= self.lng <= 180):
            raise ValueError("Longitude must be between -180 and 180")

    def update_pricing(self, new_rate):
        """Updates the nightly rate with validation"""
        if new_rate >= 0:
            self.nightly_rate = new_rate
            self.save()
        else:
            raise ValueError("Rate cannot be negative")
