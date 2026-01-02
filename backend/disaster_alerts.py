import json
import random
from datetime import datetime, timedelta

class DisasterAlertsEngine:
    def __init__(self, data_folder='data'):
        # Massive disaster alerts data
        self.active_alerts = self._generate_active_alerts()
        self.historical_disasters = self._generate_historical_data()
        self.risk_zones = self._generate_risk_zones()
        self.preparedness_measures = self._generate_preparedness_data()
        
    def _generate_active_alerts(self):
        alert_types = ["drought", "flood", "cyclone", "hailstorm", "frost", "heat_wave", "pest_outbreak"]
        severity_levels = ["Low", "Medium", "High", "Critical"]
        
        alerts = []
        for i in range(50):  # Generate 50 active alerts
            alert = {
                "id": f"DA{3000 + i}",
                "type": random.choice(alert_types),
                "severity": random.choice(severity_levels),
                "location": f"District {random.choice(['Pune', 'Mumbai', 'Nashik', 'Aurangabad', 'Nagpur'])}",
                "state": random.choice(["Maharashtra", "Karnataka", "Gujarat", "Rajasthan", "Punjab"]),
                "issued_date": (datetime.now() - timedelta(days=random.randint(0, 7))).strftime("%Y-%m-%d"),
                "valid_until": (datetime.now() + timedelta(days=random.randint(1, 14))).strftime("%Y-%m-%d"),
                "affected_crops": random.sample(["wheat", "rice", "cotton", "sugarcane", "tomato", "onion"], random.randint(2, 4)),
                "expected_impact": random.choice(["Minimal", "Moderate", "Severe", "Devastating"]),
                "confidence_level": random.randint(70, 95),
                "source": random.choice(["IMD", "State Agriculture Dept", "Satellite Data", "Local Observers"]),
                "description": f"Weather alert for potential {alert_types[alert_types.index(random.choice(alert_types))].replace('_', ' ')} conditions",
                "recommended_actions": self._get_recommended_actions(random.choice(alert_types)),
                "contact_numbers": ["1800-180-1551", "108", "1077"]
            }
            alerts.append(alert)
        return alerts
    
    def _generate_historical_data(self):
        disasters = []
        disaster_types = ["drought", "flood", "cyclone", "hailstorm", "locust_attack"]
        
        for i in range(200):  # Generate 200 historical disasters
            disaster = {
                "id": f"HD{4000 + i}",
                "type": random.choice(disaster_types),
                "date": (datetime.now() - timedelta(days=random.randint(30, 1825))).strftime("%Y-%m-%d"),
                "location": f"{random.choice(['North', 'South', 'East', 'West', 'Central'])} {random.choice(['Maharashtra', 'Karnataka', 'Gujarat'])}",
                "affected_area_hectares": random.randint(1000, 50000),
                "crop_loss_percentage": random.randint(10, 80),
                "economic_loss_crores": random.randint(50, 2000),
                "farmers_affected": random.randint(500, 25000),
                "recovery_time_months": random.randint(3, 24),
                "government_compensation": random.randint(1000, 50000),
                "lessons_learned": f"Improved early warning systems needed for {random.choice(disaster_types)}"
            }
            disasters.append(disaster)
        return disasters
    
    def _generate_risk_zones(self):
        return {
            "drought_prone": {
                "districts": ["Ahmednagar", "Beed", "Osmanabad", "Latur", "Solapur"],
                "risk_level": "High",
                "monsoon_dependency": 85,
                "groundwater_depletion": "Critical",
                "recommended_crops": ["jowar", "bajra", "tur", "cotton"],
                "mitigation_measures": ["Drip irrigation", "Rainwater harvesting", "Drought-resistant varieties"]
            },
            "flood_prone": {
                "districts": ["Kolhapur", "Sangli", "Satara", "Pune", "Nashik"],
                "risk_level": "Medium",
                "rainfall_average": 1200,
                "drainage_capacity": "Moderate",
                "recommended_crops": ["rice", "sugarcane", "banana"],
                "mitigation_measures": ["Improved drainage", "Flood-resistant varieties", "Early warning systems"]
            },
            "cyclone_prone": {
                "districts": ["Mumbai", "Thane", "Raigad", "Ratnagiri", "Sindhudurg"],
                "risk_level": "High",
                "cyclone_season": "June-November",
                "wind_speed_risk": "150+ kmph",
                "recommended_crops": ["coconut", "cashew", "mango"],
                "mitigation_measures": ["Windbreaks", "Sturdy crop support", "Insurance coverage"]
            }
        }
    
    def _generate_preparedness_data(self):
        return {
            "drought": {
                "early_indicators": ["Delayed monsoon", "Reduced soil moisture", "Declining groundwater"],
                "immediate_actions": ["Water conservation", "Mulching", "Stress-resistant varieties"],
                "long_term_measures": ["Watershed development", "Micro-irrigation", "Crop diversification"],
                "emergency_contacts": ["District Collector", "Agriculture Officer", "Water Department"]
            },
            "flood": {
                "early_indicators": ["Heavy rainfall forecast", "River water levels", "Upstream dam releases"],
                "immediate_actions": ["Drainage clearing", "Harvest ready crops", "Livestock evacuation"],
                "long_term_measures": ["Flood-resistant infrastructure", "Crop insurance", "Alternative livelihoods"],
                "emergency_contacts": ["Disaster Management", "Revenue Department", "Police Control Room"]
            },
            "pest_outbreak": {
                "early_indicators": ["Unusual insect activity", "Crop damage patterns", "Weather conditions"],
                "immediate_actions": ["Integrated pest management", "Biological control", "Targeted spraying"],
                "long_term_measures": ["Resistant varieties", "Crop rotation", "Natural predator conservation"],
                "emergency_contacts": ["Plant Protection Officer", "Krishi Vigyan Kendra", "Extension Officer"]
            }
        }
    
    def get_alerts_by_location(self, location, alert_type=None):
        filtered_alerts = [alert for alert in self.active_alerts if location.lower() in alert["location"].lower()]
        
        if alert_type:
            filtered_alerts = [alert for alert in filtered_alerts if alert["type"] == alert_type]
        
        return {
            "location": location,
            "total_alerts": len(filtered_alerts),
            "active_alerts": filtered_alerts,
            "risk_assessment": self._assess_location_risk(location),
            "preparedness_status": self._get_preparedness_status(location)
        }
    
    def _get_recommended_actions(self, alert_type):
        action_map = {
            "drought": ["Implement water conservation", "Use drought-resistant varieties", "Apply mulching"],
            "flood": ["Ensure proper drainage", "Harvest mature crops", "Relocate livestock"],
            "cyclone": ["Secure farm structures", "Harvest ready crops", "Protect livestock"],
            "hailstorm": ["Use protective nets", "Harvest if possible", "Seek shelter"],
            "frost": ["Use frost protection methods", "Light smudge fires", "Cover sensitive crops"],
            "heat_wave": ["Increase irrigation frequency", "Provide shade", "Adjust working hours"],
            "pest_outbreak": ["Apply targeted pesticides", "Use biological control", "Monitor regularly"]
        }
        return action_map.get(alert_type, ["Monitor situation", "Contact local authorities", "Follow official guidelines"])
    
    def _assess_location_risk(self, location):
        # Simulate risk assessment based on location
        risk_factors = {
            "drought_risk": random.randint(20, 80),
            "flood_risk": random.randint(10, 70),
            "cyclone_risk": random.randint(5, 60),
            "pest_risk": random.randint(15, 50),
            "overall_risk": random.randint(30, 75)
        }
        
        risk_level = "Low"
        if risk_factors["overall_risk"] > 60:
            risk_level = "High"
        elif risk_factors["overall_risk"] > 40:
            risk_level = "Medium"
        
        return {
            "risk_factors": risk_factors,
            "overall_risk_level": risk_level,
            "primary_threats": ["drought", "pest_outbreak"] if risk_factors["drought_risk"] > 50 else ["flood", "cyclone"],
            "seasonal_vulnerability": "Monsoon season" if risk_factors["flood_risk"] > 40 else "Summer season"
        }
    
    def _get_preparedness_status(self, location):
        return {
            "early_warning_systems": random.choice(["Excellent", "Good", "Needs Improvement"]),
            "emergency_response_time": f"{random.randint(2, 24)} hours",
            "resource_availability": random.choice(["Adequate", "Limited", "Insufficient"]),
            "community_awareness": random.choice(["High", "Medium", "Low"]),
            "insurance_coverage": f"{random.randint(30, 85)}% of farmers covered"
        }
    
    def create_custom_alert(self, alert_data):
        new_alert = {
            "id": f"CA{len(self.active_alerts) + 5000}",
            "type": "custom",
            "created_by": "farmer",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            **alert_data
        }
        self.active_alerts.append(new_alert)
        return new_alert
        
    def get_alerts(self, location='all'):
        if location.lower() == 'all':
            return self.active_alerts
        else:
            return [alert for alert in self.active_alerts if location.lower() in alert["location"].lower()]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Disaster Alerts is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
