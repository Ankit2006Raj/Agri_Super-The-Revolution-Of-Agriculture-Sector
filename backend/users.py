import json
import os
from datetime import datetime
import hashlib

class UserManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'users_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
            self.save_data()
    
    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def generate_default_data(self):
        # Create a default admin user
        return {
            "users": [
                {
                    "id": "USR001",
                    "username": "admin",
                    "email": "admin@agrisuper.com",
                    "password_hash": self.hash_password("admin123"),
                    "full_name": "Admin User",
                    "role": "admin",
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "last_login": None
                },
                {
                    "id": "USR002",
                    "username": "farmer",
                    "email": "farmer@example.com",
                    "password_hash": self.hash_password("farmer123"),
                    "full_name": "Demo Farmer",
                    "role": "farmer",
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "last_login": None
                }
            ]
        }
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, stored_hash, provided_password):
        return stored_hash == self.hash_password(provided_password)
    
    def authenticate_user(self, username, password):
        for user in self.data["users"]:
            if user["username"] == username and self.verify_password(user["password_hash"], password):
                user["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_data()
                return user
        return None
    
    def register_user(self, username, email, password, full_name, phone='', user_type='farmer'):
        # Check if username or email already exists
        for user in self.data["users"]:
            if user["username"] == username:
                return {"success": False, "message": "Username already exists"}
            if user["email"] == email:
                return {"success": False, "message": "Email already exists"}
        
        # Create new user
        user_id = f"USR{str(len(self.data['users']) + 1).zfill(3)}"
        new_user = {
            "id": user_id,
            "username": username,
            "email": email,
            "password_hash": self.hash_password(password),
            "full_name": full_name,
            "phone": phone,
            "role": user_type,  # Use the provided user_type
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": None
        }
        
        self.data["users"].append(new_user)
        self.save_data()
        return {"success": True, "message": "User registered successfully", "user": new_user}
    
    def get_user_by_id(self, user_id):
        for user in self.data["users"]:
            if user["id"] == user_id:
                return user
        return None
    
    def get_user_by_username(self, username):
        for user in self.data["users"]:
            if user["username"] == username:
                return user
        return None
    
    def get_user_by_email(self, email):
        for user in self.data["users"]:
            if user["email"] == email:
                return user
        return None
    
    def verify_login(self, username, password):
        user = self.get_user_by_username(username)
        if user and self.verify_password(user["password_hash"], password):
            user["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_data()
            return user
        return None
    
    def test_connection(self):
        return {"status": "success", "message": "User management system is operational"}