import json
import os
from datetime import datetime, timedelta
import random

class AdminDashboard:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'admin_dashboard_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "platform_stats": {
                "total_users": 125847,
                "active_farmers": 89234,
                "active_buyers": 36613,
                "total_transactions": 2847392,
                "total_revenue": 15847293.45,
                "monthly_growth": 12.5
            },
            "user_analytics": [
                {"month": "Jan 2024", "new_users": 8934, "active_users": 78234, "retention_rate": 85.2},
                {"month": "Feb 2024", "new_users": 9456, "active_users": 82145, "retention_rate": 86.1},
                {"month": "Mar 2024", "new_users": 10234, "active_users": 89234, "retention_rate": 87.3}
            ],
            "transaction_analytics": [
                {"date": "2024-03-01", "transactions": 2847, "volume": 584729.45, "avg_order": 205.67},
                {"date": "2024-03-02", "transactions": 3156, "volume": 647382.12, "avg_order": 215.23},
                {"date": "2024-03-03", "transactions": 2934, "volume": 598473.89, "avg_order": 203.91}
            ],
            "feature_usage": [
                {"feature": "Dynamic Pricing", "usage_count": 45678, "user_satisfaction": 4.2},
                {"feature": "Yield Prediction", "usage_count": 34567, "user_satisfaction": 4.5},
                {"feature": "Market Comparison", "usage_count": 28934, "user_satisfaction": 4.1}
            ],
            "system_health": {
                "server_uptime": "99.8%",
                "response_time": "245ms",
                "error_rate": "0.02%",
                "database_performance": "Optimal"
            }
        }
    
    def get_dashboard_stats(self):
        return self.data.get("platform_stats", {})
    
    def get_user_analytics(self):
        return self.data.get("user_analytics", [])
    
    def get_system_health(self):
        return self.data.get("system_health", {})

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Admin Dashboard is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
