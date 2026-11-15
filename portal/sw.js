/* WayneFlow phone alerts. Shows a notification when the server sends one, and opens the app when it is tapped. */
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener('push', function (e) {
  var d = {}; try { d = e.data.json(); } catch (x) { d = { title: 'WayneFlow', body: e.data ? e.data.text() : '' }; }
  e.waitUntil(self.registration.showNotification(d.title || 'WayneFlow', {
    body: d.body || '', icon: '/portal/icon-192.png', badge: '/portal/icon-192.png', tag: d.tag || 'wayneflow', data: { url: d.url || '/portal/' } }));
});
self.addEventListener('notificationclick', function (e) {
  e.notification.close();
  var url = (e.notification.data && e.notification.data.url) || '/portal/', go = (url.split('#')[1] || '');
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (cs) {
    for (var i = 0; i < cs.length; i++) { if (cs[i].url.indexOf('/portal/') >= 0) { cs[i].postMessage({ go: go }); return cs[i].focus(); } }
    return self.clients.openWindow(url);
  }));
});
