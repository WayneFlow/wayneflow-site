import re
# Builds /blog/ from /home/claude/blog/*.html fragments. Called from build8.py after the main pages.
import json, re, os, glob, html as H
from datetime import date

ORDER = ['b2b-appointment-setting-guide', 'cold-email-deliverability', 'how-to-write-a-cold-email',
         'outsourced-appointment-setting-vs-in-house-sdr', 'is-cold-email-legal', 'is-cold-email-legal-in-canada', 'dns-records-for-cold-email']
SERVICES = [('svc-lead-generation-services', 'lead-generation-services.html', 'Lead generation services'), ('svc-canada', 'canada.html', 'Canada')]
PUBLISHED = '2026-10-27'
AUTHOR = 'Syed Asim Hussain & Syed Ali Hassan'

def load(order=None):
    posts = []
    for slug in (order or ORDER):
        f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog', f'{slug}.html')
        if not os.path.exists(f): continue
        raw = open(f).read()
        m = re.search(r'<script type="application/json" id="meta">(.*?)</script>', raw, re.S)
        if not m: continue
        meta = json.loads(m.group(1)); body = raw[m.end():].strip()
        meta['slug'] = slug; meta['body'] = body
        meta['words'] = len(re.sub('<[^>]+>', ' ', body).split())
        meta['toc'] = [(i, re.sub('<[^>]+>', '', t)) for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]
        posts.append(meta)
    return posts


CAL_URL = 'https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers'
CASES = {
 'agency': ('case-01', 'Agency client', '2,146 people said "Yes, tell me more."',
   'A marketing agency needed a steady flow of conversations with business owners. In four and a half months, the campaign turned cold lists into thousands of positive replies, without touching the agency\'s main domain.',
   [('82,671','emails sent'),('2,429','replies'),('2,146','interested'),('$175,000','pipeline')]),
 'construction': ('case-02', 'Construction software', 'From a cold inbox to 6 signed annual contracts.',
   'A construction software company wanted demos with contractors who had never heard of them. Cold email took them from zero awareness to sales-qualified demos and signed annual deals.',
   [('162,073','emails sent'),('4,449','replies'),('31','qualified demos'),('6','annual contracts')]),
 'blitz': ('case-03', 'The 5 day blitz', '96,408 emails. Five days. 25 calls on the calendar.',
   'A client needed meetings fast. With inboxes already warm and lists verified, we ran a five day push and filled the calendar inside a single week, with a bounce rate under half a percent.',
   [('96,408','emails in 5 days'),('1,095','replies'),('115','interested'),('25','calls booked')]),
 'quarter': ('case-04', 'A full quarter', '1,061 interested leads in one quarter.',
   'Over one quarter we ran a steady, high-volume program. Consistent daily sending, list hygiene and constant testing produced a reliable stream of interested buyers month after month.',
   [('236,545','emails sent'),('4,372','replies'),('3.69%','reply rate'),('1,061','interested')]),
 'pilot': ('case-05', 'Small pilot', '103 opportunities from 10,284 people.',
   'A small, tightly targeted pilot to prove the model before scaling. A sharp list and a simple offer turned about ten thousand contacts into more than a hundred real opportunities.',
   [('10,284','contacted'),('417','replied'),('4%','reply rate'),('103','opportunities')]),
 'linkedin': ('case-06', 'LinkedIn outreach', '154 replies from founders and investors.',
   'Not every buyer lives in the inbox. For one of the hardest audiences to reach, founders and angel investors, we ran LinkedIn outreach alongside email and opened 154 conversations.',
   [('1,375','invites'),('351','accepted'),('1,628','InMails'),('154','replies')]),
}
PLAN = {  # which two case studies each guide features, and its three CTA messages
 'b2b-appointment-setting-guide': (['blitz','agency'], [
   ('Want to see this funnel built for your market?', 'Book a free 20-minute call and get a mini plan: who we would target, the angle we would use, and how many calls you could expect in 30 days.', 'Get my free mini plan'),
   ('Rather skip the setup and just take the calls?', 'We build and run the whole system and guarantee 25 qualified appointments a month once your campaign is live.', 'See if you qualify')]),
 'cold-email-deliverability': (['quarter','blitz'], [
   ('Not sure if your emails are landing in spam?', 'On a free strategy call we will review your sending setup and tell you exactly what we would fix first. Keep the advice either way.', 'Get a free deliverability review'),
   ('Want inboxes, domains and warmup handled for you?', 'We set up separate sending domains, authentication and warmup, then run the campaigns. Your main domain is never at risk.', 'Talk to our team')]),
 'how-to-write-a-cold-email': (['pilot','agency'], [
   ('Want a second pair of eyes on your cold email?', 'Bring your current email to a free 20-minute call. We will show you the angle and offer we would test for your market.', 'Get my email reviewed'),
   ('Prefer to have the writing, testing and follow-ups done for you?', 'We write, send, test and handle replies, then book qualified buyers into your calendar.', 'Book a 20-minute call')]),
 'outsourced-appointment-setting-vs-in-house-sdr': (['construction','blitz'], [
   ('Want your real cost per meeting worked out?', 'On a free call we will run these numbers for your deal size and market, and show you what an outsourced program would look like.', 'Run my numbers'),
   ('Need meetings before an SDR would even finish ramping?', 'Campaigns usually go live in about three weeks, with replies in the first week after launch.', 'See how fast we can start')]),
 'is-cold-email-legal-in-canada': (['pilot','construction'], [
   ('Selling into Canada and want it done right?', 'We run CASL-aware campaigns: published business addresses relevant to the role, clear identification, a working unsubscribe and suppression lists. Ask us how on a free call.', 'Book a CASL-aware 20-minute call'),
   ('Rather not manage consent rules yourself?', 'We handle targeting, sending and opt-outs, and book qualified Canadian buyers into your calendar.', 'Talk to our team')]),
 'svc-lead-generation-services': (['agency','construction'], [
   ('Want to know how many meetings you could get?', 'Book a free 20-minute call. We will show you who we would target, the angle we would use, and how many calls to expect in 30 days.', 'Get my free mini plan'),
   ('Ready for 25 qualified appointments a month?', 'Once your campaign is live, we guarantee 25 qualified sales appointments a month. We explain exactly how it works on the call.', 'Book a 20-minute call')]),
 'svc-canada': (['quarter','blitz'], [
   ('Want a CASL-aware plan for your Canadian market?', 'On a free call we will map your buyers by province, the consent path we would use, and how many meetings to expect.', 'Get my Canada plan'),
   ('Rather have Canadian meetings booked for you?', 'We build and run the whole system and book qualified buyers into your calendar in your time zone.', 'Book a 20-minute call')]),
 'is-cold-email-legal': (['quarter','linkedin'], [
   ('Want outreach that is compliant from day one?', 'Every campaign we run includes accurate sender details, honest subject lines, a working opt-out and suppression lists. Ask us how it works on a free call.', 'Book a compliance-first call'),
   ('Rather not manage the rules yourself?', 'We handle the setup, sending and opt-outs, and book qualified appointments into your calendar.', 'Talk to our team')]),
}

def case_card(key):
    cid, label, h, p, st = CASES[key]
    stats = ''.join(f'<span><b>{a}</b> {b}</span>' for a, b in st)
    return (f'<div class="case-card"><span class="cc-badge" aria-hidden="true">Case<br>{cid[-2:]}</span><div>'
            f'<span class="cc-k">Real case study · {label}</span><h3 class="cc-h">{h}</h3><p>{p}</p><div class="cc-stats">{stats}</div>'
            f'<a class="cc-link" href="/results.html#{cid}">Read the full case study with live dashboards →</a></div></div>')

def inline_cta(t):
    h, p, btn = t
    return f'<div class="inline-cta"><div><b>{h}</b><p>{p}</p></div><a class="btn btn-primary" href="{CAL_URL}" target="_blank" rel="noopener">{btn}</a></div>'

def enrich(body, slug):
    if slug == 'is-cold-email-legal' and 'is-cold-email-legal-in-canada' not in body:
        body = body.replace('<h2 id="faq">', '<div class="inline-cta"><div><b>Emailing prospects in Canada?</b><p>Canada works differently: CASL requires consent before you send. Read our <a href="/blog/is-cold-email-legal-in-canada.html">CASL guide for B2B teams</a>.</p></div></div><h2 id="faq">', 1)
    if slug not in PLAN: return body
    cases, ctas = PLAN[slug]
    heads = [m.start() for m in re.finditer(r'<h2 id="(?!faq|next-step)[^"]+">', body)]
    n = len(heads)
    if n < 4: return body
    # insert positions (before these h2s): case 1 ~25%, CTA 1 ~40%, case 2 ~60%, CTA 2 ~78%
    picks = sorted({max(1, round(n*0.25)), max(2, round(n*0.42)), max(3, round(n*0.6)), min(n-1, max(4, round(n*0.8)))})
    blocks = [case_card(cases[0]), inline_cta(ctas[0]), case_card(cases[1]), inline_cta(ctas[1])]
    for idx, blk in sorted(zip(picks, blocks), reverse=True):
        pos = heads[idx]; body = body[:pos] + blk + body[pos:]
    return body

def fix_anchors(body, slug):
    # pages use <base href="/">, so same-page anchors must carry the path
    return re.sub(r'href="#', f'href="/blog/{slug}.html#', body)

def build_services(OUT, page, SITE, CAL, faq_ld):
    done = []
    items = {x[0]: x for x in SERVICES}
    for p in load([x[0] for x in SERVICES]):
        _, fname, crumb = items[p['slug']]
        toc = ''.join(f'<a href="/{fname}#{i}">{H.escape(t)}</a>' for i, t in p['toc'] if i != 'next-step')
        body_html = re.sub(r'href="#', f'href="/{fname}#', enrich(p['body'], p['slug']))
        body = f'''<section class="sec svc-hero">
  <div class="wrap">
    <div class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span>{crumb}</span></div>
    <div class="split top">
      <div><span class="kicker">{crumb} · {"CASL-aware" if fname=="canada.html" else "USA and Canada"}</span><h1>{H.escape(p["h1"])}</h1><p class="lead">{H.escape(p["excerpt"])}</p>
        <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a><a class="btn btn-secondary" href="/results.html">See live results</a></div></div>
      <div class="card svc-proof"><b class="sp-k">Real numbers from our dashboards</b>
        <div class="sp-grid"><div><b>588,000</b><span>emails sent</span></div><div><b>12,900+</b><span>replies</span></div><div><b>3,400+</b><span>interested buyers</span></div><div><b>100+</b><span>calls booked</span></div></div>
        <p class="sp-g">25 qualified sales appointments a month. <span class="hl">Guaranteed.</span></p></div>
    </div>
  </div>
</section>
<section class="sec post" style="padding-top:0">
  <div class="wrap"><div class="post-grid">
    <aside class="post-toc"><details><summary>On this page</summary>{toc}</details>
      <div class="toc-cta"><b>Want this done for you?</b><p>25 qualified appointments a month, guaranteed.</p><a class="btn btn-primary btn-sm" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div>
        <a class="toc-pb" href="/free-cold-email-playbook.html"><img src="/assets/img/playbook-cover.webp" alt="Free cold email playbook" width="60" height="78" loading="lazy"><span><b>Free cold email playbook</b>35 pages · 7 real case studies</span></a></aside>
    <article class="post-body">{body_html}</article>
  </div></div>
</section>'''
        url = f'{SITE}/{fname}'
        svc_ld = {"@context":"https://schema.org","@type":"Service","name":p['h1'],"serviceType":p['keyword'],"description":p['description'],"url":url,
                  "provider":{"@id":SITE+"/#org"},"areaServed":[{"@type":"Country","name":"United States"},{"@type":"Country","name":"Canada"}],
                  "offers":{"@type":"Offer","url":CAL,"description":"Free 20-minute strategy call"}}
        crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":crumb,"item":url}]}
        sch = [svc_ld, crumbs] + ([faq_ld([(x['q'], x['a']) for x in p['faq']])] if p.get('faq') else [])
        open(f'{OUT}/{fname}', 'w').write(page('svc', p['title'], p['description'], body, False, True, fname, sch, False, True))
        done.append(fname)
    return done

def build(OUT, page, SITE, CAL, crumb_ld, faq_ld):
    posts = load()
    os.makedirs(f'{OUT}/blog', exist_ok=True)
    for p in posts:
        toc = ''.join(f'<a href="/blog/{p["slug"]}.html#{i}">{H.escape(t)}</a>' for i, t in p['toc'] if i not in ('next-step',))
        related = [q for q in posts if q['slug'] != p['slug']][:3]
        rel = ''.join(f'<a class="card post-card" href="/blog/{q["slug"]}.html"><span class="tag">{q["readMinutes"]} min read</span><h3>{H.escape(q["h1"])}</h3><p>{H.escape(q["excerpt"])}</p><span class="go">Read the guide →</span></a>' for q in related)
        body = f'''<section class="sec post">
  <div class="wrap">
    <div class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/blog/">Blog</a><span>/</span><span>{H.escape(re.split(r"(?<=\?)\s|:\s", p["h1"])[0])}</span></div>
    <header class="post-head"><span class="kicker">Guide · {p["readMinutes"]} min read</span><h1>{H.escape(p["h1"])}</h1><p class="lead">{H.escape(p["excerpt"])}</p>
      <div class="byline"><span class="author-photos"><img src="/assets/team/asim-sq.webp" alt="Syed Asim Hussain" width="44" height="44"><img src="/assets/team/ali-sq.webp" alt="Syed Ali Hassan" width="44" height="44"></span><div><b>By <a href="/about.html" style="color:inherit">{AUTHOR}</a></b><span>Updated <time datetime="{PUBLISHED}">October 27, 2026</time> · Based on 588,000+ emails we have sent</span></div></div></header>
    <div class="post-grid">
      <aside class="post-toc"><details><summary>On this page</summary>{toc}</details>
        <div class="toc-cta"><b>Want this done for you?</b><p>25 qualified appointments a month, guaranteed.</p><a class="btn btn-primary btn-sm" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div>
        <a class="toc-pb" href="/free-cold-email-playbook.html"><img src="/assets/img/playbook-cover.webp" alt="Free cold email playbook" width="60" height="78" loading="lazy"><span><b>Free cold email playbook</b>35 pages · 7 real case studies</span></a></aside>
      <article class="post-body">{fix_anchors(enrich(p["body"], p["slug"]), p["slug"])}
        <div class="author-box"><span class="author-photos"><img src="/assets/team/asim-sq.webp" alt="Syed Asim Hussain" width="44" height="44"><img src="/assets/team/ali-sq.webp" alt="Syed Ali Hassan" width="44" height="44"></span><div><b>About the authors</b><p><a href="/about.html">Syed Asim Hussain and Syed Ali Hassan</a> run WayneFlow, a done-for-you B2B appointment setting agency for U.S. companies. Every number in this guide comes from campaigns we ran ourselves or from the sources linked. <a href="/results.html">See our live dashboards</a>.</p></div></div>
      </article>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="head"><span class="kicker">Keep reading</span><h2>More guides from <span class="hl">the WayneFlow team.</span></h2></div><div class="grid3">{rel}</div></div></section>'''
        url = f'{SITE}/blog/{p["slug"]}.html'
        article_ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p['h1'], "description": p['description'],
            "mainEntityOfPage": url, "url": url, "image": SITE + "/assets/og.jpg", "datePublished": PUBLISHED, "dateModified": PUBLISHED,
            "wordCount": p['words'], "inLanguage": "en-US", "keywords": p['keyword'],
            "author": [{"@type": "Person", "name": "Syed Asim Hussain", "url": SITE + "/about.html#asim"}, {"@type": "Person", "name": "Syed Ali Hassan", "url": SITE + "/about.html#ali"}], "publisher": {"@id": SITE + "/#org"}}
        crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p['h1'], "item": url}]}
        sch = [article_ld, crumbs] + ([faq_ld([(x['q'], x['a']) for x in p['faq']])] if p.get('faq') else [])
        out = page('blog', p['title'], p['description'], body, False, True, f'blog/{p["slug"]}.html', sch, False, True)
        out = out.replace('<meta property="og:type" content="website">', f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{PUBLISHED}">')
        open(f'{OUT}/blog/{p["slug"]}.html', 'w').write(out)
    # index
    cards = ''.join(f'<a class="card post-card reveal" href="/blog/{q["slug"]}.html"><span class="tag">{q["readMinutes"]} min read</span><h3>{H.escape(q["h1"])}</h3><p>{H.escape(q["excerpt"])}</p><span class="go">Read the guide →</span></a>' for q in posts)
    ib = f'''<section class="sec">
  <div class="wrap">
    <div class="head"><span class="kicker">The WayneFlow blog</span><h1>Cold email and appointment setting, <span class="hl">explained with real numbers.</span></h1>
    <p class="lead">Practical guides for U.S. B2B founders and sales leaders. No theory from people who have never sent a campaign. Everything here comes from 588,000+ emails we have sent and the sources we link.</p>
    <p><a class="toc-pb" style="display:inline-flex" href="/free-cold-email-playbook.html"><img src="/assets/img/playbook-cover.webp" alt="Free cold email playbook" width="60" height="78" loading="lazy"><span><b>New: the free cold email playbook</b>35 pages, step by step, with 7 real case studies</span></a></p></div>
    <h2 class="sr-only">All guides</h2><div class="grid3 posts">{cards}</div>
  </div>
</section>'''
    blog_ld = {"@context": "https://schema.org", "@type": "Blog", "name": "The WayneFlow Blog", "url": SITE + "/blog/", "publisher": {"@id": SITE + "/#org"},
               "blogPost": [{"@type": "BlogPosting", "headline": q['h1'], "url": f'{SITE}/blog/{q["slug"]}.html', "datePublished": PUBLISHED} for q in posts]}
    open(f'{OUT}/blog/index.html', 'w').write(page('blog', 'Cold Email & B2B Appointment Setting Blog | WayneFlow',
        'Practical guides on B2B appointment setting, cold email deliverability, copywriting, compliance and SDR costs, written from 588,000+ emails sent.',
        ib, False, True, 'blog/', [blog_ld], False, True))
    posts_svcs = build_services(OUT, page, SITE, CAL, faq_ld)
    build.services = posts_svcs
    return posts
