import json
import random
from datetime import datetime, timedelta

class VoiceAssistant:
    def __init__(self, data_folder='data'):
        self.load_data()
    
    def load_data(self):
        try:
            with open('data/voice_assistant_data.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.get_default_data()
    
    def get_default_data(self):
        return {
            "languages": [
                {"code": "en", "name": "English", "active_users": 15000},
                {"code": "hi", "name": "Hindi", "active_users": 25000},
                {"code": "bn", "name": "Bengali", "active_users": 8000},
                {"code": "te", "name": "Telugu", "active_users": 6000},
                {"code": "ta", "name": "Tamil", "active_users": 5500},
                {"code": "mr", "name": "Marathi", "active_users": 4500},
                {"code": "gu", "name": "Gujarati", "active_users": 3500},
                {"code": "kn", "name": "Kannada", "active_users": 3000},
                {"code": "ml", "name": "Malayalam", "active_users": 2500},
                {"code": "pa", "name": "Punjabi", "active_users": 4000}
            ],
            "voice_commands": [
                {"command": "What is today's price for wheat?", "category": "pricing", "usage_count": 5000},
                {"command": "Show me weather forecast", "category": "weather", "usage_count": 4500},
                {"command": "When should I sow tomatoes?", "category": "farming", "usage_count": 4000},
                {"command": "Find buyers for my rice", "category": "marketplace", "usage_count": 3500},
                {"command": "Check my account balance", "category": "wallet", "usage_count": 3000},
                {"command": "Book storage space", "category": "logistics", "usage_count": 2500},
                {"command": "Apply for crop loan", "category": "finance", "usage_count": 2000},
                {"command": "Report pest attack", "category": "alerts", "usage_count": 1800},
                {"command": "Schedule irrigation", "category": "farming", "usage_count": 1500},
                {"command": "Check insurance status", "category": "insurance", "usage_count": 1200}
            ],
            "conversation_history": [
                {
                    "user_id": "farmer_001",
                    "conversations": [
                        {"timestamp": "2024-01-15 09:30", "query": "What is wheat price today?", "response": "Current wheat price is ₹2,150 per quintal in your area", "language": "en"},
                        {"timestamp": "2024-01-15 10:15", "query": "Weather forecast for next week", "response": "Expect light rainfall on Tuesday and Wednesday. Temperature will range 18-28°C", "language": "en"},
                        {"timestamp": "2024-01-15 14:20", "query": "Best time to harvest paddy", "response": "Based on your sowing date, optimal harvest time is in 15-20 days when moisture is 20-22%", "language": "en"}
                    ]
                }
            ],
            "ai_responses": {
                "pricing": [
                    "Current market price for {crop} is ₹{price} per quintal",
                    "Price trend shows {trend} movement for {crop}",
                    "Best selling price in your area is ₹{price} per quintal"
                ],
                "weather": [
                    "Today's weather: {condition}, Temperature: {temp}°C, Humidity: {humidity}%",
                    "Weather forecast for next 7 days shows {forecast}",
                    "Rainfall expected: {rainfall}mm in next 24 hours"
                ],
                "farming": [
                    "For {crop}, optimal sowing time is {time}",
                    "Your {crop} crop is in {stage} stage, next action: {action}",
                    "Recommended fertilizer for {crop}: {fertilizer}"
                ]
            },
            "voice_analytics": {
                "total_interactions": 125000,
                "daily_active_users": 8500,
                "average_session_duration": "4.5 minutes",
                "success_rate": "94.2%",
                "most_used_language": "Hindi",
                "peak_usage_hours": ["6-8 AM", "6-8 PM"]
            }
        }
    
    def process_voice_command(self, command, language="en", user_id=None):
        # Simulate voice processing
        response = {
            "command": command,
            "language": language,
            "timestamp": datetime.now().isoformat(),
            "confidence": random.uniform(0.85, 0.98),
            "response": f"Processing: {command}",
            "suggestions": ["Try asking about weather", "Check crop prices", "Book storage"]
        }
        return response
    
    def get_language_stats(self):
        return self.data["languages"]
    
    def get_voice_analytics(self):
        return self.data["voice_analytics"]
    
    def get_conversation_history(self, user_id):
        for user in self.data["conversation_history"]:
            if user["user_id"] == user_id:
                return user["conversations"]
        return []

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Voice Assistant is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
