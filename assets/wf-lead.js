/* WayneFlow lead capture: free case-study pack in exchange for an email.
   The email is saved to the visitor's record in PostHog (identify), so every page they
   read before and after is linked to it. No third-party form service. */
(function () {
  'use strict';
  var W = window, D = document, L = location;
  var PDF = '/assets/wayneflow-case-studies.pdf';
  var page = L.pathname.replace(/index\.html$/, '') || '/';
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function ph() { return W.posthog && W.posthog.capture ? W.posthog : null; }
  function cap(ev, p) { var x = ph(); if (x) x.capture(ev, p || {}); }
  if (/\/book\.html$|\/privacy\.html$|\/terms\.html$|\/404\.html$/.test(page)) return;

  function formHTML(id, compact) {
    return '<form class="wl-form" novalidate data-wl="' + id + '">' +
      '<label class="wl-sr" for="wl-email-' + id + '">Work email</label>' +
      '<input class="wl-input" id="wl-email-' + id + '" name="email" type="email" autocomplete="email" placeholder="Your work email" required>' +
      (compact ? '' : '<label class="wl-sr" for="wl-site-' + id + '">Company website</label><input class="wl-input" id="wl-site-' + id + '" name="website" type="text" autocomplete="url" placeholder="Company website (optional)">') +
      '<button class="btn btn-primary wl-btn" type="submit">Send me the free playbook</button>' +
      '<p class="wl-fine">Instant download. No spam. We may follow up by email; unsubscribe anytime. <a href="/privacy.html">Privacy</a></p>' +
      '<p class="wl-msg" role="status" aria-live="polite"></p></form>';
  }
  var BOX = function (id) {
    return '<div class="wl-box" id="wl-box-' + id + '"><div class="wl-copy"><span class="kicker">Free playbook · $300 value</span>' +
      '<h3>Get the playbook behind $510K+ in client pipeline.</h3>' +
      '<p>6 real campaigns, 588,000 emails and the dashboards behind them, plus the 5 rules that turn cold email into booked sales appointments. Free, instant download.</p>' +
      '<ul class="wl-pts"><li>The exact funnels that booked 25 calls in 5 days</li><li>How 6 annual contracts came from a cold inbox</li><li>5 rules to stay out of spam, starting today</li></ul></div>' +
      formHTML(id) + '</div>';
  };

  function done(form, email) {
    ls('wf_lead', '1');
    var msg = form.querySelector('.wl-msg');
    form.querySelectorAll('input,button').forEach(function (el) { el.disabled = true; });
    msg.innerHTML = 'Thanks! Your download is starting. <a href="' + PDF + '" download>Download again</a>';
    var a = D.createElement('a'); a.href = PDF; a.download = 'WayneFlow-case-studies.pdf'; D.body.appendChild(a); a.click(); a.remove();
  }

  D.addEventListener('submit', function (e) {
    var form = e.target.closest && e.target.closest('.wl-form'); if (!form) return;
    e.preventDefault();
    var email = (form.email.value || '').trim().toLowerCase();
    var site = form.website ? (form.website.value || '').trim().slice(0, 200) : '';
    var msg = form.querySelector('.wl-msg');
    if (!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(email)) { msg.textContent = 'Please enter a valid email.'; form.email.focus(); return; }
    var x = ph();
    var props = { email: email, lead_magnet: 'case-study-pack', lead_page: page, lead_form: form.getAttribute('data-wl') };
    if (site) props.company_website = site;
    if (x) {
      try { x.identify(email, { email: email, company_website: site || undefined, lead_magnet: 'case-study-pack' }, { first_lead_page: page }); } catch (err) {}
      x.capture('lead_captured', props);
    }
    done(form, email);
    var pop = D.getElementById('wl-pop'); if (pop && form.closest('#wl-pop')) setTimeout(function () { /* keep success visible */ }, 0);
  });

  /* inline box: results page, blog posts, service pages */
  function place() {
    var anchor = null;
    if (/\/results\.html$/.test(page)) { var bands = D.querySelectorAll('.band'); anchor = bands.length ? (bands[bands.length - 1].closest('section, .wrap') || bands[bands.length - 1]) : null; }
    else if (/\/blog\/.+\.html$|lead-generation-services\.html$|canada\.html$/.test(page)) { var pb = D.querySelector('.post-body .soft-cta') || D.querySelector('.post-body'); if (pb) { var w = D.createElement('div'); w.innerHTML = BOX('inline'); pb.parentNode.insertBefore(w.firstChild, pb.nextSibling); return; } }
    if (anchor) { var s = D.createElement('section'); s.className = 'sec wl-sec'; s.innerHTML = '<div class="wrap">' + BOX('inline') + '</div>'; anchor.parentNode.insertBefore(s, anchor); }
  }
  place();

  /* popup: once every 14 days, never after a lead or a booking click this visit */
  function canPop() {
    if (ls('wf_lead') === '1') return false;
    var last = parseInt(ls('wf_pop_at') || '0', 10); if (Date.now() - last < 14 * 864e5) return false;
    try { if (sessionStorage.getItem('wf_booked')) return false; } catch (e) {}
    return true;
  }
  var shown = false;
  function pop(trigger) {
    if (shown || !canPop()) return; shown = true; ls('wf_pop_at', String(Date.now()));
    var d = D.createElement('div'); d.id = 'wl-pop'; d.className = 'wl-pop'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-labelledby', 'wl-pop-h');
    d.innerHTML = '<div class="wl-card"><button class="wl-x" type="button" aria-label="Close">×</button>' +
      '<span class="wl-badge">FREE · $300 VALUE</span><h3 id="wl-pop-h">Wait. Take the playbook behind $510K+ in pipeline.</h3>' +
      '<p>The 6 campaigns, 588,000 emails and 5 rules that turned cold email into booked sales appointments for our clients. Yours free, instant download.</p>' +
      '<p class="wl-fomo">Your competitors are already in your buyers\u2019 inboxes. Get the playbook before they book the meeting.</p>' + formHTML('popup', true) + '</div>';
    D.body.appendChild(d);
    requestAnimationFrame(function () { d.classList.add('in'); });
    var input = d.querySelector('input'); setTimeout(function () { try { input.focus({ preventScroll: true }); } catch (e) {} }, 250);
    function close() { d.classList.remove('in'); setTimeout(function () { d.remove(); }, 250); D.removeEventListener('keydown', esc); }
    function esc(e) { if (e.key === 'Escape') { cap('lead_popup_closed', { page: page, how: 'escape' }); close(); } }
    d.addEventListener('click', function (e) { if (e.target === d || e.target.closest('.wl-x')) { cap('lead_popup_closed', { page: page, how: 'close' }); close(); } });
    D.addEventListener('keydown', esc);
    cap('lead_popup_shown', { page: page, trigger: trigger });
  }
  // remember a booking click so we never interrupt a buyer
  D.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a[href*="calendly.com"]'); if (a) { try { sessionStorage.setItem('wf_booked', '1'); } catch (er) {} } }, true);
  var t0 = Date.now();
  // desktop: mouse leaves through the top of the window
  D.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY <= 0 && Date.now() - t0 > 8000 && W.innerWidth > 960) pop('exit'); });
  // phones and tablets: read most of the page and stayed a while
  W.addEventListener('scroll', function () {
    if (W.innerWidth > 960 || Date.now() - t0 < 25000) return;
    var h = D.documentElement.scrollHeight - W.innerHeight; if (h > 0 && W.scrollY / h > 0.6) pop('scroll');
  }, { passive: true });
})();
