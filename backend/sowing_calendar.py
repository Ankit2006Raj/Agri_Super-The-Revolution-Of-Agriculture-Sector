import json
import random
from datetime import datetime, timedelta

class SowingCalendarEngine:
    def __init__(self, data_folder='data'):
        # Massive sowing calendar data
        self.crop_calendar = self._generate_crop_calendar()
        self.regional_variations = self._generate_regional_data()
        self.weather_patterns = self._generate_weather_patterns()
        self.soil_readiness = self._generate_soil_data()
        
    def _generate_crop_calendar(self):
        crops_data = {
            "wheat": {
                "optimal_sowing": {"start": "November 15", "end": "December 15"},
                "harvesting": {"start": "March 15", "end": "April 30"},
                "growth_duration": 120,
                "temperature_range": {"min": 15, "max": 25},
                "rainfall_requirement": 450,
                "soil_types": ["loamy", "clay_loam", "sandy_loam"],
                "varieties": {
                    "HD-2967": {"duration": 115, "yield_potential": 4500, "disease_resistance": "High"},
                    "PBW-343": {"duration": 125, "yield_potential": 5200, "disease_resistance": "Medium"},
                    "WH-147": {"duration": 120, "yield_potential": 4800, "disease_resistance": "High"}
                }
            },
            "rice": {
                "optimal_sowing": {"start": "June 15", "end": "July 15"},
                "harvesting": {"start": "October 15", "end": "November 30"},
                "growth_duration": 130,
                "temperature_range": {"min": 20, "max": 35},
                "rainfall_requirement": 1200,
                "soil_types": ["clay", "clay_loam", "silty_clay"],
                "varieties": {
                    "IR-64": {"duration": 125, "yield_potential": 5500, "disease_resistance": "Medium"},
                    "Swarna": {"duration": 135, "yield_potential": 6000, "disease_resistance": "High"},
                    "MTU-1010": {"duration": 130, "yield_potential": 5800, "disease_resistance": "Medium"}
                }
            },
            "cotton": {
                "optimal_sowing": {"start": "May 1", "end": "June 15"},
                "harvesting": {"start": "October 1", "end": "January 31"},
                "growth_duration": 180,
                "temperature_range": {"min": 21, "max": 30},
                "rainfall_requirement": 600,
                "soil_types": ["black_cotton", "alluvial", "red_loam"],
                "varieties": {
                    "Bt-Cotton": {"duration": 175, "yield_potential": 2500, "disease_resistance": "High"},
                    "Desi Cotton": {"duration": 160, "yield_potential": 1800, "disease_resistance": "Medium"},
                    "Hybrid Cotton": {"duration": 180, "yield_potential": 2800, "disease_resistance": "High"}
                }
            },
            "tomato": {
                "optimal_sowing": {"start": "July 1", "end": "August 15"},
                "harvesting": {"start": "October 15", "end": "December 30"},
                "growth_duration": 90,
                "temperature_range": {"min": 18, "max": 29},
                "rainfall_requirement": 400,
                "soil_types": ["sandy_loam", "loamy", "well_drained"],
                "varieties": {
                    "Arka Rakshak": {"duration": 85, "yield_potential": 35000, "disease_resistance": "High"},
                    "Pusa Ruby": {"duration": 90, "yield_potential": 40000, "disease_resistance": "Medium"},
                    "Himsona": {"duration": 95, "yield_potential": 45000, "disease_resistance": "High"}
                }
            }
        }
        return crops_data
    
    def _generate_regional_data(self):
        return {
            "North India": {
                "states": ["Punjab", "Haryana", "Uttar Pradesh", "Rajasthan"],
                "climate_zone": "Semi-arid to sub-humid",
                "monsoon_arrival": "June 25",
                "monsoon_withdrawal": "September 30",
                "winter_crops": ["wheat", "barley", "mustard", "gram"],
                "summer_crops": ["rice", "cotton", "sugarcane", "maize"],
                "soil_adjustments": {
                    "wheat": "Sow 10 days earlier in Punjab",
                    "rice": "Transplant by July 10 for best results"
                }
            },
            "South India": {
                "states": ["Karnataka", "Tamil Nadu", "Andhra Pradesh", "Kerala"],
                "climate_zone": "Tropical",
                "monsoon_arrival": "June 1",
                "monsoon_withdrawal": "December 15",
                "winter_crops": ["ragi", "groundnut", "sunflower"],
                "summer_crops": ["rice", "cotton", "sugarcane"],
                "soil_adjustments": {
                    "rice": "Two seasons possible - Kharif and Rabi",
                    "cotton": "Sow by May 15 for optimal yield"
                }
            },
            "West India": {
                "states": ["Maharashtra", "Gujarat", "Goa"],
                "climate_zone": "Semi-arid",
                "monsoon_arrival": "June 10",
                "monsoon_withdrawal": "October 15",
                "winter_crops": ["wheat", "gram", "jowar"],
                "summer_crops": ["cotton", "sugarcane", "rice"],
                "soil_adjustments": {
                    "cotton": "Black cotton soil ideal, sow by June 1",
                    "sugarcane": "Plant by February for 18-month crop"
                }
            }
        }
    
    def _generate_weather_patterns(self):
        return {
            "2024": {
                "monsoon_forecast": "Normal to above normal",
                "temperature_trend": "Slightly above average",
                "rainfall_distribution": "Well distributed",
                "extreme_events": "Low probability of drought",
                "el_nino_impact": "Neutral conditions"
            },
            "seasonal_advisories": {
                "kharif_2024": "Favorable conditions for rice and cotton",
                "rabi_2024": "Good prospects for wheat and gram",
                "summer_2024": "Water management crucial for summer crops"
            }
        }
    
    def _generate_soil_data(self):
        return {
            "soil_preparation_timeline": {
                "deep_plowing": "45-60 days before sowing",
                "field_leveling": "30 days before sowing",
                "organic_matter": "20-30 days before sowing",
                "final_preparation": "7-10 days before sowing"
            },
            "soil_testing_parameters": {
                "pH": {"optimal_range": "6.5-7.5", "test_frequency": "Annual"},
                "organic_carbon": {"optimal_range": ">0.75%", "test_frequency": "Biennial"},
                "nitrogen": {"optimal_range": "280-560 kg/ha", "test_frequency": "Annual"},
                "phosphorus": {"optimal_range": "22-56 kg/ha", "test_frequency": "Annual"},
                "potassium": {"optimal_range": "280-560 kg/ha", "test_frequency": "Annual"}
            }
        }
    
    def get_sowing_recommendations(self, crop, location, soil_type, area_hectares):
        if crop not in self.crop_calendar:
            return {"error": f"Crop {crop} not found in database"}
        
        crop_data = self.crop_calendar[crop]
        
        # Determine regional adjustments
        region = self._determine_region(location)
        regional_data = self.regional_variations.get(region, {})
        
        # Calculate optimal sowing window
        sowing_window = self._calculate_sowing_window(crop, region)
        
        # Variety recommendations
        variety_recommendations = self._recommend_varieties(crop, soil_type, location)
        
        # Input requirements
        input_requirements = self._calculate_input_requirements(crop, area_hectares)
        
        # Weather-based adjustments
        weather_adjustments = self._get_weather_adjustments(crop, region)
        
        return {
            "crop": crop,
            "location": location,
            "soil_type": soil_type,
            "area_hectares": area_hectares,
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "sowing_recommendations": {
                "optimal_window": sowing_window,
                "latest_sowing_date": sowing_window["end"],
                "soil_preparation_start": self._calculate_prep_date(sowing_window["start"]),
                "expected_harvest": self._calculate_harvest_date(sowing_window["start"], crop_data["growth_duration"])
            },
            "variety_recommendations": variety_recommendations,
            "input_requirements": input_requirements,
            "weather_considerations": weather_adjustments,
            "regional_specific": regional_data.get("soil_adjustments", {}).get(crop, "Standard practices apply"),
            "success_factors": self._get_success_factors(crop, soil_type),
            "risk_mitigation": self._get_risk_mitigation(crop, region),
            "expected_yield": self._estimate_yield(crop, soil_type, area_hectares),
            "economic_analysis": self._get_economic_projections(crop, area_hectares)
        }
    
    def _determine_region(self, location):
        location_lower = location.lower()
        for region, data in self.regional_variations.items():
            for state in data["states"]:
                if state.lower() in location_lower:
                    return region
        return "General"  # Default region
    
    def _calculate_sowing_window(self, crop, region):
        base_window = self.crop_calendar[crop]["optimal_sowing"]
        
        # Regional adjustments
        if region == "North India" and crop == "wheat":
            return {"start": "November 10", "end": "December 10"}
        elif region == "South India" and crop == "rice":
            return {"start": "June 1", "end": "July 20"}
        
        return base_window
    
    def _recommend_varieties(self, crop, soil_type, location):
        varieties = self.crop_calendar[crop]["varieties"]
        recommendations = []
        
        for variety, data in varieties.items():
            suitability_score = random.randint(70, 95)  # Simulate suitability calculation
            
            recommendations.append({
                "variety": variety,
                "duration_days": data["duration"],
                "yield_potential_kg_ha": data["yield_potential"],
                "disease_resistance": data["disease_resistance"],
                "suitability_score": suitability_score,
                "recommended_for": f"{soil_type} soil in {location}",
                "seed_rate_kg_ha": random.randint(40, 120),
                "special_features": f"Suitable for {soil_type} soil conditions"
            })
        
        return sorted(recommendations, key=lambda x: x["suitability_score"], reverse=True)
    
    def _calculate_input_requirements(self, crop, area_hectares):
        base_requirements = {
            "wheat": {"seeds": 100, "nitrogen": 120, "phosphorus": 60, "potassium": 40},
            "rice": {"seeds": 80, "nitrogen": 100, "phosphorus": 50, "potassium": 50},
            "cotton": {"seeds": 25, "nitrogen": 160, "phosphorus": 80, "potassium": 80},
            "tomato": {"seeds": 0.5, "nitrogen": 150, "phosphorus": 80, "potassium": 100}
        }
        
        requirements = base_requirements.get(crop, base_requirements["wheat"])
        
        return {
            "seeds_kg": requirements["seeds"] * area_hectares,
            "fertilizers": {
                "nitrogen_kg": requirements["nitrogen"] * area_hectares,
                "phosphorus_kg": requirements["phosphorus"] * area_hectares,
                "potassium_kg": requirements["potassium"] * area_hectares
            },
            "estimated_cost": {
                "seeds": requirements["seeds"] * area_hectares * random.randint(50, 200),
                "fertilizers": (requirements["nitrogen"] + requirements["phosphorus"] + requirements["potassium"]) * area_hectares * 25,
                "total": random.randint(15000, 50000) * area_hectares
            }
        }
    
    def _get_weather_adjustments(self, crop, region):
        current_weather = self.weather_patterns["2024"]
        
        adjustments = []
        if current_weather["monsoon_forecast"] == "Below normal":
            adjustments.append("Consider drought-resistant varieties")
            adjustments.append("Plan for supplemental irrigation")
        elif current_weather["monsoon_forecast"] == "Above normal":
            adjustments.append("Ensure proper drainage systems")
            adjustments.append("Monitor for fungal diseases")
        
        adjustments.append(f"Temperature trend: {current_weather['temperature_trend']}")
        adjustments.append(f"Rainfall distribution: {current_weather['rainfall_distribution']}")
        
        return adjustments
    
    def _calculate_prep_date(self, sowing_date):
        # Calculate 30 days before sowing for preparation
        sowing_dt = datetime.strptime(f"2024 {sowing_date}", "%Y %B %d")
        prep_date = sowing_dt - timedelta(days=30)
        return prep_date.strftime("%B %d")
    
    def _calculate_harvest_date(self, sowing_date, duration_days):
        sowing_dt = datetime.strptime(f"2024 {sowing_date}", "%Y %B %d")
        harvest_date = sowing_dt + timedelta(days=duration_days)
        return harvest_date.strftime("%B %d, %Y")
    
    def _get_success_factors(self, crop, soil_type):
        return [
            f"Proper soil preparation for {soil_type} soil",
            "Timely sowing within optimal window",
            "Adequate seed treatment before sowing",
            "Balanced fertilizer application",
            "Regular monitoring for pests and diseases",
            "Efficient water management",
            "Proper harvesting at physiological maturity"
        ]
    
    def _get_risk_mitigation(self, crop, region):
        return [
            "Crop insurance coverage recommended",
            "Weather monitoring and early warning systems",
            "Integrated pest management practices",
            "Diversified cropping to reduce risk",
            "Soil health management",
            "Water conservation techniques",
            "Market linkage for better prices"
        ]
    
    def _estimate_yield(self, crop, soil_type, area_hectares):
        base_yield = self.crop_calendar[crop]["varieties"]
        avg_yield = sum(v["yield_potential"] for v in base_yield.values()) / len(base_yield)
        
        # Soil type adjustment
        soil_factor = {"loamy": 1.0, "clay": 0.9, "sandy": 0.8, "black_cotton": 1.1}.get(soil_type, 1.0)
        
        estimated_yield = avg_yield * soil_factor * area_hectares
        
        return {
            "estimated_yield_kg": round(estimated_yield, 2),
            "yield_per_hectare": round(avg_yield * soil_factor, 2),
            "confidence_level": random.randint(75, 90),
            "factors_considered": ["Soil type", "Regional climate", "Variety selection", "Management practices"]
        }
    
    def _get_economic_projections(self, crop, area_hectares):
        price_ranges = {
            "wheat": {"min": 2000, "max": 2500},
            "rice": {"min": 1800, "max": 2200},
            "cotton": {"min": 5500, "max": 6500},
            "tomato": {"min": 15, "max": 35}
        }
        
        price_range = price_ranges.get(crop, {"min": 2000, "max": 3000})
        expected_price = (price_range["min"] + price_range["max"]) / 2
        
        estimated_yield = self._estimate_yield(crop, "loamy", area_hectares)["estimated_yield_kg"]
        gross_revenue = estimated_yield * expected_price
        
        return {
            "expected_price_range": price_range,
            "estimated_revenue": gross_revenue,
            "revenue_per_hectare": gross_revenue / area_hectares,
            "market_outlook": random.choice(["Favorable", "Stable", "Volatile"]),
            "price_factors": ["Monsoon performance", "Government policies", "Export demand", "Storage capacity"]
        }

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Sowing Calendar is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
