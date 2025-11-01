"""
Repository factory for creating appropriate repository instances.
"""
import os
from app.persistence.memory_repository import InMemoryRepository
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


def get_repository(use_database=None):
    """
    Factory function to get the appropriate repository.
    
    Args:
        use_database: Boolean to determine repository type.
                     If None, checks USE_DATABASE environment variable.
                     If True, returns SQLAlchemyRepository.
                     If False, returns InMemoryRepository.
    
    Returns:
        Repository instance (InMemoryRepository or SQLAlchemyRepository)
        
    Note: For now, this returns InMemoryRepository by default.
          Once models are mapped to SQLAlchemy in the next task,
          the default can be changed to use the database.
    """
    if use_database is None:
        # Check environment variable
        use_database = os.environ.get('USE_DATABASE', 'False').lower() == 'true'
    
    if use_database:
        # Return SQLAlchemy repository
        # Note: This will need model classes once they're mapped
        # For now, it's here as a placeholder for the next task
        return SQLAlchemyRepository
    else:
        # Return in-memory repository (default for now)
        return InMemoryRepository()
