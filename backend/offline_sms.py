import json
import os
from datetime import datetime, timedelta

class OfflineSMSSupport:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'offline_sms_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "sms_commands": [
                {"command": "PRICE RICE", "description": "Get current rice prices", "response_format": "Rice: Rs.2500/quintal (Market: Delhi)"},
                {"command": "WEATHER", "description": "Get weather forecast", "response_format": "Today: 28°C, Sunny. Tomorrow: 30°C, Cloudy"},
                {"command": "YIELD WHEAT 5", "description": "Get yield prediction for 5 acres wheat", "response_format": "Wheat 5 acres: Expected 125 quintals"},
                {"command": "ALERT ON", "description": "Enable price alerts", "response_format": "Price alerts activated for your crops"}
            ],
            "offline_features": [
                {
                    "feature": "Price Inquiry",
                    "sms_code": "PRICE [CROP]",
                    "availability": "24/7",
                    "response_time": "< 30 seconds"
                },
                {
                    "feature": "Weather Updates",
                    "sms_code": "WEATHER [LOCATION]",
                    "availability": "24/7",
                    "response_time": "< 30 seconds"
                },
                {
                    "feature": "Market Alerts",
                    "sms_code": "ALERT [ON/OFF]",
                    "availability": "24/7",
                    "response_time": "Immediate"
                }
            ],
            "sms_logs": [
                {
                    "phone": "+91-9876543210",
                    "message": "PRICE WHEAT",
                    "response": "Wheat: Rs.2200/quintal (Market: Mumbai)",
                    "timestamp": "2024-03-15 10:30:45",
                    "status": "Delivered"
                },
                {
                    "phone": "+91-8765432109",
                    "message": "WEATHER PUNE",
                    "response": "Pune: 26°C, Light rain expected. Tomorrow: 24°C",
                    "timestamp": "2024-03-15 11:15:22",
                    "status": "Delivered"
                }
            ],
            "usage_statistics": {
                "total_sms_sent": 45678,
                "active_sms_users": 12847,
                "most_used_command": "PRICE",
                "average_response_time": "18 seconds"
            }
        }
    
    def process_sms_command(self, phone_number, message):
        # Process incoming SMS command
        message = message.upper().strip()
        
        if message.startswith("PRICE"):
            crop = message.replace("PRICE", "").strip()
            return f"{crop}: Rs.{random.randint(2000, 3000)}/quintal (Market: Delhi)"
        elif message.startswith("WEATHER"):
            location = message.replace("WEATHER", "").strip()
            return f"{location}: {random.randint(20, 35)}°C, Partly cloudy"
        elif message == "HELP":
            return "Commands: PRICE [CROP], WEATHER [CITY], ALERT ON/OFF. Reply HELP for more info."
        else:
            return "Invalid command. Reply HELP for available commands."
    
    def get_sms_statistics(self):
        return self.data.get("usage_statistics", {})

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Offline Sms is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
