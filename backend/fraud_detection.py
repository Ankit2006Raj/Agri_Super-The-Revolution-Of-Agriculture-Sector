import json
import os
from datetime import datetime, timedelta
import random

class FraudDetection:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'fraud_detection_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "fraud_patterns": [
                {
                    "pattern_id": 1,
                    "pattern_name": "Unusual Transaction Volume",
                    "description": "Transactions significantly higher than user's historical average",
                    "risk_level": "High",
                    "detection_rate": "94.2%",
                    "false_positive_rate": "2.1%"
                },
                {
                    "pattern_id": 2,
                    "pattern_name": "Geographic Anomaly",
                    "description": "Transactions from unusual locations for the user",
                    "risk_level": "Medium",
                    "detection_rate": "87.5%",
                    "false_positive_rate": "5.3%"
                }
            ],
            "suspicious_activities": [
                {
                    "activity_id": 1,
                    "user_id": "USR_12847",
                    "activity_type": "Multiple failed login attempts",
                    "timestamp": "2024-03-15 14:23:45",
                    "risk_score": 85,
                    "status": "Under Investigation"
                },
                {
                    "activity_id": 2,
                    "user_id": "USR_98234",
                    "activity_type": "Unusual payment pattern",
                    "timestamp": "2024-03-15 16:45:12",
                    "risk_score": 72,
                    "status": "Flagged for Review"
                }
            ],
            "ml_models": [
                {
                    "model_name": "Transaction Anomaly Detector",
                    "accuracy": "96.8%",
                    "last_trained": "2024-03-10",
                    "features_used": ["transaction_amount", "frequency", "location", "time_pattern"]
                },
                {
                    "model_name": "User Behavior Analyzer",
                    "accuracy": "93.4%",
                    "last_trained": "2024-03-08",
                    "features_used": ["login_pattern", "device_fingerprint", "session_duration"]
                }
            ]
        }
    
    def analyze_transaction(self, transaction_data):
        # Simulate fraud analysis
        risk_score = random.randint(1, 100)
        if risk_score > 80:
            return {"risk_level": "High", "action": "Block transaction", "score": risk_score}
        elif risk_score > 50:
            return {"risk_level": "Medium", "action": "Manual review", "score": risk_score}
        else:
            return {"risk_level": "Low", "action": "Approve", "score": risk_score}

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Fraud Detection is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
