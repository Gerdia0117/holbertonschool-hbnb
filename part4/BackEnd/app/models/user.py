from .base_model import BaseModel
from app.extensions import bcrypt, db


class User(BaseModel):
    """Represents a user in the HBnB application."""
    
    __tablename__ = 'users'
    
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def hash_password(self, password):
        """Hash the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify a password against the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Convert user to dictionary, excluding password."""
        data = super().to_dict()
        data.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        })
        return data
