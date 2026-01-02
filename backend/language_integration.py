"""
Multilingual Integration Module for app.py
This module integrates the multilingual system into the main Flask application
"""

from flask import session, request, jsonify
from backend.multilingual_system import MultilingualSystem
import os


# Initialize multilingual system
ml_system = MultilingualSystem(default_language='hi')


def register_language_routes(app):
    """
    Register language-related routes in the Flask application
    
    Routes:
    - /api/languages: Get list of supported languages
    - /api/language/set: Set user's preferred language
    - /api/translations/<lang>: Get translations for specific language
    - /api/language/detect: Auto-detect language from device/browser
    """
    
    @app.route('/api/languages')
    def get_supported_languages():
        """Get list of all supported languages"""
        languages = []
        for code, info in ml_system.SUPPORTED_LANGUAGES.items():
            languages.append({
                'code': code,
                'name': info['name'],
                'native_name': info['native'],
                'speakers_million': info['speakers'],
                'script': info['script']
            })
        
        # Sort by number of speakers (descending)
        languages.sort(key=lambda x: x['speakers_million'], reverse=True)
        
        return jsonify({
            'status': 'success',
            'total': len(languages),
            'languages': languages,
            'default': 'hi'
        })
    
    @app.route('/api/language/set', methods=['POST'])
    def set_user_language():
        """Set user's preferred language"""
        data = request.get_json()
        lang_code = data.get('language', 'hi')
        
        # Validate language code
        if lang_code not in ml_system.SUPPORTED_LANGUAGES:
            return jsonify({
                'status': 'error',
                'message': f'Unsupported language: {lang_code}'
            }), 400
        
        # Save to session
        session['language'] = lang_code
        
        # In production, also save to user profile in database
        
        return jsonify({
            'status': 'success',
            'language': lang_code,
            'native_name': ml_system.SUPPORTED_LANGUAGES[lang_code]['native']
        })
    
    @app.route('/api/translations/<lang_code>')
    def get_translations(lang_code):
        """Get translations for specific language"""
        if lang_code not in ml_system.SUPPORTED_LANGUAGES:
            return jsonify({
                'status': 'error',
                'message': f'Unsupported language: {lang_code}'
            }), 400
        
        translations = ml_system.get_translations(lang_code)
        
        return jsonify({
            'status': 'success',
            'language': lang_code,
            'translations': translations
        })
    
    @app.route('/api/language/detect')
    def detect_language():
        """Auto-detect language from browser/device settings"""
        # Get Accept-Language header
        accept_language = request.headers.get('Accept-Language', 'hi')
        
        # Parse first language code
        detected_lang = accept_language.split(',')[0].split('-')[0]
        
        # Map to supported language
        if detected_lang not in ml_system.SUPPORTED_LANGUAGES:
            detected_lang = 'hi'  # Default to Hindi
        
        return jsonify({
            'status': 'success',
            'detected_language': detected_lang,
            'native_name': ml_system.SUPPORTED_LANGUAGES[detected_lang]['native']
        })
    
    @app.route('/api/language/voice-config/<lang_code>')
    def get_voice_config(lang_code):
        """Get voice input/output configuration for language"""
        if lang_code not in ml_system.SUPPORTED_LANGUAGES:
            return jsonify({
                'status': 'error',
                'message': f'Unsupported language: {lang_code}'
            }), 400
        
        voice_config = ml_system.get_voice_config_for_language(lang_code)
        
        return jsonify({
            'status': 'success',
            'language': lang_code,
            'voice_config': voice_config
        })
    
    @app.route('/api/language/selector-config')
    def get_language_selector_config():
        """Get configuration for language selector UI"""
        config = ml_system.get_language_selector_config()
        return jsonify(config)


def get_user_language():
    """
    Get current user's preferred language
    Checks: session > browser header > default
    """
    # Check session
    if 'language' in session:
        return session['language']
    
    # Check browser
    accept_language = request.headers.get('Accept-Language', 'hi')
    detected_lang = accept_language.split(',')[0].split('-')[0]
    
    # Validate and return
    if detected_lang in ml_system.SUPPORTED_LANGUAGES:
        return detected_lang
    
    return 'hi'  # Default to Hindi


def translate(key: str, lang_code: str = None):
    """
    Translate a key to user's language
    Usage in templates: {{ translate('market_price') }}
    """
    if lang_code is None:
        lang_code = get_user_language()
    
    translations = ml_system.get_translations(lang_code)
    return translations.get(key, key)


def register_template_filters(app):
    """
    Register Jinja2 template filters for translations
    Usage in templates: {{ 'market_price' | translate }}
    """
    @app.template_filter('translate')
    def translate_filter(key, lang_code=None):
        return translate(key, lang_code)
    
    @app.template_filter('t')
    def t_filter(key, lang_code=None):
        """Shorthand for translate"""
        return translate(key, lang_code)


def add_language_context_processor(app):
    """
    Add language variables to all templates automatically
    """
    @app.context_processor
    def inject_language():
        current_lang = get_user_language()
        return {
            'current_language': current_lang,
            'language_name': ml_system.SUPPORTED_LANGUAGES[current_lang]['native'],
            'all_languages': ml_system.SUPPORTED_LANGUAGES,
            'translate': translate,
            't': translate  # Shorthand
        }


# Usage instructions for app.py integration
INTEGRATION_INSTRUCTIONS = """
To integrate multilingual support into app.py:

1. Import the module:
   from backend.language_integration import (
       register_language_routes,
       register_template_filters,
       add_language_context_processor,
       get_user_language,
       translate
   )

2. Register everything after app initialization:
   # Register routes
   register_language_routes(app)
   
   # Register template filters
   register_template_filters(app)
   
   # Add context processor
   add_language_context_processor(app)

3. Use in Python code:
   user_lang = get_user_language()
   greeting = translate('welcome', user_lang)

4. Use in templates (Jinja2):
   <h1>{{ 'welcome' | translate }}</h1>
   <p>{{ 'market_price' | t }}</p>
   
   Or:
   <h1>{{ translate('welcome') }}</h1>
   <p>{{ t('market_price') }}</p>

5. Language selector in template:
   <select id="language-selector" onchange="changeLanguage(this.value)">
       {% for code, info in all_languages.items() %}
       <option value="{{ code }}" {% if code == current_language %}selected{% endif %}>
           {{ info['native'] }}
       </option>
       {% endfor %}
   </select>
   
   <script>
   function changeLanguage(langCode) {
       fetch('/api/language/set', {
           method: 'POST',
           headers: {'Content-Type': 'application/json'},
           body: JSON.stringify({language: langCode})
       }).then(() => location.reload());
   }
   </script>

6. Test multilingual:
   - Visit: http://localhost:5000/api/languages
   - Change language: POST to /api/language/set with {"language": "pa"}
   - Verify translations appear in your language
"""


if __name__ == '__main__':
    print("=" * 60)
    print("MULTILINGUAL INTEGRATION GUIDE")
    print("=" * 60)
    print(f"\nSupported Languages: {len(ml_system.SUPPORTED_LANGUAGES)}")
    print("\nTop 5 by speakers:")
    for code, info in sorted(ml_system.SUPPORTED_LANGUAGES.items(), 
                            key=lambda x: x[1]['speakers'], reverse=True)[:5]:
        print(f"  {info['native']} ({info['name']}): {info['speakers']}M speakers")
    
    print("\n" + INTEGRATION_INSTRUCTIONS)
