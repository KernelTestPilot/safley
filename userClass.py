import json
from datetime import datetime

class User:
    def __init__(self, birth_year, gender, location, success, reason=None, created_at=None):
        self.birth_year = birth_year 
        self.gender = gender
        self.location = location
        self.success = bool(success)
        self.reason = reason
        self.created_at = created_at
        self.age = datetime.now().year - birth_year
    
    @staticmethod
    def create_user(birth_year, gender, location, success, reason=None):
        return User(
            birth_year,
            gender,
            location,
            success,
            reason,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    def to_dict(self):
        return {
            "birth_year": self.birth_year,
            "age": self.age,
            "gender": self.gender,
            "location": self.location,
            "success": self.success,
            "reason": self.reason,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return User(
            data["birth_year"],
            data["gender"],
            data["location"],
            data["success"],
            data.get("reason"),
            data.get("created_at")
        )

    @staticmethod
    def load_users(filename="users.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return [User.from_dict(u) for u in data]
        except FileNotFoundError:
            return []
    @staticmethod
    def save_users(users, filename="users.json"):
        with open(filename, "w") as f:
            json.dump([u.to_dict() for u in users], f, indent=4)