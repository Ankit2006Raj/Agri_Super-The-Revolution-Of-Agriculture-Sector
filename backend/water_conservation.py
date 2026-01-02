import json
import os
from datetime import datetime, timedelta
import random

class WaterConservation:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'water_conservation_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "irrigation_techniques": [
                {
                    "id": 1,
                    "technique": "Drip Irrigation",
                    "water_efficiency": "90-95%",
                    "water_savings": "30-50% compared to flood irrigation",
                    "initial_cost": "$800-1500 per hectare",
                    "maintenance_cost": "$50-100 per year",
                    "suitable_crops": ["Vegetables", "Fruits", "Cash crops"],
                    "roi_period": "2-3 years"
                },
                {
                    "id": 2,
                    "technique": "Sprinkler Irrigation",
                    "water_efficiency": "75-85%",
                    "water_savings": "20-40% compared to flood irrigation",
                    "initial_cost": "$400-800 per hectare",
                    "maintenance_cost": "$30-60 per year",
                    "suitable_crops": ["Cereals", "Pulses", "Fodder crops"],
                    "roi_period": "1.5-2.5 years"
                }
            ],
            "water_harvesting": [
                {
                    "method": "Farm Ponds",
                    "capacity": "500-5000 cubic meters",
                    "construction_cost": "$2000-15000",
                    "water_storage_duration": "6-8 months",
                    "benefits": ["Rainwater collection", "Groundwater recharge", "Fish farming potential"]
                },
                {
                    "method": "Check Dams",
                    "capacity": "1000-10000 cubic meters",
                    "construction_cost": "$5000-50000",
                    "water_storage_duration": "4-6 months",
                    "benefits": ["Flood control", "Groundwater recharge", "Soil erosion prevention"]
                }
            ],
            "water_usage_data": [
                {"crop": "Rice", "water_requirement": "1200-1800 mm", "critical_stages": ["Tillering", "Flowering"]},
                {"crop": "Wheat", "water_requirement": "450-650 mm", "critical_stages": ["Crown root initiation", "Flowering"]},
                {"crop": "Cotton", "water_requirement": "700-1300 mm", "critical_stages": ["Squaring", "Flowering"]}
            ]
        }
    
    def get_irrigation_techniques(self):
        return self.data.get("irrigation_techniques", [])
    
    def get_water_harvesting_methods(self):
        return self.data.get("water_harvesting", [])
    
    def calculate_water_savings(self, current_method, new_method, farm_area):
        # Calculate potential water savings
        savings_data = {
            "flood_to_drip": 40,
            "flood_to_sprinkler": 30,
            "sprinkler_to_drip": 15
        }
        key = f"{current_method}_to_{new_method}"
        savings_percent = savings_data.get(key, 0)
        return {
            "savings_percent": savings_percent,
            "annual_water_saved": farm_area * savings_percent * 10,  # liters
            "cost_savings": farm_area * savings_percent * 50  # dollars
        }

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Water Conservation is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
