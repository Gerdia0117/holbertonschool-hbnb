"""
Repository factory for creating appropriate repository instances.
"""
import os
from app.persistence.memory_repository import InMemoryRepository
from app.persistence.user_repository import UserRepository
from app.persistence.place_repository import PlaceRepository
from app.persistence.review_repository import ReviewRepository
from app.persistence.amenity_repository import AmenityRepository


def get_repository(repository_type='user', use_database=None):
    """
    Factory function to get the appropriate repository.
    
    Args:
        repository_type: Type of repository ('user', 'place', etc.)
        use_database: Boolean to determine repository type.
                     If None, checks USE_DATABASE environment variable.
                     If True, returns SQLAlchemy-based repository.
                     If False, returns InMemoryRepository.
    
    Returns:
        Repository instance
    """
    if use_database is None:
        # Check environment variable - now defaults to True for database
        use_database = os.environ.get('USE_DATABASE', 'True').lower() == 'true'
    
    if use_database:
        # Return appropriate SQLAlchemy repository based on type
        if repository_type == 'user':
            return UserRepository()
        elif repository_type == 'place':
            return PlaceRepository()
        elif repository_type == 'review':
            return ReviewRepository()
        elif repository_type == 'amenity':
            return AmenityRepository()
        # Fallback to InMemoryRepository for unknown types
        return InMemoryRepository()
    else:
        # Return in-memory repository
        return InMemoryRepository()
