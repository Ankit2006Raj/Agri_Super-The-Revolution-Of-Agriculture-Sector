import json
import random
from datetime import datetime, timedelta

class CropInsurance:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/crop_insurance_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "insurance_schemes": [
                {
                    "scheme_id": "PMFBY001",
                    "name": "Pradhan Mantri Fasal Bima Yojana",
                    "type": "Government",
                    "coverage": "Comprehensive",
                    "premium_rate": {"kharif": 2.0, "rabi": 1.5, "commercial": 5.0},
                    "sum_insured": "Scale of Finance or Actuarial Rate",
                    "risks_covered": ["Drought", "Flood", "Hailstorm", "Cyclone", "Fire", "Disease", "Pest"],
                    "claim_settlement": "Within 2 months",
                    "enrollment_period": "Sowing to 2 weeks after sowing",
                    "subsidy": "Government subsidizes premium"
                },
                {
                    "scheme_id": "WBI001",
                    "name": "Weather Based Crop Insurance",
                    "type": "Private",
                    "coverage": "Weather Parameters",
                    "premium_rate": {"rainfall": 3.0, "temperature": 2.5, "humidity": 2.0},
                    "sum_insured": "Based on historical yield",
                    "risks_covered": ["Rainfall deficit/excess", "Temperature variation", "Humidity"],
                    "claim_settlement": "Automatic based on weather data",
                    "enrollment_period": "Before sowing season",
                    "subsidy": "Partial government subsidy"
                }
            ],
            "insurance_policies": [
                {
                    "policy_id": "POL001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "scheme_id": "PMFBY001",
                    "crop": "Wheat",
                    "area_insured": 5.0,
                    "sum_insured": 75000,
                    "premium_amount": 1125,
                    "farmer_share": 1125,
                    "government_subsidy": 0,
                    "policy_start": "2023-11-01",
                    "policy_end": "2024-04-30",
                    "status": "Active",
                    "claims": []
                },
                {
                    "policy_id": "POL002",
                    "farmer_id": "F002",
                    "farmer_name": "Priya Sharma",
                    "scheme_id": "WBI001",
                    "crop": "Cotton",
                    "area_insured": 8.0,
                    "sum_insured": 120000,
                    "premium_amount": 3600,
                    "farmer_share": 2400,
                    "government_subsidy": 1200,
                    "policy_start": "2023-06-01",
                    "policy_end": "2023-12-31",
                    "status": "Claimed",
                    "claims": [
                        {
                            "claim_id": "CLM001",
                            "claim_date": "2023-09-15",
                            "cause": "Drought",
                            "claim_amount": 45000,
                            "status": "Settled",
                            "settlement_date": "2023-11-10"
                        }
                    ]
                }
            ],
            "claim_history": [
                {
                    "claim_id": "CLM001",
                    "policy_id": "POL002",
                    "farmer_name": "Priya Sharma",
                    "crop": "Cotton",
                    "cause": "Drought",
                    "claim_date": "2023-09-15",
                    "claim_amount": 45000,
                    "documents_submitted": ["Crop cutting experiment", "Revenue records", "Weather data"],
                    "assessment_date": "2023-10-05",
                    "settlement_amount": 45000,
                    "settlement_date": "2023-11-10",
                    "status": "Settled"
                },
                {
                    "claim_id": "CLM002",
                    "policy_id": "POL003",
                    "farmer_name": "Amit Patel",
                    "crop": "Rice",
                    "cause": "Flood",
                    "claim_date": "2023-08-20",
                    "claim_amount": 60000,
                    "documents_submitted": ["Damage assessment report", "Village revenue officer certificate"],
                    "assessment_date": "2023-09-10",
                    "settlement_amount": 55000,
                    "settlement_date": "2023-10-15",
                    "status": "Settled"
                }
            ],
            "risk_assessment": [
                {
                    "district": "Ludhiana, Punjab",
                    "crop": "Wheat",
                    "risk_factors": {
                        "drought": {"probability": 15, "impact": "Medium"},
                        "flood": {"probability": 10, "impact": "High"},
                        "hailstorm": {"probability": 8, "impact": "High"},
                        "pest_attack": {"probability": 20, "impact": "Medium"},
                        "disease": {"probability": 12, "impact": "Medium"}
                    },
                    "overall_risk": "Medium",
                    "recommended_coverage": 80000,
                    "premium_rate": 1.8
                },
                {
                    "district": "Nashik, Maharashtra",
                    "crop": "Cotton",
                    "risk_factors": {
                        "drought": {"probability": 25, "impact": "High"},
                        "flood": {"probability": 15, "impact": "High"},
                        "bollworm": {"probability": 30, "impact": "High"},
                        "pink_bollworm": {"probability": 25, "impact": "Medium"},
                        "whitefly": {"probability": 20, "impact": "Medium"}
                    },
                    "overall_risk": "High",
                    "recommended_coverage": 120000,
                    "premium_rate": 4.5
                }
            ],
            "insurance_statistics": {
                "total_policies": 45000,
                "total_sum_insured": 6750000000,
                "total_premium": 202500000,
                "claims_received": 3500,
                "claims_settled": 3200,
                "settlement_ratio": 91.4,
                "average_claim_amount": 42000,
                "total_claims_paid": 134400000
            }
        }
    
    def calculate_premium(self, crop, area, sum_insured, scheme_type="PMFBY"):
        rates = {
            "PMFBY": {"kharif": 2.0, "rabi": 1.5, "commercial": 5.0},
            "WBI": {"rainfall": 3.0, "temperature": 2.5, "humidity": 2.0}
        }
        
        # Determine crop season
        season = "kharif" if crop in ["Rice", "Cotton", "Sugarcane"] else "rabi"
        if crop in ["Fruits", "Vegetables"]:
            season = "commercial"
        
        rate = rates[scheme_type].get(season, 2.0)
        premium = (sum_insured * rate) / 100
        
        return {
            "premium_amount": premium,
            "farmer_share": premium if scheme_type == "WBI" else premium,
            "government_subsidy": 0 if scheme_type == "WBI" else premium * 0.5,
            "rate_percent": rate
        }
    
    def assess_claim(self, policy_id, damage_percent, cause):
        # Find policy
        policy = None
        for p in self.data["insurance_policies"]:
            if p["policy_id"] == policy_id:
                policy = p
                break
        
        if not policy:
            return {"error": "Policy not found"}
        
        # Calculate claim amount
        claim_amount = (policy["sum_insured"] * damage_percent) / 100
        
        # Apply deductibles and limits
        if damage_percent < 20:
            claim_amount = 0  # Minimum threshold
        elif damage_percent > 90:
            claim_amount = policy["sum_insured"]  # Maximum payout
        
        return {
            "eligible_amount": claim_amount,
            "damage_percent": damage_percent,
            "cause": cause,
            "processing_time": "45-60 days",
            "required_documents": [
                "Crop cutting experiment report",
                "Village revenue officer certificate",
                "Weather data (if applicable)",
                "Photographs of damaged crop"
            ]
        }
    
    def get_insurance_schemes(self):
        return self.data["insurance_schemes"]
    
    def get_policies(self):
        return self.data["insurance_policies"]
    
    def get_claim_history(self):
        return self.data["claim_history"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Crop Insurance is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
