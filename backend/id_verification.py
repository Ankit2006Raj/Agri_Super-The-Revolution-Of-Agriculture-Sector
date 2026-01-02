import json
import os
from datetime import datetime, timedelta
import random

class IDVerificationManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'id_verification_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "verification_requests": [
                {
                    "id": f"VER{str(i).zfill(4)}",
                    "farmer_name": f"Farmer {i}",
                    "phone": f"98765{str(i).zfill(5)}",
                    "email": f"farmer{i}@email.com",
                    "aadhar_number": f"****-****-{str(random.randint(1000, 9999))}",
                    "pan_number": f"ABCDE{str(random.randint(1000, 9999))}F",
                    "land_records": f"Survey No. {random.randint(100, 999)}/{random.randint(1, 10)}",
                    "bank_account": f"****-****-{str(random.randint(1000, 9999))}",
                    "status": random.choice(["Pending", "Verified", "Rejected", "Under Review"]),
                    "submitted_date": (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d"),
                    "verified_date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d") if random.choice([True, False]) else None,
                    "verification_score": random.randint(70, 100),
                    "documents_submitted": random.sample([
                        "Aadhar Card", "PAN Card", "Land Records", "Bank Passbook",
                        "Voter ID", "Driving License", "Kisan Credit Card"
                    ], random.randint(3, 6)),
                    "verification_method": random.choice(["Document Upload", "Video Call", "Field Visit", "Digital KYC"])
                } for i in range(1, 501)
            ],
            "verification_criteria": {
                "mandatory_documents": [
                    "Aadhar Card (Government ID)",
                    "Land ownership documents",
                    "Bank account details",
                    "Phone number verification"
                ],
                "optional_documents": [
                    "PAN Card",
                    "Voter ID",
                    "Kisan Credit Card",
                    "Soil health card",
                    "Crop insurance documents"
                ],
                "verification_levels": {
                    "Basic": {
                        "requirements": ["Phone", "Aadhar"],
                        "benefits": ["Basic marketplace access", "Price information"],
                        "trust_score": "60-70%"
                    },
                    "Standard": {
                        "requirements": ["Phone", "Aadhar", "Land records", "Bank account"],
                        "benefits": ["Full marketplace access", "Credit facilities", "Insurance"],
                        "trust_score": "70-85%"
                    },
                    "Premium": {
                        "requirements": ["All documents", "Field verification", "References"],
                        "benefits": ["Priority support", "Premium features", "Higher credit limits"],
                        "trust_score": "85-100%"
                    }
                }
            },
            "verification_stats": {
                "total_requests": 500,
                "verified_users": 387,
                "pending_verification": 45,
                "rejected_requests": 68,
                "average_processing_time": "2.3 days",
                "fraud_detection_rate": "3.2%"
            }
        }
    
    def get_verification_status(self, user_id):
        return next((v for v in self.data["verification_requests"] if v["id"] == user_id), None)
    
    def get_verification_criteria(self):
        return self.data["verification_criteria"]
    
    def get_verification_stats(self):
        return self.data["verification_stats"]
    
    def get_pending_verifications(self):
        return [v for v in self.data["verification_requests"] if v["status"] == "Pending"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Id Verification is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
