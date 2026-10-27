/* WayneFlow lead capture: free cold email playbook in exchange for an email.
   The email is saved to the visitor's record in PostHog (identify), so every page they
   read before and after is linked to it. No third-party form service. */
(function () {
  'use strict';
  var W = window, D = document, L = location;
  var PDF = '/assets/wayneflow-cold-email-playbook.pdf';
  var page = L.pathname.replace(/index\.html$/, '') || '/';
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function ph() { return W.posthog && W.posthog.capture ? W.posthog : null; }
  function cap(ev, p) { var x = ph(); if (x) x.capture(ev, p || {}); }
  if (/\/book\.html$|\/privacy\.html$|\/terms\.html$|\/404\.html$/.test(page)) return;

  function formHTML(id) {
    return '<form class="wl-form" novalidate data-wl="' + id + '">' +
      '<label class="wl-sr" for="wl-email-' + id + '">Work email</label>' +
      '<div class="wl-row"><input class="wl-input" id="wl-email-' + id + '" name="email" type="email" autocomplete="email" inputmode="email" placeholder="Your work email" required>' +
      '<button class="btn btn-primary wl-btn" type="submit">' + (id === 'news' ? 'Subscribe' : 'Send me the playbook') + '</button></div>' +
      '<p class="wl-fine">' + (id === 'news' ? 'Free · No spam · Unsubscribe anytime' : 'Instant download · No spam · Unsubscribe anytime') + ' · <a href="/privacy.html">Privacy</a></p>' +
      '<p class="wl-msg" role="status" aria-live="polite"></p></form>';
  }
  var COVER = '<div class="wl-cover"><img src="/assets/img/playbook-cover.webp" alt="The WayneFlow Cold Email Playbook cover" width="210" height="272" loading="lazy"></div>';
  var CHIPS = '<ul class="wl-chips"><li>Exact DNS setup</li><li>3-week warmup</li><li>7 real case studies</li></ul>';
  var BOX = function (id) {
    return '<div class="wl-box" id="wl-box-' + id + '">' + COVER + '<div class="wl-copy"><span class="wl-badge">FREE · $300 VALUE</span>' +
      '<h3>Steal our cold email system. Free.</h3>' +
      '<p>35 pages, step by step: the exact setup we run for clients, from a blank domain to booked sales calls, with 7 real client dashboards.</p>' + CHIPS +
      formHTML(id) + '<p class="wl-more"><a href="/free-cold-email-playbook.html">See what is inside &rarr;</a></p></div></div>';
  };

  function done(form, email) {
    ls('wf_lead', '1');
    if (form.getAttribute('data-wl') === 'news') {
      ls('wf_sub', '1');
      form.querySelectorAll('input,button').forEach(function (el) { el.disabled = true; });
      form.querySelector('.wl-msg').innerHTML = 'You\u2019re in! Welcome gift: <a href="' + PDF + '" download>download the free playbook</a>.';
      return;
    }
    var msg = form.querySelector('.wl-msg');
    form.querySelectorAll('input,button').forEach(function (el) { el.disabled = true; });
    msg.innerHTML = 'Thanks! Your download is starting. <a href="' + PDF + '" download>Download again</a>';
    var a = D.createElement('a'); a.href = PDF; a.download = 'WayneFlow-Cold-Email-Playbook.pdf'; D.body.appendChild(a); a.click(); a.remove();
  }

  D.addEventListener('submit', function (e) {
    var form = e.target.closest && e.target.closest('.wl-form'); if (!form) return;
    e.preventDefault();
    var email = (form.email.value || '').trim().toLowerCase();
    var site = '';
    var phone = '';
    var msg = form.querySelector('.wl-msg');
    if (!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(email)) { msg.textContent = 'Please enter a valid email.'; form.email.focus(); return; }
    var x = ph();
    // everything we know about this visit goes with the lead, in one click
    var tz = ''; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (err) {}
    var sess = {}, first = {}, org = {}; try { sess = JSON.parse(sessionStorage.getItem('wf_sess') || '{}'); first = JSON.parse(ls('wf_first') || '{}'); org = JSON.parse(ls('wf_org') || '{}'); } catch (err) {}
    var hs = D.documentElement.scrollHeight - W.innerHeight;
    var ctx = {
      lead_page: page, lead_form: form.getAttribute('data-wl'), lead_magnet: form.getAttribute('data-wl') === 'news' ? 'newsletter' : 'cold-email-playbook', newsletter: form.getAttribute('data-wl') === 'news',
      timezone: tz, local_time: new Date().toString().slice(0, 24), language: navigator.language || '',
      device: W.innerWidth < 641 ? 'mobile' : W.innerWidth < 1025 ? 'tablet' : 'desktop', screen: screen.width + 'x' + screen.height,
      browser_info: navigator.userAgent.slice(0, 200),
      source_this_visit: sess.source || '', channel_this_visit: sess.channel || '', landing_page: sess.landing || '',
      pages_this_visit: sess.pages || 1, visit_number: sess.n || 1, seconds_this_visit: sess.start ? Math.round((Date.now() - sess.start) / 1000) : null,
      first_source: first.source || '', first_seen: first.ts || '', network: org.org || '', network_kind: org.kind || '',
      scroll_depth: hs > 0 ? Math.round(W.scrollY / hs * 100) : 100,
      referrer: (D.referrer || '').slice(0, 200), page_title: (D.title || '').slice(0, 120), utm_campaign: sess.utm_campaign || '', utm_source: sess.utm_source || '', email_domain: email.split('@')[1] || '', work_email: !/@(gmail|yahoo|hotmail|outlook|icloud|aol|proton|live|msn)\./i.test(email)
    };
    var person = { email: email, lead_magnet: ctx.lead_magnet, timezone: tz, language: ctx.language, lead_page: page, lead_at: new Date().toISOString() };
    if (site) { person.company_website = site; ctx.company_website = site; }
    if (phone) { person.phone = phone; ctx.phone = phone; ctx.sms_call_consent = true; }
    if (org.org) person.network = org.org;
    var props = Object.assign({ email: email }, ctx);
    if (x) {
      try { x.identify(email, person, { first_lead_page: page, first_source: first.source || '' }); } catch (err) {}
      x.capture('lead_captured', props);
      if (ctx.newsletter) { x.capture('newsletter_subscribed', props); try { x.people && x.people.set && x.people.set({ newsletter: true }); } catch (err) {} }
    }
    done(form, email);
    var pop = D.getElementById('wl-pop'); if (pop && form.closest('#wl-pop')) setTimeout(function () { /* keep success visible */ }, 0);
  });

  /* inline box: results page, blog posts, service pages */
  function place() {
    if (ls('wf_lead') === '1') return; // already has the playbook: no box, no popup
    var anchor = null;
    if (/\/results\.html$/.test(page)) { var bands = D.querySelectorAll('.band'); anchor = bands.length ? (bands[bands.length - 1].closest('section, .wrap') || bands[bands.length - 1]) : null; }
    else if (/\/blog\/.+\.html$|lead-generation-services\.html$|canada\.html$/.test(page)) { var pb = D.querySelector('.post-body .soft-cta') || D.querySelector('.post-body'); if (pb) { var w = D.createElement('div'); w.innerHTML = BOX('inline'); pb.parentNode.insertBefore(w.firstChild, pb.nextSibling); return; } }
    if (anchor) { var s = D.createElement('section'); s.className = 'sec wl-sec'; s.innerHTML = '<div class="wrap">' + BOX('inline') + '</div>'; anchor.parentNode.insertBefore(s, anchor); }
  }
  place();

  /* playbook landing page: forms go into #wl-slot / #wl-slot2 */
  var IS_PB = /free-cold-email-playbook\.html$/.test(page);
  ['wl-slot', 'wl-slot2'].forEach(function (sid, i) {
    var el = D.getElementById(sid); if (!el) return;
    if (ls('wf_lead') === '1') { el.innerHTML = '<p class="wl-msg" style="display:block">You already have the playbook. <a href="' + PDF + '" download>Download it again</a>.</p>'; return; }
    el.innerHTML = formHTML('page' + (i ? '2' : ''));
  });

  /* newsletter: end of every page, always there for people who skipped the popup */
  function news() {
    if (ls('wf_sub') === '1' || /free-cold-email-playbook\.html$/.test(page)) return;
    var f = D.querySelector('footer'); if (!f) return;
    var s = D.createElement('section'); s.className = 'wl-news'; s.id = 'newsletter';
    s.innerHTML = '<div class="wrap"><div class="wl-nbox"><div class="wl-ncopy"><span class="wl-nk">The WayneFlow Newsletter</span>' +
      '<h3>Cold email tactics that book meetings, in your inbox.</h3>' +
      '<p>Real lessons from our live client campaigns. Short, practical, no fluff. Subscribe free and get the $300 playbook as a welcome gift.</p></div>' +
      formHTML('news') + '</div></div>';
    f.parentNode.insertBefore(s, f);
  }
  news();

  /* popup: at most 2 times per person (2nd only on a later visit), never after an email or a booking click */
  function canPop() {
    if (IS_PB) return false; // the landing page already shows the form
    if (ls('wf_lead') === '1' || ls('wf_sub') === '1') return false;
    if (parseInt(ls('wf_pop_n') || '0', 10) >= 2) return false;           // ignored twice: stop
    try { if (sessionStorage.getItem('wf_popped')) return false; } catch (e) {} // once per visit
    try { if (sessionStorage.getItem('wf_booked')) return false; } catch (e) {}
    return true;
  }
  var shown = false;
  function pop(trigger) {
    if (shown || !canPop()) return; shown = true; ls('wf_pop_n', String(parseInt(ls('wf_pop_n') || '0', 10) + 1)); try { sessionStorage.setItem('wf_popped', '1'); } catch (e) {}
    var d = D.createElement('div'); d.id = 'wl-pop'; d.className = 'wl-pop'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-labelledby', 'wl-pop-h');
    d.innerHTML = '<div class="wl-card"><button class="wl-x" type="button" aria-label="Close">×</button>' +
      '<div class="wl-hero"><span class="wl-badge">FREE · $300 VALUE</span>' + COVER + '<span class="wl-meta">35 pages · 7 case studies</span></div>' +
      '<div class="wl-body"><h3 id="wl-pop-h">Steal our cold email system. Free.</h3>' +
      '<p>The exact step-by-step setup behind $510K+ in client pipeline, proven with 7 real case studies.</p>' + CHIPS + formHTML('popup') + '</div></div>';
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
  // test switch: add ?wf_pop=1 to any page URL to see the popup right away (ignores all rules)
  if (/[?&]wf_pop=1/.test(L.search)) { setTimeout(function () { shown = false; try { localStorage.removeItem('wf_pop_n'); localStorage.removeItem('wf_lead'); localStorage.removeItem('wf_sub'); sessionStorage.removeItem('wf_popped'); } catch (e) {} pop('test'); }, 600); }
  // desktop: mouse leaves through the top of the window
  D.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY <= 0 && Date.now() - t0 > 8000 && W.innerWidth > 960) pop('exit'); });
  // phones and tablets: 10+ seconds on the page and 40% scrolled
  W.addEventListener('scroll', function () {
    if (W.innerWidth > 960 || Date.now() - t0 < 10000) return;
    var h = D.documentElement.scrollHeight - W.innerHeight; if (h > 0 && W.scrollY / h > 0.4) pop('scroll');
  }, { passive: true });
})();
