"""Landing page for the free lead magnet: The WayneFlow Cold Email Playbook.
The form itself is injected by assets/wf-lead.js into #wl-slot (and #wl-slot2), so leads are
saved exactly like the popup. Visuals: cover, page previews, locked "sneak peeks", case grid."""
import html

SLUG = 'free-cold-email-playbook.html'
TITLE = 'Free Cold Email Playbook (2026): Setup, Warmup & Emails | WayneFlow'
DESC = ('Free 35-page cold email playbook: domains, SPF, DKIM and DMARC records, a 3-week warmup schedule, '
        'emails that get replies and 7 real case studies behind $510K+ in client pipeline.')
PAGES = 35

CHAPTERS = [
 ('Part 1 · The plan', [('1', 'The math before the machine', 'Work backward from the calls you want. Real funnels from 5 campaigns and a planning worksheet.'),
                         ('2', 'Your tool stack and what it really costs', 'The six tools you need and a realistic first-month budget of about $185 to $335.')]),
 ('Part 2 · The sending machine', [('3', 'Buy the right domains', 'Why you never send from your main domain, and names buyers trust.'),
                                   ('4', 'Google Workspace and your inboxes', 'Users, profiles and signatures that look like real people.'),
                                   ('5', 'DNS: MX, SPF, DKIM and DMARC', 'The exact records to copy, and how to check them in 5 minutes.'),
                                   ('6', 'Redirects, connecting inboxes, tracking', 'Finish the machine and switch off the setting that hurts delivery.'),
                                   ('7', 'Warmup: the 3-week rule', 'The week-by-week schedule we use for every new inbox.'),
                                   ('8', 'The 10-minute daily health check', 'The morning routine that catches problems before results drop.')]),
 ('Part 3 · The list', [('9', 'Pick buyers who are ready now', 'Your ideal customer profile plus buying triggers.'),
                        ('10', 'Build and verify the list by hand', 'Where to find buyers, what to remove, how to verify every address.')]),
 ('Part 4 · The message', [('11', 'Write emails people answer', 'The 5-part email under 80 words, with examples.'),
                           ('12', 'Follow-ups that add something new', 'The schedule behind the 42% of replies that come after email one.')]),
 ('Part 5 · Launch and run', [('13', 'Launch day and the volume ramp', 'Settings that matter and the first 14 days.'),
                              ('14', 'From reply to booked meeting', 'Reply buckets, replies that book the call, and the show rate.'),
                              ('15', 'Testing and reading your numbers', 'What to test first and the numbers that matter.')]),
 ('Part 6 · Stay safe', [('16', 'The law: USA and Canada', 'CAN-SPAM and CASL in plain English.'),
                         ('17', 'When emails hit spam', 'Our 7-step recovery plan.')]),
]

CASES = [
 ('case-05', 'pilot', 'Small pilot', '103', 'opportunities from 10,284 people'),
 ('case-02', 'construction', 'Construction software', '6', 'signed annual contracts'),
 ('case-03', 'blitz', 'The 5-day blitz', '25', 'calls booked in one week'),
 ('case-04', 'q1', 'One full quarter', '1,061', 'interested buyers'),
 ('case-01', 'agency', 'Marketing agency', '$175K', 'pipeline, ~100 interested replies a week'),
 ('calendly', 'calendly', 'One client calendar', '50+', 'discovery calls booked'),
 ('case-06', 'linkedin', 'Founders and investors', '154', 'replies on LinkedIn'),
]

FAQ = [
 ('Is the cold email playbook really free?', 'Yes. Enter your work email and the 35-page PDF downloads instantly. There is no payment and no credit card. We may send you a follow-up email, and you can unsubscribe anytime.'),
 ('What is inside the playbook?', 'Seventeen chapters in six parts: funnel math, tools and costs, buying domains, Google Workspace inboxes, the exact MX, SPF, DKIM and DMARC records, redirects and tracking, a 3-week warmup schedule, a 10-minute daily health check, building and verifying lists, writing cold emails and follow-ups, launch, reply handling and booking, testing, U.S. and Canadian law, spam recovery, plus a 30-day calendar, checklists and 7 real case studies.'),
 ('Does it depend on AI tools?', 'No. Everything in the playbook is manual work you can do with Google Workspace, a domain registrar, one cold email sending platform and a verification tool. It is the same hands-on process we use for clients.'),
 ('Who wrote it?', 'Syed Ali Hassan and Syed Asim Hussain, the founders of WayneFlow, a B2B appointment setting agency. They have 8 years in digital marketing and outbound and have worked with dozens of companies, mostly in the United States and Canada.'),
 ('How long does it take to set up cold email from scratch?', 'Plan on about 30 days from a blank domain to your first booked call. Most of that time is the warmup: at least 14 days, and 21 days is safer, before real campaigns start.'),
 ('Are the numbers in the playbook real?', 'Yes. Every result comes from a real client campaign dashboard in 2026, and the screenshots are inside the PDF and on our results page. Results vary by offer, market and execution.'),
 ('Can you set it up and run it for me instead?', 'Yes. WayneFlow builds the domains, inboxes, records, warmup, lists and emails, answers the replies and books qualified buyers into your calendar. Book a free 20-minute call to see what we would do for your company.'),
]

def faq_html():
    return '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in FAQ) + '</div>'

def schema(SITE):
    url = f'{SITE}/{SLUG}'
    return {"@context": "https://schema.org", "@type": "Book", "@id": url + "#playbook", "name": "The WayneFlow Cold Email Playbook",
            "alternateName": "Free Cold Email Playbook 2026", "url": url, "bookFormat": "https://schema.org/EBook", "numberOfPages": PAGES,
            "inLanguage": "en-US", "isAccessibleForFree": True, "datePublished": "2026-10-27",
            "image": f"{SITE}/assets/img/playbook-cover.webp",
            "description": DESC,
            "about": ["Cold email", "Email deliverability", "SPF, DKIM and DMARC", "Email warmup", "B2B appointment setting", "Outbound lead generation"],
            "author": [{"@type": "Person", "name": "Syed Ali Hassan", "url": f"{SITE}/about.html#ali"},
                       {"@type": "Person", "name": "Syed Asim Hussain", "url": f"{SITE}/about.html#asim"}],
            "publisher": {"@id": f"{SITE}/#org"},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": url}}

def playbook_html(CAL, CHECK, SITE):
    toc = ''.join(
        f'<div class="pb-part reveal"><h3>{html.escape(p)}</h3>' + ''.join(
            f'<div class="pb-ch"><i>{n}</i><div><b>{html.escape(t)}</b><span>{html.escape(d)}</span></div></div>' for n, t, d in chs) + '</div>'
        for p, chs in CHAPTERS)
    cases = ''.join(
        f'<a class="pb-case reveal" href="results.html{"" if cid == "calendly" else "#" + cid}"><span class="pb-ci"><img src="assets/img/{img}-hd.webp" alt="{html.escape(label)} campaign dashboard" loading="lazy"></span>'
        f'<span class="pb-cl">{html.escape(label)}</span><b>{num}</b><span class="pb-cd">{html.escape(desc)}</span></a>' for cid, img, label, num, desc in CASES)
    return f'''<section class="phero pb-hero">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="kicker">Free download · $300 value</span>
        <h1>The free cold email playbook <span class="hl">behind $510K+ in client pipeline.</span></h1>
        <p class="lead">8 years of outbound work in {PAGES} pages. The exact manual setup we run for clients, from a blank domain to booked sales calls: domains, DNS records, warmup, lists, emails and replies. Proven with 7 real client case studies.</p>
        <div id="wl-slot" class="pb-form"></div>
        <div class="pb-trust"><span class="author-photos"><img src="assets/team/asim-sq.webp" alt="Syed Asim Hussain" width="40" height="40"><img src="assets/team/ali-sq.webp" alt="Syed Ali Hassan" width="40" height="40"></span><span>Written by <b>Ali &amp; Asim</b>, founders of WayneFlow · 8 years in outbound</span></div>
      </div>
      <div class="pb-visual" aria-hidden="true">
        <img class="pb-p pb-p3" src="assets/img/pb-page-17.webp" alt="" loading="eager">
        <img class="pb-p pb-p2" src="assets/img/pb-page-12.webp" alt="" loading="eager">
        <img class="pb-cov" src="assets/img/playbook-cover.webp" alt="" width="420" height="544" loading="eager">
        <span class="pb-chip c1"><b>{PAGES}</b> pages</span><span class="pb-chip c2"><b>7</b> case studies</span><span class="pb-chip c3"><b>17</b> chapters</span>
      </div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:clamp(20px,3vw,36px)">
  <div class="wrap">
    <div class="stats-row pb-stats reveal">
      <div><b>588,000</b><span>cold emails sent for clients</span></div>
      <div><b>12,900+</b><span>replies from buyers</span></div>
      <div><b>3,400+</b><span>buyers who asked to talk</span></div>
      <div><b>$510K+</b><span>pipeline for clients</span></div>
    </div>
    <p class="pb-note">Every number comes from a live client dashboard in 2026. Pipeline is counted at our clients&#39; average deal size of about $2,500.</p>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head"><span class="kicker">Why it is worth $300</span><h2>8 years of trial and error, <span class="hl">so you can skip it.</span></h2>
    <p class="lead">Most cold email advice is written by people who sell software. This playbook is written by people who run campaigns every day.</p></div>
    <div class="grid3 pb-why">
      <div class="card reveal"><span class="pb-ic">01</span><h3>The tricks behind real money</h3><p>The same setup, warmup and writing rules behind $510K+ in pipeline, 6 signed annual contracts and 25 calls booked in a single week.</p></div>
      <div class="card reveal"><span class="pb-ic">02</span><h3>Exact steps, not theory</h3><p>Copy-paste DNS records, a week-by-week warmup schedule, a 10-minute daily check, reply templates and a 30-day launch calendar.</p></div>
      <div class="card reveal"><span class="pb-ic">03</span><h3>Mistakes that cost weeks</h3><p>A burned domain costs about three weeks to replace. We show the mistakes we see most, so you avoid them the first time.</p></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head"><span class="kicker">A look inside</span><h2>Four pages <span class="hl">from the playbook.</span></h2><p class="lead">A small taste. The full records, schedules and templates are in the free PDF.</p></div>
    <div class="grid2 pb-peeks">
      <div class="card pb-peek reveal"><span class="pb-tag">Chapter 1 · The math</span><h3>3,200 people per booked call</h3>
        <div class="pb-funnel"><div style="width:100%">10,000 contacted</div><div style="width:82%">~138 replies</div><div style="width:62%">~14 interested</div><div style="width:44%">~3 booked calls</div></div>
        <p>That was our most average campaign. Our sharpest pilot turned 10,284 contacts into 103 opportunities. The playbook shows what made the difference.</p></div>
      <div class="card pb-peek reveal"><span class="pb-tag">Chapter 5 · DNS records</span><h3>The four records that decide inbox or spam</h3>
        <div class="pb-rec"><span>SPF</span><code>v=spf1 include:_spf.google.com ~all</code></div>
        <div class="pb-rec pb-lock"><span>DKIM</span><code>v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A</code></div>
        <div class="pb-rec pb-lock"><span>DMARC</span><code>v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com</code></div>
        <p>Plus the MX record, where to click in Google Workspace, and the two mistakes we fix for almost every new client.</p></div>
      <div class="card pb-peek reveal"><span class="pb-tag">Chapter 7 · Warmup</span><h3>The 3-week warmup schedule</h3>
        <table class="pb-tbl"><tr><th>Week</th><th>Warmup / day</th><th>Cold / day</th></tr><tr><td>1</td><td>5 → 15</td><td>0</td></tr><tr><td>2</td><td>15 → 25</td><td>0</td></tr><tr class="pb-lock"><td>3</td><td>25 → 35</td><td>0</td></tr><tr class="pb-lock"><td>4</td><td>~20 to 30</td><td>10 → 15</td></tr><tr class="pb-lock"><td>5+</td><td>keep running</td><td>up to ~30</td></tr></table>
        <p>This schedule is why one client could send 96,408 emails in 5 days with a 0.45% bounce rate.</p></div>
      <div class="card pb-peek reveal"><span class="pb-tag">Chapter 11 · The email</span><h3>The 5-part cold email under 80 words</h3>
        <div class="pb-parts"><span>Subject</span><span>First line</span><span>Problem</span><span>Proof</span><span>Ask</span></div>
        <div class="pb-mail pb-lock">Hi Mark, saw Carter Roofing is hiring two estimators ahead of storm season. Most roofing owners we talk to lose good jobs in that rush because quotes go out late...</div>
        <p>Full examples, follow-up schedule and the replies that turn "sure, tell me more" into a booked call.</p></div>
    </div>
    <div class="pb-mid"><a class="btn btn-primary" href="#top-form">Get the full playbook free</a></div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head"><span class="kicker">What is inside</span><h2>17 chapters. <span class="hl">Every step, by hand.</span></h2></div>
    <div class="pb-toc">{toc}</div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head"><span class="kicker">Proof on every few pages</span><h2>7 real case studies, <span class="hl">with the dashboards.</span></h2><p class="lead">Each one sits next to the chapter it proves. Click any card to see the live dashboard.</p></div>
    <div class="pb-cases">{cases}</div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="kicker">Who it is for</span><h2 style="margin-top:14px">Built for B2B teams <span class="hl">that sell by meeting.</span></h2>
        <div class="checks" style="margin-top:18px">
          <div>{CHECK}<span><b>Founders and agency owners</b> who want a steady flow of sales calls without paid ads.</span></div>
          <div>{CHECK}<span><b>Sales leaders</b> setting up outbound for a new SDR team.</span></div>
          <div>{CHECK}<span><b>Anyone whose cold email lands in spam</b> and wants to know exactly why.</span></div>
          <div>{CHECK}<span><b>Teams hiring an agency</b> who want to know what a good system looks like before they pay.</span></div>
        </div></div>
      <div class="card reveal pb-dfy"><span class="kicker">Rather have it done for you?</span><h3>Our experts can build and run all of it.</h3>
        <p>The playbook is the full method, and it is a lot of careful daily work. If you would rather spend your time on sales calls, our team, with 8 years in outbound, builds the system and books qualified buyers into your calendar.</p>
        <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="kicker">FAQ</span><h2 style="margin:14px 0 20px">Questions about <span class="hl">the playbook.</span></h2>{faq_html()}</div>
      <div class="card reveal pb-final" id="top-form"><img src="assets/img/playbook-cover.webp" alt="The WayneFlow Cold Email Playbook cover" width="420" height="544" loading="lazy">
        <h3>Get the playbook free</h3><p>{PAGES} pages, 7 case studies, instant download.</p><div id="wl-slot2" class="pb-form"></div></div>
    </div>
  </div>
</section>'''

PB_CSS = r'''
/* v29: playbook landing page */
.pb-hero .split{align-items:center}
.pb-form{margin-top:22px;max-width:520px}
.pb-form .wl-fine{color:var(--muted)}
.pb-trust{display:flex;align-items:center;gap:12px;margin-top:18px;font-size:14px;color:var(--muted)}
.pb-trust .author-photos img{width:40px;height:40px;border-radius:50%;border:2px solid #fff;object-fit:cover}
.pb-trust .author-photos img+img{margin-left:-12px}
.pb-visual{position:relative;height:clamp(340px,40vw,500px)}
.pb-visual img{position:absolute;height:auto;border-radius:10px;box-shadow:0 30px 60px -20px rgba(11,26,58,.45)}
.pb-cov{width:58%;left:21%;top:4%;transform:rotate(-3deg);z-index:3}
.pb-p2{width:46%;left:2%;top:16%;transform:rotate(-11deg);z-index:2;opacity:.95}
.pb-p3{width:46%;right:0;top:14%;transform:rotate(9deg);z-index:1;opacity:.95}
.pb-chip{position:absolute;z-index:4;background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:14px;color:var(--muted);box-shadow:0 12px 30px -12px rgba(11,26,58,.35)}
.pb-chip b{color:var(--blue-d);font-size:16px;margin-right:4px}
.pb-chip.c1{left:4%;bottom:12%}.pb-chip.c2{right:2%;bottom:20%}.pb-chip.c3{right:10%;top:0}
.pb-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pb-stats div{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.pb-stats b{display:block;font-size:clamp(24px,3vw,34px);color:var(--blue-d);letter-spacing:-.02em}
.pb-stats div:last-child b{color:#0E8A4B}
.pb-stats span{font-size:14px;color:var(--muted)}
.pb-note{font-size:13px;color:var(--muted);margin:10px 0 0}
.pb-why .card h3{margin:10px 0 6px}
.pb-ic{display:inline-grid;place-items:center;width:40px;height:40px;border-radius:12px;background:#EAF1FF;color:var(--blue-d);font-weight:800}
.pb-peeks{gap:18px}
.pb-peek{position:relative;overflow:hidden}
.pb-peek h3{margin:8px 0 12px}
.pb-tag{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--blue-d);background:#EAF1FF;border-radius:999px;padding:4px 10px}
.pb-funnel div{margin:0 auto 6px;background:linear-gradient(90deg,#1F6BFF,#19B4E6);color:#fff;border-radius:8px;padding:8px 12px;font-weight:700;font-size:14px;text-align:center}
.pb-rec{display:flex;gap:10px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:8px 10px;margin-bottom:8px;overflow:hidden}
.pb-rec span{flex:none;font-weight:800;font-size:13px;color:#fff;background:#0B1A3A;border-radius:6px;padding:3px 8px}
.pb-rec code{font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--text)}
.pb-lock{filter:blur(4px);user-select:none;position:relative}
.pb-tbl{width:100%;border-collapse:collapse;font-size:14px;margin-bottom:12px}
.pb-tbl th{background:#0B1A3A;color:#fff;text-align:left;padding:7px 10px}
.pb-tbl td{padding:7px 10px;border-bottom:1px solid var(--line)}
.pb-parts{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.pb-parts span{font-size:13px;font-weight:700;background:#E6F7EC;color:#0B7A42;border-radius:999px;padding:4px 10px}
.pb-mail{border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:14px;margin-bottom:12px}
.pb-peek p{font-size:14.5px;color:var(--muted);margin:0}
.pb-mid{text-align:center;margin-top:24px}
.pb-toc{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pb-part{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}
.pb-part h3{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue-d);margin:0 0 10px}
.pb-ch{display:flex;gap:10px;margin:10px 0}
.pb-ch i{flex:none;font-style:normal;width:26px;height:26px;border-radius:8px;background:#1F6BFF;color:#fff;font-weight:800;font-size:13px;display:grid;place-items:center}
.pb-ch b{display:block;font-size:15px}.pb-ch span{font-size:13.5px;color:var(--muted);line-height:1.45}
.pb-cases{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pb-case{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px;text-decoration:none;color:var(--text);transition:transform .2s,box-shadow .2s}
.pb-case:hover{transform:translateY(-3px);box-shadow:0 18px 40px -20px rgba(11,26,58,.35)}
.pb-ci{display:block;height:120px;border-radius:10px;overflow:hidden;border:1px solid var(--line);margin-bottom:10px;background:#F7F9FD}
.pb-ci{background:#fff}.pb-ci img{width:100%;height:100%;object-fit:contain;object-position:center}
.pb-cl{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--blue-d)}
.pb-case b{font-size:28px;letter-spacing:-.02em;margin:2px 0}
.pb-cd{font-size:13.5px;color:var(--muted)}
.pb-dfy h3{margin:8px 0 8px}.pb-dfy p{color:var(--muted)}
.pb-final{text-align:center}
.pb-final img{width:150px;height:auto;border-radius:8px;transform:rotate(-3deg);box-shadow:0 20px 40px -16px rgba(11,26,58,.45);margin:4px auto 14px;display:block}
.pb-final h3{margin:0 0 4px}.pb-final p{color:var(--muted);margin:0}
.pb-final .pb-form{margin:16px auto 0;text-align:left}
@media (max-width:960px){.pb-toc{grid-template-columns:1fr 1fr}.pb-cases{grid-template-columns:repeat(2,1fr)}}
@media (max-width:760px){.pb-stats{grid-template-columns:1fr 1fr}.pb-visual{height:320px;margin-top:10px}.pb-toc{grid-template-columns:1fr}}
@media (max-width:420px){.pb-cases{grid-template-columns:1fr 1fr;gap:10px}.pb-case b{font-size:22px}.pb-ci{height:90px}}
/* home page promo */
.pb-home{display:grid;grid-template-columns:auto 1fr auto;gap:clamp(18px,3vw,36px);align-items:center;background:linear-gradient(135deg,#F2F7FF,#EAF6FF);border:1px solid #D6E3FF;border-radius:var(--r);padding:clamp(20px,3vw,32px)}
.pb-home img{width:120px;height:auto;border-radius:8px;transform:rotate(-4deg);box-shadow:0 20px 40px -16px rgba(11,26,58,.45)}
.pb-home h2{margin:8px 0 6px;font-size:clamp(22px,2.6vw,30px)}
.pb-home p{margin:0;color:var(--muted)}
@media (max-width:760px){.pb-home{grid-template-columns:1fr;text-align:center}.pb-home img{margin:0 auto}}
'''

HOME_PROMO = f'''<section class="sec" id="playbook" style="padding-top:0">
  <div class="wrap"><div class="pb-home reveal"><img src="assets/img/playbook-cover.webp" alt="The WayneFlow Cold Email Playbook" width="420" height="544" loading="lazy">
    <div><span class="kicker">Free playbook · $300 value</span><h2>Steal our cold email system. <span class="hl">Free.</span></h2>
    <p>{PAGES} pages: the exact manual setup behind $510K+ in client pipeline, from domains and DNS records to warmup, emails and replies. With 7 real case studies.</p></div>
    <a class="btn btn-primary" href="{SLUG}">Get the free playbook</a></div></div>
</section>'''
