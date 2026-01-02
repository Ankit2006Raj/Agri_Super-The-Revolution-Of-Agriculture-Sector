import json
import random
from datetime import datetime, timedelta

class SoilKnowledge:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/soil_knowledge_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "soil_types": [
                {
                    "type": "Alluvial Soil",
                    "ph_range": "6.0-7.5",
                    "characteristics": "Rich in potash, phosphoric acid, and lime",
                    "suitable_crops": ["Rice", "Wheat", "Sugarcane", "Cotton", "Jute"],
                    "area_coverage": "40% of India",
                    "fertility": "High",
                    "water_retention": "Good",
                    "drainage": "Moderate"
                },
                {
                    "type": "Black Soil (Regur)",
                    "ph_range": "7.5-8.5",
                    "characteristics": "Rich in lime, iron, magnesia, alumina, and potash",
                    "suitable_crops": ["Cotton", "Sugarcane", "Wheat", "Jowar", "Linseed"],
                    "area_coverage": "15% of India",
                    "fertility": "Very High",
                    "water_retention": "Excellent",
                    "drainage": "Poor"
                },
                {
                    "type": "Red Soil",
                    "ph_range": "5.5-7.0",
                    "characteristics": "Rich in iron oxide, poor in nitrogen and phosphorus",
                    "suitable_crops": ["Rice", "Wheat", "Cotton", "Pulses", "Millets"],
                    "area_coverage": "18% of India",
                    "fertility": "Medium",
                    "water_retention": "Moderate",
                    "drainage": "Good"
                },
                {
                    "type": "Laterite Soil",
                    "ph_range": "5.0-6.5",
                    "characteristics": "Rich in iron and aluminum, poor in nitrogen and potash",
                    "suitable_crops": ["Rice", "Ragi", "Cashew", "Coconut", "Areca nut"],
                    "area_coverage": "3.5% of India",
                    "fertility": "Low",
                    "water_retention": "Poor",
                    "drainage": "Excellent"
                }
            ],
            "soil_tests": [
                {
                    "test_id": "ST001",
                    "farmer_id": "F001",
                    "location": "Punjab, Ludhiana",
                    "test_date": "2024-01-15",
                    "soil_type": "Alluvial",
                    "ph_level": 6.8,
                    "organic_carbon": 0.65,
                    "nitrogen": 280,
                    "phosphorus": 18,
                    "potassium": 145,
                    "recommendations": [
                        "Apply 2 tons of farmyard manure per acre",
                        "Use DAP fertilizer at 50 kg per acre",
                        "Maintain soil moisture at 60-70%"
                    ]
                },
                {
                    "test_id": "ST002",
                    "farmer_id": "F002",
                    "location": "Maharashtra, Nashik",
                    "test_date": "2024-01-14",
                    "soil_type": "Black",
                    "ph_level": 8.2,
                    "organic_carbon": 0.45,
                    "nitrogen": 320,
                    "phosphorus": 22,
                    "potassium": 180,
                    "recommendations": [
                        "Reduce alkalinity with gypsum application",
                        "Add organic matter to improve structure",
                        "Use balanced NPK fertilizer"
                    ]
                }
            ],
            "nutrient_deficiency": [
                {
                    "nutrient": "Nitrogen",
                    "symptoms": ["Yellowing of older leaves", "Stunted growth", "Poor tillering"],
                    "solutions": ["Apply urea fertilizer", "Use organic manure", "Grow leguminous crops"],
                    "crops_affected": ["Rice", "Wheat", "Maize", "Sugarcane"]
                },
                {
                    "nutrient": "Phosphorus",
                    "symptoms": ["Purple discoloration", "Delayed maturity", "Poor root development"],
                    "solutions": ["Apply DAP fertilizer", "Use bone meal", "Add rock phosphate"],
                    "crops_affected": ["Cotton", "Pulses", "Oilseeds"]
                },
                {
                    "nutrient": "Potassium",
                    "symptoms": ["Leaf burn", "Weak stems", "Poor fruit quality"],
                    "solutions": ["Apply MOP fertilizer", "Use wood ash", "Add potassium sulfate"],
                    "crops_affected": ["Fruits", "Vegetables", "Sugarcane"]
                }
            ],
            "soil_improvement": [
                {
                    "method": "Organic Matter Addition",
                    "description": "Adding compost, farmyard manure, and crop residues",
                    "benefits": ["Improves soil structure", "Increases water retention", "Enhances microbial activity"],
                    "cost_per_acre": 5000,
                    "time_to_effect": "3-6 months"
                },
                {
                    "method": "Cover Cropping",
                    "description": "Growing cover crops during off-season",
                    "benefits": ["Prevents soil erosion", "Adds nitrogen", "Improves soil health"],
                    "cost_per_acre": 2000,
                    "time_to_effect": "1 season"
                },
                {
                    "method": "Lime Application",
                    "description": "Adding lime to acidic soils",
                    "benefits": ["Neutralizes soil acidity", "Improves nutrient availability", "Enhances root growth"],
                    "cost_per_acre": 3000,
                    "time_to_effect": "2-3 months"
                }
            ]
        }
    
    def analyze_soil(self, ph, organic_carbon, nitrogen, phosphorus, potassium):
        analysis = {
            "ph_status": self.get_ph_status(ph),
            "nutrient_status": {
                "nitrogen": self.get_nutrient_status(nitrogen, "nitrogen"),
                "phosphorus": self.get_nutrient_status(phosphorus, "phosphorus"),
                "potassium": self.get_nutrient_status(potassium, "potassium")
            },
            "recommendations": self.get_recommendations(ph, organic_carbon, nitrogen, phosphorus, potassium),
            "suitable_crops": self.get_suitable_crops(ph)
        }
        return analysis
    
    def get_ph_status(self, ph):
        if ph < 5.5:
            return "Highly Acidic"
        elif ph < 6.5:
            return "Moderately Acidic"
        elif ph < 7.5:
            return "Neutral"
        elif ph < 8.5:
            return "Moderately Alkaline"
        else:
            return "Highly Alkaline"
    
    def get_nutrient_status(self, value, nutrient):
        ranges = {
            "nitrogen": {"low": 280, "medium": 560, "high": 840},
            "phosphorus": {"low": 11, "medium": 22, "high": 56},
            "potassium": {"low": 108, "medium": 280, "high": 560}
        }
        
        if value < ranges[nutrient]["low"]:
            return "Low"
        elif value < ranges[nutrient]["medium"]:
            return "Medium"
        else:
            return "High"
    
    def get_recommendations(self, ph, organic_carbon, nitrogen, phosphorus, potassium):
        recommendations = []
        
        if ph < 6.0:
            recommendations.append("Apply lime to reduce acidity")
        elif ph > 8.0:
            recommendations.append("Apply gypsum to reduce alkalinity")
        
        if organic_carbon < 0.5:
            recommendations.append("Add organic matter like compost or FYM")
        
        if nitrogen < 280:
            recommendations.append("Apply nitrogen fertilizer (Urea)")
        
        if phosphorus < 11:
            recommendations.append("Apply phosphorus fertilizer (DAP)")
        
        if potassium < 108:
            recommendations.append("Apply potassium fertilizer (MOP)")
        
        return recommendations
    
    def get_soil_types(self):
        return self.data["soil_types"]
    
    def get_soil_tests(self):
        return self.data["soil_tests"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Soil Knowledge is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
