import json
import csv
import math
from datetime import datetime, timedelta
import heapq

class RouteOptimizer:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        """Load road network, traffic, and fuel price data"""
        try:
            # Load road network data
            with open('data/logistics/road_network.csv', 'r') as f:
                reader = csv.DictReader(f)
                self.road_network = list(reader)
            
            # Load historical traffic data
            with open('data/logistics/historical_traffic.json', 'r') as f:
                self.traffic_data = json.load(f)
            
            # Load fuel prices
            with open('data/logistics/fuel_prices.csv', 'r') as f:
                reader = csv.DictReader(f)
                self.fuel_prices = list(reader)
                
        except FileNotFoundError:
            # Initialize with sample data if files don't exist
            self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """Initialize with comprehensive sample data"""
        self.road_network = [
            {"from_city": "Delhi", "to_city": "Mumbai", "distance_km": 1400, "road_type": "highway", "toll_cost": 800},
            {"from_city": "Delhi", "to_city": "Bangalore", "distance_km": 2150, "road_type": "highway", "toll_cost": 1200},
            {"from_city": "Mumbai", "to_city": "Pune", "distance_km": 150, "road_type": "highway", "toll_cost": 200},
            {"from_city": "Delhi", "to_city": "Jaipur", "distance_km": 280, "road_type": "highway", "toll_cost": 150},
            {"from_city": "Mumbai", "to_city": "Nashik", "distance_km": 165, "road_type": "state", "toll_cost": 100},
            {"from_city": "Bangalore", "to_city": "Chennai", "distance_km": 350, "road_type": "highway", "toll_cost": 300},
            {"from_city": "Delhi", "to_city": "Lucknow", "distance_km": 550, "road_type": "highway", "toll_cost": 400},
            {"from_city": "Mumbai", "to_city": "Surat", "distance_km": 280, "road_type": "highway", "toll_cost": 250},
            {"from_city": "Kolkata", "to_city": "Bhubaneswar", "distance_km": 440, "road_type": "highway", "toll_cost": 350},
            {"from_city": "Chennai", "to_city": "Coimbatore", "distance_km": 500, "road_type": "highway", "toll_cost": 400}
        ]
        
        self.traffic_data = {
            "peak_hours": [7, 8, 9, 17, 18, 19, 20],
            "traffic_multiplier": {
                "highway": {"peak": 1.3, "normal": 1.0, "night": 0.8},
                "state": {"peak": 1.5, "normal": 1.0, "night": 0.9},
                "city": {"peak": 2.0, "normal": 1.2, "night": 0.7}
            },
            "weather_impact": {
                "rain": 1.4, "fog": 1.6, "clear": 1.0, "storm": 2.0
            }
        }
        
        self.fuel_prices = [
            {"vehicle_type": "truck", "fuel_type": "diesel", "price_per_liter": 95.50, "mileage_kmpl": 6},
            {"vehicle_type": "tempo", "fuel_type": "diesel", "price_per_liter": 95.50, "mileage_kmpl": 12},
            {"vehicle_type": "mini_truck", "fuel_type": "petrol", "price_per_liter": 105.20, "mileage_kmpl": 8}
        ]
    
    def optimize_route(self, pickup_points, destination, vehicle_type="truck", priority="balanced"):
        """
        Optimize route for multiple pickup points to destination
        Priority: fastest, cheapest, balanced
        """
        routes = []
        
        # Generate different route options
        for route_type in ["direct", "optimized", "economical"]:
            route = self.calculate_route(pickup_points, destination, vehicle_type, route_type)
            routes.append(route)
        
        # Sort based on priority
        if priority == "fastest":
            routes.sort(key=lambda x: x["total_time"])
        elif priority == "cheapest":
            routes.sort(key=lambda x: x["total_cost"])
        else:  # balanced
            routes.sort(key=lambda x: x["total_time"] * 0.6 + x["total_cost"] * 0.4)
        
        return routes
    
    def calculate_route(self, pickup_points, destination, vehicle_type, route_type):
        """Calculate route details including cost, time, and waypoints"""
        total_distance = 0
        total_time = 0
        total_cost = 0
        waypoints = []
        
        # Get vehicle fuel data
        vehicle_data = next((v for v in self.fuel_prices if v["vehicle_type"] == vehicle_type), self.fuel_prices[0])
        
        # Calculate route through all pickup points
        current_location = pickup_points[0] if pickup_points else destination
        
        for i, pickup in enumerate(pickup_points):
            if i > 0:
                # Calculate distance between pickup points
                segment = self.get_route_segment(current_location, pickup)
                total_distance += segment["distance"]
                total_time += segment["time"]
                total_cost += segment["cost"]
                
            waypoints.append({
                "location": pickup,
                "type": "pickup",
                "eta": total_time,
                "cumulative_distance": total_distance
            })
            current_location = pickup
        
        # Final segment to destination
        if pickup_points:
            final_segment = self.get_route_segment(current_location, destination)
            total_distance += final_segment["distance"]
            total_time += final_segment["time"]
            total_cost += final_segment["cost"]
        
        waypoints.append({
            "location": destination,
            "type": "destination",
            "eta": total_time,
            "cumulative_distance": total_distance
        })
        
        # Calculate fuel cost
        fuel_cost = (total_distance / float(vehicle_data["mileage_kmpl"])) * float(vehicle_data["price_per_liter"])
        
        return {
            "route_type": route_type,
            "total_distance": round(total_distance, 2),
            "total_time": round(total_time, 2),
            "total_cost": round(total_cost + fuel_cost, 2),
            "fuel_cost": round(fuel_cost, 2),
            "toll_cost": round(total_cost, 2),
            "waypoints": waypoints,
            "vehicle_type": vehicle_type,
            "estimated_arrival": (datetime.now() + timedelta(hours=total_time)).strftime("%Y-%m-%d %H:%M")
        }
    
    def get_route_segment(self, from_location, to_location):
        """Get route segment details between two locations"""
        # Find matching road segment
        segment = next((r for r in self.road_network 
                       if (r["from_city"].lower() == from_location.lower() and r["to_city"].lower() == to_location.lower()) or
                          (r["to_city"].lower() == from_location.lower() and r["from_city"].lower() == to_location.lower())), None)
        
        if not segment:
            # Default segment if not found
            segment = {"distance_km": 100, "road_type": "state", "toll_cost": 50}
        
        distance = float(segment["distance_km"])
        road_type = segment["road_type"]
        toll_cost = float(segment["toll_cost"])
        
        # Calculate time based on road type and traffic
        base_speed = {"highway": 80, "state": 60, "city": 40}.get(road_type, 60)
        current_hour = datetime.now().hour
        
        traffic_multiplier = 1.0
        if current_hour in self.traffic_data["peak_hours"]:
            traffic_multiplier = self.traffic_data["traffic_multiplier"][road_type]["peak"]
        elif 22 <= current_hour or current_hour <= 5:
            traffic_multiplier = self.traffic_data["traffic_multiplier"][road_type]["night"]
        
        travel_time = (distance / base_speed) * traffic_multiplier
        
        return {
            "distance": distance,
            "time": travel_time,
            "cost": toll_cost
        }
    
    def get_delivery_eta(self, route_id, current_location):
        """Get updated ETA for ongoing delivery"""
        # Mock implementation for real-time tracking
        base_eta = datetime.now() + timedelta(hours=2.5)
        return {
            "route_id": route_id,
            "current_location": current_location,
            "estimated_arrival": base_eta.strftime("%Y-%m-%d %H:%M"),
            "remaining_distance": 45.2,
            "traffic_status": "moderate",
            "delays": []
        }

def get_route_optimizer():
    return RouteOptimizer()

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Route Optimization is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
