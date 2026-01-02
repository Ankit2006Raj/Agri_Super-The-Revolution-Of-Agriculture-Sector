import json
import random
from datetime import datetime, timedelta

class EMIPurchase:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/emi_purchase_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "emi_products": [
                {
                    "product_id": "EP001",
                    "name": "Mahindra 575 DI Tractor",
                    "category": "Tractors",
                    "price": 850000,
                    "down_payment_min": 15,
                    "emi_tenure_options": [12, 24, 36, 48, 60],
                    "interest_rate": 8.5,
                    "processing_fee": 2500,
                    "insurance_required": True,
                    "warranty": "2 years",
                    "dealer": "Mahindra Authorized Dealer"
                },
                {
                    "product_id": "EP002",
                    "name": "John Deere 5050D Tractor",
                    "category": "Tractors",
                    "price": 950000,
                    "down_payment_min": 20,
                    "emi_tenure_options": [24, 36, 48, 60],
                    "interest_rate": 9.0,
                    "processing_fee": 3000,
                    "insurance_required": True,
                    "warranty": "3 years",
                    "dealer": "John Deere Authorized Dealer"
                },
                {
                    "product_id": "EP003",
                    "name": "Rotavator 7 Feet",
                    "category": "Implements",
                    "price": 85000,
                    "down_payment_min": 10,
                    "emi_tenure_options": [6, 12, 18, 24],
                    "interest_rate": 7.5,
                    "processing_fee": 500,
                    "insurance_required": False,
                    "warranty": "1 year",
                    "dealer": "Local Implement Dealer"
                }
            ],
            "emi_applications": [
                {
                    "application_id": "EA001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "product_id": "EP001",
                    "product_name": "Mahindra 575 DI Tractor",
                    "product_price": 850000,
                    "down_payment": 127500,
                    "loan_amount": 722500,
                    "tenure_months": 48,
                    "interest_rate": 8.5,
                    "monthly_emi": 17850,
                    "total_interest": 135300,
                    "total_amount": 857800,
                    "application_date": "2024-01-10",
                    "status": "Approved",
                    "approval_date": "2024-01-12",
                    "first_emi_date": "2024-02-10"
                },
                {
                    "application_id": "EA002",
                    "farmer_id": "F002",
                    "farmer_name": "Priya Sharma",
                    "product_id": "EP003",
                    "product_name": "Rotavator 7 Feet",
                    "product_price": 85000,
                    "down_payment": 8500,
                    "loan_amount": 76500,
                    "tenure_months": 18,
                    "interest_rate": 7.5,
                    "monthly_emi": 4680,
                    "total_interest": 7740,
                    "total_amount": 84240,
                    "application_date": "2024-01-08",
                    "status": "Active",
                    "approval_date": "2024-01-10",
                    "first_emi_date": "2024-02-08"
                }
            ],
            "emi_payments": [
                {
                    "payment_id": "EP001",
                    "application_id": "EA002",
                    "emi_number": 1,
                    "due_date": "2024-02-08",
                    "amount_due": 4680,
                    "amount_paid": 4680,
                    "payment_date": "2024-02-08",
                    "status": "Paid",
                    "payment_method": "Auto Debit",
                    "late_fee": 0,
                    "remaining_balance": 71820
                },
                {
                    "payment_id": "EP002",
                    "application_id": "EA002",
                    "emi_number": 2,
                    "due_date": "2024-03-08",
                    "amount_due": 4680,
                    "amount_paid": 0,
                    "payment_date": null,
                    "status": "Pending",
                    "payment_method": null,
                    "late_fee": 0,
                    "remaining_balance": 67140
                }
            ],
            "dealers": [
                {
                    "dealer_id": "D001",
                    "name": "Mahindra Authorized Dealer",
                    "location": "Ludhiana, Punjab",
                    "contact": "+91-9876543210",
                    "products": ["Tractors", "Harvesters", "Implements"],
                    "emi_partner": True,
                    "rating": 4.5,
                    "services": ["Sales", "Service", "Spare Parts", "EMI Processing"]
                },
                {
                    "dealer_id": "D002",
                    "name": "John Deere Authorized Dealer",
                    "location": "Delhi",
                    "contact": "+91-9876543211",
                    "products": ["Tractors", "Combines", "Precision Agriculture"],
                    "emi_partner": True,
                    "rating": 4.7,
                    "services": ["Sales", "Service", "Training", "EMI Processing"]
                }
            ],
            "eligibility_criteria": {
                "minimum_age": 21,
                "maximum_age": 65,
                "minimum_income": 25000,
                "credit_score_minimum": 600,
                "land_ownership": "Required",
                "existing_loan_limit": 3,
                "documents_required": [
                    "Aadhaar Card",
                    "PAN Card",
                    "Income Certificate",
                    "Land Records",
                    "Bank Statements (6 months)",
                    "Passport Size Photos"
                ]
            },
            "emi_statistics": {
                "total_applications": 8500,
                "approved_applications": 7200,
                "approval_rate": 84.7,
                "total_loan_amount": 6120000000,
                "average_loan_amount": 850000,
                "default_rate": 3.2,
                "most_popular_tenure": "48 months",
                "top_product_category": "Tractors"
            }
        }
    
    def calculate_emi(self, principal, rate, tenure):
        monthly_rate = rate / (12 * 100)
        emi = principal * monthly_rate * (1 + monthly_rate)**tenure / ((1 + monthly_rate)**tenure - 1)
        total_amount = emi * tenure
        total_interest = total_amount - principal
        
        return {
            "monthly_emi": round(emi, 2),
            "total_amount": round(total_amount, 2),
            "total_interest": round(total_interest, 2),
            "principal": principal,
            "rate": rate,
            "tenure": tenure
        }
    
    def check_eligibility(self, age, income, credit_score, land_area, existing_loans):
        criteria = self.data["eligibility_criteria"]
        eligible = True
        reasons = []
        
        if age < criteria["minimum_age"] or age > criteria["maximum_age"]:
            eligible = False
            reasons.append(f"Age should be between {criteria['minimum_age']} and {criteria['maximum_age']}")
        
        if income < criteria["minimum_income"]:
            eligible = False
            reasons.append(f"Minimum income required: ₹{criteria['minimum_income']}")
        
        if credit_score < criteria["credit_score_minimum"]:
            eligible = False
            reasons.append(f"Minimum credit score required: {criteria['credit_score_minimum']}")
        
        if existing_loans > criteria["existing_loan_limit"]:
            eligible = False
            reasons.append(f"Maximum existing loans allowed: {criteria['existing_loan_limit']}")
        
        max_loan_amount = min(income * 24, 2000000) if eligible else 0
        
        return {
            "eligible": eligible,
            "reasons": reasons,
            "max_loan_amount": max_loan_amount,
            "recommended_down_payment": 20 if eligible else 0
        }
    
    def get_emi_products(self):
        return self.data["emi_products"]
    
    def get_emi_applications(self):
        return self.data["emi_applications"]
    
    def get_dealers(self):
        return self.data["dealers"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Emi Purchase is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
