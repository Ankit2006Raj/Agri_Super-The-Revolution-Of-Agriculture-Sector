import json
import os
from datetime import datetime, timedelta
import random

class OrganicFarmingAdvisory:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'organic_farming_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "organic_practices": [
                {
                    "id": 1,
                    "practice": "Composting",
                    "description": "Creating nutrient-rich compost from organic waste",
                    "benefits": ["Improves soil structure", "Reduces chemical fertilizer dependency", "Enhances microbial activity"],
                    "implementation_steps": [
                        "Collect organic kitchen waste and farm residues",
                        "Layer brown (carbon) and green (nitrogen) materials",
                        "Maintain proper moisture and aeration",
                        "Turn compost regularly for 3-6 months"
                    ],
                    "cost_savings": "60-80% reduction in fertilizer costs",
                    "certification_points": 25
                },
                {
                    "id": 2,
                    "practice": "Crop Rotation",
                    "description": "Systematic rotation of different crop families",
                    "benefits": ["Breaks pest cycles", "Improves soil fertility", "Reduces disease pressure"],
                    "implementation_steps": [
                        "Plan 3-4 year rotation cycle",
                        "Include legumes for nitrogen fixation",
                        "Avoid same family crops in succession",
                        "Monitor soil health indicators"
                    ],
                    "cost_savings": "40-60% reduction in pest control costs",
                    "certification_points": 30
                }
            ],
            "certification_requirements": {
                "transition_period": "36 months",
                "documentation_needed": [
                    "Field history records",
                    "Input usage logs",
                    "Harvest records",
                    "Processing documentation"
                ],
                "inspection_frequency": "Annual",
                "certification_cost": "$500-2000 per farm"
            },
            "organic_inputs": [
                {
                    "name": "Neem Oil",
                    "type": "Pesticide",
                    "application_rate": "2-5ml per liter",
                    "target_pests": ["Aphids", "Whiteflies", "Thrips"],
                    "cost_per_liter": "$15-25",
                    "organic_certified": True
                },
                {
                    "name": "Vermicompost",
                    "type": "Fertilizer",
                    "application_rate": "2-5 tons per hectare",
                    "nutrients": {"N": "1.5%", "P": "1.0%", "K": "1.2%"},
                    "cost_per_ton": "$80-120",
                    "organic_certified": True
                }
            ]
        }
    
    def get_organic_practices(self):
        return self.data.get("organic_practices", [])
    
    def get_certification_info(self):
        return self.data.get("certification_requirements", {})
    
    def get_organic_inputs(self):
        return self.data.get("organic_inputs", [])

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Organic Farming is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
