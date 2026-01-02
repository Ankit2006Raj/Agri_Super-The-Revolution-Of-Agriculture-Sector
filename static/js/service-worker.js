/**
 * Service Worker for AgriSuper-App
 * Enables offline functionality for farmers in rural areas with poor connectivity
 */

const CACHE_NAME = 'agrisuper-v1.0.0';
const OFFLINE_URL = '/offline.html';

// Critical assets to cache for offline use
const CRITICAL_ASSETS = [
  '/',
  '/offline.html',
  '/static/css/main.css',
  '/static/css/bootstrap.min.css',
  '/static/js/app.js',
  '/static/js/jquery.min.js',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
  '/templates/dashboard.html'
];

// API endpoints to cache responses
const API_CACHE_ENDPOINTS = [
  '/api/pricing/live',
  '/api/weather/farm',
  '/api/forum/questions',
  '/api/elearning/courses'
];

// Install event - cache critical assets
self.addEventListener('install', (event) => {
  console.log('[ServiceWorker] Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[ServiceWorker] Caching critical assets');
        return cache.addAll(CRITICAL_ASSETS);
      })
      .then(() => {
        console.log('[ServiceWorker] Skip waiting');
        return self.skipWaiting();
      })
      .catch((error) => {
        console.error('[ServiceWorker] Installation failed:', error);
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activating...');
  
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== CACHE_NAME) {
              console.log('[ServiceWorker] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('[ServiceWorker] Claiming clients');
        return self.clients.claim();
      })
  );
});

// Fetch event - serve from cache with network fallback
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }

  // Handle API requests with network-first strategy
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(networkFirstStrategy(request));
    return;
  }

  // Handle static assets with cache-first strategy
  if (url.pathname.startsWith('/static/')) {
    event.respondWith(cacheFirstStrategy(request));
    return;
  }

  // Handle HTML pages with network-first strategy
  if (request.headers.get('accept').includes('text/html')) {
    event.respondWith(networkFirstStrategy(request));
    return;
  }

  // Default: cache-first for everything else
  event.respondWith(cacheFirstStrategy(request));
});

/**
 * Network-first strategy
 * Try network first, fall back to cache if offline
 */
async function networkFirstStrategy(request) {
  try {
    // Try to fetch from network
    const networkResponse = await fetch(request);
    
    // If successful, cache the response for offline use
    if (networkResponse && networkResponse.status === 200) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    console.log('[ServiceWorker] Network request failed, trying cache:', request.url);
    
    // Network failed, try cache
    const cachedResponse = await caches.match(request);
    
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // If HTML request and no cache, return offline page
    if (request.headers.get('accept').includes('text/html')) {
      const offlineResponse = await caches.match(OFFLINE_URL);
      if (offlineResponse) {
        return offlineResponse;
      }
    }
    
    // Return error response
    return new Response(
      JSON.stringify({
        error: 'Offline',
        message: 'आप ऑफ़लाइन हैं। कृपया इंटरनेट कनेक्शन जांचें। You are offline. Please check your internet connection.',
        cached: false
      }),
      {
        status: 503,
        statusText: 'Service Unavailable',
        headers: new Headers({
          'Content-Type': 'application/json'
        })
      }
    );
  }
}

/**
 * Cache-first strategy
 * Use cached version if available, otherwise fetch from network
 */
async function cacheFirstStrategy(request) {
  // Try cache first
  const cachedResponse = await caches.match(request);
  
  if (cachedResponse) {
    console.log('[ServiceWorker] Serving from cache:', request.url);
    return cachedResponse;
  }
  
  // Not in cache, fetch from network
  try {
    const networkResponse = await fetch(request);
    
    // Cache the new response
    if (networkResponse && networkResponse.status === 200) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    console.error('[ServiceWorker] Cache and network both failed:', error);
    
    return new Response('Offline - No cached version available', {
      status: 503,
      statusText: 'Service Unavailable'
    });
  }
}

// Background sync for offline actions
self.addEventListener('sync', (event) => {
  console.log('[ServiceWorker] Background sync:', event.tag);
  
  if (event.tag === 'sync-offline-data') {
    event.waitUntil(syncOfflineData());
  }
});

/**
 * Sync offline data when connection is restored
 */
async function syncOfflineData() {
  try {
    // Get pending offline actions from IndexedDB or localStorage
    const pendingActions = await getPendingActions();
    
    // Process each pending action
    for (const action of pendingActions) {
      try {
        const response = await fetch(action.url, {
          method: action.method,
          headers: action.headers,
          body: action.body
        });
        
        if (response.ok) {
          // Remove from pending queue
          await removePendingAction(action.id);
          console.log('[ServiceWorker] Synced offline action:', action.id);
        }
      } catch (error) {
        console.error('[ServiceWorker] Failed to sync action:', action.id, error);
      }
    }
  } catch (error) {
    console.error('[ServiceWorker] Sync failed:', error);
    throw error;
  }
}

/**
 * Push notification handler
 */
self.addEventListener('push', (event) => {
  console.log('[ServiceWorker] Push notification received');
  
  const options = {
    body: event.data ? event.data.text() : 'New update available!',
    icon: '/static/icons/icon-192.png',
    badge: '/static/icons/badge-72.png',
    vibrate: [200, 100, 200],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'View Details',
        icon: '/static/icons/checkmark.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/static/icons/xmark.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('AgriSuper Alert', options)
  );
});

/**
 * Notification click handler
 */
self.addEventListener('notificationclick', (event) => {
  console.log('[ServiceWorker] Notification clicked:', event.action);
  
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});

/**
 * Message handler for communication with main app
 */
self.addEventListener('message', (event) => {
  console.log('[ServiceWorker] Message received:', event.data);
  
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CACHE_URLS') {
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then((cache) => cache.addAll(event.data.urls))
    );
  }
});

// Helper functions for IndexedDB operations
async function getPendingActions() {
  // Placeholder - implement IndexedDB logic
  return [];
}

async function removePendingAction(actionId) {
  // Placeholder - implement IndexedDB logic
  return true;
}

console.log('[ServiceWorker] Loaded successfully');
