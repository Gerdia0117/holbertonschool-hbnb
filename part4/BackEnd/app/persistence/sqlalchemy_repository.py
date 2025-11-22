"""
SQLAlchemy-based repository implementation.
This repository uses SQLAlchemy for database persistence.
"""
from app.extensions import db
from app.persistence.repository_interface import RepositoryInterface


class SQLAlchemyRepository(RepositoryInterface):
    """
    SQLAlchemy repository for database persistence.
    
    Note: This implementation assumes models will be mapped to SQLAlchemy
    in the next task. For now, it provides the structure.
    """
    
    def __init__(self, model_class):
        """
        Initialize repository with a specific model class.
        
        Args:
            model_class: The SQLAlchemy model class (e.g., User, Place, etc.)
        """
        self.model = model_class
    
    def save(self, obj):
        """
        Save or update an object in the database.
        
        Args:
            obj: The object to save
            
        Returns:
            The saved object
        """
        db.session.add(obj)
        db.session.commit()
        return obj
    
    def get(self, obj_type, obj_id):
        """
        Retrieve an object by its type and ID.
        
        Args:
            obj_type: The class name (string) of the object
            obj_id: The ID of the object
            
        Returns:
            The object if found, None otherwise
        """
        # For now, obj_type is passed but we use self.model
        # In a multi-model setup, you'd map obj_type to the correct model
        return self.model.query.get(obj_id)
    
    def all(self, obj_type):
        """
        Retrieve all objects of a specific type.
        
        Args:
            obj_type: The class name (string) of the objects
            
        Returns:
            List of all objects of the specified type
        """
        return self.model.query.all()
    
    def delete(self, obj_type, obj_id):
        """
        Delete an object by its type and ID.
        
        Args:
            obj_type: The class name (string) of the object
            obj_id: The ID of the object
            
        Returns:
            The deleted object if found, None otherwise
        """
        obj = self.get(obj_type, obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
        return obj
    
    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object by a specific attribute.
        
        Args:
            attr_name: The attribute name to search by
            attr_value: The value to match
            
        Returns:
            The first object matching the criteria, None otherwise
        """
        return self.model.query.filter_by(**{attr_name: attr_value}).first()
    
    def update(self, obj):
        """
        Update an existing object in the database.
        
        Args:
            obj: The object to update
            
        Returns:
            The updated object
        """
        db.session.commit()
        return obj
