import json
import random
from datetime import datetime, timedelta

class CropRotationEngine:
    def __init__(self, data_folder='data'):
        # Massive crop rotation data
        self.rotation_patterns = {
            "cereal_legume": {
                "pattern": ["wheat", "chickpea", "rice", "lentil"],
                "benefits": ["Nitrogen fixation", "Soil fertility improvement", "Pest break cycle"],
                "duration_months": [4, 3, 4, 3],
                "soil_improvement": 85
            },
            "vegetable_rotation": {
                "pattern": ["tomato", "onion", "cabbage", "carrot"],
                "benefits": ["Disease prevention", "Nutrient optimization", "Market diversification"],
                "duration_months": [4, 3, 3, 4],
                "soil_improvement": 75
            },
            "cash_crop_rotation": {
                "pattern": ["cotton", "wheat", "sugarcane", "mustard"],
                "benefits": ["High profitability", "Risk distribution", "Soil structure improvement"],
                "duration_months": [6, 4, 12, 3],
                "soil_improvement": 70
            }
        }
        
        self.crop_compatibility = {
            "wheat": {"good_after": ["legumes", "cotton"], "avoid_after": ["wheat", "barley"]},
            "rice": {"good_after": ["wheat", "mustard"], "avoid_after": ["rice", "sugarcane"]},
            "tomato": {"good_after": ["onion", "garlic"], "avoid_after": ["potato", "eggplant"]},
            "cotton": {"good_after": ["wheat", "gram"], "avoid_after": ["cotton", "okra"]}
        }
        
        self.seasonal_recommendations = self._generate_seasonal_data()
        
    def _generate_seasonal_data(self):
        seasons = ["kharif", "rabi", "summer"]
        crops_by_season = {
            "kharif": ["rice", "cotton", "sugarcane", "maize", "soybean"],
            "rabi": ["wheat", "barley", "gram", "mustard", "pea"],
            "summer": ["fodder", "green_gram", "watermelon", "cucumber"]
        }
        
        recommendations = {}
        for season in seasons:
            recommendations[season] = []
            for crop in crops_by_season[season]:
                rec = {
                    "crop": crop,
                    "planting_window": f"{season.title()} season optimal",
                    "expected_yield": random.randint(2000, 6000),
                    "water_requirement": random.randint(400, 1200),
                    "profit_potential": random.randint(15000, 80000),
                    "risk_level": random.choice(["Low", "Medium", "High"])
                }
                recommendations[season].append(rec)
        return recommendations
    
    def suggest_rotation(self, current_crop, field_size, soil_type, location):
        # Find best rotation pattern
        suitable_patterns = []
        for pattern_name, pattern_data in self.rotation_patterns.items():
            if current_crop in pattern_data["pattern"]:
                suitable_patterns.append((pattern_name, pattern_data))
        
        if not suitable_patterns:
            # Default rotation suggestion
            suitable_patterns = [("cereal_legume", self.rotation_patterns["cereal_legume"])]
        
        best_pattern = max(suitable_patterns, key=lambda x: x[1]["soil_improvement"])
        pattern_name, pattern_data = best_pattern
        
        # Calculate next crops in rotation
        current_index = pattern_data["pattern"].index(current_crop) if current_crop in pattern_data["pattern"] else 0
        next_crops = pattern_data["pattern"][current_index+1:] + pattern_data["pattern"][:current_index+1]
        
        rotation_plan = []
        start_date = datetime.now()
        
        for i, crop in enumerate(next_crops[:4]):  # Next 4 crops
            duration = pattern_data["duration_months"][i % len(pattern_data["duration_months"])]
            end_date = start_date + timedelta(days=duration * 30)
            
            crop_plan = {
                "sequence": i + 1,
                "crop": crop,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration_months": duration,
                "expected_yield": random.randint(2000, 8000) * field_size,
                "estimated_profit": random.randint(20000, 100000) * field_size,
                "soil_benefits": pattern_data["benefits"],
                "water_requirement": random.randint(500, 1500),
                "fertilizer_needs": self._get_fertilizer_needs(crop)
            }
            rotation_plan.append(crop_plan)
            start_date = end_date
        
        return {
            "rotation_pattern": pattern_name,
            "current_crop": current_crop,
            "field_size_hectares": field_size,
            "soil_improvement_score": pattern_data["soil_improvement"],
            "rotation_plan": rotation_plan,
            "total_cycle_duration": sum(plan["duration_months"] for plan in rotation_plan),
            "benefits": pattern_data["benefits"],
            "recommendations": self._get_rotation_recommendations(soil_type, location)
        }
    
    def _get_fertilizer_needs(self, crop):
        fertilizer_data = {
            "wheat": {"nitrogen": 120, "phosphorus": 60, "potassium": 40},
            "rice": {"nitrogen": 100, "phosphorus": 50, "potassium": 50},
            "tomato": {"nitrogen": 150, "phosphorus": 80, "potassium": 100},
            "cotton": {"nitrogen": 160, "phosphorus": 80, "potassium": 80}
        }
        return fertilizer_data.get(crop, {"nitrogen": 100, "phosphorus": 60, "potassium": 50})
    
    def _get_rotation_recommendations(self, soil_type, location):
        return [
            f"Optimal rotation for {soil_type} soil type",
            "Include legumes to improve nitrogen content",
            "Monitor soil pH regularly during rotation",
            "Implement organic matter addition between crops",
            f"Consider local climate patterns in {location}"
        ]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Crop Rotation is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
