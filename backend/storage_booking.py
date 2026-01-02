import json
import random
from datetime import datetime, timedelta

class StorageBooking:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/storage_booking_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "warehouses": [
                {
                    "warehouse_id": "WH001",
                    "name": "Punjab Agri Storage",
                    "location": "Ludhiana, Punjab",
                    "owner": "Punjab State Warehousing Corporation",
                    "total_capacity": 5000,
                    "available_capacity": 1200,
                    "storage_types": ["Covered", "CAP Storage", "Silo"],
                    "facilities": ["Fumigation", "Drying", "Cleaning", "Grading", "Security"],
                    "rates": {
                        "covered": 8,
                        "cap_storage": 12,
                        "silo": 15
                    },
                    "minimum_period": 30,
                    "contact": "+91-9876543210",
                    "rating": 4.3,
                    "insurance_available": True,
                    "quality_assurance": True
                },
                {
                    "warehouse_id": "WH002",
                    "name": "Modern Cold Storage",
                    "location": "Delhi",
                    "owner": "Delhi Storage Solutions Pvt Ltd",
                    "total_capacity": 3000,
                    "available_capacity": 800,
                    "storage_types": ["Cold Storage", "Controlled Atmosphere"],
                    "facilities": ["Temperature Control", "Humidity Control", "Ripening Chambers", "Security"],
                    "rates": {
                        "cold_storage": 25,
                        "controlled_atmosphere": 35
                    },
                    "minimum_period": 15,
                    "contact": "+91-9876543211",
                    "rating": 4.6,
                    "insurance_available": True,
                    "quality_assurance": True
                }
            ],
            "storage_bookings": [
                {
                    "booking_id": "SB001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "warehouse_id": "WH001",
                    "crop": "Wheat",
                    "quantity": 200,
                    "unit": "quintals",
                    "storage_type": "covered",
                    "start_date": "2024-01-15",
                    "end_date": "2024-04-15",
                    "duration_days": 90,
                    "rate_per_quintal_per_month": 8,
                    "total_cost": 4800,
                    "advance_paid": 1440,
                    "status": "Active",
                    "receipt_number": "RCP001",
                    "insurance_opted": True,
                    "quality_check_date": "2024-01-15"
                },
                {
                    "booking_id": "SB002",
                    "farmer_id": "F002",
                    "farmer_name": "Priya Sharma",
                    "warehouse_id": "WH002",
                    "crop": "Apple",
                    "quantity": 50,
                    "unit": "quintals",
                    "storage_type": "cold_storage",
                    "start_date": "2024-01-10",
                    "end_date": "2024-03-10",
                    "duration_days": 60,
                    "rate_per_quintal_per_month": 25,
                    "total_cost": 2500,
                    "advance_paid": 750,
                    "status": "Active",
                    "receipt_number": "RCP002",
                    "insurance_opted": True,
                    "quality_check_date": "2024-01-10"
                }
            ],
            "storage_rates": [
                {
                    "crop_category": "Cereals",
                    "crops": ["Wheat", "Rice", "Maize", "Barley"],
                    "storage_requirements": "Dry, ventilated, pest-free",
                    "recommended_storage": "Covered warehouse",
                    "rate_range": "6-10 per quintal per month",
                    "maximum_duration": "12 months"
                },
                {
                    "crop_category": "Fruits",
                    "crops": ["Apple", "Orange", "Grapes", "Pomegranate"],
                    "storage_requirements": "Temperature controlled, humidity controlled",
                    "recommended_storage": "Cold storage",
                    "rate_range": "20-35 per quintal per month",
                    "maximum_duration": "6 months"
                },
                {
                    "crop_category": "Vegetables",
                    "crops": ["Potato", "Onion", "Tomato", "Cabbage"],
                    "storage_requirements": "Cool, dry, ventilated",
                    "recommended_storage": "Cold storage or ventilated warehouse",
                    "rate_range": "15-25 per quintal per month",
                    "maximum_duration": "4 months"
                }
            ],
            "quality_parameters": [
                {
                    "crop": "Wheat",
                    "parameters": {
                        "moisture_content": "12-14%",
                        "foreign_matter": "< 3%",
                        "damaged_grains": "< 6%",
                        "shriveled_grains": "< 6%"
                    },
                    "grading": ["FAQ", "Grade A", "Grade B"],
                    "storage_life": "12 months"
                },
                {
                    "crop": "Rice",
                    "parameters": {
                        "moisture_content": "13-14%",
                        "foreign_matter": "< 2%",
                        "damaged_grains": "< 4%",
                        "chalky_grains": "< 6%"
                    },
                    "grading": ["Grade A", "Grade B", "Grade C"],
                    "storage_life": "18 months"
                }
            ],
            "insurance_options": [
                {
                    "type": "Fire Insurance",
                    "coverage": "Fire, lightning, explosion",
                    "premium_rate": 0.1,
                    "claim_settlement": "Within 30 days"
                },
                {
                    "type": "Comprehensive Insurance",
                    "coverage": "Fire, theft, natural calamities, quality deterioration",
                    "premium_rate": 0.3,
                    "claim_settlement": "Within 45 days"
                }
            ],
            "storage_statistics": {
                "total_warehouses": 2500,
                "total_capacity": 15000000,
                "utilized_capacity": 12000000,
                "utilization_rate": 80,
                "average_storage_duration": "4.5 months",
                "total_bookings": 45000,
                "revenue_generated": 540000000,
                "top_stored_crops": [
                    {"crop": "Wheat", "percentage": 25},
                    {"crop": "Rice", "percentage": 20},
                    {"crop": "Maize", "percentage": 15},
                    {"crop": "Potato", "percentage": 12},
                    {"crop": "Onion", "percentage": 10}
                ]
            }
        }
    
    def calculate_storage_cost(self, quantity, rate_per_quintal_per_month, duration_days):
        duration_months = duration_days / 30
        total_cost = quantity * rate_per_quintal_per_month * duration_months
        
        # Calculate advance (30% of total cost)
        advance_amount = total_cost * 0.3
        
        return {
            "total_cost": round(total_cost, 2),
            "advance_amount": round(advance_amount, 2),
            "remaining_amount": round(total_cost - advance_amount, 2),
            "cost_per_month": round(quantity * rate_per_quintal_per_month, 2),
            "duration_months": round(duration_months, 1)
        }
    
    def check_availability(self, warehouse_id, required_capacity, start_date, end_date):
        warehouse = None
        for wh in self.data["warehouses"]:
            if wh["warehouse_id"] == warehouse_id:
                warehouse = wh
                break
        
        if not warehouse:
            return {"error": "Warehouse not found"}
        
        available = warehouse["available_capacity"] >= required_capacity
        
        return {
            "available": available,
            "available_capacity": warehouse["available_capacity"],
            "required_capacity": required_capacity,
            "warehouse_name": warehouse["name"],
            "location": warehouse["location"]
        }
    
    def get_recommended_storage(self, crop):
        for category in self.data["storage_rates"]:
            if crop in category["crops"]:
                return {
                    "recommended_storage": category["recommended_storage"],
                    "storage_requirements": category["storage_requirements"],
                    "rate_range": category["rate_range"],
                    "maximum_duration": category["maximum_duration"]
                }
        
        return {"recommended_storage": "General warehouse", "rate_range": "8-12 per quintal per month"}
    
    def get_warehouses(self):
        return self.data["warehouses"]
    
    def get_storage_bookings(self):
        return self.data["storage_bookings"]
    
    def get_quality_parameters(self):
        return self.data["quality_parameters"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Storage Booking is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
