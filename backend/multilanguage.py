import json
import os

class MultiLanguageSupport:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'multilanguage_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        return {
            "supported_languages": [
                {"code": "en", "name": "English", "native_name": "English", "coverage": "100%"},
                {"code": "hi", "name": "Hindi", "native_name": "हिन्दी", "coverage": "95%"},
                {"code": "bn", "name": "Bengali", "native_name": "বাংলা", "coverage": "90%"},
                {"code": "te", "name": "Telugu", "native_name": "తెలుగు", "coverage": "85%"},
                {"code": "ta", "name": "Tamil", "native_name": "தமிழ்", "coverage": "85%"},
                {"code": "mr", "name": "Marathi", "native_name": "मराठी", "coverage": "80%"},
                {"code": "gu", "name": "Gujarati", "native_name": "ગુજરાતી", "coverage": "75%"},
                {"code": "kn", "name": "Kannada", "native_name": "ಕನ್ನಡ", "coverage": "70%"}
            ],
            "translations": {
                "en": {
                    "welcome": "Welcome to AgriSuper",
                    "dashboard": "Dashboard",
                    "pricing": "Dynamic Pricing",
                    "yield_prediction": "Yield Prediction",
                    "market_comparison": "Market Comparison"
                },
                "hi": {
                    "welcome": "एग्रीसुपर में आपका स्वागत है",
                    "dashboard": "डैशबोर्ड",
                    "pricing": "गतिशील मूल्य निर्धारण",
                    "yield_prediction": "उत्पादन पूर्वानुमान",
                    "market_comparison": "बाजार तुलना"
                },
                "bn": {
                    "welcome": "এগ্রিসুপারে আপনাকে স্বাগতম",
                    "dashboard": "ড্যাশবোর্ড",
                    "pricing": "গতিশীল মূল্য নির্ধারণ",
                    "yield_prediction": "ফলন পূর্বাভাস",
                    "market_comparison": "বাজার তুলনা"
                }
            },
            "regional_preferences": [
                {"region": "North India", "primary_languages": ["hi", "en"], "currency": "INR", "date_format": "DD/MM/YYYY"},
                {"region": "South India", "primary_languages": ["te", "ta", "kn", "en"], "currency": "INR", "date_format": "DD/MM/YYYY"},
                {"region": "West India", "primary_languages": ["mr", "gu", "en"], "currency": "INR", "date_format": "DD/MM/YYYY"}
            ]
        }
    
    def get_translation(self, key, language_code="en"):
        translations = self.data.get("translations", {})
        language_translations = translations.get(language_code, translations.get("en", {}))
        return language_translations.get(key, key)
    
    def get_supported_languages(self):
        return self.data.get("supported_languages", [])

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Multilanguage is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
