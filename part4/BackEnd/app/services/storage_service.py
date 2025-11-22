# app/services/storage_service.py

class StorageService:
    """Simple mock storage for testing."""
    def __init__(self):
        self.users = {}

    def get_user(self, user_id):
        return self.users.get(user_id)

    def add_user(self, user):
        self.users[user["id"]] = user

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user_id, data):
        if user_id in self.users:
            self.users[user_id].update(data)
            return self.users[user_id]
        return None


# Create a single shared instance
storage = StorageService()
