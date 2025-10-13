"""
Repository interface defining basic operations.
"""
from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    """Abstract repository definition."""

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def get(self, obj_type, obj_id):
        pass

    @abstractmethod
    def delete(self, obj_type, obj_id):
        pass

    @abstractmethod
    def all(self, obj_type):
        pass
