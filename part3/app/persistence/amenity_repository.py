"""
Amenity-specific repository for database operations.
"""
from app.models.amenity import Amenity
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class AmenityRepository(SQLAlchemyRepository):
    """
    Repository for Amenity-specific database operations.
    Extends SQLAlchemyRepository with Amenity-specific methods.
    """
    
    def __init__(self):
        """Initialize AmenityRepository with Amenity model."""
        super().__init__(Amenity)
