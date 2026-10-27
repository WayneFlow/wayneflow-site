/* WayneFlow first-party visitor tracking ("WF pixel").
   Works on top of PostHog. Detects traffic source (search, AI assistants, social,
   marketplaces, ads, email, direct), stores first touch, tracks behaviour and
   passes the source into Calendly bookings. */
(function () {
  'use strict';
  var W = window, D = document, L = location, ph = function () { return W.posthog && W.posthog.capture ? W.posthog : null; };
  function cap(ev, props) { var p = ph(); if (p) p.capture(ev, props || {}); }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  var T0 = Date.now(), qs = new URLSearchParams(L.search);

  /* ---------- 1. where did this visitor come from? ---------- */
  var RULES = [
    // AI assistants
    [/(^|\.)chatgpt\.com$|(^|\.)chat\.openai\.com$|(^|\.)openai\.com$/, 'chatgpt', 'ai'],
    [/(^|\.)claude\.ai$|(^|\.)anthropic\.com$/, 'claude', 'ai'],
    [/(^|\.)perplexity\.ai$/, 'perplexity', 'ai'],
    [/(^|\.)gemini\.google\.com$|(^|\.)bard\.google\.com$/, 'gemini', 'ai'],
    [/(^|\.)copilot\.microsoft\.com$|(^|\.)copilot\.cloud\.microsoft$/, 'copilot', 'ai'],
    [/(^|\.)meta\.ai$/, 'meta_ai', 'ai'],
    [/(^|\.)grok\.com$|(^|\.)x\.ai$/, 'grok', 'ai'],
    [/(^|\.)deepseek\.com$/, 'deepseek', 'ai'],
    [/(^|\.)poe\.com$|(^|\.)you\.com$|(^|\.)phind\.com$|(^|\.)mistral\.ai$/, 'other_ai', 'ai'],
    // search engines
    [/(^|\.)google\.[a-z.]+$/, 'google', 'organic_search'],
    [/(^|\.)bing\.com$/, 'bing', 'organic_search'],
    [/(^|\.)duckduckgo\.com$/, 'duckduckgo', 'organic_search'],
    [/(^|\.)search\.yahoo\.com$|(^|\.)yahoo\.com$/, 'yahoo', 'organic_search'],
    [/(^|\.)search\.brave\.com$/, 'brave', 'organic_search'],
    [/(^|\.)ecosia\.org$|(^|\.)yandex\.[a-z]+$|(^|\.)baidu\.com$|(^|\.)qwant\.com$|(^|\.)startpage\.com$/, 'other_search', 'organic_search'],
    // social
    [/(^|\.)facebook\.com$|(^|\.)fb\.com$|(^|\.)fb\.me$/, 'facebook', 'social'],
    [/(^|\.)instagram\.com$/, 'instagram', 'social'],
    [/(^|\.)tiktok\.com$/, 'tiktok', 'social'],
    [/(^|\.)youtube\.com$|(^|\.)youtu\.be$/, 'youtube', 'social'],
    [/(^|\.)linkedin\.com$|(^|\.)lnkd\.in$/, 'linkedin', 'social'],
    [/(^|\.)t\.co$|(^|\.)twitter\.com$|(^|\.)x\.com$/, 'x_twitter', 'social'],
    [/(^|\.)reddit\.com$/, 'reddit', 'social'],
    [/(^|\.)quora\.com$/, 'quora', 'social'],
    [/(^|\.)pinterest\.[a-z.]+$/, 'pinterest', 'social'],
    [/(^|\.)whatsapp\.com$|(^|\.)wa\.me$/, 'whatsapp', 'social'],
    [/(^|\.)threads\.net$/, 'threads', 'social'],
    // marketplaces & review sites
    [/(^|\.)fiverr\.com$/, 'fiverr', 'marketplace'],
    [/(^|\.)upwork\.com$/, 'upwork', 'marketplace'],
    [/(^|\.)clutch\.co$|(^|\.)g2\.com$|(^|\.)goodfirms\.co$|(^|\.)trustpilot\.com$/, 'review_site', 'marketplace'],
    // email clients
    [/(^|\.)mail\.google\.com$|(^|\.)outlook\.(live|office|office365)\.com$|(^|\.)mail\.yahoo\.com$/, 'email', 'email']
  ];
  var CLICK_IDS = [['gclid', 'google_ads'], ['gbraid', 'google_ads'], ['wbraid', 'google_ads'], ['msclkid', 'bing_ads'],
    ['fbclid', 'facebook'], ['ttclid', 'tiktok_ads'], ['li_fat_id', 'linkedin_ads'], ['twclid', 'x_ads']];

  function detect() {
    var ref = D.referrer || '', host = '';
    try { host = ref ? new URL(ref).hostname.replace(/^www\.|^m\.|^l\.|^lm\./, '') : ''; } catch (e) {}
    var utm = {}; ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(function (k) { var v = qs.get(k); if (v) utm[k] = v.slice(0, 100); });
    var r = { source: 'direct', channel: 'direct', referrer: ref.slice(0, 300), referrer_host: host };
    var self = host && (host === L.hostname.replace(/^www\./, '') || /wayne-?flow/.test(host));
    if (self) { r.source = 'internal'; r.channel = 'internal'; }
    else if (host) {
      r.source = host; r.channel = 'referral';
      for (var i = 0; i < RULES.length; i++) if (RULES[i][0].test(host)) { r.source = RULES[i][1]; r.channel = RULES[i][2]; break; }
    }
    // ChatGPT and some AI tools add ?utm_source=chatgpt.com even with no referrer
    if (utm.utm_source) {
      var u = utm.utm_source.toLowerCase(), m = (utm.utm_medium || '').toLowerCase();
      r.source = u.replace(/\.com$|\.ai$/, '').replace(/[^a-z0-9_]+/g, '_');
      if (/chatgpt|openai|perplexity|claude|gemini|copilot|meta\.?ai|grok|deepseek/.test(u)) r.channel = 'ai';
      else if (/cpc|ppc|paid|ads?$|display|retarget/.test(m)) r.channel = /facebook|instagram|meta|tiktok|linkedin|x|twitter|youtube/.test(u) ? 'paid_social' : 'paid_search';
      else if (/email|newsletter|outreach|cold/.test(m + u)) r.channel = 'email';
      else if (/fiverr|upwork|clutch|g2/.test(u)) r.channel = 'marketplace';
      else if (/facebook|instagram|tiktok|youtube|linkedin|twitter|x$|reddit|whatsapp/.test(u)) r.channel = 'social';
      else if (r.channel === 'direct' || r.channel === 'internal') r.channel = 'campaign';
    }
    for (var j = 0; j < CLICK_IDS.length; j++) if (qs.get(CLICK_IDS[j][0])) {
      r.click_id = CLICK_IDS[j][0];
      r.source = CLICK_IDS[j][1] === 'facebook' && /ads|cpc|paid/.test(utm.utm_medium || '') ? 'facebook_ads' : (CLICK_IDS[j][1] === 'facebook' ? r.source === 'direct' ? 'facebook' : r.source : CLICK_IDS[j][1]);
      if (/_ads$/.test(r.source)) r.channel = /google|bing/.test(r.source) ? 'paid_search' : 'paid_social';
      break;
    }
    for (var k in utm) r[k] = utm[k];
    return r;
  }

  var touch = detect();
  var page = L.pathname.replace(/index\.html$/, '') || '/';
  // a visit (session) keeps its entry source even when the visitor moves between pages
  var sess = null; try { sess = JSON.parse(ss('wf_sess') || 'null'); } catch (e) {}
  var newSession = !sess || touch.channel !== 'internal' && touch.source !== sess.source;
  if (newSession) {
    if (touch.channel === 'internal') touch = { source: 'direct', channel: 'direct', referrer: '', referrer_host: '' };
    var n = parseInt(ls('wf_visits') || '0', 10) + 1; ls('wf_visits', String(n));
    sess = { source: touch.source, channel: touch.channel, landing: page, start: T0, n: n, pages: 0 };
    for (var key in touch) if (/^utm_|click_id/.test(key)) sess[key] = touch[key];
  }
  sess.pages = (sess.pages || 0) + 1; ss('wf_sess', JSON.stringify(sess));

  var first = null; try { first = JSON.parse(ls('wf_first') || 'null'); } catch (e) {}
  if (!first) { first = { source: sess.source, channel: sess.channel, landing: sess.landing, ts: new Date(T0).toISOString() }; ls('wf_first', JSON.stringify(first)); }

  var supers = { wf_source: sess.source, wf_channel: sess.channel, wf_landing_page: sess.landing, wf_visit_number: sess.n,
    wf_returning: sess.n > 1, wf_first_source: first.source, wf_first_channel: first.channel,
    wf_days_since_first_visit: Math.floor((T0 - Date.parse(first.ts)) / 864e5) };
  if (sess.utm_campaign) supers.wf_campaign = sess.utm_campaign;
  var p0 = ph(); if (p0) { p0.register(supers); }
  if (newSession) {
    var tz = ''; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (e) {}
    var nc = navigator.connection || {};
    var now = new Date();
    var vp = { referrer: touch.referrer, referrer_host: touch.referrer_host, landing_page: page, visit_number: sess.n,
      device: W.innerWidth < 641 ? 'mobile' : W.innerWidth < 1025 ? 'tablet' : 'desktop',
      timezone: tz, language: navigator.language || '', languages: (navigator.languages || []).slice(0, 3).join(','),
      local_hour: now.getHours(), local_weekday: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][now.getDay()],
      screen: (screen.width || 0) + 'x' + (screen.height || 0), viewport: W.innerWidth + 'x' + W.innerHeight,
      touch: ('ontouchstart' in W) || navigator.maxTouchPoints > 0, dark_mode: !!(W.matchMedia && W.matchMedia('(prefers-color-scheme: dark)').matches),
      connection: nc.effectiveType || '', device_memory_gb: navigator.deviceMemory || null, cpu_cores: navigator.hardwareConcurrency || null,
      $set: { last_source: sess.source, last_channel: sess.channel, visits: sess.n, timezone: tz, language: navigator.language || '' },
      $set_once: { first_source: first.source, first_channel: first.channel, first_landing_page: first.landing, first_seen: first.ts } };
    for (var u2 in touch) if (/^utm_|click_id/.test(u2)) vp[u2] = touch[u2];
    cap('wf_visit', vp);
  }

  /* ---------- 1b. which company / network is this visitor on? (free IP lookup) ---------- */
  var ISP = /comcast|verizon|at&t|att |charter|spectrum|cox |centurylink|lumen|frontier|t-mobile|tmobile|sprint|optimum|altice|rogers|bell canada|telus|shaw|videotron|cogeco|vodafone|orange|telefonica|telekom|telecom|telstra|airtel|jio|ptcl|jazz|zong|ufone|nayatel|stormfiber|wateen|mobilink|broadband|cable|wireless|cellular|mobile|internet service|communications|telecommunication|starlink|o2 |ee limited|virgin media|bt |sky |etisalat|du |stc |claro|tim |movistar/i;
  var HOST = /amazon|aws|google llc|google cloud|microsoft|azure|digitalocean|ovh|hetzner|linode|akamai|cloudflare|oracle|alibaba|tencent|vultr|leaseweb|m247|datacamp|choopa|contabo|hostinger|godaddy|vpn|proxy|tor /i;
  function orgKind(o) { return !o ? '' : HOST.test(o) ? 'hosting_or_vpn' : ISP.test(o) ? 'home_or_mobile_isp' : 'company_network'; }
  function saveOrg(o, src) {
    o = String(o || '').replace(/^AS\d+\s+/, '').slice(0, 120); if (!o) return;
    var kind = orgKind(o); ls('wf_org', JSON.stringify({ org: o, kind: kind, at: Date.now() }));
    var p = ph(); if (p) { p.register({ wf_org: o, wf_org_kind: kind }); p.capture('wf_company', { network: o, network_kind: kind, lookup: src, $set: { network: o, network_kind: kind }, $set_once: { first_network: o } }); }
  }
  (function lookup() {
    var c = null; try { c = JSON.parse(ls('wf_org') || 'null'); } catch (e) {}
    if (c && Date.now() - c.at < 7 * 864e5) { var p0 = ph(); if (p0) p0.register({ wf_org: c.org, wf_org_kind: c.kind }); return; }
    if (!W.fetch) return;
    fetch('https://ipinfo.io/json', { headers: { Accept: 'application/json' } }).then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (j) { if (j && j.org) saveOrg(j.org, 'ipinfo'); else throw 0; })
      .catch(function () { fetch('https://ipapi.co/json/').then(function (r) { return r.json(); }).then(function (j) { if (j && j.org) saveOrg(j.org, 'ipapi'); }).catch(function () {}); });
  })();

  /* ---------- 2. behaviour ---------- */
  function secs() { return Math.round((Date.now() - T0) / 1000); }
  var maxScroll = 0, marks = [25, 50, 75, 90], sent = {};
  function scrollPct() { var h = D.documentElement.scrollHeight - W.innerHeight; return h > 0 ? Math.min(100, Math.round(W.scrollY / h * 100)) : 100; }
  W.addEventListener('scroll', function () {
    var s = scrollPct(); if (s > maxScroll) maxScroll = s;
    marks.forEach(function (m) { if (s >= m && !sent[m]) { sent[m] = 1; cap('wf_scroll', { depth: m, seconds_on_page: secs(), page: page }); } });
  }, { passive: true });

  // active (visible) time milestones
  var active = 0, last = Date.now(), timeMarks = [15, 30, 60, 120, 300], tSent = {};
  setInterval(function () {
    var now = Date.now(); if (!D.hidden) active += (now - last) / 1000; last = now;
    timeMarks.forEach(function (m) { if (active >= m && !tSent[m]) { tSent[m] = 1; cap('wf_engaged', { active_seconds: m, page: page, scroll_depth: maxScroll }); } });
  }, 1000);

  // which sections people actually see
  if ('IntersectionObserver' in W) {
    var seen = {}, io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { var id = e.target.id; if (e.isIntersecting && id && !seen[id]) { seen[id] = 1; cap('wf_section_view', { section: id, seconds_on_page: secs(), page: page }); } });
    }, { threshold: 0.35 });
    D.querySelectorAll('main section[id], main [id].story-block, main div[id="story"]').forEach(function (el) { io.observe(el); });
  }

  function sectionOf(el) { var s = el.closest('section[id], [id].story-block, footer, nav'); return s ? (s.id || s.tagName.toLowerCase()) : ''; }

  // clicks: booking CTA, outbound links, FAQ, screenshots, menu
  D.addEventListener('click', function (e) {
    var t = e.target; if (!t.closest) return;
    var a = t.closest('a[href]');
    if (a) {
      var href = a.getAttribute('href') || '', label = (a.textContent || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60);
      var base = { label: label, page: page, section: sectionOf(a), seconds_on_page: secs(), scroll_depth: maxScroll, active_seconds: Math.round(active) };
      if (/calendly\.com/.test(href)) {
        // pass the source into Calendly so every booking shows where the lead came from
        try {
          var cu = new URL(a.href);
          cu.searchParams.set('utm_source', 'website');
          cu.searchParams.set('utm_medium', sess.channel);
          cu.searchParams.set('utm_campaign', sess.source + (sess.utm_campaign ? ':' + sess.utm_campaign : ''));
          cu.searchParams.set('utm_content', (page + '#' + base.section).slice(0, 90));
          cu.searchParams.set('utm_term', 'visit' + sess.n + '_first-' + first.source);
          a.href = cu.toString();
        } catch (err) {}
        base.visit_number = sess.n; base.pages_this_visit = sess.pages;
        base.seconds_this_visit = Math.round((Date.now() - sess.start) / 1000);
        cap('book_call_click', base);
        var p = ph(); if (p) p.capture('$set', { $set: { clicked_book_call: true, last_cta_page: page }, $set_once: { first_cta_click: new Date().toISOString() } });
      } else if (/^mailto:/.test(href)) cap('email_click', base);
      else if (/^tel:|wa\.me/.test(href)) { base.dest = href.slice(0, 80); cap('wf_contact_click', base); }
      else if (/^https?:/.test(href) && a.hostname !== L.hostname) { base.dest_host = a.hostname.replace(/^www\./, ''); base.dest = a.href.slice(0, 200); cap('wf_outbound_click', base); }
      return;
    }
    var sum = t.closest('details > summary'); if (sum) { cap('wf_faq_open', { question: sum.textContent.trim().slice(0, 120), page: page }); return; }
    var fig = t.closest('figure.shot'); if (fig) { var im = fig.querySelector('img'); cap('wf_screenshot_zoom', { image: im ? (im.currentSrc || im.src).split('/').pop() : '', page: page, section: sectionOf(fig) }); return; }
    if (t.closest('.nav-toggle, button[aria-controls="menu"]')) cap('wf_menu_open', { page: page });
  }, true);

  // calculator use (How it works page)
  var calcSent = false;
  D.addEventListener('input', function (e) { if (!calcSent && e.target.type === 'range') { calcSent = true; cap('wf_calculator_use', { page: page }); } }, true);

  // copy text (people copying an email or a line)
  D.addEventListener('copy', function () { var s = (W.getSelection && String(W.getSelection())) || ''; if (s) cap('wf_copy', { text: s.slice(0, 120), page: page }); });

  // leaving: how long and how far
  var left = false;
  function bye() { if (left) return; left = true; cap('wf_page_exit', { page: page, seconds_on_page: secs(), active_seconds: Math.round(active), scroll_depth: maxScroll }); }
  W.addEventListener('pagehide', bye); D.addEventListener('visibilitychange', function () { if (D.visibilityState === 'hidden') bye(); });
})();
