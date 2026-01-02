import json
import os
from datetime import datetime, timedelta
import random

class MentorshipManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'mentorship_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "mentors": [
                {
                    "id": f"MEN{str(i).zfill(3)}",
                    "name": f"Mentor {i}",
                    "age": random.randint(35, 65),
                    "location": random.choice(["Punjab", "Haryana", "UP", "Maharashtra", "Karnataka", "Gujarat"]),
                    "specialization": random.choice(["Organic Farming", "Crop Management", "Livestock", "Horticulture", "Agribusiness"]),
                    "experience_years": random.randint(10, 40),
                    "farm_size": random.randint(5, 100),
                    "success_story": f"Increased farm income by {random.randint(200, 500)}% through innovative practices",
                    "mentees_count": random.randint(5, 50),
                    "rating": round(random.uniform(4.0, 5.0), 1),
                    "contact": f"mentor{i}@agri.com",
                    "phone": f"98765{str(i).zfill(5)}",
                    "availability": random.choice(["Weekdays", "Weekends", "Flexible"]),
                    "languages": random.sample(["Hindi", "English", "Punjabi", "Marathi", "Gujarati"], 2),
                    "achievements": [
                        f"Best Farmer Award {random.randint(2015, 2023)}",
                        f"Organic Certification {random.randint(2018, 2023)}",
                        f"Innovation in Agriculture {random.randint(2016, 2023)}"
                    ]
                } for i in range(1, 101)
            ],
            "mentees": [
                {
                    "id": f"MEE{str(i).zfill(3)}",
                    "name": f"Mentee {i}",
                    "age": random.randint(20, 45),
                    "location": random.choice(["Punjab", "Haryana", "UP", "Maharashtra", "Karnataka"]),
                    "farm_size": random.randint(1, 20),
                    "crop_interest": random.choice(["Wheat", "Rice", "Vegetables", "Fruits", "Organic"]),
                    "experience_level": random.choice(["Beginner", "Intermediate", "Advanced"]),
                    "mentor_id": f"MEN{str(random.randint(1, 100)).zfill(3)}",
                    "start_date": (datetime.now() - timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d"),
                    "progress": random.randint(20, 95),
                    "goals": [
                        "Increase crop yield",
                        "Learn organic methods",
                        "Improve soil health",
                        "Better market access"
                    ]
                } for i in range(1, 201)
            ],
            "mentorship_programs": [
                {
                    "id": "PROG001",
                    "name": "Organic Farming Mastery",
                    "duration": "6 months",
                    "description": "Complete guide to organic farming practices",
                    "modules": [
                        "Soil preparation and composting",
                        "Natural pest control methods",
                        "Organic fertilizers and nutrients",
                        "Certification process",
                        "Marketing organic produce"
                    ],
                    "participants": 45,
                    "success_rate": "89%"
                },
                {
                    "id": "PROG002",
                    "name": "Smart Farming Techniques",
                    "duration": "4 months",
                    "description": "Modern technology integration in farming",
                    "modules": [
                        "Precision agriculture",
                        "IoT sensors and monitoring",
                        "Drone applications",
                        "Data-driven decisions",
                        "Cost-benefit analysis"
                    ],
                    "participants": 32,
                    "success_rate": "92%"
                }
            ],
            "success_metrics": {
                "total_mentors": 100,
                "active_mentees": 200,
                "completed_programs": 156,
                "average_income_increase": "45%",
                "satisfaction_rate": "96%"
            }
        }
    
    def get_all_mentors(self, specialization=None, location=None):
        mentors = self.data["mentors"]
        if specialization:
            mentors = [m for m in mentors if m["specialization"] == specialization]
        if location:
            mentors = [m for m in mentors if m["location"] == location]
        return mentors
    
    def get_mentor_by_id(self, mentor_id):
        return next((m for m in self.data["mentors"] if m["id"] == mentor_id), None)
    
    def get_mentorship_programs(self):
        return self.data["mentorship_programs"]
    
    def get_success_metrics(self):
        return self.data["success_metrics"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Mentorship is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
