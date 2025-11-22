"""
Review-specific repository for database operations.
"""
from app.models.review import Review
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class ReviewRepository(SQLAlchemyRepository):
    """
    Repository for Review-specific database operations.
    Extends SQLAlchemyRepository with Review-specific methods.
    """
    
    def __init__(self):
        """Initialize ReviewRepository with Review model."""
        super().__init__(Review)
