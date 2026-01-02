"""
UI/UX Enhancement Integration Module for app.py
This module integrates farmer-friendly UI enhancements into the main Flask application
"""

from flask import jsonify, request, render_template
from backend.farmer_friendly_ui import FarmerFriendlyUI
import json


# Initialize UI system
ui_system = FarmerFriendlyUI()


def register_ui_enhancement_routes(app):
    """
    Register UI/UX enhancement routes in the Flask application
    
    Routes:
    - /api/ui/dashboard: Get simplified dashboard layout
    - /api/ui/wizard/<task>: Get step-by-step wizard for task
    - /api/ui/accessibility: Get accessibility features config
    - /api/ui/voice-commands: Get voice command configuration
    - /api/ui/notifications: Get notification settings
    """
    
    @app.route('/api/ui/dashboard')
    def get_dashboard_layout():
        """Get farmer-friendly dashboard layout"""
        user_role = request.args.get('role', 'farmer')
        layout = ui_system.get_simplified_dashboard_layout(user_role)
        
        return jsonify({
            'status': 'success',
            'layout': layout
        })
    
    @app.route('/api/ui/wizard/<task>')
    def get_wizard(task):
        """Get step-by-step wizard for specific task"""
        wizard_steps = ui_system.generate_step_by_step_wizard(task)
        
        if not wizard_steps:
            return jsonify({
                'status': 'error',
                'message': f'No wizard available for task: {task}'
            }), 404
        
        return jsonify({
            'status': 'success',
            'task': task,
            'total_steps': len(wizard_steps),
            'steps': wizard_steps
        })
    
    @app.route('/api/ui/accessibility')
    def get_accessibility_features():
        """Get accessibility features configuration"""
        features = ui_system.get_accessibility_features()
        
        return jsonify({
            'status': 'success',
            'features': features
        })
    
    @app.route('/api/ui/voice-commands')
    def get_voice_commands():
        """Get voice command configuration"""
        commands = ui_system.get_voice_commands_config()
        
        return jsonify({
            'status': 'success',
            'voice_commands': commands
        })
    
    @app.route('/api/ui/notifications')
    def get_notification_settings():
        """Get notification settings"""
        settings = ui_system.get_notification_settings()
        
        return jsonify({
            'status': 'success',
            'notification_settings': settings
        })
    
    @app.route('/api/ui/visual-guides')
    def get_visual_guides():
        """Get visual guides configuration"""
        guides = ui_system.get_visual_guides()
        
        return jsonify({
            'status': 'success',
            'visual_guides': guides
        })
    
    @app.route('/api/ui/forms-config')
    def get_forms_config():
        """Get simplified forms configuration"""
        config = ui_system.get_simplified_forms_config()
        
        return jsonify({
            'status': 'success',
            'forms_config': config
        })


def render_farmer_dashboard(user_data=None):
    """
    Render farmer-friendly dashboard with enhanced UI
    Can be used to replace existing dashboard route
    """
    layout = ui_system.get_simplified_dashboard_layout('farmer')
    accessibility = ui_system.get_accessibility_features()
    
    return render_template(
        'farmer_dashboard.html',
        layout=layout,
        accessibility=accessibility,
        user=user_data
    )


def generate_large_button_component(action_data, language='hi'):
    """
    Generate HTML for large touch-friendly button component
    Can be used in templates via Jinja2 macro
    """
    from backend.farmer_friendly_ui import generate_large_button_html
    return generate_large_button_html(action_data, language)


def generate_wizard_component(step_data, current_step, total_steps):
    """
    Generate HTML for wizard step component
    """
    from backend.farmer_friendly_ui import generate_wizard_step_html
    return generate_wizard_step_html(step_data, current_step, total_steps)


def add_ui_context_processor(app):
    """
    Add UI helper functions to all templates
    """
    @app.context_processor
    def inject_ui_helpers():
        return {
            'ui_system': ui_system,
            'generate_button': generate_large_button_component,
            'generate_wizard': generate_wizard_component,
            'action_icons': ui_system.action_icons,
            'color_scheme': ui_system.color_scheme
        }


def add_custom_css_route(app):
    """
    Serve farmer-friendly CSS styles
    """
    from backend.farmer_friendly_ui import FARMER_UI_CSS
    
    @app.route('/static/css/farmer-ui.css')
    def serve_farmer_ui_css():
        from flask import Response
        return Response(FARMER_UI_CSS, mimetype='text/css')


# Usage instructions for app.py integration
INTEGRATION_INSTRUCTIONS = """
To integrate UI/UX enhancements into app.py:

1. Import the module:
   from backend.ui_integration import (
       register_ui_enhancement_routes,
       add_ui_context_processor,
       add_custom_css_route,
       render_farmer_dashboard
   )

2. Register everything after app initialization:
   # Register routes
   register_ui_enhancement_routes(app)
   
   # Add context processor
   add_ui_context_processor(app)
   
   # Add custom CSS route
   add_custom_css_route(app)

3. Replace existing dashboard route:
   @app.route('/dashboard')
   def dashboard():
       user = get_current_user()  # Your auth function
       return render_farmer_dashboard(user)

4. Use in templates - Add farmer UI CSS:
   <link rel="stylesheet" href="/static/css/farmer-ui.css">

5. Use large buttons in templates:
   {% for action in layout.hero_actions %}
       {{ generate_button(action, current_language) | safe }}
   {% endfor %}

6. Use wizards in templates:
   <div id="wizard-container"></div>
   <script>
   fetch('/api/ui/wizard/sell_crop')
       .then(r => r.json())
       .then(data => {
           // Render wizard steps
           console.log(data.steps);
       });
   </script>

7. Enable voice commands:
   <script>
   fetch('/api/ui/voice-commands')
       .then(r => r.json())
       .then(config => {
           // Initialize voice recognition with config
           initVoiceCommands(config.voice_commands);
       });
   </script>

8. Use accessibility features:
   <body class="{% if high_contrast_enabled %}high-contrast{% endif %}
                {% if large_text_enabled %}large-text{% endif %}">

EXAMPLE: Complete dashboard route with all enhancements:

@app.route('/dashboard')
def dashboard():
    # Get user data
    user = session.get('user', {})
    
    # Get UI layout
    layout = ui_system.get_simplified_dashboard_layout('farmer')
    
    # Get current language
    from backend.language_integration import get_user_language, translate
    current_lang = get_user_language()
    
    # Render enhanced template
    return render_template(
        'enhanced_dashboard.html',
        layout=layout,
        user=user,
        language=current_lang,
        translate=translate
    )

EXAMPLE: Enhanced dashboard template (templates/enhanced_dashboard.html):

<!DOCTYPE html>
<html lang="{{ language }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ 'dashboard' | translate }} - AgriSuper</title>
    
    <!-- Farmer UI CSS -->
    <link rel="stylesheet" href="/static/css/farmer-ui.css">
    
    <!-- PWA Meta Tags -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#4CAF50">
</head>
<body>
    <div class="farmer-dashboard">
        <!-- Hero Actions (Top 4 most-used features) -->
        <section class="hero-actions">
            {% for action in layout.hero_actions %}
                {{ generate_button(action, language) | safe }}
            {% endfor %}
        </section>
        
        <!-- Quick Actions Grid -->
        <section class="quick-actions">
            <h2>{{ 'more_features' | translate }}</h2>
            <div class="action-grid">
                {% for action in layout.quick_actions %}
                    <a href="{{ action.action }}" class="quick-action-card">
                        <span class="action-icon">{{ action.icon }}</span>
                        <span class="action-title">{{ action.title_hi }}</span>
                    </a>
                {% endfor %}
            </div>
        </section>
        
        <!-- Voice Command Button -->
        <button id="voice-command-btn" class="voice-btn">
            🎤 {{ 'voice_command' | translate }}
        </button>
    </div>
    
    <!-- Voice Commands Script -->
    <script src="/static/js/voice-commands.js"></script>
</body>
</html>
"""


if __name__ == '__main__':
    print("=" * 60)
    print("UI/UX ENHANCEMENT INTEGRATION GUIDE")
    print("=" * 60)
    print("\nFarmer-Friendly Features:")
    print("  ✅ Large 48x48px touch buttons")
    print("  ✅ Icon-based navigation (low literacy)")
    print("  ✅ 3-step wizards for complex tasks")
    print("  ✅ Voice command support")
    print("  ✅ High contrast for outdoor visibility")
    print("  ✅ Offline-first design")
    
    print("\nAccessibility Features:")
    accessibility = ui_system.get_accessibility_features()
    for category, features in accessibility.items():
        print(f"\n{category.upper()}:")
        for feature, enabled in features.items():
            status = "✅" if enabled else "❌"
            print(f"  {status} {feature.replace('_', ' ').title()}")
    
    print("\n" + INTEGRATION_INSTRUCTIONS)
