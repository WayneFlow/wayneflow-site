"""WayneFlow Cold Email Playbook: the free lead magnet PDF.
Builds cover.html + body.html, renders both with Chromium, merges into one PDF."""
import asyncio, html, sys
from pathlib import Path
sys.path.insert(0, '/home/claude')
HERE = Path(__file__).parent
A = 'file:///home/claude/site8/assets'
CAL = 'https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers'
def cal(src): return f'{CAL}?utm_source=playbook&amp;utm_medium=pdf&amp;utm_campaign={src}'
SITE = 'https://wayne-flow.site'

CSS = r'''
@page { size: Letter; margin: .62in .68in .72in }
* { box-sizing: border-box }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact }
body { margin: 0; font-family: Inter, sans-serif; color: #0B1A3A; font-size: 11pt; line-height: 1.55 }
h1, h2, h3, h4 { font-family: 'Inter Display', Inter, sans-serif; letter-spacing: -.02em; line-height: 1.15; break-after: avoid }
h2 { font-size: 19pt; margin: 26px 0 8px }
h3 { font-size: 13.5pt; margin: 20px 0 6px }
p { margin: 0 0 10px; color: #26334D }
ul, ol { margin: 0 0 12px; padding-left: 20px; color: #26334D }
li { margin: 4px 0 }
b, strong { color: #0B1A3A }
a { color: #1556D6 }
code, .mono { font-family: 'DejaVu Sans Mono', Menlo, monospace; font-size: 9.6pt }
code { background: #EEF3FC; padding: 1px 5px; border-radius: 4px; color: #0B1A3A }
.chap { break-before: page; margin: 0 0 18px; }
.chap .num { font-size: 10pt; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; color: #1F6BFF }
.chap h1 { font-size: 30pt; margin: 6px 0 10px; font-weight: 800 }
.chap .lead { font-size: 13pt; color: #3E4C66; line-height: 1.5; border-left: 4px solid #1F6BFF; padding-left: 14px; margin: 0 0 6px }
.part { break-before: page; height: 9.3in; display: flex; flex-direction: column; justify-content: center; background: linear-gradient(160deg,#0B1A3A,#12306E 70%,#1F6BFF 140%); color: #fff; border-radius: 22px; padding: 0 .6in }
.part .pk { font-size: 11pt; letter-spacing: .2em; text-transform: uppercase; color: #8FB6FF; font-weight: 800 }
.part h1 { font-size: 40pt; margin: 10px 0 14px; color: #fff; font-weight: 800 }
.part p { color: #CFE0FF; font-size: 13.5pt; max-width: 32em }
.part ol { color: #fff; font-size: 12.5pt; margin-top: 18px }
.box { border-radius: 12px; padding: 13px 16px; margin: 14px 0; break-inside: avoid }
.box .bt { display: block; font-size: 8.8pt; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 4px }
.box p:last-child, .box ul:last-child { margin-bottom: 0 }
.proof { background: #EEF4FF; border-left: 5px solid #1F6BFF } .proof .bt { color: #1556D6 }
.tip { background: #FFF7E3; border-left: 5px solid #F2A900 } .tip .bt { color: #9A6A00 }
.warn { background: #FFEDEE; border-left: 5px solid #E0384B } .warn .bt { color: #B4192B }
.real { background: #E9F7EF; border-left: 5px solid #0E8A4B } .real .bt { color: #0B6E3C }
table { width: 100%; border-collapse: collapse; margin: 10px 0 14px; font-size: 10pt; break-inside: avoid }
th { background: #0B1A3A; color: #fff; text-align: left; padding: 7px 9px; font-weight: 700 }
td { padding: 7px 9px; border-bottom: 1px solid #E3E9F5; vertical-align: top; color: #26334D }
tr:nth-child(even) td { background: #F7F9FD }
.dns { border: 1px solid #D8E2F3; border-radius: 12px; overflow: hidden; margin: 12px 0; break-inside: avoid }
.dns .dh { background: #0B1A3A; color: #fff; padding: 8px 14px; font-weight: 800; font-size: 10.5pt; display: flex; justify-content: space-between }
.dns .dh span { color: #8FB6FF; font-weight: 600 }
.dns table { margin: 0 } .dns td:first-child { width: 22%; font-weight: 700; color: #0B1A3A }
.dns .what { padding: 9px 14px; font-size: 10pt; background: #F7F9FD; color: #3E4C66 }
.steps { counter-reset: s; list-style: none; padding: 0 }
.steps > li { counter-increment: s; position: relative; padding: 2px 0 6px 40px; margin: 6px 0 }
.steps > li::before { content: counter(s); position: absolute; left: 0; top: 0; width: 27px; height: 27px; border-radius: 8px; background: #1F6BFF; color: #fff; font-weight: 800; display: grid; place-items: center; font-size: 10.5pt }
.check { list-style: none; padding: 0 } .check li { padding-left: 26px; position: relative; margin: 6px 0 }
.check li::before { content: ''; position: absolute; left: 0; top: 3px; width: 14px; height: 14px; border: 2px solid #1F6BFF; border-radius: 4px }
.email { border: 1px solid #D8E2F3; border-radius: 12px; margin: 12px 0; break-inside: avoid; background: #fff; box-shadow: 0 2px 0 #EEF3FC }
.email .eh { border-bottom: 1px solid #E3E9F5; padding: 8px 14px; font-size: 9.8pt; color: #5B6B85 }
.email .eh b { color: #0B1A3A }
.email .eb { padding: 12px 14px; font-size: 10.6pt; white-space: pre-line; color: #0B1A3A; line-height: 1.55 }
.email .en { padding: 8px 14px; background: #F7F9FD; font-size: 9.4pt; color: #3E4C66; border-top: 1px solid #E3E9F5 }
.stats { display: grid; grid-template-columns: repeat(4,1fr); gap: 8px; margin: 10px 0; break-inside: avoid }
.stats div { background: #fff; border: 1px solid #D8E2F3; border-radius: 10px; padding: 8px 10px }
.stats b { display: block; font-size: 15pt; color: #1F6BFF } .stats span { font-size: 8.8pt; color: #5B6B85; line-height: 1.3; display: block }
.stats div:last-child b { color: #0E8A4B }
.shot { border: 1px solid #D8E2F3; border-radius: 12px; overflow: hidden; margin: 12px 0 4px; break-inside: avoid }
.shot img { width: 100%; height: 2.6in; object-fit: cover; object-position: top; display: block }
.cap { font-size: 9pt; color: #5B6B85; margin: 0 0 14px }
.cta { break-inside: avoid; margin: 22px 0; border-radius: 18px; padding: 22px 24px; color: #fff; background: linear-gradient(120deg,#0B1A3A 0%,#1F4FBF 60%,#1F6BFF 100%); display: flex; gap: 18px; align-items: center }
.cta .ct { flex: 1 } .cta .ck { font-size: 8.8pt; letter-spacing: .16em; text-transform: uppercase; font-weight: 800; color: #8FD8FF }
.cta h3 { color: #fff; font-size: 16pt; margin: 4px 0 6px } .cta p { color: #D7E4FF; margin: 0; font-size: 10.5pt }
.cta a.btn { flex: none; background: #fff; color: #1556D6; font-weight: 800; text-decoration: none; padding: 12px 18px; border-radius: 11px; font-size: 11pt; white-space: nowrap }
.faces { display: flex } .faces img { width: 46px; height: 46px; border-radius: 50%; border: 2px solid #fff; object-fit: cover } .faces img + img { margin-left: -16px }
.toc { columns: 2; column-gap: 28px; font-size: 10.6pt; margin-top: 8px }
.toc div { break-inside: avoid; margin: 0 0 6px; display: flex; gap: 8px } .toc i { font-style: normal; color: #1F6BFF; font-weight: 800; width: 20px; flex: none }
.toc .tp { font-size: 8.8pt; letter-spacing: .14em; text-transform: uppercase; color: #8A97AE; font-weight: 800; margin-top: 8px }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 10px 0 } .grid2 > div { border: 1px solid #D8E2F3; border-radius: 12px; padding: 12px 14px; break-inside: avoid }
.grid2 h4 { margin: 0 0 4px; font-size: 11.5pt } .grid2 p { font-size: 10pt; margin: 0 }
.funnel { margin: 12px 0; break-inside: avoid }
.funnel div { margin: 0 auto 5px; background: linear-gradient(90deg,#1F6BFF,#19B4E6); color: #fff; border-radius: 8px; padding: 7px 14px; display: flex; justify-content: space-between; font-weight: 700; font-size: 10.5pt }
.funnel div span { font-weight: 500; color: #E3EEFF }
.pill { display: inline-block; background: #E9F7EF; color: #0B6E3C; border-radius: 99px; padding: 1px 9px; font-size: 9pt; font-weight: 700 }
.pill.r { background: #FFEDEE; color: #B4192B } .pill.y { background: #FFF7E3; color: #9A6A00 }
.small { font-size: 9.4pt; color: #5B6B85 }
.final h1 { font-size: 28pt }
.choice { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 10px 0 } .choice li { margin: 2px 0 }
.choice > div { border-radius: 16px; padding: 14px 16px; font-size: 10.2pt; break-inside: avoid }
.choice .diy { border: 2px solid #D8E2F3 } .choice .dfy { background: #0B1A3A; color: #fff } .choice .dfy p, .choice .dfy li { color: #D7E4FF } .choice .dfy h3, .choice .dfy b { color: #fff }
.choice h3 { margin: 0 0 8px }
'''

def chap(n, title, lead, anchor):
    return f'<section class="chap" id="{anchor}"><div class="num">Chapter {n}</div><h1>{title}</h1><p class="lead">{lead}</p></section>'

def part(n, title, text, items):
    li = ''.join(f'<li>{i}</li>' for i in items)
    return f'<section class="part"><div class="pk">Part {n}</div><h1>{title}</h1><p>{text}</p><ol>{li}</ol></section>'

def box(kind, title, body):
    return f'<div class="box {kind}"><span class="bt">{title}</span>{body}</div>'

def proof(body): return box('proof', 'From our dashboards', body)
def tip(body): return box('tip', 'Pro tip', body)
def warn(body): return box('warn', 'Mistake to avoid', body)
def real(body, t='Real client example'): return box('real', t, body)

def stats(items):
    return '<div class="stats">' + ''.join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in items) + '</div>'

def shot(img, caption):
    return f'<div class="shot"><img src="{A}/img/{img}-hd.webp"></div><p class="cap">{caption}</p>'

def cta(kick, title, text, btn, src):
    return f'''<div class="cta"><div class="faces"><img src="{A}/team/asim-sq.webp"><img src="{A}/team/ali-sq.webp"></div>
<div class="ct"><div class="ck">{kick}</div><h3>{title}</h3><p>{text}</p></div><a class="btn" href="{cal(src)}">{btn} &rarr;</a></div>'''

def dns(name, where, rows, what):
    r = ''.join(f'<tr><td>{k}</td><td class="mono">{v}</td></tr>' for k, v in rows)
    return f'<div class="dns"><div class="dh">{name}<span>{where}</span></div><table>{r}</table><div class="what">{what}</div></div>'

def email(frm, subj, body, note=''):
    n = f'<div class="en">{note}</div>' if note else ''
    return f'<div class="email"><div class="eh"><b>From:</b> {frm} &nbsp;·&nbsp; <b>Subject:</b> {subj}</div><div class="eb">{body}</div>{n}</div>'

def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><tr>{h}</tr>{b}</table>'

# ------------------------------------------------------------------ content
S = []
add = S.append

# Welcome + contents
add(f'''<section id="start"><div class="num" style="font-size:10pt;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#1F6BFF">Before you start</div>
<h1 style="font-size:28pt;margin:6px 0 12px">Read this first</h1>
<p>Most cold email advice is written by people who sell software. This playbook is written by people who run campaigns. We are Ali and Asim, two cousins from Pakistan who have spent the last 8 years building outbound systems for B2B companies, mostly in the USA and Canada.</p>
<p>In 2026 alone our campaigns sent <b>588,000 cold emails</b> for clients. They produced <b>12,900+ replies</b>, <b>3,400+ buyers who said "yes, let's talk"</b>, and <b>$510K+ in qualified pipeline</b>. Every number in this guide comes from those live dashboards. Where we use a public rule (Google, Microsoft, the FTC), we tell you where it comes from.</p>
<p>Here is the honest deal. Everything we do is in these pages: how we buy domains, set up inboxes, write DNS records, warm up, build lists by hand, write the emails, and book the meetings. None of it is secret. It is just a lot of careful, manual work, done every day without skipping steps.</p>
{box('tip', 'How to use this playbook', '<ul><li><b>Doing it yourself?</b> Go chapter by chapter. Each one ends with a step you can finish the same day. Plan on about 30 days from zero to your first booked call.</li><li><b>Short on time?</b> Read Chapter 1 (the math) and the checklists at the end. You will know exactly what a good system needs, and how to judge anyone you hire.</li><li><b>Want it done for you?</b> Skip to the last page. We build and run the whole system and book the calls into your calendar.</li></ul>')}
<h1 style="font-size:24pt;margin:0 0 6px;break-before:page">What is inside</h1><p>17 chapters in 6 parts. Click any chapter to jump to it.</p>
<div class="toc">
<div class="tp">Part 1 · The plan</div>
<div><i>1</i><a href="#c1">The math before the machine</a></div>
<div><i>2</i><a href="#c2">Your tool stack and what it really costs</a></div>
<div class="tp">Part 2 · The sending machine</div>
<div><i>3</i><a href="#c3">Buy the right domains</a></div>
<div><i>4</i><a href="#c4">Google Workspace and your inboxes</a></div>
<div><i>5</i><a href="#c5">DNS: MX, SPF, DKIM and DMARC</a></div>
<div><i>6</i><a href="#c6">Redirects, connecting inboxes, tracking</a></div>
<div><i>7</i><a href="#c7">Warmup: the 3-week rule</a></div>
<div><i>8</i><a href="#c8">The 10-minute daily health check</a></div>
<div class="tp">Part 3 · The list</div>
<div><i>9</i><a href="#c9">Pick buyers who are ready now</a></div>
<div><i>10</i><a href="#c10">Build and verify the list by hand</a></div>
<div class="tp">Part 4 · The message</div>
<div><i>11</i><a href="#c11">Write emails people answer</a></div>
<div><i>12</i><a href="#c12">Follow-ups that add something new</a></div>
<div class="tp">Part 5 · Launch and run</div>
<div><i>13</i><a href="#c13">Launch day and the volume ramp</a></div>
<div><i>14</i><a href="#c14">From reply to booked meeting</a></div>
<div><i>15</i><a href="#c15">Testing and reading your numbers</a></div>
<div class="tp">Part 6 · Stay safe</div>
<div><i>16</i><a href="#c16">The law: USA and Canada</a></div>
<div><i>17</i><a href="#c17">When emails hit spam</a></div>
<div class="tp">Tools</div>
<div><i>✓</i><a href="#lists">The 30-day calendar and checklists</a></div>
<div><i>→</i><a href="#final">Do it yourself, or let us do it</a></div>
</div></section>''')

# ---------------- PART 1
add(part(1, 'The plan', 'Before you buy a single domain, know what the machine has to produce and what it will cost. Most failed campaigns were doomed on day one by bad math.', ['The math before the machine', 'Your tool stack and what it really costs']))

add(chap(1, 'The math before the machine', 'A booked sales call is the end of a long funnel. Work backward from the calls you want, and you will know how many people you need to reach every day.', 'c1'))
add(f'''<p>The "book 5 to 10 demos a day" guides you see online usually start with a fantasy projection: send 1,000 emails a day, get a 5% reply rate, close 16 deals. Real campaigns are messier. Here is what our real funnels looked like, with nothing rounded up.</p>
{table(['Campaign', 'People contacted', 'Replies', 'Reply rate', 'Interested buyers', 'Bounce'], [
 ['Marketing agency, 1 quarter', '76,081', '2,429', '3.19%', '2,146', '1.64%'],
 ['Construction software', '158,322', '4,449', '2.81%', '31 demos held', '2.87%'],
 ['5-day blitz', '79,587', '1,095', '1.38%', '115 → 25 calls', '0.45%'],
 ['One quarter, high volume', '118,387', '4,372', '3.69%', '1,061', '3.08%'],
 ['Pilot campaign', '10,284', '417', '4.05%', '103 opportunities', 'n/a'],
])}
<p class="small">"Interested" means the person replied with real interest: asked for details, a price, or a time to talk. Pipeline is counted at our clients' average deal size of about $2,500.</p>
<h2>The funnel, in plain numbers</h2>
<p>Take the 5-day blitz, our most "average" campaign, and follow 10,000 people through it:</p>
<div class="funnel">
<div style="width:100%">10,000 people contacted <span>verified emails, 3-step sequence</span></div>
<div style="width:82%">~138 replies <span>1.4% reply rate</span></div>
<div style="width:62%">~14 interested buyers <span>about 1 in 10 replies</span></div>
<div style="width:44%">~3 booked calls <span>about 1 in 5 interested</span></div>
</div>
<p>That is roughly <b>3,200 people contacted for every booked call</b>. Our better campaigns did several times better. The pilot campaign turned 10,284 contacts into 103 opportunities, because the offer and the list were extremely sharp. That gap is the whole game: the same infrastructure, very different results, depending on who you target and what you say.</p>
{box('proof', 'From our dashboards', '<p>The industry benchmark backs this up. The sending platform Instantly reports an average reply rate of 3.43%, about 5.5% for the top quarter of senders and 10.7% for the top 10%. Across 588,000 emails, our tuned campaigns landed between 2.8% and 4%.</p>')}
<h2>Your planning worksheet</h2>
<p>Fill this in with a pen. Use the "careful" column until you have your own data.</p>
{table(['Step', 'Careful plan', 'Good campaign', 'Your number'], [
 ['Calls you want per month', '10', '10', '_____'],
 ['Interested buyers needed (calls ÷ 0.2)', '50', '50', '_____'],
 ['Replies needed (interested ÷ share that are interested)', '500 (10%)', '200 (25%)', '_____'],
 ['People to contact (replies ÷ reply rate)', '33,000 (1.5%)', '6,700 (3%)', '_____'],
 ['New people per weekday (÷ 21 days)', '~1,570', '~320', '_____'],
])}
<h3>Turn people into inboxes</h3>
<p>Each new person gets about 3 emails over 2 to 3 weeks. So your daily sends are roughly <b>new people per day × 2.5</b> once the sequence is running. Then divide by a safe volume per inbox.</p>
{table(['New people a day', 'Total sends a day', 'Inboxes (30 sends each)', 'Domains (3 inboxes each)'], [
 ['100', '~250', '9', '3'],
 ['300', '~750', '25', '9'],
 ['600', '~1,500', '50', '17'],
])}
{tip('<p>Grow wide, not hard. Never push one inbox past about 30 cold emails a day. When you need more volume, add inboxes and domains. Our 5-day blitz sent 96,408 emails across many warmed inboxes; each single inbox stayed quiet. The total came from width, not intensity.</p>')}
<p><b>Today\'s step:</b> fill in the worksheet and write down two numbers: new people per day and the number of inboxes you need.</p>''')

add(chap(2, 'Your tool stack and what it really costs', 'You need six kinds of tools. None of them are fancy. Here is what each one does, what we use, and a realistic first-month budget.', 'c2'))
add(f'''{table(['Job', 'What it does', 'Options', 'Typical cost'], [
 ['Domains', 'Separate web addresses you send from, so your main domain is never at risk', 'Namecheap, GoDaddy, Porkbun, Cloudflare', 'About $10 to $15 per domain per year'],
 ['Inboxes', 'Real mailboxes on those domains', 'Google Workspace (our default), Microsoft 365', 'Workspace Business Starter: $7/user/mo yearly or $8.40 monthly'],
 ['Sending platform', 'Sends sequences from many inboxes, rotates them, runs warmup, collects replies in one place', 'Instantly, Smartlead, lemlist', 'Instantly Growth $47/mo; Hypergrowth $97/mo (monthly billing)'],
 ['Lead data', 'Finds decision makers and their work emails', 'Apollo, LinkedIn Sales Navigator, industry directories', 'Free tiers exist; paid plans from about $50/mo'],
 ['Verification', 'Checks every email is real before you send', 'MillionVerifier, NeverBounce, ZeroBounce', 'Roughly $3 to $8 per 1,000 emails'],
 ['Health checks', 'DNS, blacklists, spam rate, test scores', 'Google Postmaster Tools, MXToolbox, mail-tester.com', 'Free'],
])}
<p class="small">Prices as listed by the vendors in late 2026. They change often, so check before you buy.</p>
<h2>A realistic first month</h2>
<p>For a starter system of <b>9 inboxes on 3 domains</b> (about 100 new people a day, which supports roughly 250 sends a day once warm):</p>
{table(['Item', 'Math', 'First month'], [
 ['3 domains', '3 × ~$12 (paid yearly)', '~$36'],
 ['9 Google Workspace inboxes', '9 × $8.40 (monthly)', '~$76'],
 ['Sending platform', 'One plan with unlimited inboxes and warmup', '$47 to $97'],
 ['Lead data', 'Free tier, or one paid seat', '$0 to $99'],
 ['Verify 5,000 emails', '5 × ~$5', '~$25'],
 ['<b>Total</b>', '', '<b>about $185 to $335</b>'],
])}
{warn('<p>Do not buy "pre-warmed" inboxes from random sellers or use free Gmail accounts for cold outreach. You do not control their history, and Google can shut down accounts that look like they were made for bulk mail. Own your domains, own your inboxes.</p>')}
<h3>Why Google Workspace?</h3>
<p>Most of our clients sell to U.S. businesses, and a large share of those businesses use Google or Microsoft for email. Mail sent from Google Workspace inboxes, with correct records, lands well in both. It is also simple to manage: one admin console for every domain and user. Microsoft 365 works too; many teams run a mix so they are not dependent on one provider.</p>
<p><b>Today\'s step:</b> open accounts with a domain registrar and a sending platform. Do not buy anything else yet.</p>''')

# ---------------- PART 2
add(part(2, 'The sending machine', 'This is the boring part that decides everything. If your domains, records and warmup are wrong, the best email in the world goes to spam. Get it right once, and it runs for months.', ['Buy the right domains', 'Google Workspace and your inboxes', 'DNS: MX, SPF, DKIM and DMARC', 'Redirects, connecting inboxes, tracking', 'Warmup: the 3-week rule', 'The 10-minute daily health check']))

add(chap(3, 'Buy the right domains', 'Never send cold email from your main company domain. You buy look-alike domains that point back to your real business, and you let them take the risk.', 'c3'))
add(f'''<p>Your main domain carries your website, your invoices, your team\'s email and your brand. If cold outreach damages its reputation, every email your company sends suffers. So every serious outbound team sends from <b>secondary domains</b>: close, honest variations of the brand name.</p>
<h2>How to pick names</h2>
<p>Say your company is <b>brightroof.com</b>. Good secondary domains look like this:</p>
{table(['Good choice', 'Why it works', 'Avoid', 'Why'], [
 ['trybrightroof.com', 'Clear, short, obviously your brand', 'bright-roof-pros.biz', 'Hyphens and odd endings look spammy'],
 ['getbrightroof.com', 'Common prefix, easy to read', 'brightrooof.com', 'Typo domains look like phishing'],
 ['brightroofhq.com', 'Professional suffix', 'brightroof.xyz', 'Cheap endings carry worse reputation'],
 ['brightroofteam.com', 'Reads naturally in an email address', 'roofingdeals4u.com', 'Hides who you are (a legal problem too)'],
])}
<ul class="check">
<li><b>Buy .com</b> whenever you can. U.S. buyers trust it most.</li>
<li><b>Short and easy to say.</b> The name shows up in every "From" line.</li>
<li><b>Honest.</b> The domain must point back to your real company. Hiding who you are breaks U.S. law (Chapter 16).</li>
<li><b>Buy them yearly with auto-renew on.</b> A domain that expires in the middle of a campaign kills every inbox on it.</li>
<li><b>Plan 2 to 3 inboxes per domain.</b> Spreading out means one bad domain only hurts a small part of your system.</li>
</ul>
{tip('<p>Buy one or two spare domains on day one and warm them with the rest. When a domain gets tired (and eventually one will), you swap in a warm spare instead of losing three weeks.</p>')}
<h2>Step by step</h2>
<ol class="steps">
<li>Write a list of 10 name ideas using prefixes (try, get, use, hey, meet, go) and suffixes (hq, team, co, mail, group).</li>
<li>Search each one at your registrar. Skip any name that was used before for spam: a quick search of the name in quotes and a check on MXToolbox\'s blacklist tool is enough.</li>
<li>Buy the number of domains from your worksheet, plus one spare. Turn on auto-renew and the free privacy protection.</li>
<li>Write down each domain in a simple sheet: domain, registrar, purchase date, renewal date. This sheet becomes your system map.</li>
</ol>
{real('<p>For a construction software client, every campaign ran on secondary domains while the client\'s main domain kept sending quotes and invoices untouched. Over 162,073 emails went out, 4,449 people replied, and 31 qualified demos became <b>6 annual contracts</b>. The main domain never felt any of it.</p>')}''')

add(chap(4, 'Google Workspace and your inboxes', 'One Workspace account can hold all your sending domains. You add each domain, create 2 to 3 real people on it, and make every inbox look like a person a buyer would trust.', 'c4'))
add(f'''<h2>Set up the account</h2>
<ol class="steps">
<li>Go to Google Workspace and start a <b>Business Starter</b> account using your <b>first secondary domain</b> (not your main domain). Choose the monthly (Flexible) plan if you want to stay flexible.</li>
<li>Google asks you to verify you own the domain. It gives you a TXT record to add at your registrar. Add it, wait a few minutes, click Verify.</li>
<li>Add your other secondary domains in the Admin console: <b>Account → Domains → Manage domains → Add a domain</b>. Pick "secondary domain" so each one can have its own users. Verify each one the same way.</li>
<li>Create users: <b>Directory → Users → Add new user</b>. Two or three per domain, using real team members\' names where you can.</li>
</ol>
<h3>How to name inboxes</h3>
{table(['Good', 'Okay', 'Avoid'], [
 ['ali@trybrightroof.com', 'ali.h@trybrightroof.com', 'sales@, info@, marketing@'],
 ['asim@getbrightroof.com', 'asimh@getbrightroof.com', 'ali123@, noreply@'],
])}
<p>A first name is what a real person would use. Role addresses like sales@ look like a blast, get lower replies and are more likely to be filtered.</p>
<h2>Make every inbox look human</h2>
<p>This takes ten minutes per inbox and most people skip it. Do not.</p>
<ul class="check">
<li><b>Profile photo:</b> a real, friendly headshot of the person. It shows next to your name in Gmail.</li>
<li><b>Display name:</b> "Ali Hassan", not "Ali from BrightRoof Sales Team".</li>
<li><b>Plain-text signature:</b> name, title, company, real website, and your postal address (U.S. law requires a physical address in commercial email). No images, no banners, no long legal text.</li>
<li><b>Sign in once from a normal browser</b> and send a couple of real emails to colleagues. A brand new inbox that has never been used by a person looks odd.</li>
<li><b>Turn on 2-step verification</b> for every user. You will need it in Chapter 6 anyway.</li>
</ul>
{email('Ali Hassan &lt;ali@trybrightroof.com&gt;', 'signature example', 'Ali Hassan\nPartner, BrightRoof\nbrightroof.com\n123 Main St, Suite 4, Austin, TX 78701', 'A clean signature: real name, real company, real site, real address. Your main website is fine here; the redirect in Chapter 6 makes the secondary domain point there too.')}
{warn('<p>Do not create 10 users on one domain to save money. Every inbox on a domain shares its reputation. Three inboxes sending 30 emails each is 90 a day per domain, which is a healthy ceiling for a cold domain.</p>')}''')

add(chap(5, 'DNS: MX, SPF, DKIM and DMARC', 'These four records tell Gmail and Outlook that your emails are really from you. Without them you are not just in spam, you can be rejected outright. Here is each record, what it does, and exactly what to type.', 'c5'))
add(f'''<p>Since February 2024, Google requires every sender to Gmail to have SPF or DKIM set up, and senders of more than 5,000 emails a day to have all three: SPF, DKIM and DMARC. Yahoo has the same rules. Since May 5, 2025, Microsoft rejects high-volume mail to Outlook that fails them, with the error <code>550 5.7.515</code>. You do this once per domain. Do all four on every domain, whatever your volume.</p>
<p>You add these at your registrar (Namecheap: <b>Domain List → Manage → Advanced DNS</b>; GoDaddy: <b>My Products → DNS</b>). Each record has a <b>Type</b>, a <b>Host</b> (or Name) and a <b>Value</b>.</p>
{dns('1 · MX record', 'where your mail is delivered', [('Type', 'MX'), ('Host', '@'), ('Value', 'smtp.google.com'), ('Priority', '1')],
 'MX tells the world which server receives mail for your domain. Without it, replies bounce. Google\'s current setup uses this single MX record. Delete any old MX records your registrar added by default (many add their own email forwarding records).')}
{dns('2 · SPF record', 'who is allowed to send', [('Type', 'TXT'), ('Host', '@'), ('Value', 'v=spf1 include:_spf.google.com ~all')],
 'SPF is a guest list. It says "Google\'s servers may send email for this domain." A domain may have only <b>one</b> SPF record. If you already have one, add the include to it instead of creating a second.')}
{dns('3 · DKIM record', 'a tamper-proof signature', [('Type', 'TXT'), ('Host', 'google._domainkey'), ('Value', 'v=DKIM1; k=rsa; p=MIIBIjANBg... (long key Google gives you)')],
 'DKIM signs every email with a secret key, so the receiver can check nothing was changed and it really came from your domain. You get your key from Google: <b>Admin console → Apps → Google Workspace → Gmail → Authenticate email</b>. Pick the domain, choose 2048-bit, click Generate. Paste the record at your registrar, wait about an hour, then come back and click <b>Start authentication</b>.')}
{dns('4 · DMARC record', 'the rulebook and the report', [('Type', 'TXT'), ('Host', '_dmarc'), ('Value', 'v=DMARC1; p=none; rua=mailto:dmarc@yourmaindomain.com; adkim=r; aspf=r')],
 'DMARC tells receivers what to do if an email fails SPF and DKIM, and where to send reports. Start with <code>p=none</code> (watch only). <code>adkim=r; aspf=r</code> means relaxed matching, which suits Google Workspace. Send the reports to an inbox on your main domain so you see all your domains in one place.')}
<h2>Check your work</h2>
<ol class="steps">
<li>Wait 30 minutes to a few hours for the records to spread (it can take up to 48 hours).</li>
<li>Open MXToolbox and run the <b>MX Lookup</b>, <b>SPF Record Lookup</b>, <b>DKIM Lookup</b> (selector: <code>google</code>) and <b>DMARC Lookup</b> for each domain. Every test should be green.</li>
<li>Send an email from the new inbox to a personal Gmail account. Open it, click the three dots → <b>Show original</b>. You want to see <b>SPF: PASS</b>, <b>DKIM: PASS</b> and <b>DMARC: PASS</b>.</li>
<li>Go to mail-tester.com, send an email to the address it shows you, and check your score. Aim for 9/10 or better before you go further.</li>
</ol>
{warn('<p>The two most common mistakes we fix for new clients: <b>two SPF records</b> on one domain (both fail), and <b>DKIM generated but never started</b> in the Admin console (Google shows "Not authenticating"). Both look fine at a glance and silently push mail to spam.</p>')}
{proof('<p>Across 588,000 emails our clients\' main domains were never used for a single cold email, and every sending domain passed SPF, DKIM and DMARC before warmup started. In one quarter we sent 236,545 emails and kept bounce rate around 3% while 4,372 people replied.</p>')}''')

add(chap(6, 'Redirects, connecting inboxes, tracking', 'Three small jobs that finish the machine: make each secondary domain open your real website, connect every inbox to your sending platform, and switch off the tracking that hurts delivery.', 'c6'))
add(f'''<h2>1 · Redirect each domain to your real site</h2>
<p>Curious buyers type the domain they saw in your email address into a browser. If they land on a parked "this domain is for sale" page, you lose trust. Point every secondary domain to your main website with a permanent (301) redirect.</p>
<ul><li><b>Namecheap:</b> Domain List → Manage → Redirect Domain → source <code>trybrightroof.com</code>, destination <code>https://brightroof.com</code>.</li>
<li><b>GoDaddy:</b> Domain → Forwarding → Add forwarding → https://brightroof.com, type <b>Permanent (301)</b>.</li></ul>
<p>The redirect only affects the website. Your MX, SPF, DKIM and DMARC records keep working for email.</p>
<h2>2 · Connect inboxes to your sending platform</h2>
<p>There are two ways. Use the first if your platform offers it.</p>
<div class="grid2"><div><h4>Option A: Sign in with Google (OAuth)</h4><p>In your Workspace Admin console go to <b>Security → Access and data control → API controls → Manage third-party app access</b>, find your sending platform and mark it <b>Trusted</b>. Then in the platform click "Add account → Google" and sign in for each inbox. No passwords stored, fewer disconnects.</p></div>
<div><h4>Option B: App password (IMAP/SMTP)</h4><p>Make sure 2-step verification is on. Sign in to the inbox, open <b>Google Account → Security → App passwords</b>, create one named after your platform and paste the 16-character code into the platform with <code>imap.gmail.com</code> (port 993) and <code>smtp.gmail.com</code> (port 587).</p></div></div>
<p>When each inbox is connected, set its daily limit in the platform. Start at the warmup numbers in Chapter 7, never at the maximum.</p>
<h2>3 · Turn tracking off</h2>
<p>Open tracking works by hiding a tiny invisible image in your email. Link tracking rewrites your links through a tracking server. Both make a cold email look more like marketing mail to spam filters, and Apple Mail privacy makes open numbers unreliable anyway.</p>
{box('proof', 'From our dashboards', '<p>Our dashboards show <b>zero opens</b> on purpose. We switched open tracking off on every campaign and judge copy by replies and booked calls only, the numbers that pay the bills. If you must use link tracking, set up a custom tracking domain (a CNAME record your platform gives you) so you are not sharing a tracking address with thousands of other senders.</p>')}
{cta('Short on time?', 'Skip the setup. We build the whole machine for you.', 'Domains, inboxes, DNS, warmup and daily monitoring, done by a team with 8 years in outbound. Book a free 20-minute call with our CEO and see what we would build for you.', 'Book my 20-minute call', 'cta1-setup')}''')

add(chap(7, 'Warmup: the 3-week rule', 'A brand-new inbox that suddenly sends hundreds of emails looks like a spammer. Warmup builds a normal-looking history first. It is the step most people rush, and the reason most campaigns die.', 'c7'))
add(f'''<p>Google\'s own guidance is direct: start with low volume, increase slowly, and avoid sudden spikes if you have no history of sending. Warmup is how you build that history. Your sending platform sends small numbers of emails between your inbox and a network of real inboxes. Those emails get opened, replied to, and pulled out of spam when they land there. That tells Gmail and Outlook that people want mail from you.</p>
<h2>The schedule we use</h2>
{table(['Week', 'Warmup emails per inbox per day', 'Cold emails per inbox per day', 'What you are doing'], [
 ['1', '5 → 15, rising a little each day', '0', 'Records checked, profiles finished, warmup on'],
 ['2', '15 → 25', '0', 'Build and verify your list, write your emails'],
 ['3', '25 → 35', '0', 'Test placement with a few manual emails'],
 ['4', 'Keep at ~20 to 30', '10 → 15', 'First campaign, small batches'],
 ['5', 'Keep at ~20 to 30', '15 → 25', 'Watch bounces and replies daily'],
 ['6+', 'Keep running in the background', 'Up to ~30', 'Scale by adding inboxes, not volume'],
])}
<ul class="check">
<li><b>14 days is the minimum. 21 is safer.</b> If you are in a hurry, the answer is more inboxes, not less warmup.</li>
<li><b>Never turn warmup off</b> after launch. It keeps your sending pattern steady on quiet days.</li>
<li><b>Watch the warmup health score</b> in your platform. A sudden drop is the earliest warning you will get.</li>
<li><b>Same schedule for every new inbox</b>, even when the rest of the system is old and healthy.</li>
</ul>
{warn('<p>Starting campaigns on day 5 because "the records are green". Green records mean you are allowed to send. They do not mean you are trusted. We see this more than any other mistake.</p>')}
{real('<p>For a 5-day push, a client needed results fast. Because the inboxes had already been warming for weeks, we could send <b>96,408 emails in 5 days</b> to 79,587 people with a bounce rate of just <b>0.45%</b>. The result: 1,095 replies, 115 interested buyers and <b>25 booked calls in one week</b>, worth about $62,500 in pipeline. Speed was only possible because of the boring preparation.</p>', 'Real client example: the 5-day blitz')}
{shot('blitz', 'The live dashboard from the 5-day blitz: 96,408 emails sent, 0.45% bounce rate. Opens show zero because tracking was switched off on purpose.')}''')

add(chap(8, 'The 10-minute daily health check', 'A cold email system is like a car engine: it rarely breaks all at once, it warns you first. This is the routine we run every morning for every client. Ten minutes, before you touch anything else.', 'c8'))
add(f'''{table(['Check', 'Where', 'Healthy', 'Act now if'], [
 ['Bounce rate per campaign', 'Sending platform', '<span class="pill">under 2%</span>', '<span class="pill r">near 3%</span> pause and re-verify the list'],
 ['Disconnected inboxes', 'Sending platform → accounts', 'All connected', 'Any error: reconnect today'],
 ['Warmup health', 'Sending platform → warmup', 'Steady, high', 'Drops for 2 days: cut that inbox\'s cold volume'],
 ['Replies waiting', 'Unified inbox', 'Interested answered within 1 hour', 'Anything older than 1 business day'],
 ['Opt-outs', 'Replies + unsubscribe list', 'Added to suppression list same day', 'Any opt-out still active in a campaign'],
 ['Spam rate', 'Google Postmaster Tools', '<span class="pill">under 0.1%</span>', '<span class="pill r">near 0.3%</span> Google\'s hard limit'],
])}
<h2>Once a week</h2>
<ul class="check">
<li>Run a <b>blacklist check</b> for every sending domain on MXToolbox.</li>
<li>Send one test email per domain to <b>mail-tester.com</b>. Keep the score at 9/10 or higher.</li>
<li><b>Manual placement test:</b> send your real campaign email from 3 or 4 inboxes to your own Gmail, Outlook and Yahoo test addresses. Write down Inbox, Promotions or Spam for each.</li>
<li>Re-read every <b>live email</b>. Has anything changed, a broken link, an outdated offer?</li>
<li>Check <b>domain renewal dates</b> in your system sheet.</li>
</ul>
<h3>Set up Google Postmaster Tools (free)</h3>
<ol class="steps"><li>Go to Google Postmaster Tools and sign in with a Google account.</li><li>Add each sending domain. Google gives you a TXT record to prove you own it. Add it at your registrar.</li><li>Check it weekly. Note: Google says it may show no data on days with low volume, which is normal for a single cold domain.</li></ol>
{proof('<p>Our dashboards show bounce rates between <b>0.45%</b> and <b>3.08%</b> across campaigns. The lowest came from a fresh, verified list. The highest came from a quarter that mixed in older data, which is exactly why we now re-verify any list older than about 60 days. The daily check is how we caught it before it turned into a spam problem.</p>')}
{shot('q1', 'One quarter at high volume: 236,545 emails, 4,372 replies (3.69%) and 1,061 interested buyers, with daily checks every morning.')}''')

# ---------------- PART 3
add(part(3, 'The list', 'Your list decides your results more than your email does. The right person with the right problem at the right time will forgive an average email. The wrong person will ignore a perfect one.', ['Pick buyers who are ready now', 'Build and verify the list by hand']))

add(chap(9, 'Pick buyers who are ready now', 'Start with the customers who already pay you, not a wish list. Then add a "trigger": a public sign that a company needs you right now.', 'c9'))
add(f'''<h2>Write your ideal customer profile (ICP)</h2>
<p>Pull up your five best customers, the ones who paid well, stayed long and were easy to work with. Fill in this table for them. The patterns are your ICP.</p>
{table(['Question', 'Example: construction software client', 'Your answer'], [
 ['Industry', 'General contractors, commercial construction', '_____'],
 ['Company size', '20 to 200 employees', '_____'],
 ['Location', 'USA, specific states', '_____'],
 ['Who signs', 'Owner, VP of Operations, Project Executive', '_____'],
 ['The painful problem', 'Losing time and margin on manual project tracking', '_____'],
 ['Proof you can show', 'Case study from a similar contractor', '_____'],
])}
<h2>Add a trigger</h2>
<p>A trigger turns "a good fit" into "a good fit right now". It also gives you an honest reason to write.</p>
<div class="grid2">
<div><h4>Hiring</h4><p>A job post for the role your product helps (an SDR, an estimator, a bookkeeper) means budget and pain.</p></div>
<div><h4>Growth</h4><p>A new location, new funding, a big new contract, a press release.</p></div>
<div><h4>Change</h4><p>A new executive in the buyer seat in the last 90 days. New leaders buy new things.</p></div>
<div><h4>Tools</h4><p>Their website or job posts show a tool you replace or plug into.</p></div>
</div>
{real('<p>For a marketing agency client, the sharpest segment was not "all agency owners". It was owners whose agencies were actively hiring account managers. They were winning work and needed more of it. That focus helped the campaign produce <b>2,146 interested buyers</b> from 76,081 people contacted in one quarter, about 100 interested replies every week, and roughly <b>$175,000 in pipeline</b>.</p>')}
{shot('agency', 'The agency campaign dashboard: 82,671 emails sent, 2,429 replies, 1.64% bounce rate.')}''')

add(chap(10, 'Build and verify the list by hand', 'Lists you buy in bulk are full of dead emails and wrong people. We build every list in small segments, check it by eye, and verify every single address before it goes near a campaign.', 'c10'))
add(f'''<h2>Where to find people</h2>
<ul><li><b>Lead databases</b> (Apollo and similar): filter by industry, size, location and job title. Export in batches of a few hundred, one segment at a time.</li>
<li><b>LinkedIn Sales Navigator:</b> the most up-to-date job titles. Use it to confirm the person is still in the role.</li>
<li><b>Industry directories:</b> state contractor license boards, chamber of commerce lists, Clutch for agencies, association member lists.</li>
<li><b>Google Maps:</b> great for local service businesses (owner names are often on the website\'s About page).</li></ul>
<h2>The columns every list needs</h2>
{table(['Column', 'Example', 'Why'], [
 ['First name', 'Mark', 'Greeting'],
 ['Company', 'Carter Builders', 'Subject and first line'],
 ['Title', 'Owner', 'Pick the right angle'],
 ['Work email', 'mark@carterbuilders.com', 'Must be verified'],
 ['Website', 'carterbuilders.com', 'Research and dedupe'],
 ['City, state', 'Denver, CO', 'Send in their time zone'],
 ['Trigger', 'Hiring 2 project managers', 'Your reason to write'],
 ['First line', 'Saw Carter is hiring two PMs for the new Aurora job', 'Written by a person, after a 2-minute look'],
])}
<h2>Clean before you verify</h2>
<ul class="check">
<li><b>Remove role addresses</b> such as info@, sales@, office@, admin@. Low replies, high complaints.</li>
<li><b>One or two people per company</b>, maximum. Ten emails into one company look like a blast and annoy the buyer.</li>
<li><b>Remove anyone outside your target country.</b> Different countries have different laws (Chapter 16).</li>
<li><b>Remove past opt-outs, customers and competitors</b> using your suppression list.</li>
</ul>
<h2>Verify every address</h2>
<p>Upload the list to a verification tool. It sorts emails into groups. Here is what we do with each:</p>
{table(['Result', 'What it means', 'What we do'], [
 ['Valid', 'The mailbox exists', '<span class="pill">Send</span>'],
 ['Invalid', 'The mailbox does not exist', '<span class="pill r">Delete</span>'],
 ['Catch-all', 'The server accepts everything, so the tool cannot tell', '<span class="pill y">Hold</span> separate small campaign later, or skip'],
 ['Unknown', 'The server did not answer', '<span class="pill y">Hold</span> re-check in a few days'],
])}
{warn('<p>Sending to an old list "because it was verified last year". People change jobs every day. Re-verify anything older than about 60 days. Bounce rate is the fastest way to burn a new domain: keep it under 2% and pause near 3%.</p>')}''')

# ---------------- PART 4
add(part(4, 'The message', 'Cold email is not marketing copy. It is a short, polite note from one person to another about a problem they probably have. The less it looks like an ad, the better it works.', ['Write emails people answer', 'Follow-ups that add something new']))

add(chap(11, 'Write emails people answer', 'Five parts, under 80 words, plain text, no images, at most one link. That is the whole formula. The hard part is saying something specific.', 'c11'))
add(f'''{table(['Part', 'Job', 'Rule'], [
 ['Subject', 'Get opened', '2 to 5 words, lowercase, looks like an internal email: "pm hiring at carter"'],
 ['First line', 'Prove it is not a blast', 'About them, not you. Their trigger, their company, their work.'],
 ['Problem', 'Make it relevant', 'One problem people like them have, in their words.'],
 ['Proof', 'Make it believable', 'One short result from a similar company. A number beats an adjective.'],
 ['Ask', 'Make replying easy', 'Ask for interest, not a meeting: "worth a look?", "open to it?"'],
])}
<h2>Example 1: a home services software company to a roofing owner</h2>
{email('Ali Hassan &lt;ali@trybrightroof.com&gt;', 'storm season leads', 'Hi Mark,\n\nSaw Carter Roofing is hiring two estimators ahead of storm season.\n\nMost roofing owners we talk to lose good jobs in that rush because quotes go out two or three days late.\n\nA Denver roofer using our quoting tool cut their quote time to same-day and won 11 more jobs last spring.\n\nWorth a quick look before the season starts?\n\nAli', '72 words. First line is about Mark, not us. One problem, one proof, one easy question. No link, no image, no attachment.')}
<h2>Example 2: an agency selling to a SaaS founder</h2>
{email('Asim Hussain &lt;asim@trywayneflow.com&gt;', 'demo calendar', 'Hi Priya,\n\nNoticed Lumen just opened two SDR roles. Usually that means the pipeline target went up.\n\nThe hard part is the 3 to 4 months before new reps produce anything.\n\nFor a software client this year we booked 31 qualified demos, which turned into 6 annual contracts, while their team kept closing.\n\nOpen to seeing how we would do it for Lumen?\n\nAsim', 'Sample email for illustration. The proof line uses a real campaign result.')}
<h2>Personalize in three layers</h2>
<ol class="steps">
<li><b>Segment:</b> one version of the email for each type of buyer (owners vs. operations leaders, roofers vs. plumbers). This alone beats one email for everyone.</li>
<li><b>Company:</b> a line about their trigger or their business, which a person writes after a two-minute look at the website or job post.</li>
<li><b>Person:</b> a line about something the person said or did (a LinkedIn post, an interview, a talk). Save this layer for your most valuable accounts.</li>
</ol>
{warn('<p>Fake "Re:" or "Fwd:" subjects, spammy words in the subject ("free", "guaranteed", "act now"), images, attachments and three links in the first email. Each one makes a filter, or a buyer, less likely to trust you.</p>')}
{proof('<p>Across 588,000 emails, our tuned campaigns earned reply rates between <b>2.8% and 4%</b> with plain-text emails under 100 words, one problem and one proof line. The pilot campaign reached a 4.05% reply rate and <b>103 opportunities</b> from just 10,284 people contacted, about $150,000 in pipeline.</p>')}''')

add(chap(12, 'Follow-ups that add something new', 'Almost half of all replies come after the first email. But "just bumping this" is not a follow-up. Every email in the sequence must add a new reason to reply.', 'c12'))
add(f'''<p>Instantly\'s benchmark data shows about <b>58% of replies come from the first email and 42% from follow-ups</b>. Stop after one email and you leave nearly half your results on the table.</p>
<h2>The schedule</h2>
{table(['Email', 'Day', 'What it adds', 'Length'], [
 ['1', 'Day 1', 'The five-part email from Chapter 11', 'Under 80 words'],
 ['2', 'Day 3 or 4', 'A different angle on the same problem, or a second proof point', 'Under 60 words'],
 ['3', 'Day 7 or 8', 'A useful resource or a specific idea for their company', 'Under 60 words'],
 ['4', 'Day 11 to 14', 'A short story: how one similar client got a result', 'Under 70 words'],
 ['5', 'Day 18 to 21', 'A polite close: "should I stop reaching out?"', 'Under 40 words'],
])}
<p>Send follow-ups in the <b>same thread</b> (reply to your own email) so the context stays with them.</p>
{email('Ali Hassan', 'Re: storm season leads', 'Hi Mark, one more idea.\n\nThe roofer I mentioned started sending a same-day "rough number" by text before the full quote. Homeowners stopped calling around.\n\nHappy to show you the exact message they use. Want it?\n\nAli', 'Follow-up #2: new idea, still about Mark, still easy to answer.')}
{email('Ali Hassan', 'Re: storm season leads', 'Hi Mark, I have not heard back, so I will assume the timing is off.\n\nShould I close the loop for now, or is it worth checking back in the fall?\n\nAli', 'The last email. Short and respectful. It often gets the "yes, check back in August" reply that turns into a deal later.')}
{tip('<p>Stop the sequence the moment anyone replies, even with "not interested". Your sending platform does this automatically if replies are connected. A follow-up sent after a "no" is how complaints happen.</p>')}
{cta('Want your campaign written by people who do this daily?', 'Get the emails, the list and the follow-ups done for you.', 'We write, test and send every email, handle every reply, and book qualified buyers into your calendar. Book a 20-minute strategy call with our CEO.', 'Book a 20-minute call', 'cta2-copy')}''')

# ---------------- PART 5
add(part(5, 'Launch and run', 'Launch is not a big day. It is a slow, careful start, followed by a daily habit of answering people fast and reading the numbers honestly.', ['Launch day and the volume ramp', 'From reply to booked meeting', 'Testing and reading your numbers']))

add(chap(13, 'Launch day and the volume ramp', 'Start smaller than you want, watch everything, then grow a little each week. A slow first two weeks protects months of sending.', 'c13'))
add(f'''<h2>Campaign settings that matter</h2>
<ul class="check">
<li><b>Sending window:</b> weekdays, roughly 8 a.m. to 5 p.m. in the <b>buyer\'s</b> time zone. A CFO in Denver should not get your email at 6 a.m. Mountain because your tool runs on Eastern.</li>
<li><b>Daily limit per inbox:</b> the ramp numbers from Chapter 7, never the platform\'s maximum.</li>
<li><b>Gap between emails:</b> randomize it (for example every 8 to 15 minutes per inbox) so sending looks human.</li>
<li><b>Text only</b>, open tracking off, link tracking off.</li>
<li><b>Stop on reply</b> turned on, including auto-replies that say the person left the company.</li>
<li><b>Unsubscribe handling:</b> an opt-out line in every email and replies like "remove me" sent straight to your suppression list.</li>
</ul>
<h2>The first 14 days</h2>
{table(['Days', 'New people per inbox per day', 'Watch for'], [
 ['1 to 3', '5 to 10', 'Bounces. If a batch bounces above 3%, stop and re-verify'],
 ['4 to 7', '10 to 15', 'First replies. Read every one; they tell you if the message lands'],
 ['8 to 14', '15 to 20', 'Warmup health steady, spam tests still in the inbox'],
 ['15+', 'Up to ~30 total sends', 'Ready to scale by adding inboxes'],
])}
{proof('<p>For a construction software client we launched on fresh domains with the same slow ramp, then held steady volume for months: <b>162,073 emails</b> to 158,322 contacts, a 2.81% reply rate, <b>31 qualified demos and 6 annual contracts</b>. The bounce rate stayed at 2.87% across the whole run.</p>')}
{shot('construction', 'The construction software campaign: 162,073 emails, 4,449 replies, 31 demos, 6 annual contracts.')}''')

add(chap(14, 'From reply to booked meeting', 'Replies are where meetings are won or lost. Speed and a helpful answer beat a clever email every single time.', 'c14'))
add(f'''<h2>Sort every reply into a bucket</h2>
{table(['Bucket', 'Example', 'What we do', 'How fast'], [
 ['Interested', '"Sure, tell me more"', 'Answer their question, then offer two times', 'Within 1 hour'],
 ['Wants info', '"Send me pricing"', 'Give a real, short answer and ask one question back', 'Same day'],
 ['Not now', '"Try me next quarter"', 'Thank them, set a reminder, write back on that date', 'Same day'],
 ['Wrong person', '"Talk to Sarah"', 'Write Sarah, mention who sent you', 'Same day'],
 ['No', '"Not interested"', 'Short thank-you, stop all emails', 'Same day'],
 ['Opt-out', '"Remove me"', 'Suppression list, no reply needed', 'Same day (law: within 10 business days)'],
])}
<h2>Replies that book the call</h2>
{email('Ali Hassan', 'Re: storm season leads', 'Hi Mark, glad it is timely.\n\nShort version: we connect to the tool you already use for measurements, and the quote goes out the same day.\n\nEasiest is a 20-minute screen share. Does Tuesday at 10:00 or Wednesday at 2:00 Mountain work? Or grab any time here: [booking link]\n\nAli', 'Answer first, then two specific times in their time zone, then a link as a backup.')}
{email('Ali Hassan', 'Re: storm season leads', 'Hi Mark, fair question.\n\nMost roofers your size pay between X and Y a month, depending on the number of estimators.\n\nTo give you an exact number I would need to know how many quotes you send a week. Roughly how many?', 'When they ask for price: give a real range, then ask one question. Dodging the question kills trust.')}
<h2>Protect the show rate</h2>
<ul class="check">
<li>Book within <b>2 to 4 business days</b>. Interest cools fast.</li>
<li>Send a <b>confirmation</b> right away, a <b>reminder the day before</b> and a short note <b>an hour before</b>.</li>
<li>When someone does not show, send a friendly, no-guilt reschedule message <b>within 24 hours</b>.</li>
<li>Track <b>show rate</b> (meetings held ÷ booked) as its own number.</li>
</ul>
{real('<p>The difference between a reply and a contract is follow-through. For the construction client, 4,449 replies were sorted the same day, interested buyers got answers within the hour, and 31 qualified demos were held. Roughly <b>1 in 5 demos became a signed annual contract</b>.</p>')}''')

add(chap(15, 'Testing and reading your numbers', 'Change one thing at a time, give each test enough people, and judge it by positive replies, never by opens.', 'c15'))
add(f'''<h2>What to test, in order</h2>
<ol class="steps">
<li><b>The list</b> (segment, title, trigger). Biggest impact by far.</li>
<li><b>The offer and the angle</b> (which problem you lead with).</li>
<li><b>The proof</b> (which result you mention).</li>
<li><b>The ask</b> ("worth a look?" vs. "open to a 15-minute call?").</li>
<li><b>The subject line.</b> Smallest impact, so test it last.</li>
</ol>
<ul class="check"><li>Send each version to at least <b>1,000 people</b> before you decide.</li><li>Judge by <b>positive replies per 1,000 people</b>, not total replies (an angry reply is still a reply).</li><li>Keep a simple test log: date, what changed, people, positive replies, decision.</li></ul>
<h2>The numbers that matter</h2>
{table(['Metric', 'How to calculate', 'Healthy range from our campaigns'], [
 ['Bounce rate', 'Bounces ÷ emails sent', '0.45% to 3%; aim under 2%'],
 ['Reply rate', 'Replies ÷ people contacted', '2.8% to 4% when tuned'],
 ['Interested rate', 'Interested ÷ replies', '10% to 25% is common'],
 ['Show rate', 'Held ÷ booked', 'Track it weekly'],
 ['Cost per qualified meeting', 'Total spend ÷ qualified meetings held', 'The number to compare any option by'],
])}
{tip('<p>Give a new system a full quarter before you judge it. The first few weeks go to setup, warmup and testing copy. Our best quarters were never our best first weeks.</p>')}
{proof('<p>Totals across all our 2026 campaigns: <b>588,000 emails</b>, <b>12,900+ replies</b>, <b>3,400+ interested buyers</b>, <b>100+ booked calls</b>, <b>6 annual contracts</b> and <b>$510K+ in pipeline</b>. One client calendar alone filled with 50+ calls.</p>')}''')

# ---------------- PART 6
add(part(6, 'Stay safe', 'Doing cold email properly is both legal and good for delivery. The rules that keep you out of court are the same habits that keep you out of spam.', ['The law: USA and Canada', 'When emails hit spam']))

add(chap(16, 'The law: USA and Canada', 'Cold B2B email is legal in the U.S. when you follow the CAN-SPAM Act. Canada is stricter. Here are the rules in plain English.', 'c16'))
add(f'''{box('warn', 'Not legal advice', '<p>This is general information based on the FTC\'s published guidance and the law as of October 2026. Talk to a qualified attorney about your situation.</p>')}
<h2>USA: CAN-SPAM in seven rules</h2>
<ol class="steps">
<li><b>No B2B exception.</b> The FTC says the law "makes no exception for business-to-business email."</li>
<li><b>Honest headers.</b> The From name, address and domain must identify you or your business.</li>
<li><b>Honest subject lines.</b> No fake "Re:" or fake invoices.</li>
<li><b>Say it is an ad</b> in a clear way that fits your style. Decide how with your counsel and apply it to every template.</li>
<li><b>A valid physical postal address</b> in every email (street address, registered P.O. box or registered private mailbox).</li>
<li><b>A clear way to opt out</b>, which you honor within <b>10 business days</b> and which keeps working for at least 30 days after you send.</li>
<li><b>You stay responsible</b> even if an agency sends for you. Both can be liable.</li>
</ol>
<p>Penalties can reach <b>$53,088 per violating email</b>. One unhonored opt-out in a big campaign is an expensive mistake.</p>
<h2>Canada: CASL is stricter</h2>
<p>Canada\'s anti-spam law needs consent before you send. For B2B there is a narrow form of implied consent: the person\'s email address is published publicly (for example on their company website), with no statement that they do not want messages, and your message is relevant to their job. You must also identify yourself, include contact details and an unsubscribe that works. If you cannot show that kind of consent, do not email them.</p>
<h2>Our compliance habits</h2>
<ul class="check"><li>Opt-out line in every email, replies monitored daily.</li><li>One master suppression list, checked before every campaign.</li><li>Real names, real company, real address in every signature.</li><li>Separate campaigns and rules for Canada; no consumer (personal) addresses at all.</li></ul>''')

add(chap(17, 'When emails hit spam', 'Every system has a bad week. What matters is spotting it early and fixing it calmly. Here is our recovery plan, step by step.', 'c17'))
add(f'''<h2>Warning signs</h2>
<ul><li>Replies drop sharply while volume stays the same.</li><li>Your manual placement test lands in spam or Promotions.</li><li>Warmup health falls for two or more days.</li><li>Bounces jump above 3%, or Postmaster spam rate climbs toward 0.3%.</li></ul>
<h2>The 7-step recovery</h2>
<ol class="steps">
<li><b>Pause new campaigns</b> on the affected inboxes. Keep warmup running.</li>
<li><b>Check the records</b> with "Show original" on a real email: SPF, DKIM and DMARC must all pass.</li>
<li><b>Check bounces and complaints.</b> Re-verify the list if bounces are high.</li>
<li><b>Strip the email</b>: remove links, tracking and anything salesy in the subject.</li>
<li><b>Check blacklists</b> on MXToolbox for the domain.</li>
<li><b>Restart small:</b> a few emails a day per inbox, test placement, then ramp up over 1 to 2 weeks.</li>
<li><b>Retire the domain</b> if it does not recover. This is why you use secondary domains: swap in your warm spare and move on.</li>
</ol>
{real('<p>On a high-volume quarter, older data slipped into the list and bounces crept toward 3%. The daily check caught it. We paused the affected inboxes, re-verified the list and slowed the ramp. The campaign finished the quarter with <b>4,372 replies</b> and <b>1,061 interested buyers</b> from 118,387 people, about $100,000 in pipeline.</p>', 'Real client example: catching it early')}
{cta('Already stuck in spam?', 'Get a free review of your setup.', 'On a 20-minute call with our CEO we look at your domains, records and numbers and tell you honestly what we would change. If you want us to fix it, we can. If not, you keep the advice.', 'Book my free review', 'cta3-spam')}''')

# ---------------- Checklists
add(f'''<section class="chap" id="lists"><div class="num">Your tools</div><h1>The 30-day calendar and checklists</h1><p class="lead">Print these pages. Tick the boxes. This is the exact order we follow for every new client.</p></section>
{table(['Days', 'What gets done', 'Chapter'], [
 ['1', 'Worksheet filled in; registrar and sending platform accounts opened', '1, 2'],
 ['2', 'Domains bought (plus one spare), auto-renew on, system sheet started', '3'],
 ['3 to 4', 'Google Workspace set up, domains verified, users created, profiles and signatures done', '4'],
 ['4 to 5', 'MX, SPF, DKIM, DMARC added; DKIM started; all tests green; mail-tester 9/10+', '5'],
 ['5', 'Redirects live, inboxes connected, tracking off, warmup on', '6, 7'],
 ['6 to 12', 'ICP and triggers written; first list segment built, cleaned and verified', '9, 10'],
 ['13 to 18', 'Emails and follow-ups written for each segment; reply templates ready', '11, 12, 14'],
 ['19 to 21', 'Placement tests; Postmaster Tools set up; suppression list ready; final checklist', '8, 16'],
 ['22', 'Launch: 5 to 10 new people per inbox per day', '13'],
 ['23 to 30', 'Daily health check every morning; reply within an hour; slow ramp', '8, 13, 14'],
])}
<div class="grid2">
<div><h4>Pre-launch checklist</h4><ul class="check">
<li>Main domain is not used for any cold email</li><li>Every domain passes SPF, DKIM, DMARC</li><li>Only one SPF record per domain</li><li>Every inbox warmed for at least 14 days</li><li>Profile photo, real name, plain signature with address</li><li>Redirects point to your real site</li><li>Open and link tracking off</li><li>List verified within the last 60 days</li><li>Role addresses and duplicates removed</li><li>Suppression list loaded</li><li>Opt-out line in every email</li><li>Sending window set to the buyer\'s time zone</li><li>Stop-on-reply turned on</li><li>Placement test landed in the inbox</li></ul></div>
<div><h4>Daily (10 minutes)</h4><ul class="check">
<li>Bounce rate under 2% on every campaign</li><li>No disconnected inboxes</li><li>Warmup health steady</li><li>Interested replies answered within an hour</li><li>Opt-outs added to suppression list</li></ul>
<h4 style="margin-top:14px">Weekly</h4><ul class="check">
<li>Blacklist check on every domain</li><li>mail-tester score 9/10+</li><li>Manual placement test (Gmail, Outlook, Yahoo)</li><li>Test log updated, one decision made</li><li>Domain renewal dates checked</li><li>Show rate and cost per meeting reviewed</li></ul></div>
</div>''')

# ---------------- Final page
add(f'''<section class="chap final" id="final"><div class="num">The choice</div><h1>Do it yourself, or let us do it</h1>
<p class="lead">You now have the full method. It works. It is also a lot of daily, careful work. Here is the honest comparison.</p></section>
<div class="choice">
<div class="diy"><h3>Do it yourself</h3><ul>
<li>About 30 days from zero to first booked call</li><li>1 to 2 hours a day once running: checks, replies, lists, testing</li><li>Roughly $185 to $335 a month in tools to start</li><li>You learn by trial and error, and some errors cost a domain</li><li>Great if you have time and want to own the skill</li></ul>
<p style="margin-top:10px"><b>Everything you need is in this playbook. Go for it.</b></p></div>
<div class="dfy"><h3>Let WayneFlow do it</h3><ul>
<li>A team with <b>8 years</b> in outbound and B2B appointment setting</li><li>We have run campaigns for <b>dozens of companies</b> in the USA and Canada</li><li><b>588,000 emails</b> sent and <b>$510K+</b> in client pipeline in 2026 alone</li><li>We build the domains, inboxes, records, warmup, lists and emails</li><li>We answer every reply and book qualified buyers into your calendar</li><li>You spend your time on sales calls, not DNS records</li></ul></div>
</div>
{stats([('588,000', 'cold emails sent for clients'), ('12,900+', 'replies from buyers'), ('3,400+', 'buyers who asked to talk'), ('$510K+', 'pipeline for clients')])}
<div class="cta" style="margin-top:20px"><div class="faces"><img src="{A}/team/asim-sq.webp"><img src="{A}/team/ali-sq.webp"></div>
<div class="ct"><div class="ck">Free · 20 minutes · No pressure</div><h3>Book a 20-minute session with our CEO</h3><p>We look at your offer and your market, then show you who we would target, the angle we would use and how many meetings to expect. Even if you decide to do it yourself, you leave with a clear plan. One good client from this system can be worth thousands of dollars.</p></div>
<a class="btn" href="{cal('cta4-final')}">Book my call &rarr;</a></div>
<p style="text-align:center;margin-top:10px" class="small">Or open this link: <a href="{cal('cta4-final-link')}">calendly.com/learnwithasimshah</a> &nbsp;·&nbsp; See every live dashboard at <a href="{SITE}/results.html?utm_source=playbook">wayne-flow.site/results</a></p>
<p class="small" style="font-size:7.8pt;margin-top:12px;border-top:1px solid #E3E9F5;padding-top:10px">© 2026 WayneFlow by Ali &amp; Asim. All campaign numbers come from real client dashboards in 2026; pipeline is counted at our clients' average deal size of about $2,500. Past results do not guarantee future results; your results depend on your offer, market and execution. Tool names and prices belong to their owners and were checked in October 2026. This playbook is general information, not legal advice.</p>''')

BODY = f'<!doctype html><html><head><meta charset="utf-8"><title>The WayneFlow Cold Email Playbook</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>'

COVER = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0 }} * {{ box-sizing: border-box }} html {{ -webkit-print-color-adjust: exact }}
body {{ margin: 0; font-family: Inter, sans-serif }}
.c {{ width: 8.5in; height: 11in; padding: .6in .65in; position: relative; overflow: hidden; color: #fff; background: radial-gradient(circle at 85% 12%, rgba(95,211,255,.35), transparent 38%), linear-gradient(160deg,#0B1A3A 0%,#12306E 62%,#1F6BFF 135%) }}
.grid {{ position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.05) 1px, transparent 1px); background-size: 36px 36px }}
.top {{ display: flex; justify-content: space-between; align-items: center; position: relative }}
.logo {{ height: 34px; filter: brightness(0) invert(1) }}
.val {{ border: 1.5px solid #5FD3FF; color: #5FD3FF; border-radius: 99px; padding: 6px 14px; font-weight: 800; font-size: 12px; letter-spacing: .12em }}
.k {{ position: relative; margin-top: 1.15in; font-size: 13px; letter-spacing: .18em; text-transform: uppercase; color: #9CC1FF; font-weight: 800 }}
h1 {{ position: relative; font-family: 'Inter Display', Inter, sans-serif; font-size: 54px; line-height: 1.02; letter-spacing: -.035em; margin: 14px 0 0; font-weight: 800 }}
h1 em {{ font-style: normal; color: #5FD3FF }}
.sub {{ position: relative; font-size: 18.5px; line-height: 1.5; color: #D5E3FF; max-width: 30em; margin-top: 20px }}
.big {{ position: relative; display: grid; grid-template-columns: repeat(3,1fr); gap: 12px; margin-top: .55in }}
.big div {{ border: 1px solid rgba(255,255,255,.22); border-radius: 14px; padding: 15px 17px; background: rgba(255,255,255,.07) }}
.big b {{ display: block; font-size: 29px; font-weight: 800 }} .big span {{ font-size: 12.5px; color: #B9CCF2 }}
.in {{ position: relative; margin-top: .4in; display: grid; grid-template-columns: 1fr 1fr; gap: 6px 22px; font-size: 13.5px; color: #E2ECFF }}
.in div::before {{ content: '✓'; color: #5FD3FF; font-weight: 800; margin-right: 8px }}
.by {{ position: absolute; left: .65in; right: .65in; bottom: .6in; display: flex; align-items: center; gap: 14px; font-size: 13.5px; color: #D5E3FF; border-top: 1px solid rgba(255,255,255,.18); padding-top: 18px }}
.by img {{ width: 54px; height: 54px; border-radius: 50%; border: 2px solid #fff; object-fit: cover }} .by img + img {{ margin-left: -22px }}
.by b {{ color: #fff; display: block; font-size: 15px }}
</style></head><body><div class="c"><div class="grid"></div>
<div class="top"><img class="logo" src="{A}/logo.png"><span class="val">FREE · $300 VALUE</span></div>
<div class="k">The WayneFlow Cold Email Playbook</div>
<h1>From a blank domain to a <em>calendar full of sales calls.</em></h1>
<p class="sub">The complete, step-by-step manual setup behind 588,000 cold emails and $510K+ in client pipeline. Domains, inboxes, DNS records, warmup, lists, emails and replies, with the real numbers from our client dashboards.</p>
<div class="big"><div><b>588,000</b><span>cold emails sent for clients</span></div><div><b>3,400+</b><span>buyers who asked to talk</span></div><div><b>$510K+</b><span>pipeline for clients</span></div></div>
<div class="in"><div>17 chapters, every step by hand</div><div>Exact DNS records to copy</div><div>The 3-week warmup schedule</div><div>Real emails that got replies</div><div>The 10-minute daily health check</div><div>30-day launch calendar + checklists</div></div>
<div class="by"><img src="{A}/team/asim-sq.webp"><img src="{A}/team/ali-sq.webp"><div><b>WayneFlow by Ali &amp; Asim</b>8 years in outbound · B2B clients across the USA and Canada</div></div>
</div></body></html>'''

FOOT = '''<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#8A97AE;padding:0 .68in;display:flex;justify-content:space-between">
<span>The WayneFlow Cold Email Playbook · wayne-flow.site</span><span><span class="pageNumber"></span></span></div>'''

async def main():
    from playwright.async_api import async_playwright
    (HERE / 'pb_cover.html').write_text(COVER); (HERE / 'pb_body.html').write_text(BODY)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto(f'file://{HERE}/pb_cover.html'); await pg.wait_for_timeout(400)
        await pg.pdf(path=str(HERE / 'pb_cover.pdf'), format='Letter', print_background=True, prefer_css_page_size=True)
        await pg.goto(f'file://{HERE}/pb_body.html'); await pg.wait_for_timeout(800)
        await pg.pdf(path=str(HERE / 'pb_body.pdf'), format='Letter', print_background=True, prefer_css_page_size=True,
                     display_header_footer=True, header_template='<div></div>', footer_template=FOOT)
        await b.close()
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    w.append(str(HERE / 'pb_cover.pdf')); w.append(str(HERE / 'pb_body.pdf'))
    w.add_metadata({'/Title': 'The WayneFlow Cold Email Playbook', '/Author': 'WayneFlow by Ali & Asim', '/Subject': 'How to build a cold email system that books B2B sales calls'})
    out = HERE / 'wayneflow-cold-email-playbook.pdf'
    with open(out, 'wb') as f: w.write(f)
    print(out, len(PdfReader(str(out)).pages), 'pages')

asyncio.run(main())
