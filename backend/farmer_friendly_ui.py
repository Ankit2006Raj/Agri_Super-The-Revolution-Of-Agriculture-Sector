"""
Farmer-Friendly UI Enhancement System
Optimized for low-literacy users with visual guides and simplified navigation
"""

from typing import Dict, List
from datetime import datetime


class FarmerFriendlyUI:
    """
    UI/UX enhancements specifically designed for farmer accessibility:
    - Large touch-friendly buttons (minimum 48x48px)
    - High contrast colors for outdoor visibility
    - Icon-based navigation for low-literacy users
    - Voice guidance integration
    - Simplified workflows (max 3 steps per task)
    - Regional language support
    """
    
    def __init__(self):
        self.design_principles = {
            'touch_target_min_size': 48,  # pixels
            'font_size_min': 16,  # pixels
            'color_contrast_ratio': 4.5,  # WCAG AA standard
            'max_steps_per_task': 3,
            'icon_size': 64,  # pixels
        }
        
        # Icon mapping for common actions (universal symbols)
        self.action_icons = {
            'market_price': '💰',
            'weather': '🌤️',
            'question': '❓',
            'learning': '📚',
            'wallet': '💳',
            'sell': '🤝',
            'buy': '🛒',
            'loan': '🏦',
            'insurance': '🛡️',
            'call': '📞',
            'message': '💬',
            'help': '❗',
            'home': '🏠',
            'back': '⬅️',
            'next': '➡️',
            'location': '📍',
            'photo': '📷',
            'success': '✅',
            'warning': '⚠️',
            'error': '❌',
            'info': 'ℹ️'
        }
        
        # Color palette optimized for outdoor visibility
        self.color_scheme = {
            'primary': '#4CAF50',      # Green (agriculture)
            'secondary': '#2E7D32',    # Dark green
            'accent': '#FF9800',       # Orange (alerts)
            'success': '#4CAF50',
            'warning': '#FFC107',
            'danger': '#F44336',
            'info': '#2196F3',
            'text_primary': '#212121',
            'text_secondary': '#757575',
            'background': '#FAFAFA',
            'surface': '#FFFFFF'
        }
    
    def get_simplified_dashboard_layout(self, user_role: str = 'farmer') -> Dict:
        """
        Generate simplified dashboard with priority features
        Organized by frequency of use and farmer needs
        """
        
        if user_role == 'farmer':
            return {
                'hero_actions': [
                    # Top 4 most-used features (large buttons)
                    {
                        'id': 'check_price',
                        'icon': self.action_icons['market_price'],
                        'title_en': 'Market Price',
                        'title_hi': 'मंडी भाव',
                        'title_regional': '{regional}',
                        'description_en': 'Check today\'s prices',
                        'description_hi': 'आज के भाव देखें',
                        'action': '/market-prices',
                        'color': self.color_scheme['primary'],
                        'priority': 1,
                        'voice_command': 'market price | mandi bhav'
                    },
                    {
                        'id': 'check_weather',
                        'icon': self.action_icons['weather'],
                        'title_en': 'Weather',
                        'title_hi': 'मौसम',
                        'title_regional': '{regional}',
                        'description_en': '7-day forecast',
                        'description_hi': '7 दिन का मौसम',
                        'action': '/weather-alerts',
                        'color': self.color_scheme['info'],
                        'priority': 2,
                        'voice_command': 'weather | mausam'
                    },
                    {
                        'id': 'ask_question',
                        'icon': self.action_icons['question'],
                        'title_en': 'Ask Expert',
                        'title_hi': 'सवाल पूछें',
                        'title_regional': '{regional}',
                        'description_en': 'Get farming advice',
                        'description_hi': 'खेती की सलाह लें',
                        'action': '/community-forum',
                        'color': self.color_scheme['accent'],
                        'priority': 3,
                        'voice_command': 'ask question | sawal pucho'
                    },
                    {
                        'id': 'my_wallet',
                        'icon': self.action_icons['wallet'],
                        'title_en': 'My Wallet',
                        'title_hi': 'मेरा वॉलेट',
                        'title_regional': '{regional}',
                        'description_en': 'Check balance',
                        'description_hi': 'बैलेंस देखें',
                        'action': '/digital-wallet',
                        'color': self.color_scheme['secondary'],
                        'priority': 4,
                        'voice_command': 'wallet | wallet check'
                    }
                ],
                
                'quick_actions': [
                    # Secondary features (smaller buttons, grid layout)
                    {
                        'id': 'sell_crop',
                        'icon': self.action_icons['sell'],
                        'title_hi': 'फसल बेचें',
                        'action': '/farmer-to-farmer-trade'
                    },
                    {
                        'id': 'buy_inputs',
                        'icon': self.action_icons['buy'],
                        'title_hi': 'खाद खरीदें',
                        'action': '/fertilizer-price-comparison'
                    },
                    {
                        'id': 'get_loan',
                        'icon': self.action_icons['loan'],
                        'title_hi': 'लोन लें',
                        'action': '/micro-loans'
                    },
                    {
                        'id': 'insurance',
                        'icon': self.action_icons['insurance'],
                        'title_hi': 'बीमा',
                        'action': '/crop-insurance'
                    },
                    {
                        'id': 'learn',
                        'icon': self.action_icons['learning'],
                        'title_hi': 'सीखें',
                        'action': '/elearning-courses'
                    },
                    {
                        'id': 'help',
                        'icon': self.action_icons['call'],
                        'title_hi': 'मदद',
                        'action': '/help'
                    }
                ],
                
                'alerts': {
                    'show': True,
                    'max_items': 3,
                    'icons': True,
                    'sound_enabled': True
                }
            }
        
        # Other role layouts (buyer, expert, etc.)
        return {}
    
    def get_accessibility_features(self) -> Dict:
        """
        Return comprehensive accessibility features for farmers
        """
        return {
            'visual': {
                'high_contrast_mode': True,
                'large_text_mode': True,
                'icon_labels': True,
                'color_blind_friendly': True,
                'outdoor_brightness_optimization': True
            },
            'interaction': {
                'touch_friendly': True,
                'gesture_navigation': True,
                'voice_commands': True,
                'haptic_feedback': True,
                'single_hand_mode': True
            },
            'language': {
                'multilingual': True,
                'text_to_speech': True,
                'speech_to_text': True,
                'visual_translations': True,
                'regional_dialects': True
            },
            'offline': {
                'offline_mode': True,
                'sms_fallback': True,
                'ussd_support': True,
                'low_bandwidth_mode': True
            },
            'assistance': {
                'guided_tours': True,
                'contextual_help': True,
                'video_tutorials': True,
                'customer_support_call': True,
                'whatsapp_support': True
            }
        }
    
    def generate_step_by_step_wizard(self, task: str) -> List[Dict]:
        """
        Break down complex tasks into simple 3-step wizards
        Example: Selling crops, applying for loans, etc.
        """
        
        wizards = {
            'sell_crop': [
                {
                    'step': 1,
                    'title_hi': 'कौनसी फसल बेचनी है?',
                    'title_en': 'Which crop to sell?',
                    'type': 'selection',
                    'input_type': 'image_grid',  # Visual crop selection
                    'options': [
                        {'value': 'wheat', 'icon': '🌾', 'label_hi': 'गेहूं'},
                        {'value': 'rice', 'icon': '🌾', 'label_hi': 'चावल'},
                        {'value': 'onion', 'icon': '🧅', 'label_hi': 'प्याज'},
                        {'value': 'potato', 'icon': '🥔', 'label_hi': 'आलू'},
                        {'value': 'tomato', 'icon': '🍅', 'label_hi': 'टमाटर'},
                    ],
                    'help_text_hi': 'अपनी फसल की तस्वीर पर क्लिक करें',
                    'voice_enabled': True
                },
                {
                    'step': 2,
                    'title_hi': 'कितनी मात्रा बेचनी है?',
                    'title_en': 'How much quantity?',
                    'type': 'input',
                    'input_type': 'number_large',  # Large number pad
                    'unit': 'quintal',
                    'unit_hi': 'क्विंटल',
                    'quick_options': [10, 20, 50, 100],  # Quick tap options
                    'help_text_hi': 'मात्रा क्विंटल में भरें',
                    'voice_enabled': True
                },
                {
                    'step': 3,
                    'title_hi': 'पुष्टि करें और भाव देखें',
                    'title_en': 'Confirm and see prices',
                    'type': 'confirmation',
                    'summary': {
                        'crop': '{crop}',
                        'quantity': '{quantity} quintal',
                        'expected_price_range': '{min} - {max} per quintal'
                    },
                    'actions': [
                        {
                            'type': 'primary',
                            'label_hi': '✅ हाँ, आगे बढ़ें',
                            'action': 'submit'
                        },
                        {
                            'type': 'secondary',
                            'label_hi': '⬅️ वापस जाएं',
                            'action': 'back'
                        }
                    ]
                }
            ],
            
            'check_price': [
                {
                    'step': 1,
                    'title_hi': 'फसल चुनें',
                    'title_en': 'Select crop',
                    'type': 'selection',
                    'input_type': 'image_grid_large',
                    'popular_first': True,
                    'voice_enabled': True
                },
                {
                    'step': 2,
                    'title_hi': 'आपकी लोकेशन',
                    'title_en': 'Your location',
                    'type': 'location',
                    'options': [
                        {'type': 'gps', 'label_hi': '📍 मेरी जगह', 'auto': True},
                        {'type': 'manual', 'label_hi': '✏️ नाम से चुनें'}
                    ]
                },
                {
                    'step': 3,
                    'title_hi': 'आज की कीमत',
                    'title_en': 'Today\'s price',
                    'type': 'result',
                    'display': 'large_price_card',
                    'show_trend': True,
                    'show_nearby_markets': True,
                    'actions': [
                        {'label_hi': '🔄 ताज़ा करें', 'action': 'refresh'},
                        {'label_hi': '📲 शेयर करें', 'action': 'share'},
                        {'label_hi': '🔔 अलर्ट सेट करें', 'action': 'set_alert'}
                    ]
                }
            ]
        }
        
        return wizards.get(task, [])
    
    def get_visual_guides(self) -> Dict:
        """
        Generate visual guides for common farming tasks
        Uses icons, images, and minimal text
        """
        return {
            'onboarding': {
                'screens': [
                    {
                        'image': '/static/guides/welcome.png',
                        'title_hi': 'स्वागत है! 🎉',
                        'subtitle_hi': 'खेती के लिए सब कुछ एक जगह',
                        'duration_seconds': 3
                    },
                    {
                        'image': '/static/guides/prices.png',
                        'title_hi': 'रोज़ की कीमतें देखें 💰',
                        'subtitle_hi': '3000+ मंडियों के भाव',
                        'duration_seconds': 3
                    },
                    {
                        'image': '/static/guides/weather.png',
                        'title_hi': 'मौसम जानें 🌤️',
                        'subtitle_hi': '7 दिन का पूर्वानुमान',
                        'duration_seconds': 3
                    },
                    {
                        'image': '/static/guides/community.png',
                        'title_hi': 'सवाल पूछें ❓',
                        'subtitle_hi': 'एक्सपर्ट की मदद लें',
                        'duration_seconds': 3
                    }
                ],
                'skip_button': True,
                'auto_play': True
            },
            
            'quick_tips': [
                {
                    'id': 'price_check',
                    'icon': '💡',
                    'tip_hi': 'सुबह 10 बजे के बाद की कीमतें ज़्यादा सही होती हैं',
                    'tip_en': 'Prices after 10 AM are more accurate'
                },
                {
                    'id': 'best_time_sell',
                    'icon': '💡',
                    'tip_hi': 'त्योहार से पहले सब्जियों की कीमत बढ़ती है',
                    'tip_en': 'Vegetable prices rise before festivals'
                },
                {
                    'id': 'weather_alert',
                    'icon': '💡',
                    'tip_hi': 'बारिश की चेतावनी मिलने पर फसल की कटाई जल्दी करें',
                    'tip_en': 'Harvest quickly when rain is forecasted'
                }
            ]
        }
    
    def get_voice_commands_config(self) -> Dict:
        """
        Configure voice commands for hands-free operation
        Critical for farmers working in fields
        """
        return {
            'enabled': True,
            'languages': ['hi-IN', 'en-IN', 'pa-IN', 'mr-IN', 'ta-IN'],
            'activation_phrase': 'Hey AgriSuper',
            'commands': {
                'navigation': {
                    'home': ['home', 'ghar', 'होम'],
                    'back': ['back', 'peeche', 'पीछे', 'wapas'],
                    'help': ['help', 'madad', 'मदद']
                },
                'features': {
                    'market_price': [
                        'market price',
                        'mandi bhav',
                        'मंडी भाव',
                        'keemat',
                        'कीमत'
                    ],
                    'weather': [
                        'weather',
                        'mausam',
                        'मौसम'
                    ],
                    'ask_question': [
                        'ask question',
                        'sawal pucho',
                        'सवाल पूछो'
                    ]
                },
                'actions': {
                    'call_support': [
                        'call support',
                        'help call',
                        'helpline',
                        'madad call'
                    ],
                    'refresh': [
                        'refresh',
                        'reload',
                        'taza karo',
                        'ताज़ा करो'
                    ]
                }
            },
            'feedback': {
                'listening': '🎤 सुन रहा हूँ...',
                'processing': '⏳ समझ रहा हूँ...',
                'success': '✅ समझ गया!',
                'error': '❌ फिर से बोलें'
            }
        }
    
    def get_simplified_forms_config(self) -> Dict:
        """
        Simplified form designs for farmers
        - Minimal fields (ask only essential info)
        - Auto-fill where possible
        - Visual indicators for required fields
        - Progress indicators
        """
        return {
            'design_rules': {
                'fields_per_page': 3,  # Max 3 questions per screen
                'required_indicator': '⭐',
                'optional_indicator': '(वैकल्पिक)',
                'help_always_visible': True,
                'auto_save': True,
                'voice_input_enabled': True
            },
            'input_enhancements': {
                'phone': {
                    'type': 'tel',
                    'format': '+91-XXXXX-XXXXX',
                    'verify_otp': True,
                    'auto_fill': True
                },
                'location': {
                    'gps_first': True,
                    'fallback': 'dropdown',
                    'nearby_suggestions': True
                },
                'date': {
                    'type': 'calendar_large',
                    'format': 'DD/MM/YYYY',
                    'past_dates_disabled': True
                },
                'number': {
                    'large_keypad': True,
                    'quick_amounts': True,  # 100, 500, 1000 buttons
                    'calculator': True
                }
            }
        }
    
    def get_notification_settings(self) -> Dict:
        """
        Smart notification system optimized for farmers
        """
        return {
            'channels': {
                'push': {'enabled': True, 'priority': 'high'},
                'sms': {'enabled': True, 'priority': 'critical'},
                'whatsapp': {'enabled': True, 'priority': 'medium'},
                'voice_call': {'enabled': True, 'priority': 'emergency'}
            },
            'timing': {
                'quiet_hours': {
                    'start': '22:00',
                    'end': '06:00'
                },
                'preferred_times': ['07:00-09:00', '17:00-19:00']
            },
            'types': {
                'price_alert': {
                    'icon': '💰',
                    'sound': 'coin',
                    'vibration': 'short',
                    'priority': 'high',
                    'channels': ['push', 'sms']
                },
                'weather_warning': {
                    'icon': '⚠️',
                    'sound': 'alarm',
                    'vibration': 'long',
                    'priority': 'critical',
                    'channels': ['push', 'sms', 'voice_call']
                },
                'payment_received': {
                    'icon': '✅',
                    'sound': 'success',
                    'vibration': 'double',
                    'priority': 'high',
                    'channels': ['push', 'sms', 'whatsapp']
                },
                'question_answered': {
                    'icon': '💬',
                    'sound': 'notification',
                    'vibration': 'short',
                    'priority': 'medium',
                    'channels': ['push']
                }
            }
        }


# Helper functions for UI components

def generate_large_button_html(action: Dict, language: str = 'hi') -> str:
    """Generate HTML for large touch-friendly button"""
    title_key = f'title_{language}'
    desc_key = f'description_{language}'
    
    return f'''
    <a href="{action['action']}" class="farmer-action-button" 
       style="background-color: {action['color']};"
       data-voice="{action['voice_command']}">
        <div class="button-icon">{action['icon']}</div>
        <div class="button-content">
            <h3 class="button-title">{action.get(title_key, action['title_en'])}</h3>
            <p class="button-desc">{action.get(desc_key, action['description_en'])}</p>
        </div>
        <div class="button-arrow">→</div>
    </a>
    '''


def generate_wizard_step_html(step: Dict, current_step: int, total_steps: int) -> str:
    """Generate HTML for wizard step"""
    progress_percent = (current_step / total_steps) * 100
    
    return f'''
    <div class="wizard-container">
        <div class="wizard-progress">
            <div class="progress-bar" style="width: {progress_percent}%"></div>
            <span class="progress-text">Step {current_step} of {total_steps}</span>
        </div>
        
        <div class="wizard-step">
            <h2 class="step-title">{step['title_hi']}</h2>
            <p class="step-help">{step.get('help_text_hi', '')}</p>
            
            <div class="step-content">
                <!-- Step-specific content goes here -->
            </div>
            
            <div class="wizard-actions">
                {f'<button class="btn-back">⬅️ पीछे</button>' if current_step > 1 else ''}
                <button class="btn-next">आगे →</button>
            </div>
        </div>
    </div>
    '''


# CSS for farmer-friendly UI
FARMER_UI_CSS = '''
/* Farmer-Friendly UI Styles */

.farmer-action-button {
    display: flex;
    align-items: center;
    padding: 20px;
    margin: 10px 0;
    border-radius: 15px;
    text-decoration: none;
    color: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
    min-height: 100px;
}

.farmer-action-button:active {
    transform: scale(0.95);
}

.button-icon {
    font-size: 48px;
    margin-right: 15px;
}

.button-content {
    flex: 1;
    text-align: left;
}

.button-title {
    font-size: 24px;
    font-weight: 600;
    margin: 0;
}

.button-desc {
    font-size: 16px;
    margin: 5px 0 0 0;
    opacity: 0.9;
}

.button-arrow {
    font-size: 32px;
    font-weight: bold;
}

/* Wizard styles */
.wizard-progress {
    background: #E0E0E0;
    height: 8px;
    border-radius: 4px;
    margin-bottom: 20px;
    position: relative;
}

.progress-bar {
    background: #4CAF50;
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s ease;
}

.progress-text {
    position: absolute;
    top: 15px;
    right: 0;
    font-size: 14px;
    color: #666;
}

/* Large number pad for quantity input */
.number-pad {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    padding: 20px;
}

.number-pad button {
    font-size: 32px;
    padding: 25px;
    border: 2px solid #4CAF50;
    background: white;
    border-radius: 10px;
    cursor: pointer;
}

.number-pad button:active {
    background: #4CAF50;
    color: white;
}

/* High contrast mode */
.high-contrast {
    filter: contrast(1.5);
}

/* Large text mode */
.large-text * {
    font-size: 1.5em !important;
}

/* Outdoor brightness optimization */
@media (light-level: washed) {
    body {
        background: white;
        color: black;
    }
}
'''
