"""
User-specific repository for database operations.
"""
from app.models.user import User
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """
    Repository for User-specific database operations.
    Extends SQLAlchemyRepository with User-specific methods.
    """
    
    def __init__(self):
        """Initialize UserRepository with User model."""
        super().__init__(User)
    
    def get_by_email(self, email):
        """
        Retrieve a user by email address.
        
        Args:
            email: The email address to search for
            
        Returns:
            User object if found, None otherwise
        """
        return self.get_by_attribute('email', email)
    
    def get_user_by_email(self, email):
        """
        Alias for get_by_email for backward compatibility.
        
        Args:
            email: The email address to search for
            
        Returns:
            User object if found, None otherwise
        """
        return self.get_by_email(email)
