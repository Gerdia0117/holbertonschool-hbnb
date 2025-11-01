"""
Place-specific repository for database operations.
"""
from app.models.place import Place
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    """
    Repository for Place-specific database operations.
    Extends SQLAlchemyRepository with Place-specific methods.
    """
    
    def __init__(self):
        """Initialize PlaceRepository with Place model."""
        super().__init__(Place)
