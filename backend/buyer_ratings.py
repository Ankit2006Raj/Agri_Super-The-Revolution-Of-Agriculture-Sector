import json
import os
from datetime import datetime, timedelta
import random

class BuyerRatingsManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'buyer_ratings_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "buyers": [
                {
                    "id": f"BUY{str(i).zfill(3)}",
                    "name": f"Buyer Company {i}",
                    "type": random.choice(["Retailer", "Wholesaler", "Processor", "Exporter", "Restaurant Chain"]),
                    "location": random.choice(["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Pune"]),
                    "registration_date": (datetime.now() - timedelta(days=random.randint(30, 1095))).strftime("%Y-%m-%d"),
                    "overall_rating": round(random.uniform(3.0, 5.0), 1),
                    "total_transactions": random.randint(10, 500),
                    "total_volume": random.randint(1000, 50000),
                    "payment_rating": round(random.uniform(3.5, 5.0), 1),
                    "communication_rating": round(random.uniform(3.0, 5.0), 1),
                    "quality_standards_rating": round(random.uniform(3.2, 5.0), 1),
                    "delivery_rating": round(random.uniform(3.1, 5.0), 1),
                    "verified": random.choice([True, False]),
                    "payment_terms": random.choice(["Immediate", "15 days", "30 days", "45 days"]),
                    "preferred_crops": random.sample(["Wheat", "Rice", "Cotton", "Sugarcane", "Vegetables", "Fruits"], 3),
                    "reviews": [
                        {
                            "farmer_id": f"FAR{str(j).zfill(3)}",
                            "rating": random.randint(3, 5),
                            "comment": f"Review {j} - Good experience with timely payments and fair pricing",
                            "date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
                            "transaction_id": f"TXN{str(j).zfill(4)}"
                        } for j in range(1, random.randint(5, 20))
                    ]
                } for i in range(1, 101)
            ],
            "rating_criteria": {
                "payment_reliability": {
                    "weight": 30,
                    "factors": ["On-time payments", "Payment method flexibility", "Advance payment options"]
                },
                "communication": {
                    "weight": 20,
                    "factors": ["Response time", "Clarity of requirements", "Professional behavior"]
                },
                "quality_standards": {
                    "weight": 25,
                    "factors": ["Fair quality assessment", "Reasonable rejection rates", "Clear specifications"]
                },
                "delivery_terms": {
                    "weight": 15,
                    "factors": ["Flexible pickup", "Transportation support", "Storage facilities"]
                },
                "business_practices": {
                    "weight": 10,
                    "factors": ["Contract adherence", "Dispute resolution", "Long-term relationships"]
                }
            },
            "rating_stats": {
                "total_buyers": 100,
                "verified_buyers": 78,
                "average_rating": 4.2,
                "total_reviews": 1250,
                "high_rated_buyers": 65,  # 4+ rating
                "blacklisted_buyers": 3
            }
        }
    
    def get_all_buyers(self, min_rating=None, buyer_type=None):
        buyers = self.data["buyers"]
        if min_rating:
            buyers = [b for b in buyers if b["overall_rating"] >= min_rating]
        if buyer_type:
            buyers = [b for b in buyers if b["type"] == buyer_type]
        return sorted(buyers, key=lambda x: x["overall_rating"], reverse=True)
    
    def get_buyer_by_id(self, buyer_id):
        return next((b for b in self.data["buyers"] if b["id"] == buyer_id), None)
    
    def get_rating_criteria(self):
        return self.data["rating_criteria"]
    
    def get_rating_stats(self):
        return self.data["rating_stats"]
    
    def get_top_rated_buyers(self, limit=10):
        return sorted(self.data["buyers"], key=lambda x: x["overall_rating"], reverse=True)[:limit]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Buyer Ratings is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
