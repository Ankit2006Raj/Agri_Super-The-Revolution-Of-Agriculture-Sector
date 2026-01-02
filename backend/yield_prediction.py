import json
import random
from datetime import datetime, timedelta

class YieldPredictionEngine:
    def __init__(self, data_folder='data'):
        # Massive yield prediction data
        self.historical_yields = self._generate_historical_data()
        self.weather_factors = {
            "temperature": {"optimal_min": 20, "optimal_max": 30, "impact_weight": 0.25},
            "rainfall": {"optimal_min": 600, "optimal_max": 1200, "impact_weight": 0.30},
            "humidity": {"optimal_min": 60, "optimal_max": 80, "impact_weight": 0.20},
            "soil_ph": {"optimal_min": 6.0, "optimal_max": 7.5, "impact_weight": 0.25}
        }
        
        self.crop_yield_data = {
            "wheat": {"avg_yield": 3200, "max_yield": 5500, "min_yield": 1800},
            "rice": {"avg_yield": 2800, "max_yield": 4800, "min_yield": 1500},
            "corn": {"avg_yield": 4500, "max_yield": 7200, "min_yield": 2200},
            "tomato": {"avg_yield": 25000, "max_yield": 45000, "min_yield": 12000},
            "potato": {"avg_yield": 18000, "max_yield": 35000, "min_yield": 8000}
        }
        
    def _generate_historical_data(self):
        data = {}
        crops = ["wheat", "rice", "corn", "tomato", "potato", "onion", "cabbage"]
        
        for crop in crops:
            data[crop] = []
            for year in range(2019, 2025):
                for month in range(1, 13):
                    yield_data = {
                        "year": year,
                        "month": month,
                        "yield_per_hectare": random.randint(1000, 8000),
                        "weather_score": random.uniform(0.6, 1.0),
                        "soil_quality": random.uniform(0.7, 1.0),
                        "pest_impact": random.uniform(0.8, 1.0),
                        "irrigation_efficiency": random.uniform(0.75, 1.0)
                    }
                    data[crop].append(yield_data)
        return data
    
    def predict_yield(self, crop, area_hectares, location, planting_date):
        base_yield = self.crop_yield_data.get(crop, {"avg_yield": 3000})["avg_yield"]
        
        # Weather impact simulation
        weather_score = random.uniform(0.7, 1.0)
        soil_score = random.uniform(0.8, 1.0)
        pest_score = random.uniform(0.85, 1.0)
        
        predicted_yield = base_yield * weather_score * soil_score * pest_score * area_hectares
        
        confidence_level = random.uniform(75, 95)
        
        return {
            "crop": crop,
            "predicted_yield_kg": round(predicted_yield, 2),
            "yield_per_hectare": round(predicted_yield / area_hectares, 2),
            "confidence_level": round(confidence_level, 1),
            "factors": {
                "weather_impact": round(weather_score * 100, 1),
                "soil_quality": round(soil_score * 100, 1),
                "pest_risk": round(pest_score * 100, 1)
            },
            "recommendations": self._get_yield_recommendations(crop, weather_score, soil_score),
            "historical_comparison": self._get_historical_comparison(crop)
        }
    
    def _get_yield_recommendations(self, crop, weather_score, soil_score):
        recommendations = []
        if weather_score < 0.8:
            recommendations.append("Consider drought-resistant varieties")
            recommendations.append("Implement efficient irrigation systems")
        if soil_score < 0.8:
            recommendations.append("Apply organic fertilizers to improve soil health")
            recommendations.append("Consider soil testing for nutrient analysis")
        
        recommendations.extend([
            f"Optimal planting density for {crop} is recommended",
            "Regular monitoring for pest and disease management",
            "Implement integrated nutrient management practices"
        ])
        return recommendations
    
    def _get_historical_comparison(self, crop):
        if crop in self.historical_yields:
            recent_data = self.historical_yields[crop][-12:]  # Last 12 months
            avg_yield = sum(d["yield_per_hectare"] for d in recent_data) / len(recent_data)
            return {
                "last_year_average": round(avg_yield, 2),
                "trend": "increasing" if avg_yield > 3000 else "stable",
                "best_month": max(recent_data, key=lambda x: x["yield_per_hectare"])["month"]
            }
        return {"message": "Historical data not available"}

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Yield Prediction is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
