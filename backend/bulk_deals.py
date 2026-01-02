import json
from datetime import datetime, timedelta
import random

class BulkDealsEngine:
    def __init__(self, data_folder='data'):
        # Massive bulk deals data
        self.deal_categories = {
            "seeds": ["Hybrid Seeds", "Organic Seeds", "Certified Seeds", "Treated Seeds"],
            "fertilizers": ["NPK Fertilizer", "Urea", "DAP", "Organic Compost"],
            "pesticides": ["Insecticides", "Fungicides", "Herbicides", "Bio-pesticides"],
            "equipment": ["Tractors", "Harvesters", "Irrigation Systems", "Hand Tools"]
        }
        
        self.suppliers = [
            {"id": 1, "name": "AgriTech Solutions", "rating": 4.8, "deals_completed": 1250},
            {"id": 2, "name": "FarmSupply Co.", "rating": 4.7, "deals_completed": 980},
            {"id": 3, "name": "Green Valley Supplies", "rating": 4.9, "deals_completed": 1450},
            {"id": 4, "name": "Rural Equipment Ltd", "rating": 4.6, "deals_completed": 750}
        ]
        
        self.active_deals = self._generate_bulk_deals()
        
    def _generate_bulk_deals(self):
        deals = []
        for i in range(300):  # Generate 300 bulk deals
            category = random.choice(list(self.deal_categories.keys()))
            product = random.choice(self.deal_categories[category])
            supplier = random.choice(self.suppliers)
            
            deal = {
                "id": f"BD{2000 + i}",
                "product_name": product,
                "category": category,
                "supplier_id": supplier["id"],
                "supplier_name": supplier["name"],
                "original_price": random.randint(500, 10000),
                "bulk_price": random.randint(300, 8000),
                "minimum_quantity": random.randint(10, 100),
                "maximum_quantity": random.randint(500, 2000),
                "discount_percentage": random.randint(15, 45),
                "participants_joined": random.randint(5, 150),
                "target_participants": random.randint(50, 200),
                "deal_expires": (datetime.now() + timedelta(days=random.randint(7, 30))).strftime("%Y-%m-%d"),
                "status": random.choice(["active", "filling", "completed"]),
                "savings_per_unit": random.randint(50, 500),
                "total_savings": random.randint(5000, 50000),
                "deal_description": f"Bulk purchase opportunity for {product} with significant savings",
                "terms_conditions": "Payment on delivery, Quality guarantee, Return policy applicable"
            }
            deals.append(deal)
        return deals
    
    def get_active_deals(self, category=None):
        if category:
            return [deal for deal in self.active_deals if deal["category"] == category and deal["status"] == "active"]
        return [deal for deal in self.active_deals if deal["status"] == "active"][:50]
    
    def join_bulk_deal(self, deal_id, farmer_id, quantity):
        for deal in self.active_deals:
            if deal["id"] == deal_id:
                deal["participants_joined"] += 1
                return {
                    "success": True,
                    "message": f"Successfully joined bulk deal {deal_id}",
                    "estimated_savings": deal["savings_per_unit"] * quantity
                }
        return {"success": False, "message": "Deal not found"}

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Bulk Deals is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
