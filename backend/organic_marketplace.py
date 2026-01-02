import json
import os
from datetime import datetime, timedelta
import random

class OrganicMarketplace:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data_file = os.path.join(data_folder, 'organic_marketplace_data.json')
        self.load_data()
    
    def load_data(self):
        """Load organic marketplace data"""
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
        """Generate comprehensive organic marketplace data"""
        organic_crops = [
            "Organic Rice", "Organic Wheat", "Organic Quinoa", "Organic Millets",
            "Organic Tomatoes", "Organic Carrots", "Organic Spinach", "Organic Kale",
            "Organic Apples", "Organic Bananas", "Organic Mangoes", "Organic Grapes",
            "Organic Turmeric", "Organic Ginger", "Organic Cardamom", "Organic Black Pepper"
        ]
        
        certifications = [
            {"name": "NPOP", "full_name": "National Programme for Organic Production", "country": "India"},
            {"name": "USDA Organic", "full_name": "United States Department of Agriculture", "country": "USA"},
            {"name": "EU Organic", "full_name": "European Union Organic", "country": "EU"},
            {"name": "JAS Organic", "full_name": "Japanese Agricultural Standards", "country": "Japan"},
            {"name": "IFOAM", "full_name": "International Federation of Organic Agriculture Movements", "country": "Global"}
        ]
        
        # Generate organic listings
        organic_listings = []
        for i in range(150):
            crop = random.choice(organic_crops)
            cert = random.choice(certifications)
            
            organic_listings.append({
                "listing_id": f"ORG{i+1:03d}",
                "farmer_id": f"OF{random.randint(1, 50):03d}",
                "farmer_name": f"Organic Farmer {random.randint(1, 50)}",
                "farm_name": f"Green Fields Farm {random.randint(1, 100)}",
                "crop_name": crop,
                "variety": f"{crop.split()[-1]} Premium",
                "quantity_available": random.randint(100, 5000),
                "unit": "kg",
                "price_per_kg": random.randint(50, 300),
                "premium_over_conventional": random.randint(20, 80),
                "certification": cert,
                "certificate_number": f"{cert['name']}-{random.randint(10000, 99999)}",
                "certificate_expiry": (datetime.now() + timedelta(days=random.randint(30, 365))).isoformat(),
                "harvest_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                "location": random.choice(["Punjab", "Haryana", "UP", "MP", "Maharashtra", "Karnataka"]),
                "farm_size": random.randint(1, 50),
                "farming_method": random.choice(["Biodynamic", "Natural", "Permaculture", "Traditional Organic"]),
                "soil_health_score": random.randint(70, 100),
                "traceability_code": f"TR{random.randint(100000, 999999)}",
                "cold_chain_required": random.choice([True, False]),
                "shelf_life": random.randint(7, 90),
                "nutritional_info": {
                    "protein": random.randint(5, 25),
                    "fiber": random.randint(2, 15),
                    "vitamins": ["A", "C", "K"] if "vegetable" in crop.lower() else ["B", "E"],
                    "minerals": ["Iron", "Calcium", "Potassium"]
                },
                "buyer_preferences": random.choice(["Restaurants", "Retail", "Export", "All"]),
                "minimum_order": random.randint(10, 100),
                "packaging_options": ["Bulk", "Retail Packs", "Custom"],
                "posted_date": (datetime.now() - timedelta(days=random.randint(1, 15))).isoformat(),
                "status": random.choice(["available", "reserved", "sold"])
            })
        
        # Generate organic buyers
        organic_buyers = []
        buyer_types = ["Restaurant", "Retail Chain", "Export Company", "Health Store", "Online Platform"]
        
        for i in range(50):
            buyer_type = random.choice(buyer_types)
            organic_buyers.append({
                "buyer_id": f"OB{i+1:03d}",
                "buyer_name": f"{buyer_type} {random.randint(1, 100)}",
                "buyer_type": buyer_type,
                "location": random.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]),
                "certification_requirements": random.sample(["NPOP", "USDA", "EU", "JAS"], random.randint(1, 3)),
                "preferred_crops": random.sample(organic_crops, random.randint(3, 8)),
                "monthly_volume": random.randint(1000, 50000),
                "price_premium_willing": random.randint(15, 60),
                "payment_terms": random.choice(["Advance", "On Delivery", "30 Days Credit"]),
                "quality_standards": {
                    "pesticide_residue": "Zero tolerance",
                    "moisture_content": "< 12%",
                    "foreign_matter": "< 2%"
                },
                "rating": round(random.uniform(3.5, 5.0), 1),
                "verified": random.choice([True, False])
            })
        
        return {
            "organic_listings": organic_listings,
            "organic_buyers": organic_buyers,
            "certifications": certifications,
            "traceability_records": [
                {
                    "trace_id": f"TR{i+1:06d}",
                    "listing_id": f"ORG{random.randint(1, 150):03d}",
                    "farm_activities": [
                        {
                            "date": (datetime.now() - timedelta(days=random.randint(60, 120))).isoformat(),
                            "activity": "Soil Preparation",
                            "inputs_used": "Organic Compost, Green Manure",
                            "weather": "Sunny, 25°C"
                        },
                        {
                            "date": (datetime.now() - timedelta(days=random.randint(30, 60))).isoformat(),
                            "activity": "Sowing",
                            "inputs_used": "Certified Organic Seeds",
                            "weather": "Cloudy, 22°C"
                        },
                        {
                            "date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                            "activity": "Harvest",
                            "inputs_used": "Manual Labor",
                            "weather": "Clear, 28°C"
                        }
                    ],
                    "inspection_records": [
                        {
                            "date": (datetime.now() - timedelta(days=random.randint(15, 45))).isoformat(),
                            "inspector": f"Inspector {random.randint(1, 10)}",
                            "findings": "Compliant with organic standards",
                            "score": random.randint(85, 100)
                        }
                    ]
                }
                for i in range(100)
            ],
            "cold_chain_providers": [
                {
                    "provider_id": f"CC{i+1:03d}",
                    "provider_name": f"Cold Chain {i+1}",
                    "coverage_areas": random.sample(["North", "South", "East", "West"], random.randint(2, 4)),
                    "temperature_range": "-2°C to 8°C",
                    "capacity": random.randint(1000, 10000),
                    "rating": round(random.uniform(3.5, 5.0), 1)
                }
                for i in range(20)
            ]
        }
    
    def get_organic_listings(self, filters=None):
        """Get organic produce listings with filters"""
        try:
            listings = self.data["organic_listings"]
            
            if filters:
                if filters.get("crop_name"):
                    listings = [l for l in listings if filters["crop_name"].lower() in l["crop_name"].lower()]
                if filters.get("certification"):
                    listings = [l for l in listings if l["certification"]["name"] == filters["certification"]]
                if filters.get("location"):
                    listings = [l for l in listings if l["location"].lower() == filters["location"].lower()]
                if filters.get("max_price"):
                    listings = [l for l in listings if l["price_per_kg"] <= int(filters["max_price"])]
                if filters.get("farming_method"):
                    listings = [l for l in listings if l["farming_method"] == filters["farming_method"]]
                if filters.get("status"):
                    listings = [l for l in listings if l["status"] == filters["status"]]
                else:
                    listings = [l for l in listings if l["status"] == "available"]
            
            return {
                "status": "success",
                "total_listings": len(listings),
                "listings": listings[:20]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_traceability_info(self, listing_id):
        """Get traceability information for organic produce"""
        try:
            trace_record = next((t for t in self.data["traceability_records"] if t["listing_id"] == listing_id), None)
            if not trace_record:
                return {"status": "error", "message": "Traceability record not found"}
            
            return {
                "status": "success",
                "traceability": trace_record
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def match_organic_buyers(self, listing_id):
        """Match organic produce with suitable buyers"""
        try:
            listing = next((l for l in self.data["organic_listings"] if l["listing_id"] == listing_id), None)
            if not listing:
                return {"status": "error", "message": "Listing not found"}
            
            # Find matching buyers
            matching_buyers = []
            for buyer in self.data["organic_buyers"]:
                # Check if buyer is interested in this crop
                if any(crop.lower() in listing["crop_name"].lower() for crop in buyer["preferred_crops"]):
                    # Check certification compatibility
                    if listing["certification"]["name"] in buyer["certification_requirements"]:
                        matching_buyers.append({
                            **buyer,
                            "match_score": random.randint(70, 95)
                        })
            
            # Sort by match score
            matching_buyers.sort(key=lambda x: x["match_score"], reverse=True)
            
            return {
                "status": "success",
                "listing_id": listing_id,
                "matching_buyers": matching_buyers[:10]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def verify_certification(self, certificate_number):
        """Verify organic certification"""
        try:
            # Simulate certification verification
            is_valid = random.choice([True, False])
            
            return {
                "status": "success",
                "certificate_number": certificate_number,
                "valid": is_valid,
                "verification_date": datetime.now().isoformat(),
                "details": {
                    "issuing_authority": random.choice([cert["full_name"] for cert in self.data["certifications"]]),
                    "expiry_date": (datetime.now() + timedelta(days=random.randint(30, 365))).isoformat(),
                    "scope": "Crop Production"
                } if is_valid else None
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def test_connection(self):
        """Test the module connection"""
        return {"status": "connected", "module": "OrganicMarketplace", "data_loaded": len(self.data.get("organic_listings", [])) > 0}
