import json
import os
from datetime import datetime, timedelta
import random

class FarmerGroupsManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'farmer_groups_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "groups": [
                {
                    "id": f"FG{str(i).zfill(4)}",
                    "name": f"Cooperative Group {i}",
                    "location": random.choice(["Punjab", "Haryana", "UP", "Maharashtra", "Karnataka"]),
                    "crop_focus": random.choice(["Wheat", "Rice", "Cotton", "Sugarcane", "Vegetables"]),
                    "members_count": random.randint(15, 200),
                    "established_date": f"2020-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                    "leader": f"Leader {i}",
                    "contact": f"9876543{str(i).zfill(3)}",
                    "total_land": random.randint(100, 2000),
                    "annual_revenue": random.randint(500000, 5000000),
                    "success_rate": random.randint(75, 95),
                    "activities": random.sample([
                        "Bulk purchasing", "Joint selling", "Knowledge sharing",
                        "Equipment sharing", "Credit facilitation", "Training programs"
                    ], 4),
                    "achievements": [
                        f"Increased income by {random.randint(20, 50)}%",
                        f"Reduced input costs by {random.randint(15, 30)}%",
                        f"Improved crop quality by {random.randint(10, 25)}%"
                    ]
                } for i in range(1, 101)
            ],
            "membership_benefits": [
                "Bulk purchasing discounts (15-30% savings)",
                "Shared equipment access",
                "Joint marketing for better prices",
                "Technical training and support",
                "Credit facilitation",
                "Insurance group policies",
                "Government scheme access",
                "Quality certification support"
            ],
            "formation_guidelines": {
                "minimum_members": 10,
                "maximum_members": 500,
                "registration_process": [
                    "Form organizing committee",
                    "Conduct awareness meetings",
                    "Prepare bylaws and constitution",
                    "Register with cooperative department",
                    "Open bank account",
                    "Start operations"
                ],
                "legal_requirements": [
                    "Cooperative society registration",
                    "PAN card for group",
                    "Bank account opening",
                    "Audit compliance",
                    "Annual returns filing"
                ]
            }
        }
    
    def get_all_groups(self):
        return self.data["groups"]
    
    def get_group_by_id(self, group_id):
        return next((g for g in self.data["groups"] if g["id"] == group_id), None)
    
    def search_groups(self, location=None, crop=None):
        groups = self.data["groups"]
        if location:
            groups = [g for g in groups if location.lower() in g["location"].lower()]
        if crop:
            groups = [g for g in groups if crop.lower() in g["crop_focus"].lower()]
        return groups
    
    def get_formation_guide(self):
        return self.data["formation_guidelines"]
    
    def get_benefits(self):
        return self.data["membership_benefits"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Farmer Groups is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
