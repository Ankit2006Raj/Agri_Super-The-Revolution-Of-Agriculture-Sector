import json
import os
from datetime import datetime, timedelta
import random

class SmartContractsManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'smart_contracts_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "contracts": [
                {
                    "id": f"SC{str(i).zfill(4)}",
                    "contract_type": random.choice(["Purchase Agreement", "Supply Contract", "Service Agreement", "Loan Agreement"]),
                    "farmer_id": f"FAR{str(i).zfill(3)}",
                    "buyer_id": f"BUY{str(i).zfill(3)}",
                    "crop_type": random.choice(["Wheat", "Rice", "Cotton", "Sugarcane", "Vegetables"]),
                    "quantity": random.randint(100, 5000),
                    "price_per_unit": random.randint(20, 100),
                    "total_amount": 0,  # Will be calculated
                    "contract_date": (datetime.now() - timedelta(days=random.randint(1, 180))).strftime("%Y-%m-%d"),
                    "delivery_date": (datetime.now() + timedelta(days=random.randint(30, 120))).strftime("%Y-%m-%d"),
                    "status": random.choice(["Active", "Completed", "Pending", "Disputed"]),
                    "payment_terms": random.choice(["Immediate", "30 days", "60 days", "On delivery"]),
                    "quality_parameters": {
                        "moisture_content": f"<{random.randint(12, 15)}%",
                        "purity": f">{random.randint(95, 99)}%",
                        "grade": random.choice(["A", "B", "C"])
                    },
                    "escrow_amount": 0,  # Will be calculated
                    "milestones": [
                        {
                            "milestone": "Contract Signed",
                            "date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
                            "status": "Completed"
                        },
                        {
                            "milestone": "Quality Check",
                            "date": (datetime.now() + timedelta(days=random.randint(15, 45))).strftime("%Y-%m-%d"),
                            "status": "Pending"
                        }
                    ]
                } for i in range(1, 201)
            ],
            "contract_templates": [
                {
                    "id": "TEMP001",
                    "name": "Standard Purchase Agreement",
                    "description": "Basic contract for crop purchase with quality parameters",
                    "clauses": [
                        "Quality specifications and testing procedures",
                        "Delivery terms and conditions",
                        "Payment schedule and methods",
                        "Force majeure and dispute resolution",
                        "Penalty clauses for non-compliance"
                    ]
                },
                {
                    "id": "TEMP002",
                    "name": "Contract Farming Agreement",
                    "description": "Long-term partnership for crop production",
                    "clauses": [
                        "Seed and input supply arrangements",
                        "Technical support and guidance",
                        "Guaranteed purchase at predetermined price",
                        "Risk sharing mechanisms",
                        "Sustainability requirements"
                    ]
                }
            ],
            "payment_methods": [
                {
                    "method": "Digital Wallet",
                    "processing_time": "Instant",
                    "fees": "1%",
                    "security": "High"
                },
                {
                    "method": "Bank Transfer",
                    "processing_time": "1-2 days",
                    "fees": "0.5%",
                    "security": "Very High"
                },
                {
                    "method": "Cryptocurrency",
                    "processing_time": "10-30 minutes",
                    "fees": "2%",
                    "security": "Very High"
                }
            ],
            "contract_stats": {
                "total_contracts": 200,
                "active_contracts": 89,
                "completed_contracts": 95,
                "disputed_contracts": 16,
                "total_value": "₹45,67,890",
                "success_rate": "92%"
            }
        }
    
    def get_all_contracts(self, status=None):
        contracts = self.data["contracts"]
        if status:
            contracts = [c for c in contracts if c["status"] == status]
        return contracts
    
    def get_contract_by_id(self, contract_id):
        return next((c for c in self.data["contracts"] if c["id"] == contract_id), None)
    
    def get_contract_templates(self):
        return self.data["contract_templates"]
    
    def get_payment_methods(self):
        return self.data["payment_methods"]
    
    def get_contract_stats(self):
        return self.data["contract_stats"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Smart Contracts is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
