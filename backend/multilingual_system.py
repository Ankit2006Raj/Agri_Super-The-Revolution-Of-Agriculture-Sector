"""
Enhanced Multilingual Support System for AgriSuper-App
Supports 22 Indian languages + English with regional dialects
"""

from typing import Dict, List, Optional
from datetime import datetime
import json


class MultilingualSystem:
    """
    Comprehensive multilingual support system
    - 22 scheduled languages + English
    - Regional dialect support
    - Dynamic translation loading
    - Voice input/output in native languages
    - Cultural context adaptation
    """
    
    # Indian languages with their codes and native names
    SUPPORTED_LANGUAGES = {
        'hi': {'name': 'Hindi', 'native': 'हिंदी', 'speakers': 52.83, 'script': 'Devanagari'},
        'en': {'name': 'English', 'native': 'English', 'speakers': 12.18, 'script': 'Latin'},
        'bn': {'name': 'Bengali', 'native': 'বাংলা', 'speakers': 8.03, 'script': 'Bengali'},
        'te': {'name': 'Telugu', 'native': 'తెలుగు', 'speakers': 8.11, 'script': 'Telugu'},
        'mr': {'name': 'Marathi', 'native': 'मराठी', 'speakers': 7.27, 'script': 'Devanagari'},
        'ta': {'name': 'Tamil', 'native': 'தமிழ்', 'speakers': 6.70, 'script': 'Tamil'},
        'gu': {'name': 'Gujarati', 'native': 'ગુજરાતી', 'speakers': 5.54, 'script': 'Gujarati'},
        'kn': {'name': 'Kannada', 'native': 'ಕನ್ನಡ', 'speakers': 4.37, 'script': 'Kannada'},
        'ml': {'name': 'Malayalam', 'native': 'മലയാളം', 'speakers': 3.48, 'script': 'Malayalam'},
        'or': {'name': 'Odia', 'native': 'ଓଡ଼ିଆ', 'speakers': 3.75, 'script': 'Odia'},
        'pa': {'name': 'Punjabi', 'native': 'ਪੰਜਾਬੀ', 'speakers': 3.15, 'script': 'Gurmukhi'},
        'as': {'name': 'Assamese', 'native': 'অসমীয়া', 'speakers': 1.53, 'script': 'Bengali'},
        'ur': {'name': 'Urdu', 'native': 'اردو', 'speakers': 5.07, 'script': 'Urdu'},
        'bh': {'name': 'Bhojpuri', 'native': 'भोजपुरी', 'speakers': 5.11, 'script': 'Devanagari'},
        'raj': {'name': 'Rajasthani', 'native': 'राजस्थानी', 'speakers': 2.60, 'script': 'Devanagari'},
        'mai': {'name': 'Maithili', 'native': 'मैथिली', 'speakers': 1.35, 'script': 'Devanagari'},
        'mg': {'name': 'Magahi', 'native': 'मगही', 'speakers': 1.27, 'script': 'Devanagari'},
        'sd': {'name': 'Sindhi', 'native': 'سنڌي', 'speakers': 0.27, 'script': 'Devanagari'},
        'ks': {'name': 'Kashmiri', 'native': 'कॉशुर', 'speakers': 0.69, 'script': 'Devanagari'},
        'ne': {'name': 'Nepali', 'native': 'नेपाली', 'speakers': 0.30, 'script': 'Devanagari'},
        'sa': {'name': 'Sanskrit', 'native': 'संस्कृतम्', 'speakers': 0.024, 'script': 'Devanagari'},
        'kok': {'name': 'Konkani', 'native': 'कोंकणी', 'speakers': 0.25, 'script': 'Devanagari'},
        'mni': {'name': 'Manipuri', 'native': 'মৈতৈলোন্', 'speakers': 0.17, 'script': 'Bengali'}
    }
    
    def __init__(self, default_language: str = 'hi'):
        self.default_language = default_language
        self.translations_cache = {}
        self.regional_variations = self._load_regional_variations()
    
    def _load_regional_variations(self) -> Dict:
        """Load regional dialect variations for better local understanding"""
        return {
            'hi': {
                'dialects': ['Braj', 'Awadhi', 'Khari Boli', 'Haryanvi'],
                'variations': {
                    'price': ['bhav', 'keemat', 'daam', 'rate'],
                    'market': ['mandi', 'bazar', 'market'],
                    'weather': ['mausam', 'weather', 'aasman'],
                    'crop': ['fasal', 'kheti', 'crop'],
                    'farmer': ['kisan', 'farmer', 'kheti karne wala']
                }
            },
            'pa': {
                'dialects': ['Majhi', 'Doabi', 'Malwai', 'Powadhi'],
                'variations': {
                    'price': ['bhaav', 'keemat', 'rate'],
                    'market': ['mandi', 'market'],
                    'weather': ['mausam', 'hawa-paani'],
                    'crop': ['fasal', 'kheti'],
                    'farmer': ['kisan', 'khethihaar']
                }
            },
            'mr': {
                'dialects': ['Standard', 'Konkani', 'Ahirani', 'Varhadi'],
                'variations': {
                    'price': ['bhaav', 'kimmat'],
                    'market': ['bajar', 'market'],
                    'weather': ['havaman'],
                    'crop': ['pik', 'lagvad'],
                    'farmer': ['shetkari', 'kisan']
                }
            }
        }
    
    def get_translations(self, language_code: str = 'hi') -> Dict:
        """
        Get comprehensive translation dictionary for specified language
        Returns all UI strings, messages, and agricultural terminology
        """
        
        # Agricultural terminology translations
        translations = {
            'hi': self._get_hindi_translations(),
            'en': self._get_english_translations(),
            'pa': self._get_punjabi_translations(),
            'mr': self._get_marathi_translations(),
            'ta': self._get_tamil_translations(),
            'te': self._get_telugu_translations(),
            'bn': self._get_bengali_translations(),
            'gu': self._get_gujarati_translations(),
            'kn': self._get_kannada_translations(),
            'ml': self._get_malayalam_translations(),
        }
        
        return translations.get(language_code, translations['hi'])
    
    def _get_hindi_translations(self) -> Dict:
        """Complete Hindi translations (primary language)"""
        return {
            # Navigation
            'home': 'होम',
            'back': 'वापस',
            'next': 'आगे',
            'submit': 'जमा करें',
            'cancel': 'रद्द करें',
            'save': 'सहेजें',
            'delete': 'मिटाएं',
            'edit': 'संपादित करें',
            'search': 'खोजें',
            'filter': 'फ़िल्टर करें',
            'sort': 'क्रमबद्ध करें',
            
            # Common actions
            'login': 'लॉगिन करें',
            'logout': 'लॉगआउट',
            'register': 'रजिस्टर करें',
            'update': 'अपडेट करें',
            'refresh': 'ताज़ा करें',
            'share': 'शेयर करें',
            'download': 'डाउनलोड करें',
            'upload': 'अपलोड करें',
            
            # Features
            'market_price': 'मंडी भाव',
            'weather': 'मौसम',
            'weather_forecast': 'मौसम पूर्वानुमान',
            'ask_question': 'सवाल पूछें',
            'community_forum': 'सामुदायिक मंच',
            'wallet': 'वॉलेट',
            'digital_wallet': 'डिजिटल वॉलेट',
            'balance': 'बैलेंस',
            'transaction': 'लेनदेन',
            'loan': 'लोन',
            'insurance': 'बीमा',
            'crop_insurance': 'फसल बीमा',
            'learning': 'सीखें',
            'courses': 'पाठ्यक्रम',
            'sell_crop': 'फसल बेचें',
            'buy_inputs': 'इनपुट खरीदें',
            'fertilizer': 'खाद',
            'seeds': 'बीज',
            'pesticide': 'कीटनाशक',
            
            # Agricultural terms
            'farmer': 'किसान',
            'farm': 'खेत',
            'crop': 'फसल',
            'harvest': 'कटाई',
            'sowing': 'बुवाई',
            'irrigation': 'सिंचाई',
            'yield': 'उपज',
            'profit': 'लाभ',
            'loss': 'हानि',
            'expense': 'खर्च',
            'income': 'आय',
            'land': 'ज़मीन',
            'soil': 'मिट्टी',
            'water': 'पानी',
            'rain': 'बारिश',
            'drought': 'सूखा',
            'flood': 'बाढ़',
            'pest': 'कीट',
            'disease': 'रोग',
            
            # Crops (common)
            'wheat': 'गेहूं',
            'rice': 'चावल',
            'paddy': 'धान',
            'sugarcane': 'गन्ना',
            'cotton': 'कपास',
            'maize': 'मक्का',
            'bajra': 'बाजरा',
            'jowar': 'ज्वार',
            'onion': 'प्याज',
            'potato': 'आलू',
            'tomato': 'टमाटर',
            'cabbage': 'पत्ता गोभी',
            'cauliflower': 'फूल गोभी',
            'brinjal': 'बैंगन',
            'okra': 'भिंडी',
            'peas': 'मटर',
            'beans': 'फलियां',
            'cucumber': 'खीरा',
            'bitter_gourd': 'करेला',
            'bottle_gourd': 'लौकी',
            
            # Units
            'quintal': 'क्विंटल',
            'kg': 'किलोग्राम',
            'ton': 'टन',
            'acre': 'एकड़',
            'hectare': 'हेक्टेयर',
            'rupees': 'रुपये',
            'per': 'प्रति',
            
            # Time
            'today': 'आज',
            'yesterday': 'कल (बीता हुआ)',
            'tomorrow': 'कल (आने वाला)',
            'week': 'सप्ताह',
            'month': 'महीना',
            'year': 'साल',
            'daily': 'रोज़ाना',
            'weekly': 'साप्ताहिक',
            'monthly': 'मासिक',
            
            # Messages
            'welcome': 'स्वागत है',
            'thank_you': 'धन्यवाद',
            'please_wait': 'कृपया प्रतीक्षा करें',
            'loading': 'लोड हो रहा है...',
            'success': 'सफल!',
            'error': 'त्रुटि',
            'no_data': 'कोई डेटा नहीं',
            'offline_mode': 'ऑफ़लाइन मोड',
            'online': 'ऑनलाइन',
            'offline': 'ऑफ़लाइन',
            
            # Questions/Prompts
            'select_crop': 'फसल चुनें',
            'select_location': 'स्थान चुनें',
            'enter_quantity': 'मात्रा दर्ज करें',
            'enter_amount': 'राशि दर्ज करें',
            'confirm': 'पुष्टि करें',
            'are_you_sure': 'क्या आप निश्चित हैं?',
            
            # Status
            'approved': 'स्वीकृत',
            'rejected': 'अस्वीकृत',
            'pending': 'लंबित',
            'completed': 'पूर्ण',
            'in_progress': 'प्रगति में',
            'cancelled': 'रद्द',
            
            # Help text
            'help': 'मदद',
            'call_support': 'सहायता कॉल करें',
            'whatsapp_support': 'व्हाट्सऐप सहायता',
            'tutorial': 'ट्यूटोरियल',
            'faq': 'आम सवाल',
            
            # Notifications
            'price_alert': 'भाव अलर्ट',
            'weather_warning': 'मौसम चेतावनी',
            'payment_received': 'भुगतान प्राप्त हुआ',
            'new_message': 'नया संदेश',
            'answer_received': 'जवाब मिला',
            
            # Long messages
            'price_check_help': 'अपनी फसल की आज की कीमत जानने के लिए फसल और अपनी लोकेशन चुनें।',
            'weather_help': 'अगले 7 दिनों का मौसम देखें और खेती के काम की योजना बनाएं।',
            'offline_message': 'आप ऑफ़लाइन हैं। कृपया इंटरनेट कनेक्शन जांचें।',
            'no_internet': 'इंटरनेट कनेक्शन नहीं मिल रहा।',
        }
    
    def _get_english_translations(self) -> Dict:
        """English translations (reference language)"""
        return {
            'home': 'Home',
            'back': 'Back',
            'next': 'Next',
            'submit': 'Submit',
            'cancel': 'Cancel',
            'market_price': 'Market Price',
            'weather': 'Weather',
            'ask_question': 'Ask Question',
            'wallet': 'Wallet',
            'balance': 'Balance',
            'loan': 'Loan',
            'insurance': 'Insurance',
            'farmer': 'Farmer',
            'crop': 'Crop',
            'wheat': 'Wheat',
            'rice': 'Rice',
            'quintal': 'Quintal',
            'today': 'Today',
            'welcome': 'Welcome',
            'loading': 'Loading...',
            'success': 'Success!',
            'offline_message': 'You are offline. Please check your internet connection.',
        }
    
    def _get_punjabi_translations(self) -> Dict:
        """Punjabi translations for Punjab/Haryana farmers"""
        return {
            'home': 'ਘਰ',
            'market_price': 'ਮੰਡੀ ਭਾਅ',
            'weather': 'ਮੌਸਮ',
            'farmer': 'ਕਿਸਾਨ',
            'crop': 'ਫ਼ਸਲ',
            'wheat': 'ਕਣਕ',
            'rice': 'ਚਾਵਲ',
            'paddy': 'ਧਾਨ',
            'quintal': 'ਕੁਇੰਟਲ',
            'sell_crop': 'ਫ਼ਸਲ ਵੇਚੋ',
            'buy_inputs': 'ਖਾਦ ਖਰੀਦੋ',
            'welcome': 'ਜੀ ਆਇਆਂ ਨੂੰ',
            'loading': 'ਲੋਡ ਹੋ ਰਿਹਾ ਹੈ...',
            'offline_message': 'ਤੁਸੀਂ ਔਫਲਾਈਨ ਹੋ। ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਜਾਂਚੋ।',
        }
    
    def _get_marathi_translations(self) -> Dict:
        """Marathi translations for Maharashtra farmers"""
        return {
            'home': 'मुख्यपृष्ठ',
            'market_price': 'बाजार भाव',
            'weather': 'हवामान',
            'farmer': 'शेतकरी',
            'crop': 'पीक',
            'wheat': 'गहू',
            'rice': 'तांदूळ',
            'quintal': 'क्विंटल',
            'sell_crop': 'पीक विका',
            'welcome': 'स्वागत आहे',
            'loading': 'लोड होत आहे...',
            'offline_message': 'तुम्ही ऑफलाइन आहात. कृपया तुमचे इंटरनेट कनेक्शन तपासा.',
        }
    
    def _get_tamil_translations(self) -> Dict:
        """Tamil translations for Tamil Nadu farmers"""
        return {
            'home': 'முகப்பு',
            'market_price': 'சந்தை விலை',
            'weather': 'வானிலை',
            'farmer': 'விவசாயி',
            'crop': 'பயிர்',
            'rice': 'அரிசி',
            'welcome': 'வரவேற்கிறோம்',
            'loading': 'ஏற்றுகிறது...',
        }
    
    def _get_telugu_translations(self) -> Dict:
        """Telugu translations for Andhra Pradesh/Telangana farmers"""
        return {
            'home': 'హోమ్',
            'market_price': 'మార్కెట్ ధర',
            'weather': 'వాతావరణం',
            'farmer': 'రైతు',
            'crop': 'పంట',
            'rice': 'వరి',
            'welcome': 'స్వాగతం',
            'loading': 'లోడ్ అవుతోంది...',
        }
    
    def _get_bengali_translations(self) -> Dict:
        """Bengali translations for West Bengal farmers"""
        return {
            'home': 'হোম',
            'market_price': 'বাজার দাম',
            'weather': 'আবহাওয়া',
            'farmer': 'কৃষক',
            'crop': 'ফসল',
            'rice': 'চাল',
            'welcome': 'স্বাগতম',
            'loading': 'লোড হচ্ছে...',
        }
    
    def _get_gujarati_translations(self) -> Dict:
        """Gujarati translations for Gujarat farmers"""
        return {
            'home': 'હોમ',
            'market_price': 'બજાર ભાવ',
            'weather': 'હવામાન',
            'farmer': 'ખેડૂત',
            'crop': 'પાક',
            'welcome': 'સ્વાગત છે',
            'loading': 'લોડ થઈ રહ્યું છે...',
        }
    
    def _get_kannada_translations(self) -> Dict:
        """Kannada translations for Karnataka farmers"""
        return {
            'home': 'ಮುಖಪುಟ',
            'market_price': 'ಮಾರುಕಟ್ಟೆ ಬೆಲೆ',
            'weather': 'ಹವಾಮಾನ',
            'farmer': 'ರೈತ',
            'crop': 'ಬೆಳೆ',
            'welcome': 'ಸ್ವಾಗತ',
            'loading': 'ಲೋಡ್ ಆಗುತ್ತಿದೆ...',
        }
    
    def _get_malayalam_translations(self) -> Dict:
        """Malayalam translations for Kerala farmers"""
        return {
            'home': 'ഹോം',
            'market_price': 'മാർക്കറ്റ് വില',
            'weather': 'കാലാവസ്ഥ',
            'farmer': 'കർഷകൻ',
            'crop': 'വിള',
            'welcome': 'സ്വാഗതം',
            'loading': 'ലോഡ് ചെയ്യുന്നു...',
        }
    
    def get_language_selector_config(self) -> Dict:
        """
        Configuration for language selector UI component
        Shows languages by popularity in region
        """
        return {
            'display_type': 'visual_grid',  # Show language names in native script
            'default_language': 'hi',
            'auto_detect': True,  # Detect from device settings
            'show_flags': False,  # Use native text instead of flags
            'popular_first': True,
            'search_enabled': True,
            'voice_enabled': True,  # "Please select your language"
            'groups': [
                {
                    'name': 'Most Popular',
                    'languages': ['hi', 'en', 'pa', 'mr', 'ta', 'te', 'bn', 'gu']
                },
                {
                    'name': 'Regional',
                    'languages': ['kn', 'ml', 'or', 'as', 'ur']
                },
                {
                    'name': 'Others',
                    'languages': ['bh', 'raj', 'mai', 'mg', 'sd', 'ks', 'ne', 'kok', 'mni']
                }
            ]
        }
    
    def get_voice_config_for_language(self, language_code: str) -> Dict:
        """
        Get voice input/output configuration for specific language
        """
        voice_configs = {
            'hi': {
                'speech_to_text': {
                    'provider': 'Google Cloud Speech',
                    'language_code': 'hi-IN',
                    'alternative_codes': ['hi-IN-Standard-A', 'hi-IN-Standard-B', 'hi-IN-Standard-C', 'hi-IN-Standard-D'],
                    'gender': 'FEMALE',  # More trusted by farmers
                    'speaking_rate': 0.9,  # Slightly slower for clarity
                    'pitch': 0
                },
                'text_to_speech': {
                    'provider': 'Google Cloud TTS',
                    'language_code': 'hi-IN',
                    'voice_name': 'hi-IN-Wavenet-D',
                    'gender': 'FEMALE',
                    'speaking_rate': 0.9,
                    'pitch': 0,
                    'volume_gain_db': 0
                },
                'pronunciation_adaptations': {
                    'quintal': 'क्विंटल',
                    'hectare': 'हेक्टेयर',
                    'tractor': 'ट्रैक्टर',
                    'fertilizer': 'खाद',
                }
            },
            'pa': {
                'speech_to_text': {
                    'provider': 'Google Cloud Speech',
                    'language_code': 'pa-IN',
                    'gender': 'FEMALE',
                    'speaking_rate': 0.9
                },
                'text_to_speech': {
                    'provider': 'Google Cloud TTS',
                    'language_code': 'pa-IN',
                    'voice_name': 'pa-IN-Standard-A',
                    'gender': 'FEMALE',
                    'speaking_rate': 0.9
                }
            },
            'en': {
                'speech_to_text': {
                    'provider': 'Google Cloud Speech',
                    'language_code': 'en-IN',
                    'gender': 'FEMALE',
                    'speaking_rate': 1.0
                },
                'text_to_speech': {
                    'provider': 'Google Cloud TTS',
                    'language_code': 'en-IN',
                    'voice_name': 'en-IN-Wavenet-D',
                    'gender': 'FEMALE',
                    'speaking_rate': 1.0
                }
            }
        }
        
        return voice_configs.get(language_code, voice_configs['hi'])
    
    def translate_agricultural_terms(self, terms: List[str], source_lang: str, target_lang: str) -> Dict[str, str]:
        """
        Translate agricultural terminology with context awareness
        Important for maintaining accuracy in farming advice
        """
        # This would integrate with translation APIs
        # For now, returning structure
        return {
            term: self._get_term_translation(term, source_lang, target_lang)
            for term in terms
        }
    
    def _get_term_translation(self, term: str, source_lang: str, target_lang: str) -> str:
        """Get context-aware translation for agricultural term"""
        # This would use agricultural dictionary
        # Placeholder implementation
        return term
    
    def get_cultural_adaptations(self, language_code: str) -> Dict:
        """
        Cultural adaptations for different regions
        Currency format, date format, units, festivals, etc.
        """
        adaptations = {
            'hi': {
                'currency_symbol': '₹',
                'currency_format': '₹{amount}',
                'date_format': 'DD/MM/YYYY',
                'time_format': '12h',
                'first_day_of_week': 'monday',
                'measurement_system': 'metric',
                'common_units': {
                    'area': 'acre',  # Also hectare
                    'weight': 'quintal',  # Also kg, ton
                    'distance': 'kilometer'
                },
                'festivals': [
                    {'name': 'होली', 'impact': 'high_vegetable_demand'},
                    {'name': 'दिवाली', 'impact': 'high_prices'},
                    {'name': 'रक्षाबंधन', 'impact': 'medium_demand'}
                ],
                'seasons': {
                    'kharif': 'खरीफ (Jun-Oct)',
                    'rabi': 'रबी (Nov-Apr)',
                    'zaid': 'ज़ायद (Mar-Jun)'
                }
            },
            'pa': {
                'currency_symbol': '₹',
                'date_format': 'DD/MM/YYYY',
                'common_units': {
                    'area': 'acre',
                    'weight': 'quintal'
                },
                'festivals': [
                    {'name': 'ਵਿਸਾਖੀ', 'impact': 'harvest_festival'},
                    {'name': 'ਲੋਹੜੀ', 'impact': 'winter_harvest'}
                ]
            }
        }
        
        return adaptations.get(language_code, adaptations['hi'])
    
    def get_sms_templates(self, language_code: str) -> Dict[str, str]:
        """
        SMS templates for offline/low-connectivity scenarios
        160 characters max (single SMS)
        """
        templates = {
            'hi': {
                'price_alert': 'AgriSuper: {crop} का भाव {location} में ₹{price}/{unit} है। {date}',
                'weather_alert': 'AgriSuper: {location} में {event} की चेतावनी। {action} करें।',
                'payment_received': 'AgriSuper: ₹{amount} प्राप्त हुआ। बैलेंस: ₹{balance}',
                'loan_approved': 'AgriSuper: आपका ₹{amount} का लोन मंज़ूर हुआ।',
                'answer_received': 'AgriSuper: आपके सवाल का जवाब मिला। ऐप खोलें।'
            },
            'en': {
                'price_alert': 'AgriSuper: {crop} price at {location} is ₹{price}/{unit}. {date}',
                'weather_alert': 'AgriSuper: {event} warning at {location}. {action}',
                'payment_received': 'AgriSuper: ₹{amount} received. Balance: ₹{balance}',
                'loan_approved': 'AgriSuper: Your loan of ₹{amount} approved.',
                'answer_received': 'AgriSuper: Your question answered. Open app.'
            }
        }
        
        return templates.get(language_code, templates['hi'])


# Helper function for dynamic translation loading
def load_translation_file(language_code: str, category: str = 'all') -> Dict:
    """
    Load translation files dynamically from JSON
    Allows for easy updates without code changes
    """
    translation_path = f"data/translations/{language_code}/{category}.json"
    try:
        with open(translation_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback to Hindi
        fallback_path = f"data/translations/hi/{category}.json"
        try:
            with open(fallback_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


# Usage example
if __name__ == "__main__":
    ml_system = MultilingualSystem(default_language='hi')
    
    # Get Hindi translations
    hindi_ui = ml_system.get_translations('hi')
    print(f"Market Price in Hindi: {hindi_ui['market_price']}")
    
    # Get Punjabi translations
    punjabi_ui = ml_system.get_translations('pa')
    print(f"Market Price in Punjabi: {punjabi_ui['market_price']}")
    
    # Get language selector config
    lang_config = ml_system.get_language_selector_config()
    print(f"\nSupported languages: {len(ml_system.SUPPORTED_LANGUAGES)}")
    
    # Get voice config for Hindi
    voice_config = ml_system.get_voice_config_for_language('hi')
    print(f"\nHindi TTS Voice: {voice_config['text_to_speech']['voice_name']}")
    
    # Get cultural adaptations
    culture = ml_system.get_cultural_adaptations('hi')
    print(f"\nCurrency format: {culture['currency_format']}")
    print(f"Common festivals: {[f['name'] for f in culture['festivals']]}")
