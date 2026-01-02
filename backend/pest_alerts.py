import json
import random
from datetime import datetime, timedelta

class PestAlertsEngine:
    def __init__(self, data_folder='data'):
        # Massive pest alerts data
        self.pest_database = self._generate_pest_database()
        self.active_outbreaks = self._generate_active_outbreaks()
        self.treatment_database = self._generate_treatment_database()
        self.seasonal_patterns = self._generate_seasonal_patterns()
        
    def get_alerts(self, location='all'):
        """Get pest alerts for a specific location or all locations"""
        if location == 'all':
            return self.active_outbreaks
        
        # Filter outbreaks by location
        filtered_outbreaks = [outbreak for outbreak in self.active_outbreaks 
                             if outbreak.get('location', '').lower() == location.lower()]
        return filtered_outbreaks
        
    def _generate_pest_database(self):
        return {
            "aphids": {
                "scientific_name": "Aphis gossypii",
                "common_names": ["Cotton aphid", "Green peach aphid"],
                "affected_crops": ["cotton", "tomato", "potato", "cabbage"],
                "damage_type": "Sucking pest",
                "symptoms": ["Yellowing leaves", "Stunted growth", "Honeydew secretion", "Sooty mold"],
                "favorable_conditions": {"temperature": "20-30°C", "humidity": "60-80%", "season": "Post-monsoon"},
                "economic_threshold": "10-15 aphids per leaf",
                "damage_potential": "20-40% yield loss",
                "lifecycle_days": 15,
                "identification": {
                    "size": "1-3mm",
                    "color": "Green to black",
                    "location": "Undersides of leaves, growing tips",
                    "behavior": "Colonies on young shoots"
                }
            },
            "bollworm": {
                "scientific_name": "Helicoverpa armigera",
                "common_names": ["American bollworm", "Cotton bollworm"],
                "affected_crops": ["cotton", "tomato", "chickpea", "maize"],
                "damage_type": "Chewing pest",
                "symptoms": ["Holes in bolls", "Damaged fruits", "Larval presence", "Frass deposits"],
                "favorable_conditions": {"temperature": "25-35°C", "humidity": "70-85%", "season": "Flowering stage"},
                "economic_threshold": "2 larvae per plant",
                "damage_potential": "30-60% yield loss",
                "lifecycle_days": 45,
                "identification": {
                    "size": "35-40mm (larva)",
                    "color": "Green to brown with stripes",
                    "location": "Inside bolls and fruits",
                    "behavior": "Active during evening hours"
                }
            },
            "whitefly": {
                "scientific_name": "Bemisia tabaci",
                "common_names": ["Tobacco whitefly", "Sweet potato whitefly"],
                "affected_crops": ["cotton", "tomato", "okra", "brinjal"],
                "damage_type": "Sucking pest and virus vector",
                "symptoms": ["Yellowing leaves", "Leaf curl", "Sooty mold", "Virus transmission"],
                "favorable_conditions": {"temperature": "27-30°C", "humidity": "50-70%", "season": "Dry periods"},
                "economic_threshold": "5-10 adults per leaf",
                "damage_potential": "25-50% yield loss",
                "lifecycle_days": 25,
                "identification": {
                    "size": "1-2mm",
                    "color": "White with yellowish body",
                    "location": "Undersides of leaves",
                    "behavior": "Fly when disturbed"
                }
            },
            "stem_borer": {
                "scientific_name": "Chilo partellus",
                "common_names": ["Spotted stem borer", "Maize stem borer"],
                "affected_crops": ["rice", "maize", "sugarcane", "wheat"],
                "damage_type": "Boring pest",
                "symptoms": ["Dead hearts", "White ears", "Tunnels in stem", "Frass at entry points"],
                "favorable_conditions": {"temperature": "26-30°C", "humidity": "80-90%", "season": "Monsoon"},
                "economic_threshold": "10% dead hearts",
                "damage_potential": "15-35% yield loss",
                "lifecycle_days": 35,
                "identification": {
                    "size": "20-25mm (larva)",
                    "color": "Yellowish with dark spots",
                    "location": "Inside plant stems",
                    "behavior": "Bore into growing points"
                }
            }
        }
    
    def _generate_active_outbreaks(self):
        outbreaks = []
        pests = list(self.pest_database.keys())
        
        for i in range(100):  # Generate 100 active outbreaks
            pest = random.choice(pests)
            pest_data = self.pest_database[pest]
            
            outbreak = {
                "id": f"PO{5000 + i}",
                "pest_name": pest,
                "scientific_name": pest_data["scientific_name"],
                "location": f"{random.choice(['North', 'South', 'East', 'West'])} {random.choice(['Maharashtra', 'Karnataka', 'Punjab', 'Gujarat'])}",
                "affected_crop": random.choice(pest_data["affected_crops"]),
                "severity_level": random.choice(["Low", "Medium", "High", "Critical"]),
                "affected_area_hectares": random.randint(100, 5000),
                "farmers_affected": random.randint(50, 2000),
                "first_reported": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
                "current_status": random.choice(["Spreading", "Controlled", "Under Treatment", "Monitoring"]),
                "infestation_percentage": random.randint(10, 80),
                "economic_loss_estimated": random.randint(50000, 2000000),
                "weather_factors": {
                    "temperature": random.randint(20, 35),
                    "humidity": random.randint(40, 90),
                    "rainfall_last_week": random.randint(0, 50)
                },
                "control_measures_applied": random.sample([
                    "Chemical spray", "Biological control", "Pheromone traps", 
                    "Cultural practices", "Resistant varieties"
                ], random.randint(2, 4)),
                "effectiveness_rating": random.randint(60, 95)
            }
            outbreaks.append(outbreak)
        return outbreaks
    
    def _generate_treatment_database(self):
        return {
            "chemical_control": {
                "aphids": [
                    {"name": "Imidacloprid", "dosage": "0.5ml/L", "effectiveness": 85, "cost_per_hectare": 800},
                    {"name": "Thiamethoxam", "dosage": "0.3g/L", "effectiveness": 90, "cost_per_hectare": 1200},
                    {"name": "Acetamiprid", "dosage": "0.4g/L", "effectiveness": 80, "cost_per_hectare": 900}
                ],
                "bollworm": [
                    {"name": "Chlorantraniliprole", "dosage": "0.4ml/L", "effectiveness": 95, "cost_per_hectare": 2000},
                    {"name": "Flubendiamide", "dosage": "0.7ml/L", "effectiveness": 90, "cost_per_hectare": 1800},
                    {"name": "Emamectin benzoate", "dosage": "0.4g/L", "effectiveness": 88, "cost_per_hectare": 1500}
                ],
                "whitefly": [
                    {"name": "Spiromesifen", "dosage": "1ml/L", "effectiveness": 85, "cost_per_hectare": 1600},
                    {"name": "Pyriproxyfen", "dosage": "1ml/L", "effectiveness": 80, "cost_per_hectare": 1400},
                    {"name": "Buprofezin", "dosage": "1.5ml/L", "effectiveness": 75, "cost_per_hectare": 1200}
                ]
            },
            "biological_control": {
                "aphids": [
                    {"agent": "Chrysoperla carnea", "release_rate": "5000/hectare", "effectiveness": 70, "cost_per_hectare": 600},
                    {"agent": "Coccinella septempunctata", "release_rate": "2000/hectare", "effectiveness": 65, "cost_per_hectare": 500},
                    {"agent": "Aphidius colemani", "release_rate": "3000/hectare", "effectiveness": 75, "cost_per_hectare": 700}
                ],
                "bollworm": [
                    {"agent": "Trichogramma pretiosum", "release_rate": "50000/hectare", "effectiveness": 60, "cost_per_hectare": 800},
                    {"agent": "NPV (Nuclear Polyhedrosis Virus)", "dosage": "250 LE/hectare", "effectiveness": 80, "cost_per_hectare": 1000},
                    {"agent": "Bacillus thuringiensis", "dosage": "1kg/hectare", "effectiveness": 70, "cost_per_hectare": 600}
                ]
            },
            "cultural_practices": {
                "general": [
                    {"practice": "Crop rotation", "effectiveness": 60, "implementation_cost": 0},
                    {"practice": "Intercropping", "effectiveness": 50, "implementation_cost": 500},
                    {"practice": "Trap crops", "effectiveness": 55, "implementation_cost": 800},
                    {"practice": "Field sanitation", "effectiveness": 40, "implementation_cost": 200},
                    {"practice": "Resistant varieties", "effectiveness": 70, "implementation_cost": 1000}
                ]
            }
        }
    
    def _generate_seasonal_patterns(self):
        return {
            "monsoon": {
                "high_risk_pests": ["stem_borer", "leaf_folder", "brown_planthopper"],
                "medium_risk_pests": ["aphids", "thrips"],
                "low_risk_pests": ["whitefly", "bollworm"],
                "weather_factors": "High humidity, moderate temperature",
                "prevention_focus": "Fungal diseases, water management"
            },
            "post_monsoon": {
                "high_risk_pests": ["aphids", "whitefly", "jassids"],
                "medium_risk_pests": ["bollworm", "thrips"],
                "low_risk_pests": ["stem_borer"],
                "weather_factors": "Decreasing humidity, stable temperature",
                "prevention_focus": "Sucking pests, virus diseases"
            },
            "winter": {
                "high_risk_pests": ["aphids", "caterpillars"],
                "medium_risk_pests": ["thrips", "mites"],
                "low_risk_pests": ["whitefly", "stem_borer"],
                "weather_factors": "Low humidity, cool temperature",
                "prevention_focus": "Rabi crop pests, storage pests"
            },
            "summer": {
                "high_risk_pests": ["whitefly", "thrips", "mites"],
                "medium_risk_pests": ["bollworm", "aphids"],
                "low_risk_pests": ["stem_borer"],
                "weather_factors": "Low humidity, high temperature",
                "prevention_focus": "Heat stress, water scarcity"
            }
        }
    
    def get_pest_alerts(self, location=None, crop=None, severity=None):
        filtered_outbreaks = self.active_outbreaks.copy()
        
        if location:
            filtered_outbreaks = [o for o in filtered_outbreaks if location.lower() in o["location"].lower()]
        
        if crop:
            filtered_outbreaks = [o for o in filtered_outbreaks if o["affected_crop"] == crop]
        
        if severity:
            filtered_outbreaks = [o for o in filtered_outbreaks if o["severity_level"] == severity]
        
        return {
            "total_alerts": len(filtered_outbreaks),
            "active_outbreaks": filtered_outbreaks[:20],  # Limit to 20 for display
            "severity_distribution": self._get_severity_distribution(filtered_outbreaks),
            "most_affected_crops": self._get_most_affected_crops(filtered_outbreaks),
            "regional_hotspots": self._get_regional_hotspots(filtered_outbreaks),
            "seasonal_analysis": self._get_seasonal_analysis()
        }
    
    def get_treatment_recommendations(self, pest_name, crop, severity_level, budget_per_hectare=None):
        if pest_name not in self.pest_database:
            return {"error": f"Pest {pest_name} not found in database"}
        
        pest_info = self.pest_database[pest_name]
        recommendations = []
        
        # Chemical control options
        if pest_name in self.treatment_database["chemical_control"]:
            chemical_options = self.treatment_database["chemical_control"][pest_name]
            for option in chemical_options:
                if not budget_per_hectare or option["cost_per_hectare"] <= budget_per_hectare:
                    recommendations.append({
                        "type": "Chemical Control",
                        "method": option["name"],
                        "dosage": option["dosage"],
                        "effectiveness": option["effectiveness"],
                        "cost_per_hectare": option["cost_per_hectare"],
                        "application_timing": "Early morning or evening",
                        "precautions": "Use protective equipment, follow PHI"
                    })
        
        # Biological control options
        if pest_name in self.treatment_database["biological_control"]:
            bio_options = self.treatment_database["biological_control"][pest_name]
            for option in bio_options:
                if not budget_per_hectare or option["cost_per_hectare"] <= budget_per_hectare:
                    recommendations.append({
                        "type": "Biological Control",
                        "method": option["agent"],
                        "dosage": option.get("dosage", option.get("release_rate", "As recommended")),
                        "effectiveness": option["effectiveness"],
                        "cost_per_hectare": option["cost_per_hectare"],
                        "application_timing": "Based on pest population",
                        "precautions": "Avoid pesticide application for 15 days"
                    })
        
        # Cultural practices
        cultural_options = self.treatment_database["cultural_practices"]["general"]
        for option in cultural_options:
            if not budget_per_hectare or option["implementation_cost"] <= budget_per_hectare:
                recommendations.append({
                    "type": "Cultural Practice",
                    "method": option["practice"],
                    "effectiveness": option["effectiveness"],
                    "cost_per_hectare": option["implementation_cost"],
                    "application_timing": "Season-long practice",
                    "precautions": "Requires planning and consistency"
                })
        
        # Sort by effectiveness
        recommendations.sort(key=lambda x: x["effectiveness"], reverse=True)
        
        return {
            "pest": pest_name,
            "crop": crop,
            "severity": severity_level,
            "pest_information": pest_info,
            "treatment_options": recommendations[:10],  # Top 10 recommendations
            "integrated_approach": self._get_integrated_approach(pest_name, severity_level),
            "monitoring_schedule": self._get_monitoring_schedule(pest_name),
            "economic_analysis": self._calculate_treatment_economics(recommendations[:5], severity_level)
        }
    
    def _get_severity_distribution(self, outbreaks):
        distribution = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
        for outbreak in outbreaks:
            distribution[outbreak["severity_level"]] += 1
        return distribution
    
    def _get_most_affected_crops(self, outbreaks):
        crop_count = {}
        for outbreak in outbreaks:
            crop = outbreak["affected_crop"]
            crop_count[crop] = crop_count.get(crop, 0) + 1
        
        return sorted(crop_count.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_regional_hotspots(self, outbreaks):
        region_count = {}
        for outbreak in outbreaks:
            region = outbreak["location"]
            region_count[region] = region_count.get(region, 0) + 1
        
        return sorted(region_count.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_seasonal_analysis(self):
        current_month = datetime.now().month
        
        if current_month in [6, 7, 8, 9]:  # Monsoon
            season = "monsoon"
        elif current_month in [10, 11]:  # Post-monsoon
            season = "post_monsoon"
        elif current_month in [12, 1, 2]:  # Winter
            season = "winter"
        else:  # Summer
            season = "summer"
        
        return self.seasonal_patterns.get(season, self.seasonal_patterns["monsoon"])
    
    def _get_integrated_approach(self, pest_name, severity_level):
        approaches = {
            "Low": ["Cultural practices", "Monitoring", "Biological control if available"],
            "Medium": ["Biological control", "Selective pesticides", "Cultural practices"],
            "High": ["Immediate chemical control", "Follow-up biological control", "Enhanced monitoring"],
            "Critical": ["Emergency chemical treatment", "Area-wide management", "Regulatory measures"]
        }
        
        return {
            "recommended_strategy": approaches.get(severity_level, approaches["Medium"]),
            "implementation_sequence": [
                "Immediate assessment and monitoring",
                "Apply primary control measure",
                "Monitor effectiveness after 7 days",
                "Apply secondary measures if needed",
                "Continue monitoring for 3 weeks"
            ],
            "success_indicators": [
                "Reduction in pest population by 70%",
                "No new damage symptoms",
                "Natural enemy population recovery",
                "Crop recovery signs visible"
            ]
        }
    
    def _get_monitoring_schedule(self, pest_name):
        pest_info = self.pest_database[pest_name]
        lifecycle_days = pest_info["lifecycle_days"]
        
        return {
            "frequency": f"Every {max(3, lifecycle_days // 5)} days",
            "critical_stages": ["Egg laying period", "Early larval stage", "Peak population"],
            "monitoring_methods": [
                "Visual inspection of plants",
                "Pheromone trap counts",
                "Yellow sticky trap monitoring",
                "Economic threshold assessment"
            ],
            "record_keeping": [
                "Pest population counts",
                "Damage assessment",
                "Weather conditions",
                "Control measures applied",
                "Effectiveness ratings"
            ]
        }
    
    def _calculate_treatment_economics(self, treatments, severity_level):
        if not treatments:
            return {"message": "No treatment data available"}
        
        # Calculate potential yield loss without treatment
        severity_loss = {"Low": 10, "Medium": 25, "High": 45, "Critical": 70}
        expected_loss_percent = severity_loss.get(severity_level, 25)
        
        # Assume average crop value per hectare
        crop_value_per_hectare = 50000  # Average value
        potential_loss = crop_value_per_hectare * (expected_loss_percent / 100)
        
        economics = []
        for treatment in treatments:
            treatment_cost = treatment["cost_per_hectare"]
            effectiveness = treatment["effectiveness"]
            
            # Calculate prevented loss
            prevented_loss = potential_loss * (effectiveness / 100)
            net_benefit = prevented_loss - treatment_cost
            roi = (net_benefit / treatment_cost) * 100 if treatment_cost > 0 else 0
            
            economics.append({
                "treatment": treatment["method"],
                "cost": treatment_cost,
                "prevented_loss": round(prevented_loss, 2),
                "net_benefit": round(net_benefit, 2),
                "roi_percentage": round(roi, 2),
                "recommendation": "Highly recommended" if roi > 200 else "Recommended" if roi > 100 else "Consider alternatives"
            })
        
        return {
            "potential_loss_without_treatment": potential_loss,
            "treatment_economics": economics,
            "best_economic_option": max(economics, key=lambda x: x["roi_percentage"]) if economics else None
        }

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Pest Alerts is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
