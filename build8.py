import shutil, os, json, re
import sys as _s0, os as _o0; SRC=_o0.path.dirname(_o0.path.abspath(__file__)); _s0.path.insert(0,SRC)
from extra_pages import *
OUT = _o0.environ.get('WF_OUT', '/home/claude/site8')
CAL = 'https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers'
shutil.copy(SRC + '/build8_css.css', f'{OUT}/assets/style.css')

def funnel(stages, top=None, right=None, sm=False):
    """stages: list of (value, label, sub, width%, drop_to_next or None)"""
    rows = []
    n = len(stages)
    for k, (v, lab, sub, w, drop) in enumerate(stages):
        last = ' last' if k == n - 1 else ''
        rows.append(f'<div class="fstage{last}"><div class="fbar" style="--w:{w}%">{v}</div><div class="flabel">{lab}{f"<small>{sub}</small>" if sub else ""}</div></div>')
        if drop:
            rows.append(f'<div class="fstage"><div class="fdrop">↓ {drop}</div><div></div></div>')
    m = MONEY.get(id(stages))
    foot = f'<div class="fc-money"><span class="lbl">{m[1]}</span><b>{m[0]}</b></div>' if m else ''
    head = f'<div class="fc-top"><span>{top}</span><em>{right or ""}</em></div>' if top else ''
    return f'<div class="funnel-card">{head}<div class="funnel{" sm" if sm else ""}">{"".join(rows)}</div>{foot}</div>'

from hot_data import HOT, LABEL, LABPOS, LABRING, MOBILE
def shot(img, bar, alt):
    def ringset(boxes, tagpos, labi, cls):
        out=''
        for i,(x,y,w,h) in enumerate(boxes):
            lab=f'<em class="hs-tag {tagpos}">{LABEL[img]}</em>' if i==labi else ''
            out+=f'<span class="hs {cls}" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%;--d:{i*0.35:.2f}s">{lab}</span>'
        return out
    m=MOBILE.get(img)
    rings=ringset(HOT.get(img,[]), LABPOS.get(img,""), LABRING.get(img,0), 'hs-d' if m else '')
    if m:
        rings+=ringset(m[1], m[2], 0, 'hs-m')
        pic=f'<picture><source media="(max-width:640px)" srcset="assets/img/{m[0]}.webp"><img src="assets/img/{img}-hd.webp" alt="{alt}" loading="lazy"></picture>'
    else:
        pic=f'<img src="assets/img/{img}-hd.webp" alt="{alt}" loading="lazy">'
    return f'<figure class="shot" role="button" tabindex="0" aria-label="View screenshot full size" style="margin:0"><div class="bar"><i></i><i></i><i></i><span>{bar}</span><span class="ok">Real data</span></div><div class="shot-media">{pic}{rings}</div></figure>'

def stats(items, cls=''):
    return f'<div class="stats {cls}">' + ''.join(f'<div class="stat {c}"><b class="num">{v}</b><span>{l}</span></div>' for v, l, c in items) + '</div>'

ICON = {
 'search': '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="M16 16l5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'shield': '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
 'pen': '<svg viewBox="0 0 24 24"><path d="M4 20l4-1 11-11-3-3L5 16z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'cal': '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'chat': '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'chart': '<svg viewBox="0 0 24 24"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'eye': '<svg viewBox="0 0 24 24"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
 'globe': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
}
ORG_LD = {"@context":"https://schema.org","@type":"ProfessionalService","@id":SITE+"/#org","name":"WayneFlow","alternateName":"WayneFlow by Ali & Asim","url":SITE+"/","logo":SITE+"/assets/logo.png","image":SITE+"/assets/og.jpg",
  "description":"Done-for-you B2B appointment setting, cold email and LinkedIn outreach that books qualified sales appointments for companies across the United States.",
  "slogan":"25 qualified sales appointments a month. Guaranteed.",
  "areaServed":[{"@type":"Country","name":"United States"},{"@type":"Country","name":"Canada"}]+[{"@type":"State","name":x} for x in ALL_STATES],
  "knowsAbout":["B2B appointment setting","Cold email outreach","Lead generation","LinkedIn outreach","Email deliverability","Sales pipeline generation"],
  "hasOfferCatalog":{"@type":"OfferCatalog","name":"Outbound services","itemListElement":[
    {"@type":"Offer","itemOffered":{"@type":"Service","name":"B2B appointment setting","serviceType":"Appointment setting"}},
    {"@type":"Offer","itemOffered":{"@type":"Service","name":"Done-for-you cold email outreach","serviceType":"Cold email lead generation"}},
    {"@type":"Offer","itemOffered":{"@type":"Service","name":"LinkedIn outreach","serviceType":"LinkedIn lead generation"}},
    {"@type":"Offer","itemOffered":{"@type":"Service","name":"Email deliverability and inbox setup","serviceType":"Email infrastructure"}}]},
  "founder":[{"@type":"Person","name":"Syed Asim Hussain","jobTitle":"Co-founder","description":"8 years in digital marketing and outbound sales systems","url":SITE+"/about.html#asim","image":SITE+"/assets/team/asim.webp","sameAs":[ASIM_LI]},{"@type":"Person","name":"Syed Ali Hassan","jobTitle":"Co-founder","description":"8 years in digital marketing, cold email and LinkedIn lead generation","url":SITE+"/about.html#ali","image":SITE+"/assets/team/ali.webp"}],
  "sameAs":[LI_COMPANY, INSTAGRAM, UPWORK, FIVERR],
  "makesOffer":{"@type":"Offer","name":"Done-for-you B2B appointment setting","url":SITE+"/book.html"},
  "contactPoint":{"@type":"ContactPoint","contactType":"sales","email":EMAIL,"url":CAL,"areaServed":["US","CA"],"availableLanguage":"English"}}
SITE_LD = {"@context":"https://schema.org","@type":"WebSite","@id":SITE+"/#website","name":"WayneFlow","url":SITE+"/","publisher":{"@id":SITE+"/#org"},"inLanguage":"en-US"}
def faq_ld(pairs): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}
def crumb_ld(name, path): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":name,"item":SITE+"/"+path}]}
ANALYTICS = """<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled getFeatureFlag onFeatureFlags identify alias set_config people.set".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
var wfMe=(function(){try{var q=location.search;if(/[?&]wf_me=1/.test(q))localStorage.setItem('wf_me','1');if(/[?&]wf_me=0/.test(q))localStorage.removeItem('wf_me');return localStorage.getItem('wf_me')==='1';}catch(e){return false;}})();
if(!wfMe&&!/^(localhost|127\\.)/.test(location.hostname)&&!/claude|anthropic/.test(location.hostname)){posthog.init('phc_ByqbttHSC95GAYA4D9vx9GZFN2UomLjE5qtdAzNK3XUU',{api_host:'https://us.i.posthog.com',person_profiles:'always',respect_dnt:true,capture_pageleave:true,session_recording:{maskAllInputs:true}});}
</script>
<script src="/assets/wf-lead.js?v=1793121095" defer></script>
<script src="/assets/wf-track.js?v=1793118066" defer></script>"""

INDEXNOW_KEY = 'b7f3c9e2a14d4f6e8c0a5d2e9f1b3a7c'
CHECK = '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#E6F7EC"/><path d="M7 12l3 3 7-7" fill="none" stroke="#17A35B" stroke-width="2.4" stroke-linecap="round"/></svg>'

BUILD4 = [('Find your buyers','We list the decision makers who match your best clients and verify every email.','search'),
          ('Protect your domain','We send from separate domains we set up and warm for you. Your main domain is never touched.','shield'),
          ('Write emails people answer','Short, plain and about their problem. You approve every one before it goes out.','pen'),
          ('Book the meeting','We reply, follow up and qualify. Interested buyers land on your calendar with a short brief.','cal')]

REVIEWS = [
 ("Lauren Bennett","Business launch","When I started my agency, I had no idea how to find my first clients consistently. WayneFlow helped us build our outbound process from scratch. It gave us a much clearer direction instead of just guessing what to do next."),
 ("Andrew Phillips","Fully managed outreach","We didn't want to hire and train an entire outbound team internally. WayneFlow helped us handle prospecting, campaign management, and follow-ups without adding that workload to our staff. Exactly the kind of support we were looking for."),
 ("Jason Parker","6-month partnership","We've been working with WayneFlow for about six months now. They manage our outreach, keep campaigns running, and handle the follow-ups. It's one less thing I have to worry about while running the business."),
 ("Brandon Scott","Fixing an existing system","We already had Instantly running, but our campaigns weren't producing much. WayneFlow looked at our setup, cleaned up the targeting, and improved how we approached prospects. We didn't have to rebuild everything from zero."),
 ("Olivia Hayes","Established business, new outreach","Our company had been around for years, but we'd never really done outbound. WayneFlow came in, built our cold email and LinkedIn setup, and helped us start reaching potential clients outside our existing network."),
 ("Kevin Murphy","Agency client acquisition","We were relying almost entirely on referrals. WayneFlow helped us introduce outbound without disrupting the business we already had. Having another way to reach potential customers has been really valuable."),
 ("Megan Collins","Startup growth","We had a service, a website, and a small team, but absolutely no system for bringing in new business. WayneFlow helped us get the outreach side organized so we could focus on delivering our services."),
 ("Christopher Reed","B2B sales","I didn't need another list of random leads. I needed conversations with business owners who might actually be interested. That's what I liked about WayneFlow's approach. It's focused on quality, not just volume."),
 ("Tyler Anderson","Campaign recovery","Our previous outreach campaigns started strong and then completely slowed down. WayneFlow helped us figure out where things were going wrong and made the process more consistent. Really appreciated how hands-on they were."),
 ("Rachel Simmons","Long-term outreach support","At first, we only needed help setting up cold email. A few months later, WayneFlow was managing our LinkedIn outreach too. It's been great having one team handle the whole process instead of juggling different freelancers."),
 ("Michael Brooks","Appointment setting","I was spending way too much time chasing prospects and following up. The WayneFlow team helped take that workload off my plate so I could focus on actual sales conversations."),
 ("Nicole Edwards","Technical setup","I honestly thought our email copy was the problem. Turns out, our sending setup needed work too. WayneFlow helped us sort out the technical side, organize our campaigns, and approach outreach a lot more strategically."),
 ("Ryan Mitchell","LinkedIn outreach","LinkedIn was eating up hours of my day, and most conversations went nowhere. WayneFlow helped us focus on reaching the right people instead of just sending more connection requests."),
 ("Sarah Thompson","Lead quality","Our biggest issue wasn't finding leads. It was finding people who actually needed what we offered. WayneFlow helped us rethink our targeting and make our outreach more relevant."),
]
def ini(n): return ''.join(w[0] for w in n.split())[:2]
def rcard(r): return f'<figure class="rcard" style="margin:0"><p>"{r[2]}"</p><figcaption class="who"><i>{ini(r[0])}</i><div><b>{r[0]}</b><span>{r[1]}</span></div></figcaption></figure>'

BOOKCARD = '''<div class="bookcard reveal" aria-label="Booking preview">
  <div class="bc-top"><img src="assets/icon.png" alt=""><div><b>Strategy call with WayneFlow</b><span>Pick a time that works for you</span></div></div>
  <div class="bc-meta"><span>⏱ 20 minutes</span><span>📹 Video call</span><span>💸 Free</span></div>
  <div class="bc-tz">🌎 Times shown in your time zone</div>
  <div class="bc-days"></div>
  <div class="bc-slots"></div>
  <p class="bc-foot">Pick a slot to see live availability on our booking page</p>
</div>'''

REVTABLE = '''<div class="rhead"><span>Your average deal</span><span></span><span>Revenue from one campaign</span></div>
<div class="rtable">
  <div class="rrow"><div>$3,000</div><span>× 6 deals</span><b>$18,000</b></div>
  <div class="rrow"><div>$10,000</div><span>× 6 deals</span><b>$60,000</b></div>
  <div class="rrow"><div>$25,000</div><span>× 6 deals</span><b>$150,000</b></div>
</div>
<p class="fine">Illustration only, using the six signed contracts from our construction software campaign. Your result depends on your offer, market and sales process.</p>'''

TIMELINE = '''<div class="tline">
  <div class="tl reveal"><i>1</i><span class="t">Day 1</span><h3>Kickoff call</h3><p>We learn your offer, your best clients and what a deal is worth.</p></div>
  <div class="tl reveal"><i>2</i><span class="t">Days 2 to 14</span><h3>Build and warm up</h3><p>Lists built and verified. New inboxes warmed so emails reach the inbox.</p></div>
  <div class="tl reveal"><i>3</i><span class="t">Days 15 to 21</span><h3>Write and approve</h3><p>You see every email before anything goes out. Then we launch.</p></div>
  <div class="tl reveal"><i>4</i><span class="t">Day 22 onward</span><h3>Meetings start</h3><p>We answer replies every day, and qualified meetings show up on your calendar.</p></div>
</div>'''

FAQ = '''<div class="faq">
  <details><summary>Will this hurt my company's email reputation?</summary><p>No. We send from separate domains set up just for outreach. Your main domain is never used.</p></details>
  <details><summary>How fast will I see calls?</summary><p>About three weeks to build lists and warm the inboxes. Replies usually start in the first week after launch. Our 5 day blitz booked 25 calls inside one week.</p></details>
  <details><summary>Why do your dashboards show 0 opens?</summary><p>We switch open tracking off on purpose. Tracking pixels are a spam signal, so removing them puts more emails in the inbox. We measure what pays you: replies and booked calls.</p></details>
  <details><summary>How much of my time does this take?</summary><p>One kickoff call and a quick review of the emails before launch. After that you just take the calls we book.</p></details>
  <details><summary>Do you guarantee appointments?</summary><p>Yes. Once your campaign is live, we guarantee a minimum of 25 qualified sales appointments a month. We walk you through exactly how the guarantee works for your market on the strategy call.</p></details>
  <details><summary>How much does it cost?</summary><p>It depends on your market, who you sell to and how many meetings you need. On the 20-minute call we learn your offer and then give you a clear quote, with everything included. No hidden fees.</p></details>
  <details><summary>Which industries do you work with?</summary><p>Marketing agencies, construction software, B2B services, and founder and investor outreach. We build each campaign around your buyer.</p></details>
</div>'''

PAGES = [('index.html','home','Home'),('results.html','results','Results'),('process.html','process','How it works'),('reviews.html','reviews','Reviews'),('blog/','blog','Blog'),('book.html','book','FAQ')]

def nav():
    links = ''.join(f'<a href="{f}" data-p="{p}">{t}</a>' for f, p, t in PAGES)
    return f'''<nav>
  <div class="wrap">
    <a href="index.html" aria-label="WayneFlow home"><span class="brand" role="img" aria-label="WayneFlow"></span></a>
    <div class="menu" id="menu">{links}<a class="btn btn-primary mcta" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div>
    <div class="navr">
      <a class="btn btn-primary btn-sm dcta" href="{CAL}" target="_blank" rel="noopener">Book a call</a>
      <button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="prog" id="prog"></div>
</nav>'''

FOOT = f'''<footer><div class="wrap">
  <div class="fgrid">
    <div><a href="index.html" aria-label="WayneFlow home"><span class="brand" role="img" aria-label="WayneFlow"></span></a><p>B2B appointment setting. Done-for-you cold email and LinkedIn outreach that books sales calls for companies in all 50 states.</p></div>
    <div><h4>Explore</h4><a href="index.html">Home</a><a href="lead-generation-services.html">Lead generation services</a><a href="results.html">Results</a><a href="process.html">How it works</a><a href="areas.html">USA (all 50 states)</a><a href="canada.html">Canada</a><a href="reviews.html">Reviews</a><a href="about.html">About us</a><a href="blog/">Blog</a></div>
    <div><h4>Get started</h4><a href="{CAL}" target="_blank" rel="noopener">Book a call</a><a href="book.html">FAQ</a><a href="{LI_COMPANY}" target="_blank" rel="noopener">LinkedIn</a><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><a href="{UPWORK}" target="_blank" rel="noopener">Upwork</a><a href="{FIVERR}" target="_blank" rel="noopener">Fiverr</a></div>
    <div><h4>Legal</h4><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="privacy.html#s6">Opt out of emails</a></div>
  </div>
  <div class="fbase"><span>© 2026 WayneFlow by Ali &amp; Asim. All rights reserved.</span><span>Every number on this site is a live screenshot from a real campaign. Results vary.</span></div>
</div></footer>'''

LB = '<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Screenshot"><button type="button" aria-label="Close">✕</button><div><img alt=""><p></p></div></div>'

def band(h='Want to see what this would look like for you?', p='Book a 20-minute call. We will show you who we would target, the angle we would use and how many meetings to expect in your first 30 days.'):
    return f'<div class="wrap"><div class="band reveal"><div><h2>{h}</h2><p>{p}</p></div><a class="btn" href="{CAL}" target="_blank" rel="noopener">Get my free mini plan</a></div></div>'

def page(key, title, desc, body, three=False, full=True, path='', schema=None, noindex=False, base=False):
    url = SITE + '/' + path
    ld = [ORG_LD, SITE_LD] + (schema or [])
    ldj = '\n'.join('<script type="application/ld+json">' + json.dumps(x, separators=(',',':')) + '</script>' for x in ld)
    head = f'''{'<base href="/">' if base else ''}<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-image-preview:large'}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="WayneFlow">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="WayneFlow: 25 qualified sales appointments a month, guaranteed">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og.jpg">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="assets/style.css?v=1793120657">
{ldj}
{ANALYTICS if full else ''}'''
    scripts = '<script src="assets/site.js?v=1793118066"></script>'
    if three:
        scripts = '<script src="assets/site.js?v=1793118066"></script>\n<script>/* 3D background: laptops and desktops only */if(window.innerWidth>640){var t=document.createElement("script");t.src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js";t.onload=function(){var s=document.createElement("script");s.src="assets/story3d.js?v=1793118066";document.body.appendChild(s);};document.body.appendChild(t);}</script>'
    inner = f'''{'<canvas id="stage" aria-hidden="true"></canvas>' if three else ''}
<div class="gridbg" aria-hidden="true"></div>
{nav()}
<main>
{body}
</main>
{FOOT}
{scripts}
<script>document.body.dataset.page="{key}";document.querySelectorAll('#menu a[data-p]').forEach(a=>a.classList.toggle('on',a.dataset.p==="{key}"));</script>'''
    if full:
        return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{head}
</head>
<body data-page="{key}">
{inner}
</body>
</html>
'''
    return '<meta name="claude:viewport-fit-sides" content="cover">\n' + head + '\n' + inner

# ---------------------------------------------------------------- funnels (all numbers from the Results File)
F_AGENCY = [('82,671','Cold emails sent',None,100,'2.9%'),('2,429','Replies',None,82,'88%'),('2,146','Positive, interested replies',None,66,None)]
F_CONSTR = [('162,073','Cold emails sent',None,100,'2.7%'),('4,449','Replies',None,84,'0.7%'),('31','Sales qualified demos held',None,66,'19%'),('6','Annual contracts signed',None,50,None)]
F_BLITZ = [('96,408','Emails in 5 days',None,100,'1.1%'),('1,095','Replies',None,84,'11%'),('115','Interested',None,68,'22%'),('25','Calls booked',None,52,None)]
F_Q1 = [('236,545','Emails sent',None,100,'1.8%'),('4,372','Replies',None,82,'24%'),('1,061','Interested leads',None,64,None)]
F_PILOT = [('10,284','People contacted',None,100,'4.1%'),('417','Replies',None,82,'25%'),('103','Sales opportunities',None,64,None)]
F_LI = [('1,375','LinkedIn invites',None,100,'26%'),('351','Connections accepted',None,82,'44%'),('154','Founder and investor replies',None,64,None)]
# dollar value at the client's $2,500 average deal. Case 02 is real closed revenue; the rest are estimates
# (1 in 5 booked calls close, from Case 02; 1 in 10 interested leads books a call, so 1 in 50 becomes a client)
MONEY = {
  id(F_CONSTR): ('$15,000','Closed deals for this client',''),
  id(F_BLITZ): ('$62,500','Pipeline generated in 5 days',''),
  id(F_PILOT): ('$150,000','Pipeline generated',''),
  id(F_AGENCY): ('$175,000','Pipeline generated',''),
  id(F_Q1): ('$100,000','Pipeline generated',''),
  id(F_LI): ('$7,500','Pipeline generated',''),
}
MONEY_NOTE = '<p class="fine moneynote">Pipeline is the value of the qualified sales opportunities we generated, at our clients\' $2,500 average deal.</p>'



# ---------------------------------------------------------------- HOME
steps_html = ''.join(f'<div><em>{k+1}</em><div><b>{t}</b><span>{d}</span></div></div>' for k, (t, d, _) in enumerate(BUILD4))
TICK_HTML = ''.join(f'<span><b>{n}</b>{l}</span>' for n, l in [('2–5', 'sales calls a day, guaranteed'), ('588,000', 'emails sent'), ('12,900+', 'replies'), ('3,400+', 'interested buyers'), ('100+', 'calls booked'), ('6', 'annual contracts'), ('$510K+', 'pipeline generated'), ('0.45%', 'bounce rate')])
HOME = f'''<div class="story" id="story">

  <section class="scn hero" id="top">
    <div class="wrap"><div class="split">
      <div>
        <div class="tick" role="marquee" aria-label="WayneFlow results in numbers"><div class="tick-run">{TICK_HTML}</div></div>
        <span class="k-pill"><i></i>Appointment setting agency</span>
        <h1 class="hero-h nh"><span class="w">A</span> <span class="w">system</span> <span class="w">that</span> <span class="w">books</span> <span class="w g25">2–5&nbsp;sales&nbsp;calls</span> <span class="w">every</span> <span class="w">day.</span> <span class="w stamp"><span class="hl">Guaranteed.</span></span></h1>
        <p class="lead">We find your buyers, write the emails, handle every reply and book the interested ones into your calendar. Your job is to show up and close.<span class="hide-m"> 588,000 emails sent so far, and 3,400+ buyers asked to talk.</span></p>
        <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a><a class="btn btn-secondary" href="results.html">See the dashboards</a></div>
        <a class="founder-strip" href="about.html"><span class="author-photos"><img src="assets/team/asim-sq.webp" alt="Syed Asim Hussain" width="44" height="44"><img src="assets/team/ali-sq.webp" alt="Syed Ali Hassan" width="44" height="44"></span><span><b>WayneFlow by Ali &amp; Asim</b><small>8 years in outbound<span class="hide-m"> · USA &amp; Canada clients</span><span class="show-m"> · USA &amp; Canada</span></small></span></a>
        {stats([('12,900+','Replies generated','hot'),('100+','Calls and demos booked','hot'),('6','Annual contracts signed',''),('$510K+','Pipeline generated','lime')], 's4')}
      </div>
      <div class="hero-viz reveal">
        {funnel(F_AGENCY, 'One client, June to October 2026', '4 months, 18 days')}
        <div class="hero-proof"><span class="hp-tag">The proof: the live dashboard</span>{shot('agency','Live dashboard · Jun to Oct 2026','Live campaign dashboard: 82,671 emails sent, 2,429 replies, 2,146 interested').replace('loading="lazy"','loading="eager"')}</div>
        <p class="hero-note">Every number on this site comes from a real campaign dashboard. Click any screenshot to see it full size.</p>
      </div>
    </div></div>
  </section>

  <section class="scn"><div class="wrap"><div class="card">
    <span class="kicker">Why most cold email fails</span>
    <h2>Most cold email <span class="hl">never gets read.</span></h2>
    <p class="lead">Bought lists, recycled templates and thousands of emails sent from your main domain. Inbox providers spot it fast, the emails go to spam, and your domain takes the hit.</p>
  </div></div></section>

  <section class="scn"><div class="wrap"><div class="card">
    <span class="kicker">How it works</span>
    <h2>You approve the emails. <span class="hl">We handle the rest.</span></h2>
    <div class="steps4">{steps_html}</div>
  </div></div></section>

  <section class="scn"><div class="wrap"><div class="card wide">
    <span class="kicker">Proof · a client's inbox</span>
    <h2>50+ meetings booked into <span class="hl">one client's calendar.</span></h2>
    <div class="viz">{shot('calendly','Real inbox · Calendly bookings','Email inbox full of Calendly discovery meeting bookings, names hidden')}</div>
  </div></div></section>

  <section class="scn"><div class="wrap"><div class="card wide">
    <span class="kicker">Proof · cold email to signed contracts</span>
    <h2>From cold emails to <span class="hl">6 signed annual contracts.</span></h2>
    <div class="viz">{funnel(F_CONSTR, 'Construction software client', 'Real data').replace('funnel-card','funnel-card" style="box-shadow:none;border:0;padding:0')}
    <div class="hero-proof"><span class="hp-tag">The proof: the live dashboard</span>{shot('construction','Live dashboard · Construction SaaS','Construction software client dashboard: 162,073 emails sent, 4,449 replies')}</div></div>
  </div></div></section>

</div>

<section class="sec" id="cases">
  <div class="wrap">
    <div class="head-row reveal"><div><span class="kicker">Case studies</span><h2>Three clients, <span class="hl">three different goals.</span></h2></div><a class="link" href="results.html">See all 6 case studies →</a></div>
    <div class="grid3">
      <a class="card pcard reveal" href="results.html#case-01"><span class="tag">Case 01 · Agency client</span><h3>2,146 people said "Yes, tell me more."</h3>{funnel(F_AGENCY, sm=True).replace('funnel-card','funnel-card" style="box-shadow:none;padding:0;border:0')}<div class="pproof">{shot('agency','Live dashboard','Agency client dashboard: 82,671 emails sent, 2,429 replies, 2,146 interested')}</div><span class="go">Read the case →</span></a>
      <a class="card pcard reveal" href="results.html#case-02"><span class="tag">Case 02 · Construction software</span><h3>From a cold inbox to 6 signed annual contracts.</h3>{funnel(F_CONSTR, sm=True).replace('funnel-card','funnel-card" style="box-shadow:none;padding:0;border:0')}<div class="pproof">{shot('construction','Live dashboard','Construction software client dashboard: 162,073 emails sent, 4,449 replies')}</div><span class="go">Read the case →</span></a>
      <a class="card pcard reveal" href="results.html#case-03"><span class="tag">Case 03 · The 5 day blitz</span><h3>96,408 emails in five days, and 25 calls booked.</h3>{funnel(F_BLITZ, sm=True).replace('funnel-card','funnel-card" style="box-shadow:none;padding:0;border:0')}<div class="pproof">{shot('blitz','Live dashboard','5 day blitz dashboard: 96,408 emails sent, 1,095 replies')}</div><span class="go">Read the case →</span></a>
    </div>
    {MONEY_NOTE}
  </div>
</section>

<section class="sec" id="scoreboard">
  <div class="wrap">
    <div class="split top">
      <div class="reveal">
        <span class="kicker">The numbers</span>
        <h2 style="margin-top:14px">Here is what we sent this year, <span class="hl">and what came back.</span></h2>
        <p class="lead">Email volume for five client campaigns. Every figure matches a screenshot on our results page.</p>
        <div class="card" style="margin-top:28px">
          <div class="bars">
            <div class="brow"><span>Quarter sprint</span><div class="tr"><i style="--w:100%"></i></div><b class="num">236,545</b></div>
            <div class="brow"><span>Construction SaaS</span><div class="tr"><i style="--w:68.5%"></i></div><b class="num">162,073</b></div>
            <div class="brow"><span>5 day blitz</span><div class="tr"><i style="--w:40.8%"></i></div><b class="num">96,408</b></div>
            <div class="brow"><span>Agency client</span><div class="tr"><i style="--w:35%"></i></div><b class="num">82,671</b></div>
            <div class="brow"><span>Pilot campaign</span><div class="tr"><i style="--w:6%"></i></div><b class="num">10,284</b></div>
          </div>
        </div>
      </div>
      <div class="grid2">
        <div class="card reveal"><div class="icon">{ICON['chat']}</div><h3>2.8% to 4% reply rates</h3><p>Across our largest campaigns, with open tracking off and every list verified before sending.</p></div>
        <div class="card reveal"><div class="icon">{ICON['shield']}</div><h3>Bounce rates under 3%</h3><p>Every list is verified before a single email goes out. Clean data keeps your inboxes healthy.</p></div>
        <div class="card reveal"><div class="icon">{ICON['eye']}</div><h3>"Why do opens show 0?"</h3><p>Because we turn open tracking off. Tracking pixels push emails toward spam, so we measure what pays you: replies and booked meetings.</p></div>
        <div class="card reveal"><div class="icon">{ICON['globe']}</div><h3>Results across industries</h3><p>Marketing agencies, construction software, B2B services, founder and investor outreach.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="founders">
  <div class="wrap">
    <div class="split founders-home">
      <div class="team-photo reveal"><img src="assets/team/founders.webp" width="900" height="900" alt="WayneFlow founders Syed Asim Hussain (left) and Syed Ali Hassan (right)" loading="lazy"></div>
      <div class="reveal"><span class="kicker">Who you will work with</span><h2 style="margin-top:14px">Meet the founders <span class="hl">behind your campaigns.</span></h2>
        <p class="lead">WayneFlow is run by two people, not a faceless call center. Together we have 8 years in digital marketing and outbound, and we have worked with dozens of companies, mostly in the United States and Canada.</p>
        <div class="fh-list">
          <a class="fh" href="about.html#asim"><img src="assets/team/asim-sq.webp" width="64" height="64" alt="Syed Asim Hussain"><div><b>Syed Asim Hussain</b><span>Co-founder. Strategy, targeting and offers. You meet him on the first call.</span></div></a>
          <a class="fh" href="about.html#ali"><img src="assets/team/ali-sq.webp" width="64" height="64" alt="Syed Ali Hassan"><div><b>Syed Ali Hassan</b><span>Co-founder. Lists, inboxes, deliverability and the system that books your meetings.</span></div></a>
        </div>
      </div>
    </div>
    {story_html(CAL, '#cases')}
  </div>
</section>



<section class="sec" id="reviews">
  <div class="wrap">
    <div class="head-row reveal"><div><span class="kicker">What clients say</span><h2>What our <span class="hl">clients say.</span></h2></div><a class="link" href="reviews.html">Read all reviews →</a></div>
  </div>
  <div class="carousel" aria-label="Client reviews"><div class="run">{''.join(rcard(r) for r in REVIEWS)}</div></div>
  <div class="cctl"><button class="btn btn-secondary btn-sm" type="button" data-toggle>Pause reviews</button></div>
</section>

<section class="sec" id="final">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="kicker">What it could mean for you</span>
        <h2 style="margin-top:14px">Run your own numbers <span class="hl">before you talk to us.</span></h2>
        <p class="lead">Our construction software client signed six annual contracts. Here is what six deals would be worth at your price.</p>
        <div style="margin-top:24px">{REVTABLE}</div>
        <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a><a class="btn btn-secondary" href="process.html">How it works</a></div>
      </div>
      {BOOKCARD}
    </div>
  </div>
</section>
'''

# ---------------------------------------------------------------- RESULTS
def case(cid, flip, kicker, h, p, stat_items, viz, extra=''):
    return f'''<article class="case{' flip' if flip else ''}" id="{cid}">
      <div class="case-copy reveal"><span class="kicker">{kicker}</span><h2>{h}</h2><p class="lead">{p}</p>{stats(stat_items)}{extra}<div class="case-cta"><a class="btn btn-primary btn-sm" href="{CAL}" target="_blank" rel="noopener">Get a plan like this for my company</a><span>Free 20-minute call. No pitch.</span></div></div>
      <div class="case-viz reveal">{viz}</div>
    </article>'''

RESULTS = f'''<section class="phero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> / Results</div>
    <div class="split">
      <div><span class="kicker">Case studies · 2026</span><h1>Six campaigns, with <span class="hl">the dashboards to prove them.</span></h1>
      <p class="lead">Every case study below comes with the screenshot it came from. Click any of them to see it full size. This is the same system we would build for you.</p></div>
      {stats([('588,000','Cold emails sent',''),('3,400+','Buyers raised their hand','hot'),('12,900+','Replies generated','hot'),('100+','Calls and demos booked',''),('6','Annual contracts signed',''),('$510K+','Pipeline generated','lime')], 's3')}
    </div>
    {MONEY_NOTE}
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    {case('case-01', False, 'Case study 01 · Agency client', '2,146 people said <span class="hl">"Yes, tell me more."</span>',
      'Between June 1 and October 19, 2026, this agency client got about 100 interested replies a week, every week, for four and a half months.',
      [('3.19%','Reply rate','hot'),('88%','Of replies positive','hot'),('1.64%','Bounce rate',''),('6','Unsubscribes total','')],
      funnel(F_AGENCY, 'Jun 1 to Oct 19, 2026', 'Live dashboard') + shot('agency','Sending dashboard · Jun 1 to Oct 19, 2026','Agency client dashboard: 82,671 emails sent, 2,429 replies, 2,146 interested'),
      '<p class="callout">Only <b>6 of 76,081</b> people asked to be removed. When the email fits the reader, people do not unsubscribe.</p>')}
    {case('case-02', True, 'Case study 02 · Construction software', 'From a cold inbox to <span class="hl">6 signed annual contracts.</span>',
      'This construction software company wanted signed contracts, not replies. We booked 31 sales-qualified demos, and their team closed 6 annual deals.',
      [('31','Demos held','hot'),('1 in 5','Demos became contracts','lime'),('5 of 6','Closed in last 2 weeks',''),('1 year','Length of each contract','')],
      funnel(F_CONSTR, '162,073 emails · 4,449 replies', 'Real data') + shot('construction','Sending dashboard · Construction software','Construction software dashboard: 162,073 emails sent, 4,449 replies'),
      '<div class="money"><b>What this means in plain money:</b> 6 contracts at our clients\' average deal of $2,500 is <b>$15,000 in closed revenue</b>, from emails sent to strangers. If your deal is worth $10,000, the same result is <b>$60,000</b>.</div>')}
    {case('case-03', False, 'Case study 03 · The 5 day blitz', '96,408 emails. Five days. <span class="hl">25 calls on the calendar.</span>',
      'Between September 7 and 11, 2026 we ran a full-scale campaign on inboxes that were already warmed up, and booked 25 calls that same week.',
      [('1,095','Replies','hot'),('115','Interested',''),('25','Calls booked','lime'),('0.45%','Bounce rate','')],
      funnel(F_BLITZ, 'Sep 7 to 11, 2026', 'Dashboard + calendar') + shot('blitz','Dashboard + calendar · Sep 7 to 11, 2026','5 day blitz dashboard: 96,408 emails, 1,095 replies, 115 interested, 25 calls booked'),
      '<p class="callout">Speed like this needs warm inboxes and a verified list ready on day one. This client had both.</p>')}
    {case('case-04', True, 'Case study 04 · A full quarter', '1,061 interested leads <span class="hl">in one quarter.</span>',
      'Steady sending from January to March 2026: a 3.69% reply rate, and about one in four replies came from a buyer who wanted to talk.',
      [('236,545','Emails sent',''),('3.69%','Reply rate','hot'),('4,372','Replies',''),('1,061','Interested leads','lime')],
      funnel(F_Q1, 'Jan to Mar 2026', 'Case 04') + shot('q1','Sending dashboard · Jan to Mar 2026','Quarter campaign dashboard: 236,545 emails, 4,372 replies, 1,061 interested'))}
    {case('case-05', False, 'Case study 05 · Small pilot', '103 opportunities <span class="hl">from 10,284 people.</span>',
      'A small test before scaling up. About 1 in every 100 people contacted became a real sales opportunity.',
      [('10,284','People contacted',''),('417','Replies','hot'),('4%','Reply rate',''),('103','Opportunities','lime')],
      funnel(F_PILOT, '10,284 contacted', 'Case 05') + shot('pilot','Campaign dashboard · Pilot','Pilot dashboard: 10,284 contacted, 417 replied, 103 opportunities'))}
    {case('case-06', True, 'Case study 06 · LinkedIn', '154 replies from <span class="hl">founders and investors.</span>',
      'Some buyers live on LinkedIn, not in their inbox. 351 decision makers accepted our connection requests, and 154 founders and angel investors replied, one of the hardest audiences to reach there.',
      [('1,375','Invites',''),('351','Accepted','hot'),('1,628','InMails',''),('154','Replies','lime')],
      funnel(F_LI, 'All time outreach', 'LinkedIn') + shot('linkedin','LinkedIn outreach analytics · All time','LinkedIn analytics: 1,375 invites, 351 accepted, 154 replies'))}
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split">
      <div class="reveal"><span class="kicker">Proof · a client's inbox</span><h2 style="margin-top:14px">50+ discovery calls in <span class="hl">one client's calendar.</span></h2>
      <p class="lead">Every line is a real Calendly booking. We blurred the names to protect our client's prospects.</p>
      {stats([('50+','Discovery calls in one calendar','hot'),('100+','Calls and demos booked overall','')], '')}</div>
      <div class="reveal">{shot('calendly','Real inbox · Calendly bookings','Inbox full of Calendly discovery meeting bookings, names hidden')}</div>
    </div>
  </div>
</section>
{band()}
'''

# ---------------------------------------------------------------- PROCESS
build_cards = ''.join(f'<div class="card reveal"><div class="step-n">{k+1}</div><h3>{t}</h3><p>{d}</p></div>' for k, (t, d, _) in enumerate(BUILD4))
offer = [('search','A list of buyers, not names','We map every company that fits your best clients and find the person who signs. Every email verified.'),
         ('shield','Inboxes that land in the inbox','Separate domains and warmed accounts, so your main domain stays clean.'),
         ('pen','Emails people actually answer','Written for your buyer and tested in batches. We keep what gets replies.'),
         ('chat','Every reply handled','We answer, follow up and qualify. You only see the conversations worth your time.'),
         ('cal','Meetings on your calendar','Each one comes with a short brief: who they are and why they replied.'),
         ('chart','A weekly report','Emails sent, replies, interested buyers and meetings booked, every week.')]
offer_html = ''.join(f'<div class="card reveal"><div class="icon">{ICON[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in offer)
PROCESS = f'''<section class="phero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> / How it works</div>
    <div class="split">
      <div><span class="kicker">How it works</span><h1>From a cold list to meetings on your calendar <span class="hl">in about three weeks.</span></h1>
      <p class="lead">You don't hire anyone, learn any software or write a single email. Here is exactly what happens after you sign up.</p>
      <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div></div>
      <div class="reveal">{funnel(F_BLITZ, 'The 5 day blitz, step by step', 'Sep 7 to 11, 2026')}</div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap">
    <div class="head reveal"><span class="kicker">The four steps</span><h2>The four <span class="hl">steps.</span></h2></div>
    <div class="grid4">{build_cards}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head reveal"><span class="kicker">Your first 30 days</span><h2>Your first 30 days, <span class="hl">day by day.</span></h2></div>
    <div class="card">{TIMELINE}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="kicker">What you get</span><h2 style="margin-top:14px">What's <span class="hl">included.</span></h2><p class="lead">Your part: one kickoff call and a quick review of the emails before launch. After that, you take the meetings.</p>
      <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div></div>
      <div class="ilist">{offer_html}</div>
    </div>
  </div>
</section>
<section class="sec" id="calculator">
  <div class="wrap">
    <div class="split">
      <div class="reveal"><span class="kicker">Do the math</span><h2 style="margin-top:14px">What would 20 meetings a month <span class="hl">be worth to you?</span></h2><p class="lead">Change the numbers to match your business.</p><div style="margin-top:24px">{REVTABLE}</div></div>
      <div class="card calc reveal">
        <label for="calls"><span class="top">Sales calls a month <b id="callsV">20</b></span><input id="calls" type="range" min="5" max="60" step="1" value="20"></label>
        <label for="close"><span class="top">You close <b id="closeV">20%</b></span><input id="close" type="range" min="5" max="50" step="1" value="20"></label>
        <label for="deal"><span class="top">One client is worth <b id="dealV">$3,000</b></span><input id="deal" type="range" min="1000" max="25000" step="500" value="3000"></label>
        <div class="out" aria-live="polite"><span>New revenue every month</span><b class="num" id="rev">$12,000</b><small id="revY">4 new clients a month.</small></div>
        <p class="fine">Example figures. Your results depend on your offer and market.</p>
      </div>
    </div>
  </div>
</section>
{band()}
'''

# ---------------------------------------------------------------- REVIEWS
REVIEWS_P = f'''<section class="phero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> / Reviews</div>
    <div class="head" style="margin-bottom:0"><span class="kicker">What clients say</span><h1>What clients say about <span class="hl">working with us.</span></h1>
    <p class="lead">New businesses, established firms and agencies that had already tried cold email and needed it to work.</p><p class="rev-ext">More client reviews on <a href="{UPWORK}" target="_blank" rel="noopener">Upwork</a> and <a href="{FIVERR}" target="_blank" rel="noopener">Fiverr</a>.</p></div>
  </div>
</section>
<section class="sec" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap"><div class="rgrid">{''.join(rcard(r) for r in REVIEWS)}</div></div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head-row reveal"><div><span class="kicker">The numbers behind it</span><h2>Results from our <span class="hl">own dashboards.</span></h2></div><a class="link" href="results.html">See the screenshots →</a></div>
    {stats([('588,000','Cold emails sent',''),('3,400+','Buyers raised their hand','hot'),('12,900+','Replies generated','hot'),('100+','Calls and demos booked',''),('6','Annual contracts signed',''),('$510K+','Pipeline generated','lime')], 's3')}
    {MONEY_NOTE}
  </div>
</section>
{band('Be our next case study.')}
'''

# ---------------------------------------------------------------- BOOK / FAQ
XL = [('You can\'t take on more clients','If your team is already at capacity, more calls just means more stress. Fix delivery first.'),
      ('Your deals are tiny','If a client is worth less than $1,000, the math of outbound gets hard. We will tell you honestly.'),
      ('You need meetings by Friday','New inboxes need about two weeks to warm up before we send. Plan for meetings in about three weeks, not by Friday.')]
xl_html = ''.join(f'<div class="card"><div class="x">✕</div><h3>{t}</h3><p>{d}</p></div>' for t, d in XL)
BOOK = f'''<section class="phero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> / FAQ</div>
    <div class="split">
      <div><span class="kicker">Book a call</span><h1>Book a 20-minute <span class="hl">strategy call.</span></h1>
      <p class="lead">You will leave with a short plan for your market: who we would target, the angle we would use and how many meetings to expect in the first 30 days. Keep it even if you never hire us.</p>
      <div class="checks"><div>{CHECK}A free mini plan for your market</div><div>{CHECK}No long pitch, no pressure</div><div>{CHECK}If the plan does not fit, keep it and use it yourself</div></div>
      <p class="ps"><b>P.S.</b> Bring your current numbers if you have them: deal size, close rate, what you have tried. The more we know, the sharper the plan.</p></div>
      {BOOKCARD}
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="kicker">Read this first</span><h2 style="margin-top:14px">Who this is not for.</h2><p class="lead">We would rather tell you now than waste your time on a call.</p><div class="xlist">{xl_html}</div></div>
      <div class="reveal"><span class="kicker">FAQ</span><h2 style="margin:14px 0 20px">Common questions.</h2>{FAQ}</div>
    </div>
  </div>
</section>
'''

DESC = 'B2B appointment setting and lead generation services for U.S. and Canadian companies. Done-for-you cold email that books 25 qualified meetings a month, guaranteed.'
FAQ_PAIRS = [(m.group(1), re.sub('<[^>]+>','',m.group(2))) for m in re.finditer(r'<summary>(.*?)</summary><p>(.*?)</p>', FAQ)]
TERMS_B = legal_wrap('Legal', 'Terms of Service', 'The rules for using this website and working with WayneFlow. Plain English where we can, legal language where we must.', TERMS_SECTIONS).replace('{CAL}', CAL)
PRIV_B = legal_wrap('Legal', 'Privacy Policy', 'What we collect, why we collect it, and the choices you have. We never sell your personal information.', PRIVACY_SECTIONS)
docs = {
 'index.html': ('home', 'B2B Appointment Setting & Lead Generation Services | WayneFlow', DESC, HOME + LB, True, '', [], False),
 'results.html': ('results', 'B2B Appointment Setting Case Studies & Results | WayneFlow', 'Six real B2B cold email case studies with live dashboards: 588,000 emails sent, 12,900+ replies, 100+ calls booked and 6 signed contracts.', RESULTS + LB, False, 'results.html', [crumb_ld('Results','results.html')], False),
 'process.html': ('process', 'How B2B Appointment Setting Works (Done for You) | WayneFlow', 'How WayneFlow builds your outbound system in four steps: verified lists, safe sending domains, emails people answer, and calls booked into your calendar.', PROCESS, False, 'process.html', [crumb_ld('How it works','process.html')], False),
 'reviews.html': ('reviews', 'Client Reviews | B2B Appointment Setting | WayneFlow', 'What U.S. founders and agency owners say about working with WayneFlow on cold email and appointment setting.', REVIEWS_P, False, 'reviews.html', [crumb_ld('Reviews','reviews.html')], False),
 'book.html': ('book', 'Book a Strategy Call + FAQ | WayneFlow', 'Book a free 20-minute strategy call with WayneFlow and get answers about cold email, deliverability, timelines and our appointment guarantee.', BOOK, False, 'book.html', [crumb_ld('Book a call','book.html'), faq_ld(FAQ_PAIRS)], False),
 'areas.html': ('areas', 'Appointment Setting Companies USA: All 50 States | WayneFlow', 'B2B appointment setting and cold email outreach for companies in all 50 U.S. states. Campaigns sent in your buyers\' local time zone, Eastern to Pacific.', areas_html(CAL, CHECK), False, 'areas.html', [crumb_ld('Service areas','areas.html'), faq_ld(AREA_FAQ)], False),
 'about.html': ('about', 'About WayneFlow: Meet the Founders | WayneFlow', 'Meet Syed Asim Hussain and Syed Ali Hassan, the founders of WayneFlow, a B2B appointment setting and cold email agency for U.S. and Canadian companies.', about_html(CAL, CHECK), False, 'about.html', [crumb_ld('About','about.html')], False),
 'privacy.html': ('privacy', 'Privacy Policy | WayneFlow B2B Appointment Setting', 'How WayneFlow collects, uses and protects personal information, and how to use your privacy rights or opt out of emails.', PRIV_B, False, 'privacy.html', [], False),
 'terms.html': ('terms', 'Terms of Service | WayneFlow B2B Appointment Setting', 'The terms that apply when you use the WayneFlow website or hire WayneFlow for B2B appointment setting and outbound lead generation.', TERMS_B, False, 'terms.html', [], False),
 '404.html': ('404', 'Page Not Found | WayneFlow B2B Appointment Setting', 'This page does not exist or has moved. Go to the WayneFlow home page or see our live campaign results.', NOTFOUND, False, '404.html', [], True),
}
for f, (key, title, desc, body, three, path, sch, noidx) in docs.items():
    open(f'{OUT}/{f}', 'w').write(page(key, title, desc, body, three, True, path, sch, noidx, f == '404.html'))
k = docs['index.html']
open(f'{OUT}/_artifact_index.html', 'w').write(page(k[0], 'WayneFlow', k[2], k[3], True, False))
import blog_build
POSTS = blog_build.build(OUT, page, SITE, CAL, crumb_ld, faq_ld)
# sitemap, robots, llms.txt
from datetime import date
urls = [('', '1.0')] + [(f, '0.9') for f in getattr(blog_build.build, 'services', [])] + [('results.html', '0.9'), ('process.html', '0.8'), ('areas.html', '0.8'), ('book.html', '0.8'), ('about.html', '0.7'), ('reviews.html', '0.7'), ('blog/', '0.8')] + [(f'blog/{q["slug"]}.html', '0.8') for q in POSTS] + [('privacy.html', '0.3'), ('terms.html', '0.3')]
open(f'{OUT}/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{u}</loc><lastmod>{date.today().isoformat()}</lastmod><priority>{pr}</priority></url>\n' for u, pr in urls) + '</urlset>\n')
open(f'{OUT}/robots.txt','w').write('# WayneFlow: open to search engines and AI assistants (ChatGPT, Claude, Perplexity, Gemini, Copilot)\nUser-agent: *\nAllow: /\nDisallow: /_artifact_index.html\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in ['OAI-SearchBot', 'ChatGPT-User', 'GPTBot', 'Claude-SearchBot', 'Claude-User', 'ClaudeBot', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Googlebot', 'Bingbot', 'Applebot', 'Applebot-Extended', 'DuckDuckBot']) + f'Sitemap: {SITE}/sitemap.xml\n')
open(f'{OUT}/'+INDEXNOW_KEY+'.txt','w').write(INDEXNOW_KEY)
open(f'{OUT}/llms.txt','w').write(f"""# WayneFlow

> WayneFlow is a done-for-you B2B appointment setting agency serving companies in all 50 U.S. states. We run cold email and LinkedIn outreach and book qualified sales appointments into clients' calendars, with a guarantee of 25 qualified appointments a month once a campaign is live.

## Key facts
- Results across campaigns: 588,000+ emails sent, 12,900+ replies, 3,400+ interested buyers, 100+ calls and demos booked, 6 annual contracts signed, $510K+ pipeline generated.
- Reply rates of 2.8% to 4% versus a typical 1%; bounce rates under 3%; open tracking switched off to protect deliverability.
- Separate sending domains so a client's main domain is never at risk. CAN-SPAM compliant.
- Industries: marketing agencies, B2B SaaS, construction software, professional services, founder and investor outreach.
- Book a call: {CAL}
- Pricing: custom quote after a 20-minute call, based on market and meeting volume.
- Founders: Syed Asim Hussain (LinkedIn: {ASIM_LI}) and Syed Ali Hassan.
- LinkedIn: {LI_COMPANY} | Instagram: {INSTAGRAM} | Upwork: {UPWORK} | Fiverr: {FIVERR}
- Contact: {EMAIL}

## Pages
- [Home]({SITE}/): overview, guarantee and live proof
- [Results]({SITE}/results.html): six case studies with live dashboard screenshots
- [How it works]({SITE}/process.html): the four-step process
- [Service areas]({SITE}/areas.html): coverage across all 50 states and time zones
- [Reviews]({SITE}/reviews.html): client testimonials
- [Book a call and FAQ]({SITE}/book.html)
- [About]({SITE}/about.html): founders Syed Asim Hussain and Syed Ali Hassan
- [Blog]({SITE}/blog/): practical guides
""" + ''.join(f"- [{q['h1']}]({SITE}/blog/{q['slug']}.html): {q['excerpt']}\n" for q in POSTS) + """""")
print('built', sorted(os.listdir(OUT)))

# old pricing URL: keep it working, send visitors and search engines to the booking page
open(f'{OUT}/pricing.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>WayneFlow | Book a 20-minute call</title>
<meta name="robots" content="noindex,follow"><link rel="canonical" href="{SITE}/book.html">
<meta http-equiv="refresh" content="0; url=/book.html"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>location.replace('/book.html'+location.hash)</script></head>
<body style="font-family:system-ui,sans-serif;padding:40px;text-align:center">This page has moved. <a href="/book.html">Book a 20-minute call with WayneFlow</a>.</body></html>''')
