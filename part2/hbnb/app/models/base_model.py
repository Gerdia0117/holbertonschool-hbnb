import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id or str(uuid.uuid4())
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or self.created_at

    def save(self):
        """Update and save when  the object is modified to a database."""
        self.updated_at = datetime.utcnow()
