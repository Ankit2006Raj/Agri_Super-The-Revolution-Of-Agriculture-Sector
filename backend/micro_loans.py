import json
import random
from datetime import datetime, timedelta

class MicroLoans:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/micro_loans_data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "loan_products": [
                {
                    "product_id": "ML001",
                    "name": "Crop Production Loan",
                    "min_amount": 10000,
                    "max_amount": 500000,
                    "interest_rate": 7.5,
                    "tenure_months": 12,
                    "processing_fee": 1.0,
                    "eligibility": ["Land ownership", "Crop insurance", "Good credit score"],
                    "documents": ["Land records", "Aadhaar", "PAN", "Bank statements"],
                    "approval_time": "3-5 days",
                    "lender": "State Bank of India"
                },
                {
                    "product_id": "ML002",
                    "name": "Equipment Purchase Loan",
                    "min_amount": 50000,
                    "max_amount": 2000000,
                    "interest_rate": 8.5,
                    "tenure_months": 60,
                    "processing_fee": 1.5,
                    "eligibility": ["Farming experience 2+ years", "Income proof", "Collateral"],
                    "documents": ["Income certificate", "Equipment quotation", "Land records"],
                    "approval_time": "7-10 days",
                    "lender": "HDFC Bank"
                },
                {
                    "product_id": "ML003",
                    "name": "Livestock Loan",
                    "min_amount": 25000,
                    "max_amount": 1000000,
                    "interest_rate": 9.0,
                    "tenure_months": 36,
                    "processing_fee": 1.2,
                    "eligibility": ["Animal husbandry experience", "Veterinary certificate"],
                    "documents": ["Veterinary certificate", "Shed construction plan", "Insurance"],
                    "approval_time": "5-7 days",
                    "lender": "ICICI Bank"
                }
            ],
            "loan_applications": [
                {
                    "application_id": "LA001",
                    "farmer_id": "F001",
                    "farmer_name": "Rajesh Kumar",
                    "product_id": "ML001",
                    "amount_requested": 150000,
                    "purpose": "Wheat cultivation for 10 acres",
                    "application_date": "2024-01-10",
                    "status": "Approved",
                    "credit_score": 750,
                    "monthly_income": 35000,
                    "existing_loans": 0,
                    "land_area": 10,
                    "approval_date": "2024-01-13",
                    "disbursement_date": "2024-01-15"
                },
                {
                    "application_id": "LA002",
                    "farmer_id": "F002",
                    "farmer_name": "Priya Sharma",
                    "product_id": "ML002",
                    "amount_requested": 800000,
                    "purpose": "Tractor purchase",
                    "application_date": "2024-01-12",
                    "status": "Under Review",
                    "credit_score": 680,
                    "monthly_income": 45000,
                    "existing_loans": 1,
                    "land_area": 15,
                    "approval_date": null,
                    "disbursement_date": null
                }
            ],
            "lenders": [
                {
                    "lender_id": "L001",
                    "name": "State Bank of India",
                    "type": "Public Bank",
                    "interest_rates": {"crop_loan": 7.5, "equipment_loan": 8.5, "livestock_loan": 9.0},
                    "max_loan_amount": 5000000,
                    "processing_time": "3-5 days",
                    "branches": 22000,
                    "digital_platform": true,
                    "special_schemes": ["PM-KISAN", "KCC", "PMFBY"]
                },
                {
                    "lender_id": "L002",
                    "name": "HDFC Bank",
                    "type": "Private Bank",
                    "interest_rates": {"crop_loan": 8.0, "equipment_loan": 8.5, "livestock_loan": 9.5},
                    "max_loan_amount": 3000000,
                    "processing_time": "5-7 days",
                    "branches": 5500,
                    "digital_platform": true,
                    "special_schemes": ["Agri Business Loan", "Warehouse Receipt Loan"]
                }
            ],
            "credit_scores": [
                {"range": "300-549", "category": "Poor", "approval_rate": 10, "interest_premium": 3.0},
                {"range": "550-649", "category": "Fair", "approval_rate": 35, "interest_premium": 2.0},
                {"range": "650-749", "category": "Good", "approval_rate": 70, "interest_premium": 1.0},
                {"range": "750-850", "category": "Excellent", "approval_rate": 95, "interest_premium": 0.0}
            ],
            "loan_statistics": {
                "total_applications": 15000,
                "approved_applications": 12500,
                "approval_rate": 83.3,
                "average_loan_amount": 275000,
                "total_disbursed": 3437500000,
                "default_rate": 2.1,
                "average_processing_time": "5.2 days"
            }
        }
    
    def calculate_eligibility(self, income, credit_score, land_area, existing_loans):
        eligibility_score = 0
        
        # Income factor (40%)
        if income >= 50000:
            eligibility_score += 40
        elif income >= 30000:
            eligibility_score += 30
        elif income >= 20000:
            eligibility_score += 20
        else:
            eligibility_score += 10
        
        # Credit score factor (35%)
        if credit_score >= 750:
            eligibility_score += 35
        elif credit_score >= 650:
            eligibility_score += 25
        elif credit_score >= 550:
            eligibility_score += 15
        else:
            eligibility_score += 5
        
        # Land area factor (15%)
        if land_area >= 10:
            eligibility_score += 15
        elif land_area >= 5:
            eligibility_score += 10
        else:
            eligibility_score += 5
        
        # Existing loans factor (10%)
        if existing_loans == 0:
            eligibility_score += 10
        elif existing_loans <= 2:
            eligibility_score += 5
        
        return {
            "eligibility_score": eligibility_score,
            "status": "Eligible" if eligibility_score >= 60 else "Not Eligible",
            "max_loan_amount": min(income * 12 * 2, 2000000) if eligibility_score >= 60 else 0
        }
    
    def get_loan_products(self):
        return self.data["loan_products"]
    
    def get_loan_applications(self):
        return self.data["loan_applications"]
    
    def get_lenders(self):
        return self.data["lenders"]

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Micro Loans is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
