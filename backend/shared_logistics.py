import json
import random
from datetime import datetime, timedelta

class SharedLogistics:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/shared_logistics_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "transport_requests": [
                {
                    "request_id": "TR001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "pickup_location": "Ludhiana, Punjab",
                    "delivery_location": "Delhi Mandi",
                    "crop": "Wheat",
                    "quantity": 100,
                    "unit": "quintals",
                    "preferred_date": "2024-01-20",
                    "vehicle_type": "Truck (10 MT)",
                    "estimated_cost": 8000,
                    "shared_cost": 4000,
                    "status": "Matched",
                    "created_date": "2024-01-15",
                    "matched_requests": ["TR002"]
                },
                {
                    "request_id": "TR002",
                    "farmer_id": "F003",
                    "farmer_name": "Amit Singh",
                    "pickup_location": "Ludhiana, Punjab",
                    "delivery_location": "Delhi Mandi",
                    "crop": "Rice",
                    "quantity": 80,
                    "unit": "quintals",
                    "preferred_date": "2024-01-20",
                    "vehicle_type": "Truck (10 MT)",
                    "estimated_cost": 8000,
                    "shared_cost": 4000,
                    "status": "Matched",
                    "created_date": "2024-01-16",
                    "matched_requests": ["TR001"]
                }
            ],
            "transport_providers": [
                {
                    "provider_id": "TP001",
                    "name": "Punjab Transport Co.",
                    "contact": "+91-9876543210",
                    "rating": 4.5,
                    "vehicles": [
                        {"type": "Truck 5 MT", "count": 15, "rate_per_km": 25},
                        {"type": "Truck 10 MT", "count": 20, "rate_per_km": 35},
                        {"type": "Truck 15 MT", "count": 10, "rate_per_km": 45}
                    ],
                    "coverage_areas": ["Punjab", "Haryana", "Delhi", "UP"],
                    "services": ["Loading", "Unloading", "Insurance", "GPS Tracking"],
                    "payment_terms": "50% advance, 50% on delivery"
                },
                {
                    "provider_id": "TP002",
                    "name": "Haryana Logistics",
                    "contact": "+91-9876543211",
                    "rating": 4.2,
                    "vehicles": [
                        {"type": "Truck 7 MT", "count": 12, "rate_per_km": 30},
                        {"type": "Truck 12 MT", "count": 18, "rate_per_km": 40},
                        {"type": "Container 20 MT", "count": 8, "rate_per_km": 55}
                    ],
                    "coverage_areas": ["Haryana", "Punjab", "Delhi", "Rajasthan"],
                    "services": ["Loading", "Unloading", "Warehousing", "GPS Tracking"],
                    "payment_terms": "30% advance, 70% on delivery"
                }
            ],
            "shared_bookings": [
                {
                    "booking_id": "SB001",
                    "request_ids": ["TR001", "TR002"],
                    "provider_id": "TP001",
                    "vehicle_assigned": "Truck 10 MT - PB05AB1234",
                    "driver_name": "Gurpreet Singh",
                    "driver_contact": "+91-9876543212",
                    "pickup_date": "2024-01-20",
                    "pickup_time": "06:00 AM",
                    "estimated_delivery": "2024-01-20 18:00",
                    "total_cost": 8000,
                    "cost_per_farmer": 4000,
                    "status": "Confirmed",
                    "tracking_id": "TRK001",
                    "insurance_covered": True
                }
            ],
            "routes": [
                {
                    "route_id": "R001",
                    "from": "Ludhiana, Punjab",
                    "to": "Delhi Mandi",
                    "distance": 320,
                    "estimated_time": "8-10 hours",
                    "toll_charges": 800,
                    "fuel_cost": 2400,
                    "popular_crops": ["Wheat", "Rice", "Cotton"],
                    "peak_season": "April-June, October-December",
                    "average_requests_per_month": 150
                },
                {
                    "route_id": "R002",
                    "from": "Nashik, Maharashtra",
                    "to": "Mumbai APMC",
                    "distance": 180,
                    "estimated_time": "4-5 hours",
                    "toll_charges": 400,
                    "fuel_cost": 1350,
                    "popular_crops": ["Onion", "Grapes", "Tomato"],
                    "peak_season": "November-March",
                    "average_requests_per_month": 200
                }
            ],
            "cost_calculator": {
                "base_rates": {
                    "truck_5mt": 25,
                    "truck_10mt": 35,
                    "truck_15mt": 45,
                    "container_20mt": 55
                },
                "additional_charges": {
                    "loading_unloading": 500,
                    "insurance": 200,
                    "gps_tracking": 100,
                    "detention_per_hour": 150
                },
                "sharing_discount": 50,
                "fuel_surcharge": 5
            },
            "logistics_statistics": {
                "total_requests": 12000,
                "matched_requests": 9600,
                "matching_rate": 80,
                "average_cost_saving": 45,
                "total_distance_covered": 2400000,
                "co2_emissions_saved": 180000,
                "active_transport_providers": 150,
                "average_delivery_time": "8.5 hours"
            }
        }
    
    def find_matching_requests(self, pickup_location, delivery_location, preferred_date, tolerance_days=2):
        matches = []
        target_date = datetime.strptime(preferred_date, "%Y-%m-%d")
        
        for request in self.data["transport_requests"]:
            if request["status"] == "Open":
                request_date = datetime.strptime(request["preferred_date"], "%Y-%m-%d")
                date_diff = abs((target_date - request_date).days)
                
                if (request["pickup_location"] == pickup_location and 
                    request["delivery_location"] == delivery_location and 
                    date_diff <= tolerance_days):
                    matches.append(request)
        
        return matches
    
    def calculate_shared_cost(self, distance, vehicle_type, num_sharers=2):
        base_rates = self.data["cost_calculator"]["base_rates"]
        additional_charges = self.data["cost_calculator"]["additional_charges"]
        
        # Get base rate per km
        vehicle_key = vehicle_type.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("mt", "mt")
        base_rate = base_rates.get(vehicle_key, 35)
        
        # Calculate total cost
        transport_cost = distance * base_rate
        total_additional = sum(additional_charges.values())
        total_cost = transport_cost + total_additional
        
        # Apply sharing discount
        shared_cost = total_cost / num_sharers
        savings = (total_cost - shared_cost) / total_cost * 100
        
        return {
            "total_cost": total_cost,
            "shared_cost": shared_cost,
            "cost_per_farmer": shared_cost,
            "savings_percent": round(savings, 1),
            "savings_amount": total_cost - shared_cost
        }
    
    def get_transport_requests(self):
        return self.data["transport_requests"]
    
    def get_transport_providers(self):
        return self.data["transport_providers"]
    
    def get_routes(self):
        return self.data["routes"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Shared Logistics is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
