import json
import os
from datetime import datetime, timedelta
import random

class FertilizerPriceComparison:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data_file = os.path.join(data_folder, 'fertilizer_price_comparison_data.json')
        self.load_data()
    
    def load_data(self):
        """Load fertilizer price comparison data"""
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
        """Generate comprehensive fertilizer price comparison data"""
        fertilizers = [
            "Urea", "DAP", "MOP", "NPK 10:26:26", "NPK 12:32:16", "NPK 20:20:0",
            "Single Super Phosphate", "Triple Super Phosphate", "Ammonium Sulphate",
            "Calcium Ammonium Nitrate", "Potassium Sulphate", "Zinc Sulphate"
        ]
        
        pesticides = [
            "Chlorpyrifos", "Imidacloprid", "Cypermethrin", "Malathion", "2,4-D",
            "Glyphosate", "Atrazine", "Mancozeb", "Carbendazim", "Thiamethoxam"
        ]
        
        vendors = [
            {"id": "V001", "name": "AgriCorp India", "type": "manufacturer", "rating": 4.5, "verified": True},
            {"id": "V002", "name": "FarmSupply Co.", "type": "distributor", "rating": 4.2, "verified": True},
            {"id": "V003", "name": "GreenFields Ltd", "type": "retailer", "rating": 4.0, "verified": True},
            {"id": "V004", "name": "CropCare Solutions", "type": "online", "rating": 4.3, "verified": True},
            {"id": "V005", "name": "Rural Agri Store", "type": "local", "rating": 3.8, "verified": False}
        ]
        
        # Generate price data for fertilizers
        fertilizer_prices = []
        for fertilizer in fertilizers:
            for vendor in vendors:
                base_price = random.randint(800, 2500)
                fertilizer_prices.append({
                    "product_id": f"F{fertilizers.index(fertilizer)+1:03d}",
                    "product_name": fertilizer,
                    "category": "fertilizer",
                    "vendor_id": vendor["id"],
                    "vendor_name": vendor["name"],
                    "vendor_type": vendor["type"],
                    "vendor_rating": vendor["rating"],
                    "verified_vendor": vendor["verified"],
                    "price_per_bag": base_price,
                    "bag_weight": "50kg",
                    "price_per_kg": round(base_price / 50, 2),
                    "stock_quantity": random.randint(50, 500),
                    "moq": random.choice([1, 5, 10, 20]),
                    "delivery_time": random.choice(["Same day", "1-2 days", "3-5 days", "1 week"]),
                    "delivery_zones": random.sample(["North", "South", "East", "West", "Central"], random.randint(2, 5)),
                    "discount_bulk": random.randint(5, 15) if random.choice([True, False]) else 0,
                    "last_updated": (datetime.now() - timedelta(hours=random.randint(1, 48))).isoformat()
                })
        
        # Generate price data for pesticides
        pesticide_prices = []
        for pesticide in pesticides:
            for vendor in vendors:
                base_price = random.randint(200, 1500)
                pesticide_prices.append({
                    "product_id": f"P{pesticides.index(pesticide)+1:03d}",
                    "product_name": pesticide,
                    "category": "pesticide",
                    "vendor_id": vendor["id"],
                    "vendor_name": vendor["name"],
                    "vendor_type": vendor["type"],
                    "vendor_rating": vendor["rating"],
                    "verified_vendor": vendor["verified"],
                    "price_per_liter": base_price,
                    "pack_size": random.choice(["250ml", "500ml", "1L", "5L"]),
                    "price_per_ml": round(base_price / 1000, 2),
                    "stock_quantity": random.randint(20, 200),
                    "moq": random.choice([1, 2, 5, 10]),
                    "delivery_time": random.choice(["Same day", "1-2 days", "3-5 days", "1 week"]),
                    "delivery_zones": random.sample(["North", "South", "East", "West", "Central"], random.randint(2, 5)),
                    "discount_bulk": random.randint(5, 20) if random.choice([True, False]) else 0,
                    "last_updated": (datetime.now() - timedelta(hours=random.randint(1, 48))).isoformat()
                })
        
        return {
            "fertilizer_prices": fertilizer_prices,
            "pesticide_prices": pesticide_prices,
            "vendors": vendors,
            "price_alerts": [
                {
                    "alert_id": f"PA{i+1:03d}",
                    "user_id": f"U{random.randint(1, 100):03d}",
                    "product_name": random.choice(fertilizers + pesticides),
                    "target_price": random.randint(500, 2000),
                    "current_price": random.randint(600, 2200),
                    "alert_type": "price_drop",
                    "status": "active",
                    "created_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()
                }
                for i in range(50)
            ],
            "bulk_discounts": [
                {
                    "vendor_id": vendor["id"],
                    "min_quantity": random.choice([10, 20, 50, 100]),
                    "discount_percent": random.randint(5, 25),
                    "valid_until": (datetime.now() + timedelta(days=random.randint(7, 30))).isoformat()
                }
                for vendor in vendors
            ]
        }
    
    def compare_prices(self, product_name, category="all", location="all"):
        """Compare prices across vendors for a specific product"""
        try:
            all_prices = []
            
            if category == "all" or category == "fertilizer":
                all_prices.extend(self.data["fertilizer_prices"])
            if category == "all" or category == "pesticide":
                all_prices.extend(self.data["pesticide_prices"])
            
            # Filter by product name
            filtered_prices = [
                price for price in all_prices 
                if product_name.lower() in price["product_name"].lower()
            ]
            
            # Sort by price
            filtered_prices.sort(key=lambda x: x.get("price_per_kg", x.get("price_per_ml", 0)))
            
            return {
                "status": "success",
                "product_name": product_name,
                "total_vendors": len(filtered_prices),
                "price_comparison": filtered_prices[:10],  # Top 10 best prices
                "price_range": {
                    "min_price": min([p.get("price_per_kg", p.get("price_per_ml", 0)) for p in filtered_prices]) if filtered_prices else 0,
                    "max_price": max([p.get("price_per_kg", p.get("price_per_ml", 0)) for p in filtered_prices]) if filtered_prices else 0,
                    "avg_price": sum([p.get("price_per_kg", p.get("price_per_ml", 0)) for p in filtered_prices]) / len(filtered_prices) if filtered_prices else 0
                }
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_bulk_discounts(self, vendor_id=None):
        """Get available bulk discounts"""
        try:
            discounts = self.data["bulk_discounts"]
            if vendor_id:
                discounts = [d for d in discounts if d["vendor_id"] == vendor_id]
            
            return {
                "status": "success",
                "bulk_discounts": discounts
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def set_price_alert(self, user_id, product_name, target_price):
        """Set price alert for a product"""
        try:
            alert = {
                "alert_id": f"PA{len(self.data['price_alerts'])+1:03d}",
                "user_id": user_id,
                "product_name": product_name,
                "target_price": target_price,
                "alert_type": "price_drop",
                "status": "active",
                "created_date": datetime.now().isoformat()
            }
            
            self.data["price_alerts"].append(alert)
            self.save_data()
            
            return {
                "status": "success",
                "message": "Price alert set successfully",
                "alert_id": alert["alert_id"]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def test_connection(self):
        """Test the module connection"""
        return {"status": "connected", "module": "FertilizerPriceComparison", "data_loaded": len(self.data.get("fertilizer_prices", [])) > 0}
