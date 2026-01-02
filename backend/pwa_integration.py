"""
PWA Integration Module for app.py
This module integrates Progressive Web App features into the main Flask application
"""

from flask import send_from_directory, jsonify
import os


def register_pwa_routes(app):
    """
    Register PWA-related routes in the Flask application
    
    Routes:
    - /manifest.json: PWA manifest file
    - /service-worker.js: Service worker for offline functionality
    - /offline: Offline fallback page
    - /api/pwa/install: Track PWA installations
    """
    
    @app.route('/manifest.json')
    def serve_manifest():
        """Serve PWA manifest file"""
        return send_from_directory('static', 'manifest.json', mimetype='application/json')
    
    @app.route('/service-worker.js')
    def serve_service_worker():
        """Serve service worker JavaScript file"""
        return send_from_directory('static/js', 'service-worker.js', mimetype='application/javascript')
    
    @app.route('/offline')
    def offline_page():
        """Serve offline fallback page"""
        from flask import render_template
        return render_template('offline.html')
    
    @app.route('/api/pwa/install', methods=['POST'])
    def track_pwa_install():
        """Track PWA installation events"""
        from flask import request
        data = request.get_json()
        
        # Log installation (in production, save to database)
        app.logger.info(f"PWA installed by user: {data.get('user_id', 'anonymous')}")
        
        return jsonify({
            'status': 'success',
            'message': 'Installation tracked'
        })
    
    @app.route('/api/pwa/notification-permission', methods=['POST'])
    def request_notification_permission():
        """Handle push notification permission requests"""
        from flask import request
        data = request.get_json()
        
        # In production, save notification subscription
        app.logger.info(f"Notification permission: {data.get('permission')}")
        
        return jsonify({
            'status': 'success',
            'permission': data.get('permission')
        })


def add_pwa_meta_tags():
    """
    Return PWA meta tags to be added to base template
    Add these to templates/base.html or your main layout template
    """
    return '''
    <!-- PWA Meta Tags -->
    <meta name="application-name" content="AgriSuper">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="AgriSuper">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#4CAF50">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json">
    
    <!-- Apple Touch Icons -->
    <link rel="apple-touch-icon" href="/static/icons/icon-192.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/static/icons/icon-152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/icons/icon-192.png">
    <link rel="apple-touch-icon" sizes="167x167" href="/static/icons/icon-192.png">
    
    <!-- Service Worker Registration -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/service-worker.js')
                    .then(function(registration) {
                        console.log('ServiceWorker registration successful');
                    })
                    .catch(function(err) {
                        console.log('ServiceWorker registration failed: ', err);
                    });
            });
        }
    </script>
    
    <!-- PWA Install Prompt -->
    <script>
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            // Show install button
            const installBtn = document.getElementById('pwa-install-btn');
            if (installBtn) {
                installBtn.style.display = 'block';
                installBtn.addEventListener('click', () => {
                    deferredPrompt.prompt();
                    deferredPrompt.userChoice.then((choiceResult) => {
                        if (choiceResult.outcome === 'accepted') {
                            console.log('User accepted the install prompt');
                            fetch('/api/pwa/install', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({user_id: 'current_user'})
                            });
                        }
                        deferredPrompt = null;
                    });
                });
            }
        });
    </script>
    '''


def check_pwa_compatibility():
    """
    Check if the application has all required PWA components
    Returns dict with status and missing components
    """
    required_files = {
        'manifest': 'static/manifest.json',
        'service_worker': 'static/js/service-worker.js',
        'offline_page': 'templates/offline.html',
        'icons': [
            'static/icons/icon-192.png',
            'static/icons/icon-512.png'
        ]
    }
    
    missing = []
    
    # Check manifest
    if not os.path.exists(required_files['manifest']):
        missing.append('manifest.json')
    
    # Check service worker
    if not os.path.exists(required_files['service_worker']):
        missing.append('service-worker.js')
    
    # Check offline page
    if not os.path.exists(required_files['offline_page']):
        missing.append('offline.html')
    
    # Check icons
    for icon in required_files['icons']:
        if not os.path.exists(icon):
            missing.append(icon)
    
    return {
        'is_ready': len(missing) == 0,
        'missing_components': missing,
        'message': 'PWA ready!' if len(missing) == 0 else f'Missing: {", ".join(missing)}'
    }


# Usage instructions for app.py integration
INTEGRATION_INSTRUCTIONS = """
To integrate PWA features into app.py:

1. Import the module:
   from backend.pwa_integration import register_pwa_routes, check_pwa_compatibility

2. Register routes after app initialization:
   register_pwa_routes(app)

3. Check PWA compatibility (optional):
   pwa_status = check_pwa_compatibility()
   app.logger.info(f"PWA Status: {pwa_status['message']}")

4. Add meta tags to base template (templates/base.html):
   - Copy the HTML from add_pwa_meta_tags() function
   - Paste in the <head> section of your base template

5. Create placeholder icons (if missing):
   - Create directory: static/icons/
   - Add icons: icon-192.png, icon-512.png (use any farmer-related image)

6. Test PWA:
   - Run app: python app.py
   - Open Chrome DevTools > Application > Manifest
   - Check "Add to Home Screen" works
   - Test offline mode (DevTools > Network > Offline)
"""

if __name__ == '__main__':
    # Test PWA compatibility
    status = check_pwa_compatibility()
    print("=" * 60)
    print("PWA COMPATIBILITY CHECK")
    print("=" * 60)
    print(f"Status: {'✅ READY' if status['is_ready'] else '❌ NOT READY'}")
    print(f"Message: {status['message']}")
    if status['missing_components']:
        print("\nMissing Components:")
        for component in status['missing_components']:
            print(f"  - {component}")
    print("\n" + INTEGRATION_INSTRUCTIONS)
