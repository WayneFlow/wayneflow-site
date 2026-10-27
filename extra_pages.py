# Extra pages: legal, service areas, 404. Imported by build8.py
import os as _os
_cn = _os.path.join(_os.environ.get('WF_OUT', '/home/claude/site8'), 'CNAME')
# the live domain comes from the CNAME file of the output folder (main branch); default is the main domain
SITE = 'https://' + (open(_cn).read().strip() if _os.path.exists(_cn) and open(_cn).read().strip() else 'wayneflow.com')
EMAIL = 'info@wayneflow.com'
UPDATED = 'October 27, 2026'

def legal_wrap(kicker, h1, intro, sections):
    toc = ''.join(f'<a href="#s{i}">{t}</a>' for i, (t, _) in enumerate(sections, 1))
    body = ''.join(f'<section id="s{i}"><h2>{i}. {t}</h2>{c}</section>' for i, (t, c) in enumerate(sections, 1))
    return f'''<section class="sec legal">
  <div class="wrap">
    <div class="legal-head"><span class="kicker">{kicker}</span><h1>{h1}</h1><p class="lead">{intro}</p><p class="fine">Last updated: {UPDATED}</p></div>
    <div class="legal-grid">
      <aside class="legal-toc"><b>On this page</b>{toc}</aside>
      <article class="legal-body">{body}</article>
    </div>
  </div>
</section>'''

P = lambda *xs: ''.join(f'<p>{x}</p>' for x in xs)
UL = lambda *xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'

# ------------------------------------------------------------------ TERMS
TERMS_SECTIONS = [
 ('Who we are and what these terms cover', P(
   'These Terms of Service ("Terms") are an agreement between you and WayneFlow ("WayneFlow", "we", "us", "our"). They apply to your use of this website and, unless a separate signed agreement says otherwise, to any services we provide to you.',
   'If you sign a proposal, order form, statement of work or service agreement with us (an "Agreement"), that Agreement controls wherever it conflicts with these Terms. By using this website, booking a call, or paying an invoice, you accept these Terms. If you are accepting on behalf of a company, you confirm you have authority to bind it.')),
 ('Our services', P(
   'We provide business-to-business outbound services such as lead research, list building, email infrastructure setup, cold email and LinkedIn outreach, reply handling and appointment setting. The exact scope, deliverables, timelines and fees are set out in your Agreement or invoice.',
   'We decide the methods, tools, sending volumes, schedules and staff we use to deliver the services. We may use contractors and third-party software to perform the work.')),
 ('Results, guarantees and case studies', P(
   'Outbound results depend on many factors outside our control, including your offer, pricing, market, sales process, response time and the decisions of the people we contact. Except for any guarantee written into a signed Agreement, we do not promise any specific number of replies, meetings, sales, revenue or return on investment.',
   'Any appointment guarantee applies only as written in your Agreement, including its definition of a "qualified" appointment, the start date, the measurement period, your obligations and the remedy. Unless your Agreement states otherwise, the only remedy under a guarantee is that we continue to work, at no extra service fee, until the guaranteed number is reached. A guarantee does not apply if you breach these Terms or your Agreement, delay approvals or onboarding, change your offer or target market, miss or fail to attend booked meetings, or pause the campaign.',
   'Case studies, screenshots, figures and reviews on this website describe real past campaigns. They are not typical, they are not a promise, and your results will vary. "Pipeline" figures are the estimated value of qualified opportunities created, not revenue received.')),
 ('Your responsibilities', UL(
   'Give us accurate information about your business, offer and ideal customer, and respond to requests for approvals and information within 2 business days.',
   'Review and approve all outreach copy, offers and claims before launch. You are responsible for the truth of everything we say on your behalf based on information you give us.',
   'Attend booked meetings, follow up with prospects and run your own sales process.',
   'Make sure your products, services and claims comply with the laws that apply to your business.',
   'Not ask us to contact anyone on a list you know is unlawful to use, or to send content that is false, misleading, harassing or infringing.')),
 ('Fees, payment and no refunds', P(
   'Fees are as stated in your Agreement or invoice and are payable in advance in US dollars, unless agreed otherwise in writing. Setup fees, tools, domains, inboxes and data costs are non-refundable once work has started.',
   'All fees paid are non-refundable, including for partial months, unless your signed Agreement expressly says otherwise. If a payment is more than 5 days late we may pause the services until it is paid, and late amounts may accrue interest at 1.5% per month or the highest rate allowed by law, whichever is lower. You are responsible for all taxes other than taxes on our income.',
   'You agree not to dispute or charge back a valid payment. If you believe an invoice is wrong, email us within 14 days of the invoice date and we will work with you in good faith.')),
 ('Term, cancellation and pausing', P(
   'Unless your Agreement says otherwise, services renew month to month. Either party may cancel with 30 days\' written notice to ' + EMAIL + '. Fees for the notice period remain due. Any minimum term in your Agreement must be completed before cancellation takes effect.',
   'We may suspend or end the services immediately if you breach these Terms, fail to pay, or ask us to do something we reasonably believe is unlawful or harmful to our sending reputation.')),
 ('Outreach compliance', P(
   'We run outreach to business contacts and design campaigns to follow the U.S. CAN-SPAM Act, including accurate sender details, honest subject lines, a working opt-out in every email and prompt handling of opt-out requests. We use separate sending domains so your main domain is not put at risk.',
   'You agree that compliance with laws specific to your industry, your offer and your own website and sales process is your responsibility. If you instruct us to contact people in other countries, you are responsible for confirming that the outreach is lawful there.')),
 ('Intellectual property and confidentiality', P(
   'You own your company data, brand and the leads and meetings delivered to you. We own our methods, templates, processes, software setups, playbooks and know-how, including anything we create that is not specific to you. We grant you a license to use the outreach copy written for you for your own business.',
   'Each party will keep the other\'s non-public business information confidential and use it only to perform or receive the services. You agree that we may name you as a client and use anonymized campaign figures and screenshots in our marketing, unless you ask us not to in writing.')),
 ('Non-solicitation', P(
   'During the services and for 12 months afterwards, you agree not to directly hire, engage or solicit any of our employees or contractors who worked on your account without our written consent. If you do, you agree to pay us a placement fee equal to 6 months of that person\'s compensation as a reasonable estimate of our loss.')),
 ('Disclaimer of warranties', P(
   'EXCEPT AS EXPRESSLY STATED IN A SIGNED AGREEMENT, THE WEBSITE AND SERVICES ARE PROVIDED "AS IS" AND "AS AVAILABLE". TO THE FULLEST EXTENT ALLOWED BY LAW, WE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT AND ANY WARRANTY THAT EMAILS WILL BE DELIVERED, OPENED OR ANSWERED.')),
 ('Limitation of liability', P(
   'TO THE FULLEST EXTENT ALLOWED BY LAW, WE WILL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR PUNITIVE DAMAGES, OR FOR LOST PROFITS, REVENUE, DEALS, DATA OR GOODWILL, EVEN IF WE WERE TOLD THEY WERE POSSIBLE.',
   'OUR TOTAL LIABILITY FOR ALL CLAIMS RELATING TO THE WEBSITE OR SERVICES IS LIMITED TO THE FEES YOU PAID US IN THE 3 MONTHS BEFORE THE EVENT THAT GAVE RISE TO THE CLAIM. ANY CLAIM MUST BE BROUGHT WITHIN 1 YEAR AFTER IT AROSE.')),
 ('Indemnity', P(
   'You will defend, indemnify and hold harmless WayneFlow and its owners, staff and contractors from any claims, losses, fines and costs (including reasonable attorneys\' fees) arising from your products or services, the information, lists or claims you provided or approved, your breach of these Terms or your Agreement, or your violation of any law.')),
 ('Disputes, arbitration and class action waiver', P(
   'Please contact us first at ' + EMAIL + '; most issues can be solved quickly. If we cannot resolve a dispute within 30 days, it will be resolved by final and binding arbitration administered by the American Arbitration Association under its Commercial Arbitration Rules, by a single arbitrator, held remotely by video unless both parties agree otherwise. Judgment on the award may be entered in any court with jurisdiction. Either party may seek urgent injunctive relief in court to protect confidential information or intellectual property, and we may bring a claim to collect unpaid fees in any court with jurisdiction.',
   'ALL CLAIMS MUST BE BROUGHT IN AN INDIVIDUAL CAPACITY, NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY CLASS, CONSOLIDATED OR REPRESENTATIVE PROCEEDING. YOU WAIVE ANY RIGHT TO A JURY TRIAL.')),
 ('Governing law', P(
   'These Terms and any Agreement are governed by the laws of the State of Delaware, USA, without regard to its conflict of law rules, and the Federal Arbitration Act.')),
 ('General', P(
   'We may update these Terms by posting a new version on this page; continued use of the website or services means you accept the update. These Terms and your Agreement are the entire agreement between us on this subject. If any part is found unenforceable, the rest remains in effect. Our failure to enforce a provision is not a waiver. You may not assign these Terms without our written consent; we may assign them to an affiliate or successor. Neither party is liable for delays caused by events beyond its reasonable control.',
   'Questions? Email <a href="mailto:' + EMAIL + '">' + EMAIL + '</a>, or the fastest way: <a href="{CAL}" target="_blank" rel="noopener">book a call</a>.')),
]

# ------------------------------------------------------------------ PRIVACY
PRIVACY_SECTIONS = [
 ('Summary', UL(
   'We collect only what we need to run this website, book calls and deliver our services.',
   'We do not sell personal information, and we do not share it for cross-context behavioral advertising.',
   'You can ask us to access, correct or delete your information, or to stop contacting you, at any time by emailing ' + EMAIL + '.')),
 ('Information we collect', '<p><b>Information you give us.</b> Your name, business email, company, phone number and anything you write when you book a call through Calendly, email us or become a client.</p><p><b>Information collected automatically.</b> When you visit the site, our analytics tool (PostHog) records pages viewed, clicks on booking buttons, approximate location from your IP address, device and browser type, and referring site. This uses cookies or similar browser storage.</p><p><b>Business contact information for outreach.</b> To run campaigns for our clients we process professional contact details, such as name, job title, company, business email and public LinkedIn profile, obtained from public sources and licensed B2B data providers.</p>'),
 ('How we use information', UL(
   'To schedule and hold calls, reply to you and provide our services.',
   'To run business-to-business outreach campaigns for our clients and handle replies and opt-outs.',
   'To understand how the website is used and improve it.',
   'To send invoices, keep records and meet legal, tax and accounting duties.',
   'To protect our rights, prevent fraud and enforce our Terms.')),
 ('How we share information', P(
   'We share information only with service providers that help us operate, such as Calendly (scheduling), PostHog (analytics), GitHub (website hosting), Google Workspace (email), email-sending and data platforms, and payment processors. They may use it only to provide services to us.',
   'For client campaigns, we share prospect replies and booked meetings with the client that the outreach was for. We may also disclose information if required by law, to protect our rights, or as part of a merger, acquisition or sale of our business.',
   'We do not sell personal information and we do not "share" it for targeted advertising as those terms are defined under California law.')),
 ('Cookies and analytics', P(
   'We use PostHog analytics and our own first-party code to understand how people find and use this website. This includes how you arrived (for example a search engine, an AI assistant, a social network, a marketplace profile, an ad or a direct visit, including any campaign tags in the link), the pages you view, how far you scroll, how long you stay, which buttons and links you click, and general device, browser and approximate location data (derived from your IP address).',
   'To understand which businesses visit, your IP address is checked once against a public IP database (IPinfo, or ipapi as a backup) to see the name of the network or company it belongs to. We store that network name, not your IP address, and use it to follow up with businesses that show interest. If you download our free playbook or subscribe to our newsletter, the email you enter is saved with your visit history, time zone, device and approximate location so we can send the file and follow up; you can opt out anytime. We call or text a phone number only if you gave it to us with consent, and you can reply STOP to opt out.',
   'We also record anonymized session replays and heatmaps to improve the site. Text you type into fields is masked and is not recorded. When you click a booking link we pass the traffic source to Calendly, so we know which channel a booked call came from.',
   'This data is stored with PostHog in the United States and kept only as long as we need it to run and improve our marketing. We honor the "Do Not Track" setting in your browser: when it is on, our analytics do not run. You can also block or delete cookies and local storage in your browser settings; the site will still work.')),
 ('Email outreach and opting out', P(
   'If you received a cold email from us or on behalf of one of our clients, it was sent to a business address for a business purpose. Every email includes a way to opt out. You can also email ' + EMAIL + ' with the subject "Remove me" and we will add your address to our suppression list within 10 business days and stop all further outreach from us.')),
 ('Your privacy rights by state', '<p>Depending on where you live, including California, Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana, Iowa, Delaware, New Hampshire, New Jersey, Nebraska, Tennessee, Minnesota, Maryland, Indiana, Kentucky and Rhode Island, you may have the right to:</p>' + UL(
   'Know what personal information we hold about you and get a copy.',
   'Correct inaccurate information.',
   'Delete your information.',
   'Opt out of the sale of personal information, targeted advertising and profiling (we do none of these).',
   'Not be discriminated against for using your rights.') + P(
   'To make a request, email ' + EMAIL + ' with the subject "Privacy request". We will verify your request using information we already hold, and we will respond within the time required by your state\'s law, usually 45 days. An authorized agent may make a request for you with your written permission. If we deny your request, you may appeal by replying to our decision, and we will respond to the appeal within the time the law requires.')),
 ('How long we keep information', P(
   'We keep information only as long as we need it for the purposes above. Booking and client records are kept for the length of the relationship plus up to 7 years for legal and tax reasons. Opt-out records are kept permanently so we never contact you again.')),
 ('Security', P(
   'We use reasonable administrative, technical and physical safeguards, including encrypted connections (HTTPS) and access controls. No method of transmission or storage is completely secure, so we cannot guarantee absolute security.')),
 ('Children', P(
   'Our website and services are for businesses. They are not directed to anyone under 16, and we do not knowingly collect information from children.')),
 ('International visitors', P(
   'We are a business serving U.S. companies. If you visit from outside the United States, your information may be processed in the United States and other countries where our providers operate.')),
 ('Changes and contact', P(
   'We may update this policy by posting a new version here with a new "Last updated" date. Questions or requests: <a href="mailto:' + EMAIL + '">' + EMAIL + '</a>.')),
]

# ------------------------------------------------------------------ SERVICE AREAS (all 50 states)
REGIONS = [
 ('Northeast', 'Eastern Time', ['Connecticut','Maine','Massachusetts','New Hampshire','New Jersey','New York','Pennsylvania','Rhode Island','Vermont'],
  'Dense with agencies, SaaS, finance and professional services firms. Buyers here expect short, direct emails and fast follow-up.'),
 ('Southeast', 'Eastern and Central Time', ['Alabama','Delaware','Florida','Georgia','Kentucky','Maryland','Mississippi','North Carolina','South Carolina','Tennessee','Virginia','West Virginia'],
  'Fast-growing markets for construction, logistics, healthcare services and B2B services, from Atlanta and Charlotte to Miami, Tampa and Nashville.'),
 ('Midwest', 'Central and Eastern Time', ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin'],
  'Manufacturing, industrial, insurance and B2B software buyers who value plain language and proof over hype.'),
 ('Southwest', 'Central and Mountain Time', ['Arizona','New Mexico','Oklahoma','Texas'],
  'Texas alone is one of the largest B2B markets in the country. Energy, construction, real estate and tech buyers across Dallas, Houston, Austin and Phoenix.'),
 ('West', 'Pacific and Mountain Time', ['California','Colorado','Idaho','Montana','Nevada','Oregon','Utah','Washington','Wyoming'],
  'Tech, SaaS, venture-backed startups and investors. We send on Pacific hours so emails land at the top of the inbox in the morning.'),
 ('Alaska and Hawaii', 'Alaska and Hawaii Time', ['Alaska','Hawaii'],
  'Smaller markets we still cover properly, with send times set to local business hours.'),
]

def areas_html(CAL, CHECK):
    blocks = ''.join(f'''<div class="card region reveal"><div class="rhead"><h3>{n}</h3><span class="tz">{tz}</span></div><p>{d}</p><ul class="states">{"".join(f"<li>{s}</li>" for s in st)}</ul></div>''' for n, tz, st, d in REGIONS)
    return f'''<section class="sec">
  <div class="wrap">
    <div class="split top">
      <div><span class="kicker">Service areas · all 50 states</span><h1>B2B appointment setting for companies <span class="hl">across the United States.</span></h1>
      <p class="lead">We book qualified sales appointments for B2B companies in every U.S. state, from New York to California, Texas to Florida. Everything is done remotely, so where you are based does not matter. What matters is where your buyers are, and we reach them in their own time zone.</p>
      <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a><a class="btn btn-secondary" href="results.html">See the results</a></div></div>
      <div class="card reveal"><h2 class="h3like" style="margin-bottom:12px">How we cover the whole country</h2><div class="checks">
        <div>{CHECK}Emails go out on weekdays during business hours in each prospect's time zone: Eastern, Central, Mountain, Pacific, Alaska and Hawaii.</div>
        <div>{CHECK}Lists are built by state, metro area, industry and job title, so your campaign targets exactly the regions you sell to.</div>
        <div>{CHECK}Meetings are booked straight into your calendar in your own time zone, with no back-and-forth emails.</div>
        <div>{CHECK}We follow the U.S. CAN-SPAM Act on every campaign: real sender details, honest subject lines and a working opt-out.</div>
      </div></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal"><span class="kicker">Every region, every state</span><h2>Where we book <span class="hl">sales appointments.</span></h2></div>
    <div class="grid3 regions">{blocks}</div>
    <p class="fine" style="margin-top:18px">Also available for Washington, D.C. Selling into Canada? See our <a href="canada.html">CASL-aware lead generation for Canada</a>.</p>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="kicker">Who we help</span><h2 style="margin-top:14px">Built for B2B companies <span class="hl">that sell high-value services.</span></h2><p class="lead">Marketing and creative agencies, B2B SaaS and software, construction technology, consulting and professional services, IT and managed services, staffing and recruiting, and founder and investor outreach.</p></div>
      <div class="faq reveal">
        <details><summary>Do you work with companies in my state?</summary><p>Yes. We work with B2B companies in all 50 states. The work is fully remote, and campaigns are set to your buyers' local business hours.</p></details>
        <details><summary>Can you target only one state or city?</summary><p>Yes. We can build lists for a single state, a few metro areas or the whole country, depending on where you sell.</p></details>
        <details><summary>Is cold email legal in the United States?</summary><p>Yes. B2B cold email is legal in the U.S. when it follows the CAN-SPAM Act: accurate sender information, honest subject lines and a clear way to opt out. We build every campaign around these rules.</p></details>
      </div>
    </div>
  </div>
</section>'''

AREA_FAQ = [
 ('Do you work with companies in my state?', 'Yes. We work with B2B companies in all 50 states. The work is fully remote, and campaigns are set to your buyers\' local business hours.'),
 ('Can you target only one state or city?', 'Yes. We can build lists for a single state, a few metro areas or the whole country, depending on where you sell.'),
 ('Is cold email legal in the United States?', 'Yes. B2B cold email is legal in the U.S. when it follows the CAN-SPAM Act: accurate sender information, honest subject lines and a clear way to opt out. We build every campaign around these rules.'),
]
ALL_STATES = sorted(s for _, _, st, _ in REGIONS for s in st)

NOTFOUND = '''<section class="sec" style="min-height:60vh;display:grid;place-items:center;text-align:center">
  <div class="wrap"><span class="kicker">Error 404</span><h1 style="margin-top:14px">This page took a <span class="hl">wrong turn.</span></h1>
  <p class="lead" style="margin-inline:auto">The page you are looking for does not exist or has moved.</p>
  <div class="ctas" style="justify-content:center"><a class="btn btn-primary" href="/">Go to the home page</a><a class="btn btn-secondary" href="/results.html">See our results</a></div></div>
</section>'''

# ------------------------------------------------------------------ ABOUT + PRICING
LI_COMPANY = 'https://www.linkedin.com/company/135164941'
INSTAGRAM = 'https://www.instagram.com/wayneflowagency/'
UPWORK = 'https://www.upwork.com/freelancers/~012a23cf646bb4fe7d'
FIVERR = 'https://www.fiverr.com/s/vbbpjRq'
ASIM_LI = 'https://www.linkedin.com/in/asim-wayneflow/'
ALI_WA = 'https://wa.me/923318159967'
SETUP, MONTHLY = 999, 1500

def about_html(CAL, CHECK):
    return f'''<section class="sec">
  <div class="wrap">
    <div class="split">
      <div><span class="kicker">About WayneFlow</span><h1>Two founders. <span class="hl">One job: fill your calendar.</span></h1>
      <p class="lead">WayneFlow is a B2B appointment setting and cold email agency founded by Syed Asim Hussain and Syed Ali Hassan. Together we have 8 years in digital marketing and outbound, and we have worked with dozens of companies, mostly in the United States and Canada. Today we build and run outbound systems that book qualified sales appointments, and we publish our real dashboards so you can judge the work before you talk to us.</p>
      <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a call with us</a><a class="btn btn-secondary" href="results.html">See our live results</a></div></div>
      <div class="team-photo"><img src="assets/team/founders.webp" width="900" height="900" alt="WayneFlow founders Syed Asim Hussain (left) and Syed Ali Hassan (right)" loading="eager"></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="head"><span class="kicker">The founders</span><h2>The people <span class="hl">behind your campaigns.</span></h2></div>
    <div class="grid2 founders">
      <article class="card founder" id="asim"><img src="assets/team/asim.webp" width="800" height="1000" alt="Syed Asim Hussain, co-founder of WayneFlow" loading="lazy">
        <div><h3>Syed Asim Hussain</h3><span class="role">Co-founder, WayneFlow</span>
        <p>Asim has spent 8 years in digital marketing and outbound sales systems. He works with clients on targeting, offers and campaign strategy, and the strategy call on this site books time directly with him. Together with Ali, he has worked with dozens of companies and helped build brands for clients around the world, most of them in the United States and Canada.</p>
        <div class="flinks"><a href="{ASIM_LI}" target="_blank" rel="noopener">LinkedIn</a><a href="{CAL}" target="_blank" rel="noopener">Book a call with Asim</a></div></div></article>
      <article class="card founder" id="ali"><img src="assets/team/ali.webp" width="800" height="1000" alt="Syed Ali Hassan, co-founder of WayneFlow" loading="lazy">
        <div><h3>Syed Ali Hassan</h3><span class="role">Co-founder, WayneFlow</span>
        <p>Ali has 8 years of experience in digital marketing and outbound, running cold email and LinkedIn lead generation for B2B clients. At WayneFlow he owns the engine itself: lists, sending infrastructure, deliverability and the systems that turn replies into booked meetings. Most of his clients are in the United States and Canada.</p>
        <div class="flinks"><a href="{ALI_WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{CAL}" target="_blank" rel="noopener">Book a call with Ali</a></div></div></article>
    </div>
    {story_html(CAL, 'results.html')}
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div><span class="kicker">What we believe</span><h2 style="margin-top:14px">How we <span class="hl">work.</span></h2>
        <p class="lead">Outbound only works long term if it protects your reputation and respects the people you contact. These rules are part of every campaign.</p></div>
      <div class="card"><div class="checks">
        <div>{CHECK}<span><b>Proof before promises.</b> Every number on this site is a live screenshot from a real campaign.</span></div>
        <div>{CHECK}<span><b>Your domain stays safe.</b> We send from separate domains, never from your main one.</span></div>
        <div>{CHECK}<span><b>Replies over vanity metrics.</b> Open tracking is off on purpose. We measure replies and booked calls.</span></div>
        <div>{CHECK}<span><b>Compliant by default.</b> CAN-SPAM in the U.S., CASL-aware in Canada, an opt-out in every email.</span></div>
        <div>{CHECK}<span><b>Skin in the game.</b> Once your campaign is live, we guarantee 25 qualified appointments a month.</span></div>
      </div></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap"><div class="band"><div><h2>Follow our work</h2><p>Campaign breakdowns, cold email tips, new results and client reviews.</p></div>
  <div class="ctas" style="margin:0"><a class="btn" href="{LI_COMPANY}" target="_blank" rel="noopener">LinkedIn</a><a class="btn" href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><a class="btn" href="{UPWORK}" target="_blank" rel="noopener">Upwork</a><a class="btn" href="{FIVERR}" target="_blank" rel="noopener">Fiverr</a></div></div></div>
</section>'''

def pricing_html(CAL, CHECK):
    year1 = SETUP + 12*MONTHLY
    return f'''<section class="sec">
  <div class="wrap">
    <div class="head" style="max-width:820px"><span class="kicker">Pricing</span><h1>Simple pricing for a <span class="hl">full outbound system.</span></h1>
    <p class="lead">WayneFlow costs a one-time ${SETUP:,} setup fee and ${MONTHLY:,} a month. That covers the full done-for-you outbound system: cold email, LinkedIn and X outreach, reply handling and booking. Once your campaign is live, we guarantee 25 qualified sales appointments a month.</p></div>
    <div class="price-grid">
      <div class="card price-card">
        <span class="tag">One-time</span><h2>Setup</h2><div class="price">${SETUP:,}</div><p class="fine">Paid once, before we start.</p>
        <div class="checks">
          <div>{CHECK}Ideal customer profile and offer workshop</div>
          <div>{CHECK}Separate sending domains and inboxes</div>
          <div>{CHECK}SPF, DKIM and DMARC authentication</div>
          <div>{CHECK}Inbox warmup before launch</div>
          <div>{CHECK}First verified prospect lists</div>
          <div>{CHECK}Email sequences written and approved by you</div>
        </div>
      </div>
      <div class="card price-card featured">
        <span class="tag">Monthly retainer</span><h2>Full outbound system</h2><div class="price">${MONTHLY:,}<small>/month</small></div><p class="fine">Billed monthly in advance, in USD.</p>
        <div class="checks">
          <div>{CHECK}Cold email campaigns, sent daily in your buyers' time zones</div>
          <div>{CHECK}LinkedIn and X outreach</div>
          <div>{CHECK}New verified leads every month</div>
          <div>{CHECK}Reply handling and follow-ups</div>
          <div>{CHECK}Qualified meetings booked into your calendar</div>
          <div>{CHECK}Ongoing testing of angles, offers and copy</div>
          <div>{CHECK}Reporting with live dashboards</div>
          <div>{CHECK}<b>Guarantee: 25 qualified appointments a month once live</b></div>
        </div>
        <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener" style="margin-top:20px;width:100%;justify-content:center">Book a 20-minute call</a>
      </div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div><span class="kicker">The math</span><h2 style="margin-top:14px">What a booked meeting <span class="hl">really costs.</span></h2>
      <p class="lead">At the guaranteed minimum of 25 qualified appointments, the monthly retainer works out to about <b>${MONTHLY//25} per qualified appointment</b>. Year one costs ${year1:,} in total, setup included.</p>
      <p class="lead">For comparison, our <a href="blog/outsourced-appointment-setting-vs-in-house-sdr.html">in-house SDR cost breakdown</a> puts one fully loaded U.S. sales development rep at roughly $114,000 to $123,000 in year one, or about $1,170 to $1,550 per held meeting, using published salary and benefits data.</p></div>
      <div class="card"><table class="ptable"><thead><tr><th></th><th>WayneFlow</th><th>In-house SDR (year one)</th></tr></thead><tbody>
        <tr><td>Year one cost</td><td><b>${year1:,}</b></td><td>$114,000 to $123,000</td></tr>
        <tr><td>Cost per meeting</td><td><b>about ${MONTHLY//25}</b> at 25/month</td><td>about $1,170 to $1,550</td></tr>
        <tr><td>Time to launch</td><td>about 3 weeks</td><td>hiring plus about 3 months ramp</td></tr>
        <tr><td>Domains, inboxes, tools</td><td>set up for you</td><td>you buy and manage them</td></tr>
        <tr><td>Guarantee</td><td>25 qualified appointments a month</td><td>none</td></tr>
      </tbody></table><p class="fine" style="margin-top:10px">SDR figures from our cost guide, which cites the Bridge Group, BLS and vendor pricing pages.</p></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div><span class="kicker">Pricing FAQ</span><h2 style="margin-top:14px">Questions about <span class="hl">cost.</span></h2></div>
      <div class="faq">
        {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in PRICING_FAQ)}
      </div>
    </div>
  </div>
</section>'''

PRICING_FAQ = [
 ('How much does WayneFlow cost?', f'A one-time setup fee of ${SETUP:,} and a monthly retainer of ${MONTHLY:,}. The retainer covers the full outbound system: cold email, LinkedIn and X outreach, reply handling and booking qualified meetings into your calendar.'),
 ('What does the setup fee cover?', 'Everything needed before the first email goes out: your ideal customer profile and offer, separate sending domains and inboxes, email authentication (SPF, DKIM, DMARC), inbox warmup, your first verified prospect lists and the email sequences you approve.'),
 ('Is there an appointment guarantee?', 'Yes. Once your campaign is live, we guarantee a minimum of 25 qualified sales appointments a month. The definition of a qualified appointment and how the guarantee works for your market are written into your agreement, and we walk you through them on the strategy call.'),
 ('How soon do appointments start?', 'Setup and inbox warmup take about three weeks. Replies usually start in the first week after launch. In one campaign we booked 25 calls inside a single week of sending.'),
 ('Is LinkedIn or X outreach extra?', 'No. The monthly retainer is the full outbound system. Depending on where your buyers are, it can include cold email, LinkedIn and X outreach.'),
 ('Do you work with Canadian companies, and what currency do you bill in?', 'Yes. We work with companies across the United States and Canada. Prices are in U.S. dollars, and Canadian campaigns are run with CASL in mind.'),
]

def story_html(CAL, cases_href='results.html', heading=True):
    steps = [
      ('2018', 'Two cousins, one laptop', 'We grew up together in Pakistan with no network, no investors and no clients. Just a laptop, a slow connection and a feeling that the internet could take us further than our street could.'),
      ('The hard years', 'We failed. A lot.', 'Our first campaigns went straight to spam. We burned domains, wrote emails nobody answered and had months with zero replies. More than once we asked each other if we should quit.'),
      ('The turn', 'We stopped guessing', 'We started measuring everything: verified lists, separate sending domains, short emails about the buyer’s problem, every reply tracked. Replies came. Then meetings. Then clients who stayed.'),
      ('Today', 'Eight years later', 'Dozens of companies helped, most of them in the USA and Canada. This year alone: 588,000 emails, 12,900+ replies and more than $510K in pipeline for our clients.'),
    ]
    items = ''.join(f'<li class="st-step"><span class="st-dot"></span><span class="st-when">{w}</span><b>{t}</b><p>{p}</p></li>' for w, t, p in steps)
    head = ('<div class="st-head"><span class="kicker">Our story</span><h2>From the streets of Pakistan to <span class="hl">$510K+ in client pipeline.</span></h2></div>' if heading else '')
    return f'''<div class="story-block reveal" id="our-story">{head}
      <ol class="st-line">{items}</ol>
      <div class="st-end"><p class="st-quote">&ldquo;We know what an empty calendar feels like. That is why we built a system that fills yours.&rdquo;<span>Ali &amp; Asim</span></p>
        <div class="ctas"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a call with Ali &amp; Asim</a><a class="btn btn-secondary" href="{cases_href}">See the case studies</a></div></div>
    </div>'''
