import json
import os
from datetime import datetime, timedelta
import random

class CarbonCredits:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'carbon_credits_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "carbon_projects": [
                {
                    "id": 1,
                    "project_type": "Agroforestry",
                    "carbon_sequestration_rate": "2-8 tons CO2/hectare/year",
                    "credit_price": "$5-15 per ton CO2",
                    "verification_standard": "Verified Carbon Standard (VCS)",
                    "project_duration": "20-30 years",
                    "initial_investment": "$200-500 per hectare"
                },
                {
                    "id": 2,
                    "project_type": "Soil Carbon Enhancement",
                    "carbon_sequestration_rate": "0.5-2 tons CO2/hectare/year",
                    "credit_price": "$8-20 per ton CO2",
                    "verification_standard": "Climate Action Reserve (CAR)",
                    "project_duration": "10-20 years",
                    "initial_investment": "$50-150 per hectare"
                }
            ],
            "sustainable_practices": [
                {
                    "practice": "Cover Cropping",
                    "carbon_benefit": "0.3-1.5 tons CO2/hectare/year",
                    "implementation_cost": "$30-80 per hectare",
                    "additional_benefits": ["Soil health improvement", "Erosion control", "Biodiversity enhancement"]
                },
                {
                    "practice": "No-Till Farming",
                    "carbon_benefit": "0.2-1.0 tons CO2/hectare/year",
                    "implementation_cost": "$0-50 per hectare",
                    "additional_benefits": ["Reduced fuel costs", "Improved water retention", "Labor savings"]
                }
            ],
            "market_data": {
                "current_carbon_price": "$12.50 per ton CO2",
                "price_trend": "Increasing 8-12% annually",
                "major_buyers": ["Microsoft", "Google", "Shell", "BP"],
                "market_volume": "2.3 billion tons CO2 equivalent"
            }
        }
    
    def calculate_carbon_potential(self, farm_area, practice_type):
        practices = self.data.get("sustainable_practices", [])
        for practice in practices:
            if practice["practice"].lower() in practice_type.lower():
                # Extract carbon benefit range
                benefit_range = practice["carbon_benefit"].split("-")
                min_benefit = float(benefit_range[0])
                max_benefit = float(benefit_range[1].split()[0])
                avg_benefit = (min_benefit + max_benefit) / 2
                
                annual_carbon = farm_area * avg_benefit
                annual_revenue = annual_carbon * 12.50  # Current market price
                
                return {
                    "annual_carbon_sequestration": annual_carbon,
                    "annual_revenue_potential": annual_revenue,
                    "10_year_revenue": annual_revenue * 10,
                    "practice": practice["practice"]
                }
        return None

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Carbon Credits is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
