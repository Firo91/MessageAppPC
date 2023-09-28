// sw.js

// Files to cache
const cacheName = 'myCache-v1';
const appShellFiles = [
  'display/',
  '/static/css/main.css',
  '/static/js/main.js',
  // Add other files you want to cache
];

// Install
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(appShellFiles);
    })
  );
});

// Fetch
self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((r) => {
      return (
        r ||
        fetch(e.request).then((response) => {
          return caches.open(cacheName).then((cache) => {
            cache.put(e.request, response.clone());
            return response;
          });
        })
      );
    })
  );
});