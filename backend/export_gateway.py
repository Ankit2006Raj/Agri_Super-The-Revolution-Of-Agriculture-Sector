import json
import csv
from datetime import datetime, timedelta

class ExportGateway:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        """Load export buyers and requirements data"""
        try:
            with open('data/logistics/export_buyers.csv', 'r') as f:
                reader = csv.DictReader(f)
                self.export_buyers = list(reader)
            
            with open('data/logistics/export_requirements_by_country.json', 'r') as f:
                self.export_requirements = json.load(f)
                
        except FileNotFoundError:
            self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """Initialize with comprehensive export data"""
        self.export_buyers = [
            {
                "buyer_id": "EXP001", "company_name": "Global Agri Trading LLC", "country": "UAE",
                "contact_person": "Ahmed Al-Rashid", "email": "ahmed@globalagri.ae",
                "phone": "+971-4-123-4567", "crops_interested": "Rice,Wheat,Pulses",
                "min_quantity_mt": "100", "max_quantity_mt": "5000", "payment_terms": "LC at sight",
                "rating": "4.8", "total_orders": "156", "established_year": "2010"
            },
            {
                "buyer_id": "EXP002", "company_name": "European Organic Foods", "country": "Germany",
                "contact_person": "Hans Mueller", "email": "hans@euroorganic.de",
                "phone": "+49-30-987-6543", "crops_interested": "Organic Rice,Turmeric,Spices",
                "min_quantity_mt": "50", "max_quantity_mt": "2000", "payment_terms": "30 days credit",
                "rating": "4.9", "total_orders": "89", "established_year": "2015"
            },
            {
                "buyer_id": "EXP003", "company_name": "Asia Pacific Commodities", "country": "Singapore",
                "contact_person": "Li Wei Chen", "email": "liwei@apcommodities.sg",
                "phone": "+65-6789-0123", "crops_interested": "Basmati Rice,Tea,Cashews",
                "min_quantity_mt": "200", "max_quantity_mt": "10000", "payment_terms": "LC 90 days",
                "rating": "4.7", "total_orders": "234", "established_year": "2008"
            },
            {
                "buyer_id": "EXP004", "company_name": "Middle East Food Corp", "country": "Saudi Arabia",
                "contact_person": "Omar Hassan", "email": "omar@mefoodcorp.sa",
                "phone": "+966-11-456-7890", "crops_interested": "Dates,Rice,Pulses",
                "min_quantity_mt": "150", "max_quantity_mt": "3000", "payment_terms": "Advance payment",
                "rating": "4.6", "total_orders": "178", "established_year": "2012"
            },
            {
                "buyer_id": "EXP005", "company_name": "African Agri Solutions", "country": "South Africa",
                "contact_person": "Nelson Mandela Jr", "email": "nelson@afriagri.co.za",
                "phone": "+27-11-234-5678", "crops_interested": "Maize,Sorghum,Pulses",
                "min_quantity_mt": "300", "max_quantity_mt": "8000", "payment_terms": "LC at sight",
                "rating": "4.5", "total_orders": "145", "established_year": "2014"
            }
        ]
        
        self.export_requirements = {
            "UAE": {
                "required_documents": [
                    "Phytosanitary Certificate", "Certificate of Origin", "Commercial Invoice",
                    "Packing List", "Bill of Lading", "Health Certificate"
                ],
                "quality_standards": "CODEX Alimentarius",
                "packaging_requirements": "Food grade packaging, proper labeling in Arabic/English",
                "inspection_required": True,
                "lead_time_days": 15,
                "port_of_entry": "Jebel Ali Port, Dubai",
                "import_duty": "5%",
                "special_requirements": "Halal certification for processed foods"
            },
            "Germany": {
                "required_documents": [
                    "Phytosanitary Certificate", "Organic Certificate (if applicable)",
                    "Commercial Invoice", "EUR.1 Certificate", "Packing List"
                ],
                "quality_standards": "EU Organic Regulation, HACCP",
                "packaging_requirements": "EU compliant packaging, German labeling",
                "inspection_required": True,
                "lead_time_days": 20,
                "port_of_entry": "Hamburg Port",
                "import_duty": "0% (under trade agreement)",
                "special_requirements": "Pesticide residue testing, organic certification"
            },
            "Singapore": {
                "required_documents": [
                    "Phytosanitary Certificate", "Certificate of Origin", "Commercial Invoice",
                    "Health Certificate", "Import Permit"
                ],
                "quality_standards": "Singapore Food Agency standards",
                "packaging_requirements": "Food grade packaging, English labeling",
                "inspection_required": True,
                "lead_time_days": 12,
                "port_of_entry": "Port of Singapore",
                "import_duty": "0-10% depending on product",
                "special_requirements": "Pre-shipment inspection may be required"
            }
        }
    
    def get_export_opportunities(self, crop_type, quantity_mt, region="all"):
        """Get matching export opportunities for given crop and quantity"""
        opportunities = []
        
        for buyer in self.export_buyers:
            crops_interested = [crop.strip().lower() for crop in buyer["crops_interested"].split(",")]
            min_qty = float(buyer["min_quantity_mt"])
            max_qty = float(buyer["max_quantity_mt"])
            
            if (crop_type.lower() in crops_interested or "all" in crops_interested) and \
               min_qty <= quantity_mt <= max_qty:
                
                country_req = self.export_requirements.get(buyer["country"], {})
                
                opportunity = {
                    "buyer_info": buyer,
                    "requirements": country_req,
                    "estimated_price_premium": self.calculate_export_premium(crop_type, buyer["country"]),
                    "total_estimated_value": self.estimate_export_value(crop_type, quantity_mt, buyer["country"]),
                    "readiness_score": self.calculate_readiness_score(crop_type, buyer["country"]),
                    "next_steps": self.get_next_steps(buyer["country"])
                }
                opportunities.append(opportunity)
        
        # Sort by estimated value and rating
        opportunities.sort(key=lambda x: (float(x["buyer_info"]["rating"]), x["total_estimated_value"]), reverse=True)
        return opportunities
    
    def calculate_export_premium(self, crop_type, country):
        """Calculate export price premium over domestic prices"""
        premiums = {
            "UAE": {"rice": 15, "wheat": 12, "pulses": 18, "default": 10},
            "Germany": {"rice": 25, "turmeric": 30, "spices": 35, "default": 20},
            "Singapore": {"rice": 20, "tea": 28, "cashews": 22, "default": 15},
            "Saudi Arabia": {"dates": 40, "rice": 18, "pulses": 16, "default": 12},
            "South Africa": {"maize": 8, "sorghum": 10, "pulses": 14, "default": 8}
        }
        
        country_premiums = premiums.get(country, {"default": 10})
        return country_premiums.get(crop_type.lower(), country_premiums["default"])
    
    def estimate_export_value(self, crop_type, quantity_mt, country):
        """Estimate total export value"""
        base_prices = {
            "rice": 800, "wheat": 350, "pulses": 1200, "turmeric": 8000,
            "spices": 5000, "tea": 3500, "cashews": 12000, "dates": 6000,
            "maize": 300, "sorghum": 280
        }
        
        base_price = base_prices.get(crop_type.lower(), 500)  # USD per MT
        premium = self.calculate_export_premium(crop_type, country)
        export_price = base_price * (1 + premium/100)
        
        return round(export_price * quantity_mt, 2)
    
    def calculate_readiness_score(self, crop_type, country):
        """Calculate export readiness score (0-100)"""
        # Mock scoring based on various factors
        base_score = 70
        
        # Adjust based on crop type and destination
        if country in ["Germany"] and crop_type.lower() in ["organic rice", "turmeric"]:
            base_score += 15  # High demand for organic
        elif country in ["UAE", "Saudi Arabia"] and crop_type.lower() in ["rice", "dates"]:
            base_score += 10  # Traditional demand
        
        return min(base_score, 100)
    
    def get_next_steps(self, country):
        """Get next steps for export preparation"""
        requirements = self.export_requirements.get(country, {})
        
        steps = [
            "Complete quality assessment and grading",
            "Obtain required certifications",
            "Prepare export documentation",
            "Arrange logistics and shipping",
            "Submit RFQ to matched buyers"
        ]
        
        if requirements.get("inspection_required"):
            steps.insert(1, "Schedule pre-shipment inspection")
        
        if "organic" in requirements.get("special_requirements", "").lower():
            steps.insert(1, "Obtain organic certification")
        
        return steps
    
    def submit_rfq(self, buyer_id, crop_details, farmer_info):
        """Submit Request for Quotation to buyer"""
        buyer = next((b for b in self.export_buyers if b["buyer_id"] == buyer_id), None)
        
        if not buyer:
            return {"success": False, "message": "Buyer not found"}
        
        rfq_id = f"RFQ{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        rfq_data = {
            "rfq_id": rfq_id,
            "buyer_info": buyer,
            "crop_details": crop_details,
            "farmer_info": farmer_info,
            "submitted_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "submitted",
            "expected_response_time": "3-5 business days"
        }
        
        return {
            "success": True,
            "rfq_id": rfq_id,
            "message": f"RFQ submitted successfully to {buyer['company_name']}",
            "rfq_data": rfq_data
        }
    
    def get_documentation_checklist(self, country):
        """Get export documentation checklist for specific country"""
        requirements = self.export_requirements.get(country, {})
        
        checklist = []
        for doc in requirements.get("required_documents", []):
            checklist.append({
                "document": doc,
                "status": "pending",
                "description": self.get_document_description(doc),
                "validity_days": self.get_document_validity(doc)
            })
        
        return checklist
    
    def get_document_description(self, document):
        """Get description for export documents"""
        descriptions = {
            "Phytosanitary Certificate": "Certificate ensuring plants/products are free from pests and diseases",
            "Certificate of Origin": "Document certifying the country where goods were produced",
            "Commercial Invoice": "Bill for goods sold, including price, terms, and shipping details",
            "Packing List": "Detailed list of package contents, weights, and dimensions",
            "Bill of Lading": "Receipt for goods shipped, contract between shipper and carrier",
            "Health Certificate": "Certificate ensuring food safety and hygiene standards",
            "Organic Certificate": "Certification for organic production methods and standards",
            "EUR.1 Certificate": "Preferential origin certificate for EU trade",
            "Import Permit": "Permission from importing country to bring in specific goods"
        }
        return descriptions.get(document, "Export documentation required by importing country")
    
    def get_document_validity(self, document):
        """Get validity period for export documents"""
        validity = {
            "Phytosanitary Certificate": 14,
            "Certificate of Origin": 30,
            "Commercial Invoice": 90,
            "Health Certificate": 30,
            "Organic Certificate": 365,
            "EUR.1 Certificate": 30
        }
        return validity.get(document, 30)

def get_export_gateway():
    return ExportGateway()

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Export Gateway is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
