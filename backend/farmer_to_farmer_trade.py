import json
import os
from datetime import datetime, timedelta
import random

class FarmerToFarmerTrade:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data_file = os.path.join(data_folder, 'farmer_to_farmer_trade_data.json')
        self.load_data()
    
    def load_data(self):
        """Load farmer-to-farmer trade data"""
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
        """Generate comprehensive farmer-to-farmer trade data"""
        trade_items = [
            "Seeds", "Saplings", "Tools", "Fertilizer", "Pesticides", "Equipment Parts",
            "Harvest Produce", "Livestock", "Feed", "Compost", "Mulch", "Irrigation Supplies"
        ]
        
        seed_varieties = [
            "Heirloom Tomato Seeds", "Organic Wheat Seeds", "Hybrid Corn Seeds", "Traditional Rice Seeds",
            "Vegetable Seeds Mix", "Flower Seeds", "Herb Seeds", "Fruit Tree Saplings"
        ]
        
        # Generate peer offers
        peer_offers = []
        for i in range(200):
            item_type = random.choice(trade_items)
            is_seed = item_type == "Seeds"
            
            offer = {
                "offer_id": f"P2P{i+1:03d}",
                "farmer_id": f"F{random.randint(1, 100):03d}",
                "farmer_name": f"Farmer {random.randint(1, 100)}",
                "location": {
                    "state": random.choice(["Punjab", "Haryana", "UP", "MP", "Maharashtra", "Karnataka"]),
                    "district": f"District {random.randint(1, 20)}",
                    "village": f"Village {random.randint(1, 50)}",
                    "coordinates": {
                        "lat": round(random.uniform(20.0, 35.0), 6),
                        "lng": round(random.uniform(70.0, 85.0), 6)
                    }
                },
                "item_type": item_type,
                "item_name": random.choice(seed_varieties) if is_seed else f"{item_type} - {random.choice(['Premium', 'Standard', 'Basic'])}",
                "description": f"High quality {item_type.lower()} available for trade or sale",
                "quantity": random.randint(1, 100),
                "unit": random.choice(["kg", "pieces", "bags", "liters"]),
                "trade_type": random.choice(["cash", "barter", "both"]),
                "cash_price": random.randint(50, 2000) if random.choice([True, False]) else None,
                "barter_preferences": random.sample(trade_items, random.randint(2, 4)),
                "condition": random.choice(["New", "Like New", "Good", "Fair"]),
                "images": [f"image_{i+1}_{j}.jpg" for j in range(random.randint(1, 4))],
                "farmer_rating": round(random.uniform(3.0, 5.0), 1),
                "farmer_reputation": random.randint(50, 100),
                "posted_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                "expiry_date": (datetime.now() + timedelta(days=random.randint(7, 60))).isoformat(),
                "status": random.choice(["available", "reserved", "traded"]),
                "views": random.randint(5, 200),
                "interested_farmers": random.randint(0, 15)
            }
            
            # Add seed-specific information
            if is_seed:
                offer.update({
                    "seed_info": {
                        "variety": random.choice(["Heirloom", "Hybrid", "Open Pollinated"]),
                        "germination_rate": random.randint(80, 98),
                        "harvest_season": random.choice(["Kharif", "Rabi", "Zaid"]),
                        "maturity_days": random.randint(60, 150),
                        "yield_potential": f"{random.randint(20, 80)} quintals/hectare",
                        "provenance": f"Grown in {random.choice(['Punjab', 'Haryana', 'UP'])} for {random.randint(3, 10)} generations"
                    }
                })
            
            peer_offers.append(offer)
        
        # Generate trade messages
        trade_messages = []
        for i in range(150):
            trade_messages.append({
                "message_id": f"MSG{i+1:03d}",
                "offer_id": f"P2P{random.randint(1, 200):03d}",
                "sender_id": f"F{random.randint(1, 100):03d}",
                "receiver_id": f"F{random.randint(1, 100):03d}",
                "message_thread": [
                    {
                        "sender": "interested_farmer",
                        "message": "Hi, I'm interested in your seeds. Are they still available?",
                        "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 48))).isoformat()
                    },
                    {
                        "sender": "offer_farmer",
                        "message": "Yes, they are available. Would you like to see them in person?",
                        "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 24))).isoformat()
                    }
                ],
                "status": random.choice(["active", "closed", "deal_agreed"]),
                "created_date": (datetime.now() - timedelta(days=random.randint(1, 15))).isoformat()
            })
        
        # Generate escrow transactions for cash trades
        escrow_transactions = []
        for i in range(50):
            escrow_transactions.append({
                "escrow_id": f"ESC{i+1:03d}",
                "offer_id": f"P2P{random.randint(1, 200):03d}",
                "buyer_id": f"F{random.randint(1, 100):03d}",
                "seller_id": f"F{random.randint(1, 100):03d}",
                "amount": random.randint(500, 10000),
                "status": random.choice(["pending", "released", "disputed", "refunded"]),
                "created_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                "release_conditions": "Item delivered and verified by buyer"
            })
        
        # Generate meetup locations
        meetup_locations = []
        for i in range(30):
            meetup_locations.append({
                "location_id": f"LOC{i+1:03d}",
                "name": f"Farmer Market {i+1}",
                "address": f"Market Street {i+1}, Village {random.randint(1, 50)}",
                "coordinates": {
                    "lat": round(random.uniform(20.0, 35.0), 6),
                    "lng": round(random.uniform(70.0, 85.0), 6)
                },
                "type": random.choice(["Market", "Community Center", "Cooperative Office"]),
                "operating_hours": "9:00 AM - 6:00 PM",
                "contact": f"+91-{random.randint(7000000000, 9999999999)}",
                "facilities": random.sample(["Parking", "Storage", "Weighing Scale", "Testing Lab"], random.randint(2, 4))
            })
        
        return {
            "peer_offers": peer_offers,
            "trade_messages": trade_messages,
            "escrow_transactions": escrow_transactions,
            "meetup_locations": meetup_locations,
            "seed_bank": [
                {
                    "seed_id": f"SB{i+1:03d}",
                    "variety_name": random.choice(seed_varieties),
                    "scientific_name": f"Species {random.randint(1, 100)}",
                    "origin_location": random.choice(["Punjab", "Haryana", "UP", "MP"]),
                    "characteristics": random.sample(["Drought Resistant", "High Yield", "Disease Resistant", "Early Maturity"], random.randint(2, 4)),
                    "preservation_method": random.choice(["Cold Storage", "Dry Storage", "Vacuum Sealed"]),
                    "viability_years": random.randint(2, 10),
                    "contributed_by": f"F{random.randint(1, 100):03d}",
                    "contribution_date": (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat()
                }
                for i in range(100)
            ]
        }
    
    def get_local_offers(self, farmer_location, radius_km=50):
        """Get offers within specified radius"""
        try:
            # Simulate proximity-based filtering
            local_offers = []
            for offer in self.data["peer_offers"]:
                if offer["status"] == "available":
                    # Simple distance simulation
                    distance = random.randint(1, 100)
                    if distance <= radius_km:
                        offer_copy = offer.copy()
                        offer_copy["distance_km"] = distance
                        local_offers.append(offer_copy)
            
            # Sort by distance
            local_offers.sort(key=lambda x: x["distance_km"])
            
            return {
                "status": "success",
                "farmer_location": farmer_location,
                "radius_km": radius_km,
                "total_offers": len(local_offers),
                "local_offers": local_offers[:20]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def create_trade_offer(self, offer_data):
        """Create a new trade offer"""
        try:
            new_offer = {
                "offer_id": f"P2P{len(self.data['peer_offers'])+1:03d}",
                "farmer_id": offer_data["farmer_id"],
                "farmer_name": offer_data["farmer_name"],
                "location": offer_data["location"],
                "item_type": offer_data["item_type"],
                "item_name": offer_data["item_name"],
                "description": offer_data["description"],
                "quantity": offer_data["quantity"],
                "unit": offer_data["unit"],
                "trade_type": offer_data["trade_type"],
                "cash_price": offer_data.get("cash_price"),
                "barter_preferences": offer_data.get("barter_preferences", []),
                "condition": offer_data["condition"],
                "posted_date": datetime.now().isoformat(),
                "expiry_date": (datetime.now() + timedelta(days=30)).isoformat(),
                "status": "available",
                "views": 0,
                "interested_farmers": 0
            }
            
            self.data["peer_offers"].append(new_offer)
            self.save_data()
            
            return {
                "status": "success",
                "message": "Trade offer created successfully",
                "offer_id": new_offer["offer_id"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def initiate_barter_trade(self, offer_id, interested_farmer_id, barter_items):
        """Initiate a barter trade"""
        try:
            offer = next((o for o in self.data["peer_offers"] if o["offer_id"] == offer_id), None)
            if not offer:
                return {"status": "error", "message": "Offer not found"}
            
            # Create barter proposal
            barter_proposal = {
                "proposal_id": f"BP{len(self.data.get('barter_proposals', []))+1:03d}",
                "offer_id": offer_id,
                "proposer_id": interested_farmer_id,
                "offer_owner_id": offer["farmer_id"],
                "proposed_items": barter_items,
                "status": "pending",
                "created_date": datetime.now().isoformat()
            }
            
            if "barter_proposals" not in self.data:
                self.data["barter_proposals"] = []
            
            self.data["barter_proposals"].append(barter_proposal)
            self.save_data()
            
            return {
                "status": "success",
                "message": "Barter proposal submitted",
                "proposal_id": barter_proposal["proposal_id"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_seed_bank(self, filters=None):
        """Get seed bank entries"""
        try:
            seed_bank = self.data["seed_bank"]
            
            if filters:
                if filters.get("variety"):
                    seed_bank = [s for s in seed_bank if filters["variety"].lower() in s["variety_name"].lower()]
                if filters.get("characteristics"):
                    seed_bank = [s for s in seed_bank if any(char in s["characteristics"] for char in filters["characteristics"])]
            
            return {
                "status": "success",
                "total_varieties": len(seed_bank),
                "seed_bank": seed_bank[:20]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def test_connection(self):
        """Test the module connection"""
        return {"status": "connected", "module": "FarmerToFarmerTrade", "data_loaded": len(self.data.get("peer_offers", [])) > 0}
