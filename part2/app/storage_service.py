"""
In-memory storage service for HBnB.
Simulates a persistence layer until SQLAlchemy integration in Part 3.
"""
class StorageService:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.update(**data)
        return user


# Global instance used across layers
storage = StorageService()
