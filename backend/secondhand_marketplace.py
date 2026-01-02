import json
import os
from datetime import datetime, timedelta
import random

class SecondhandMarketplace:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data_file = os.path.join(data_folder, 'secondhand_marketplace_data.json')
        self.load_data()
    
    def load_data(self):
        """Load secondhand marketplace data"""
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_sample_data()
            self.save_data()
    
    def save_data(self):
        """Save data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def generate_sample_data(self):
        """Generate comprehensive secondhand marketplace data"""
        equipment_types = [
            "Tractor", "Harvester", "Plough", "Cultivator", "Seed Drill", "Sprayer",
            "Thresher", "Rotavator", "Disc Harrow", "Water Pump", "Generator", "Trailer"
        ]
        
        brands = ["Mahindra", "John Deere", "Sonalika", "Swaraj", "New Holland", "Kubota", "Escorts", "VST"]
        conditions = ["Excellent", "Good", "Fair", "Needs Repair"]
        
        listings = []
        for i in range(200):
            equipment = random.choice(equipment_types)
            brand = random.choice(brands)
            condition = random.choice(conditions)
            year = random.randint(2010, 2023)
            
            # Price based on condition and age
            base_price = random.randint(50000, 1500000)
            condition_multiplier = {"Excellent": 0.9, "Good": 0.7, "Fair": 0.5, "Needs Repair": 0.3}
            age_factor = max(0.3, 1 - (2024 - year) * 0.05)
            final_price = int(base_price * condition_multiplier[condition] * age_factor)
            
            listings.append({
                "listing_id": f"SH{i+1:03d}",
                "seller_id": f"S{random.randint(1, 50):03d}",
                "seller_name": f"Farmer {random.randint(1, 50)}",
                "seller_rating": round(random.uniform(3.0, 5.0), 1),
                "equipment_type": equipment,
                "brand": brand,
                "model": f"{brand} {equipment} {random.randint(100, 999)}",
                "year": year,
                "condition": condition,
                "price": final_price,
                "negotiable": random.choice([True, False]),
                "hours_used": random.randint(100, 5000) if equipment in ["Tractor", "Harvester"] else None,
                "location": random.choice(["Punjab", "Haryana", "UP", "MP", "Maharashtra", "Karnataka"]),
                "description": f"{condition} condition {brand} {equipment} from {year}. Well maintained and ready to use.",
                "images": [f"image_{i+1}_{j}.jpg" for j in range(random.randint(2, 5))],
                "inspection_report": {
                    "engine_condition": random.choice(["Excellent", "Good", "Fair"]),
                    "hydraulics": random.choice(["Working", "Needs Service", "Not Working"]),
                    "tires": random.choice(["New", "Good", "Worn", "Needs Replacement"]),
                    "overall_score": random.randint(60, 95)
                },
                "vin_serial": f"VIN{random.randint(100000, 999999)}",
                "verified": random.choice([True, False]),
                "posted_date": (datetime.now() - timedelta(days=random.randint(1, 60))).isoformat(),
                "views": random.randint(10, 500),
                "inquiries": random.randint(0, 20),
                "status": random.choice(["active", "sold", "reserved"])
            })
        
        # Generate chat messages
        chat_messages = []
        for i in range(100):
            chat_messages.append({
                "chat_id": f"CH{i+1:03d}",
                "listing_id": f"SH{random.randint(1, 200):03d}",
                "buyer_id": f"B{random.randint(1, 100):03d}",
                "seller_id": f"S{random.randint(1, 50):03d}",
                "messages": [
                    {
                        "sender": "buyer",
                        "message": "Is this equipment still available?",
                        "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 48))).isoformat()
                    },
                    {
                        "sender": "seller",
                        "message": "Yes, it's available. Would you like to inspect it?",
                        "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 24))).isoformat()
                    }
                ],
                "status": random.choice(["active", "closed", "deal_pending"])
            })
        
        return {
            "listings": listings,
            "chat_messages": chat_messages,
            "escrow_transactions": [
                {
                    "transaction_id": f"ESC{i+1:03d}",
                    "listing_id": f"SH{random.randint(1, 200):03d}",
                    "buyer_id": f"B{random.randint(1, 100):03d}",
                    "seller_id": f"S{random.randint(1, 50):03d}",
                    "amount": random.randint(50000, 1000000),
                    "status": random.choice(["pending", "released", "disputed"]),
                    "created_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()
                }
                for i in range(50)
            ],
            "inspection_checklist": {
                "engine": ["Oil level", "Coolant level", "Belt condition", "Noise check"],
                "hydraulics": ["Fluid level", "Leak check", "Pressure test", "Cylinder operation"],
                "electrical": ["Battery condition", "Lights", "Gauges", "Wiring"],
                "mechanical": ["Tire condition", "Brake system", "Steering", "PTO operation"]
            }
        }
    
    def get_listings(self, filters=None):
        """Get equipment listings with filters"""
        try:
            listings = self.data["listings"]
            
            if filters:
                if filters.get("equipment_type"):
                    listings = [l for l in listings if l["equipment_type"].lower() == filters["equipment_type"].lower()]
                if filters.get("brand"):
                    listings = [l for l in listings if l["brand"].lower() == filters["brand"].lower()]
                if filters.get("condition"):
                    listings = [l for l in listings if l["condition"].lower() == filters["condition"].lower()]
                if filters.get("max_price"):
                    listings = [l for l in listings if l["price"] <= int(filters["max_price"])]
                if filters.get("location"):
                    listings = [l for l in listings if l["location"].lower() == filters["location"].lower()]
                if filters.get("status"):
                    listings = [l for l in listings if l["status"] == filters["status"]]
                else:
                    listings = [l for l in listings if l["status"] == "active"]
            
            return {
                "status": "success",
                "total_listings": len(listings),
                "listings": listings[:20]  # Return first 20 results
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_listing_details(self, listing_id):
        """Get detailed information about a specific listing"""
        try:
            listing = next((l for l in self.data["listings"] if l["listing_id"] == listing_id), None)
            if not listing:
                return {"status": "error", "message": "Listing not found"}
            
            return {
                "status": "success",
                "listing": listing,
                "inspection_checklist": self.data["inspection_checklist"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def create_listing(self, listing_data):
        """Create a new equipment listing"""
        try:
            new_listing = {
                "listing_id": f"SH{len(self.data['listings'])+1:03d}",
                "seller_id": listing_data["seller_id"],
                "seller_name": listing_data["seller_name"],
                "equipment_type": listing_data["equipment_type"],
                "brand": listing_data["brand"],
                "model": listing_data["model"],
                "year": listing_data["year"],
                "condition": listing_data["condition"],
                "price": listing_data["price"],
                "negotiable": listing_data.get("negotiable", True),
                "location": listing_data["location"],
                "description": listing_data["description"],
                "posted_date": datetime.now().isoformat(),
                "views": 0,
                "inquiries": 0,
                "status": "active"
            }
            
            self.data["listings"].append(new_listing)
            self.save_data()
            
            return {
                "status": "success",
                "message": "Listing created successfully",
                "listing_id": new_listing["listing_id"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def initiate_escrow(self, listing_id, buyer_id, amount):
        """Initiate escrow transaction"""
        try:
            listing = next((l for l in self.data["listings"] if l["listing_id"] == listing_id), None)
            if not listing:
                return {"status": "error", "message": "Listing not found"}
            
            transaction = {
                "transaction_id": f"ESC{len(self.data['escrow_transactions'])+1:03d}",
                "listing_id": listing_id,
                "buyer_id": buyer_id,
                "seller_id": listing["seller_id"],
                "amount": amount,
                "status": "pending",
                "created_date": datetime.now().isoformat()
            }
            
            self.data["escrow_transactions"].append(transaction)
            self.save_data()
            
            return {
                "status": "success",
                "message": "Escrow transaction initiated",
                "transaction_id": transaction["transaction_id"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def test_connection(self):
        """Test the module connection"""
        return {"status": "connected", "module": "SecondhandMarketplace", "data_loaded": len(self.data.get("listings", [])) > 0}
