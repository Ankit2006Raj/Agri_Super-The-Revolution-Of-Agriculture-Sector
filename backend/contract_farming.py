import json
from datetime import datetime, timedelta
import random

class ContractFarmingEngine:
    def __init__(self, data_folder='data'):
        # Massive contract farming data
        self.contract_templates = {
            "vegetables": {
                "tomato": {"min_price": 25, "max_price": 45, "duration": 120, "quality_grade": "A+"},
                "onion": {"min_price": 15, "max_price": 35, "duration": 150, "quality_grade": "A"},
                "potato": {"min_price": 12, "max_price": 28, "duration": 90, "quality_grade": "A+"},
                "cabbage": {"min_price": 8, "max_price": 18, "duration": 75, "quality_grade": "A"},
                "cauliflower": {"min_price": 20, "max_price": 40, "duration": 85, "quality_grade": "A+"}
            },
            "grains": {
                "wheat": {"min_price": 2100, "max_price": 2500, "duration": 180, "quality_grade": "FAQ"},
                "rice": {"min_price": 1800, "max_price": 2200, "duration": 150, "quality_grade": "Grade A"},
                "corn": {"min_price": 1600, "max_price": 2000, "duration": 120, "quality_grade": "Premium"},
                "barley": {"min_price": 1400, "max_price": 1800, "duration": 140, "quality_grade": "Standard"}
            }
        }
        
        self.buyers_database = [
            {"id": 1, "name": "FreshMart Retail Chain", "type": "retail", "rating": 4.8, "contracts_completed": 245},
            {"id": 2, "name": "Organic Foods Ltd", "type": "processor", "rating": 4.9, "contracts_completed": 189},
            {"id": 3, "name": "Export House India", "type": "exporter", "rating": 4.7, "contracts_completed": 156},
            {"id": 4, "name": "Hotel Chain Group", "type": "hospitality", "rating": 4.6, "contracts_completed": 98}
        ]
        
        self.active_contracts = self._generate_active_contracts()
        
    def _generate_active_contracts(self):
        contracts = []
        for i in range(500):  # Generate 500 active contracts
            crop_category = random.choice(list(self.contract_templates.keys()))
            crop = random.choice(list(self.contract_templates[crop_category].keys()))
            buyer = random.choice(self.buyers_database)
            
            contract = {
                "id": f"CF{1000 + i}",
                "crop": crop,
                "category": crop_category,
                "buyer_id": buyer["id"],
                "buyer_name": buyer["name"],
                "quantity": random.randint(100, 5000),
                "price_per_unit": random.randint(
                    self.contract_templates[crop_category][crop]["min_price"],
                    self.contract_templates[crop_category][crop]["max_price"]
                ),
                "duration_days": self.contract_templates[crop_category][crop]["duration"],
                "quality_requirements": self.contract_templates[crop_category][crop]["quality_grade"],
                "advance_payment": random.randint(20, 50),  # percentage
                "status": random.choice(["active", "pending", "completed"]),
                "created_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
                "delivery_date": (datetime.now() + timedelta(days=random.randint(30, 180))).strftime("%Y-%m-%d")
            }
            contracts.append(contract)
        return contracts
    
    def get_contract_opportunities(self, crop_type=None):
        if crop_type:
            return [c for c in self.active_contracts if c["crop"].lower() == crop_type.lower()]
        return self.active_contracts[:50]  # Return first 50 for display
    
    def create_contract(self, farmer_id, contract_data):
        new_contract = {
            "id": f"CF{len(self.active_contracts) + 1000}",
            "farmer_id": farmer_id,
            **contract_data,
            "status": "pending",
            "created_date": datetime.now().strftime("%Y-%m-%d")
        }
        self.active_contracts.append(new_contract)
        return new_contract
    
    def test_connection(self):
        """Test if the contract farming engine is working"""
        try:
            contracts = self.get_contract_opportunities()
            if contracts:
                return {'status': 'success', 'message': 'Contract Farming Engine is operational'}
            return {'status': 'error', 'message': 'Contract Farming Engine test failed'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
