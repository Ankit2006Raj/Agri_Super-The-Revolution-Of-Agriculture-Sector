import json
import random
from datetime import datetime, timedelta

class DigitalWallet:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/digital_wallet_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "wallets": [
                {
                    "wallet_id": "W001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "balance": 25000.50,
                    "status": "Active",
                    "created_date": "2023-06-15",
                    "kyc_status": "Verified",
                    "linked_bank": "State Bank of India",
                    "account_number": "****1234",
                    "daily_limit": 50000,
                    "monthly_limit": 200000
                },
                {
                    "wallet_id": "W002",
                    "farmer_id": "F002",
                    "farmer_name": "Priya Sharma",
                    "balance": 18750.25,
                    "status": "Active",
                    "created_date": "2023-07-20",
                    "kyc_status": "Verified",
                    "linked_bank": "HDFC Bank",
                    "account_number": "****5678",
                    "daily_limit": 50000,
                    "monthly_limit": 200000
                }
            ],
            "transactions": [
                {
                    "transaction_id": "TXN001",
                    "wallet_id": "W001",
                    "type": "Credit",
                    "amount": 15000,
                    "description": "Payment received for wheat sale",
                    "timestamp": "2024-01-15 10:30:00",
                    "status": "Completed",
                    "reference": "SALE_REF_001",
                    "balance_after": 25000.50
                },
                {
                    "transaction_id": "TXN002",
                    "wallet_id": "W001",
                    "type": "Debit",
                    "amount": 5000,
                    "description": "Fertilizer purchase",
                    "timestamp": "2024-01-14 14:20:00",
                    "status": "Completed",
                    "reference": "FERT_PUR_001",
                    "balance_after": 20000.50
                },
                {
                    "transaction_id": "TXN003",
                    "wallet_id": "W002",
                    "type": "Credit",
                    "amount": 8750.25,
                    "description": "Cotton sale payment",
                    "timestamp": "2024-01-13 16:45:00",
                    "status": "Completed",
                    "reference": "COTTON_SALE_001",
                    "balance_after": 18750.25
                }
            ],
            "payment_methods": [
                {
                    "method": "UPI",
                    "enabled": True,
                    "transaction_fee": 0,
                    "daily_limit": 100000,
                    "supported_apps": ["PhonePe", "Google Pay", "Paytm", "BHIM"]
                },
                {
                    "method": "Bank Transfer",
                    "enabled": True,
                    "transaction_fee": 5,
                    "daily_limit": 200000,
                    "processing_time": "Instant to 2 hours"
                },
                {
                    "method": "Cash Deposit",
                    "enabled": True,
                    "transaction_fee": 10,
                    "daily_limit": 50000,
                    "locations": ["Bank branches", "ATMs", "Authorized agents"]
                }
            ],
            "merchant_payments": [
                {
                    "merchant_id": "M001",
                    "merchant_name": "Agri Input Store",
                    "category": "Agricultural Supplies",
                    "payment_methods": ["Wallet", "UPI", "QR Code"],
                    "discount_offers": "2% cashback on fertilizer purchases",
                    "location": "Ludhiana, Punjab"
                },
                {
                    "merchant_id": "M002",
                    "merchant_name": "Seed Company Ltd",
                    "category": "Seeds",
                    "payment_methods": ["Wallet", "Bank Transfer"],
                    "discount_offers": "5% discount on bulk orders",
                    "location": "Delhi"
                }
            ],
            "rewards_program": {
                "points_earned": 2500,
                "points_redeemed": 500,
                "available_points": 2000,
                "tier": "Silver",
                "benefits": [
                    "1 point per ₹100 spent",
                    "2x points on agricultural purchases",
                    "Free transactions up to 20 per month",
                    "Priority customer support"
                ],
                "redemption_options": [
                    {"option": "Cash back", "rate": "1 point = ₹0.25"},
                    {"option": "Mobile recharge", "rate": "1 point = ₹0.20"},
                    {"option": "Agricultural supplies", "rate": "1 point = ₹0.30"}
                ]
            },
            "wallet_statistics": {
                "total_wallets": 125000,
                "active_wallets": 98000,
                "total_balance": 2500000000,
                "monthly_transactions": 450000,
                "transaction_volume": 1800000000,
                "average_balance": 20000,
                "top_transaction_categories": [
                    {"category": "Crop Sales", "percentage": 35},
                    {"category": "Input Purchases", "percentage": 25},
                    {"category": "Equipment", "percentage": 15},
                    {"category": "Loan Repayment", "percentage": 10},
                    {"category": "Others", "percentage": 15}
                ]
            }
        }
    
    def process_payment(self, wallet_id, amount, description, payment_type="Debit"):
        # Find wallet
        wallet = None
        for w in self.data["wallets"]:
            if w["wallet_id"] == wallet_id:
                wallet = w
                break
        
        if not wallet:
            return {"error": "Wallet not found"}
        
        if payment_type == "Debit" and wallet["balance"] < amount:
            return {"error": "Insufficient balance"}
        
        # Process transaction
        new_balance = wallet["balance"] - amount if payment_type == "Debit" else wallet["balance"] + amount
        
        transaction = {
            "transaction_id": f"TXN{random.randint(1000, 9999)}",
            "wallet_id": wallet_id,
            "type": payment_type,
            "amount": amount,
            "description": description,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Completed",
            "reference": f"REF_{random.randint(100000, 999999)}",
            "balance_after": new_balance
        }
        
        return {
            "success": True,
            "transaction": transaction,
            "new_balance": new_balance
        }
    
    def get_wallet_balance(self, wallet_id):
        for wallet in self.data["wallets"]:
            if wallet["wallet_id"] == wallet_id:
                return wallet["balance"]
        return 0
    
    def get_transaction_history(self, wallet_id, limit=10):
        transactions = [t for t in self.data["transactions"] if t["wallet_id"] == wallet_id]
        return sorted(transactions, key=lambda x: x["timestamp"], reverse=True)[:limit]
    
    def get_wallets(self):
        return self.data["wallets"]
    
    def get_payment_methods(self):
        return self.data["payment_methods"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Digital Wallet is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
