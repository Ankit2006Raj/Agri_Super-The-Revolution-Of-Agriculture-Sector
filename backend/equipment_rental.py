import json
import csv
from datetime import datetime, timedelta

class EquipmentRental:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        """Load equipment listings and rental data"""
        try:
            with open('data/marketplace/equipment_listings.csv', 'r') as f:
                reader = csv.DictReader(f)
                self.equipment_listings = list(reader)
        except FileNotFoundError:
            self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """Initialize with comprehensive equipment rental data"""
        self.equipment_listings = [
            {
                "equipment_id": "EQ001", "name": "John Deere 5050D Tractor", "category": "Tractor",
                "owner_name": "Rajesh Kumar", "location": "Ludhiana, Punjab", "phone": "+91-98765-43210",
                "hourly_rate": "800", "daily_rate": "6000", "weekly_rate": "35000",
                "horsepower": "50", "year": "2020", "condition": "Excellent",
                "availability": "Available", "rating": "4.8", "total_bookings": "156",
                "features": "Power steering,4WD,PTO", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Optional (+₹500/day)"
            },
            {
                "equipment_id": "EQ002", "name": "Mahindra 575 DI Tractor", "category": "Tractor",
                "owner_name": "Suresh Patel", "location": "Ahmedabad, Gujarat", "phone": "+91-87654-32109",
                "hourly_rate": "700", "daily_rate": "5500", "weekly_rate": "32000",
                "horsepower": "47", "year": "2019", "condition": "Good",
                "availability": "Available", "rating": "4.6", "total_bookings": "134",
                "features": "Hydraulic steering,2WD,Live PTO", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Yes"
            },
            {
                "equipment_id": "EQ003", "name": "New Holland TC5070 Combine", "category": "Harvester",
                "owner_name": "Harpreet Singh", "location": "Amritsar, Punjab", "phone": "+91-76543-21098",
                "hourly_rate": "2500", "daily_rate": "18000", "weekly_rate": "110000",
                "horsepower": "140", "year": "2021", "condition": "Excellent",
                "availability": "Booked until 2024-01-15", "rating": "4.9", "total_bookings": "89",
                "features": "GPS guidance,Grain tank 4500L,Chopper", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Yes"
            },
            {
                "equipment_id": "EQ004", "name": "Kubota DC-70G Combine", "category": "Harvester",
                "owner_name": "Ramesh Yadav", "location": "Karnal, Haryana", "phone": "+91-65432-10987",
                "hourly_rate": "2200", "daily_rate": "16000", "weekly_rate": "95000",
                "horsepower": "75", "year": "2020", "condition": "Good",
                "availability": "Available", "rating": "4.7", "total_bookings": "112",
                "features": "Rubber tracks,Grain tank 3500L,Easy maintenance", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Optional (+₹800/day)"
            },
            {
                "equipment_id": "EQ005", "name": "Lemken Plough 4-Furrow", "category": "Tillage",
                "owner_name": "Vikram Singh", "location": "Jalandhar, Punjab", "phone": "+91-54321-09876",
                "hourly_rate": "400", "daily_rate": "2500", "weekly_rate": "15000",
                "horsepower": "N/A", "year": "2019", "condition": "Good",
                "availability": "Available", "rating": "4.5", "total_bookings": "78",
                "features": "Reversible plough,Auto reset,Heavy duty", "fuel_type": "N/A",
                "insurance_covered": "Yes", "operator_included": "No"
            },
            {
                "equipment_id": "EQ006", "name": "Fieldking Rotavator 7ft", "category": "Tillage",
                "owner_name": "Mohan Lal", "location": "Meerut, UP", "phone": "+91-43210-98765",
                "hourly_rate": "350", "daily_rate": "2200", "weekly_rate": "13000",
                "horsepower": "N/A", "year": "2020", "condition": "Excellent",
                "availability": "Available", "rating": "4.4", "total_bookings": "95",
                "features": "Side drive,L-shaped blades,Adjustable depth", "fuel_type": "N/A",
                "insurance_covered": "Yes", "operator_included": "No"
            },
            {
                "equipment_id": "EQ007", "name": "Swaraj 855 FE Tractor", "category": "Tractor",
                "owner_name": "Balwinder Singh", "location": "Patiala, Punjab", "phone": "+91-32109-87654",
                "hourly_rate": "750", "daily_rate": "5800", "weekly_rate": "34000",
                "horsepower": "55", "year": "2018", "condition": "Good",
                "availability": "Available", "rating": "4.3", "total_bookings": "167",
                "features": "Power steering,Dual clutch,High lift capacity", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Optional (+₹600/day)"
            },
            {
                "equipment_id": "EQ008", "name": "Preet 987 Self Propelled Reaper", "category": "Harvester",
                "owner_name": "Gurdeep Kaur", "location": "Bathinda, Punjab", "phone": "+91-21098-76543",
                "hourly_rate": "1800", "daily_rate": "12000", "weekly_rate": "75000",
                "horsepower": "35", "year": "2021", "condition": "Excellent",
                "availability": "Available", "rating": "4.8", "total_bookings": "67",
                "features": "Self propelled,Grain tank,Easy operation", "fuel_type": "Diesel",
                "insurance_covered": "Yes", "operator_included": "Yes"
            }
        ]
        
        # Add booking history and availability calendar
        self.booking_history = []
        self.availability_calendar = {}
        
        # Initialize availability for next 30 days
        for equipment in self.equipment_listings:
            equipment_id = equipment["equipment_id"]
            self.availability_calendar[equipment_id] = {}
            
            for i in range(30):
                date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
                # Randomly make some dates unavailable
                if equipment["availability"] == "Available":
                    self.availability_calendar[equipment_id][date] = "available"
                else:
                    self.availability_calendar[equipment_id][date] = "booked"
    
    def search_equipment(self, category="all", location="all", date_range=None, max_rate=None):
        """Search equipment based on filters"""
        filtered_equipment = []
        
        for equipment in self.equipment_listings:
            # Filter by category
            if category != "all" and equipment["category"].lower() != category.lower():
                continue
            
            # Filter by location (basic string matching)
            if location != "all" and location.lower() not in equipment["location"].lower():
                continue
            
            # Filter by rate
            if max_rate and float(equipment["daily_rate"]) > max_rate:
                continue
            
            # Check availability for date range
            if date_range:
                available = self.check_availability(equipment["equipment_id"], date_range)
                if not available:
                    continue
            
            # Add calculated fields
            equipment_copy = equipment.copy()
            equipment_copy["total_revenue"] = self.calculate_total_revenue(equipment["equipment_id"])
            equipment_copy["next_available"] = self.get_next_available_date(equipment["equipment_id"])
            
            filtered_equipment.append(equipment_copy)
        
        # Sort by rating and availability
        filtered_equipment.sort(key=lambda x: (float(x["rating"]), x["availability"] == "Available"), reverse=True)
        
        return filtered_equipment
    
    def check_availability(self, equipment_id, date_range):
        """Check if equipment is available for given date range"""
        start_date, end_date = date_range
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        
        while current_date <= end_date_obj:
            date_str = current_date.strftime("%Y-%m-%d")
            if self.availability_calendar.get(equipment_id, {}).get(date_str) != "available":
                return False
            current_date += timedelta(days=1)
        
        return True
    
    def get_next_available_date(self, equipment_id):
        """Get next available date for equipment"""
        for i in range(30):
            date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
            if self.availability_calendar.get(equipment_id, {}).get(date) == "available":
                return date
        return "Not available in next 30 days"
    
    def calculate_total_revenue(self, equipment_id):
        """Calculate total revenue generated by equipment"""
        # Mock calculation based on bookings
        equipment = next((e for e in self.equipment_listings if e["equipment_id"] == equipment_id), None)
        if equipment:
            total_bookings = int(equipment["total_bookings"])
            avg_daily_rate = float(equipment["daily_rate"])
            return round(total_bookings * avg_daily_rate * 0.7, 2)  # Assuming 70% utilization
        return 0
    
    def create_booking(self, equipment_id, renter_info, booking_details):
        """Create new equipment booking"""
        equipment = next((e for e in self.equipment_listings if e["equipment_id"] == equipment_id), None)
        
        if not equipment:
            return {"success": False, "message": "Equipment not found"}
        
        # Check availability
        date_range = (booking_details["start_date"], booking_details["end_date"])
        if not self.check_availability(equipment_id, date_range):
            return {"success": False, "message": "Equipment not available for selected dates"}
        
        # Calculate costs
        start_date = datetime.strptime(booking_details["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(booking_details["end_date"], "%Y-%m-%d")
        rental_days = (end_date - start_date).days + 1
        
        daily_rate = float(equipment["daily_rate"])
        rental_cost = daily_rate * rental_days
        
        # Add operator cost if requested
        operator_cost = 0
        if booking_details.get("operator_required") and "Optional" in equipment["operator_included"]:
            operator_rate = 500  # Default operator rate
            operator_cost = operator_rate * rental_days
        
        # Security deposit (20% of rental cost)
        security_deposit = rental_cost * 0.2
        
        total_cost = rental_cost + operator_cost + security_deposit
        
        booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        booking = {
            "booking_id": booking_id,
            "equipment_id": equipment_id,
            "equipment_name": equipment["name"],
            "renter_info": renter_info,
            "booking_details": booking_details,
            "cost_breakdown": {
                "rental_cost": rental_cost,
                "operator_cost": operator_cost,
                "security_deposit": security_deposit,
                "total_cost": total_cost
            },
            "status": "confirmed",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "owner_contact": equipment["phone"]
        }
        
        # Update availability calendar
        current_date = start_date
        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            self.availability_calendar[equipment_id][date_str] = "booked"
            current_date += timedelta(days=1)
        
        self.booking_history.append(booking)
        
        return {
            "success": True,
            "booking_id": booking_id,
            "message": "Booking confirmed successfully",
            "booking_details": booking
        }
    
    def get_booking_details(self, booking_id):
        """Get booking details by ID"""
        booking = next((b for b in self.booking_history if b["booking_id"] == booking_id), None)
        
        if not booking:
            return {"success": False, "message": "Booking not found"}
        
        return {"success": True, "booking": booking}
    
    def get_equipment_reviews(self, equipment_id):
        """Get reviews for specific equipment"""
        # Mock reviews data
        reviews = [
            {
                "reviewer_name": "Amit Sharma",
                "rating": 5,
                "review": "Excellent tractor, very well maintained. Owner was very helpful.",
                "date": "2024-01-10",
                "verified_booking": True
            },
            {
                "reviewer_name": "Priya Patel",
                "rating": 4,
                "review": "Good equipment, slight delay in delivery but overall satisfied.",
                "date": "2024-01-05",
                "verified_booking": True
            },
            {
                "reviewer_name": "Ravi Kumar",
                "rating": 5,
                "review": "Perfect for my 10-acre farm. Fuel efficient and powerful.",
                "date": "2023-12-28",
                "verified_booking": True
            }
        ]
        
        return reviews
    
    def submit_review(self, booking_id, review_data):
        """Submit review for completed booking"""
        booking = next((b for b in self.booking_history if b["booking_id"] == booking_id), None)
        
        if not booking:
            return {"success": False, "message": "Booking not found"}
        
        review = {
            "booking_id": booking_id,
            "equipment_id": booking["equipment_id"],
            "reviewer_name": review_data["reviewer_name"],
            "rating": review_data["rating"],
            "review": review_data["review"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "verified_booking": True
        }
        
        return {
            "success": True,
            "message": "Review submitted successfully",
            "review": review
        }

def get_equipment_rental():
    return EquipmentRental()

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Equipment Rental is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
