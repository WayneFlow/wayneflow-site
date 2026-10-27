import sys, html
sys.path.insert(0, '/home/claude')
from blog_build import CASES
A = 'file:///home/claude/site8/assets'
CAL = 'https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers'
IMG = {'agency':'agency','construction':'construction','blitz':'blitz','quarter':'q1','pilot':'pilot','linkedin':'linkedin'}
LESSON = {
 'agency':'Consistency beats bursts. About 100 interested replies a week, every week, came from steady daily sending and a list that kept getting sharper.',
 'construction':'Judge cold email by contracts, not replies. 4,449 replies became 31 qualified demos and 6 annual deals because every reply was handled fast.',
 'blitz':'Speed needs preparation. Warm inboxes and a verified list made a five day push possible, with a bounce rate under half a percent.',
 'quarter':'Volume only works with hygiene. 236,545 emails stayed out of spam because every list was verified and daily volume per inbox stayed low.',
 'pilot':'Test small before you scale. Ten thousand well-chosen contacts were enough to prove the offer before spending more.',
 'linkedin':'Go where the buyer reads. For founders and investors, LinkedIn opened conversations that email alone would not have.',
}
def case(k):
    cid, label, head, desc, stats = CASES[k]
    tiles = ''.join(f'<div class="t"><b>{html.escape(v)}</b><span>{html.escape(l)}</span></div>' for v, l in stats)
    return f'''<section class="case"><div class="ck">{cid.replace('case-','Case ')} · {html.escape(label)}</div>
<h2>{html.escape(head)}</h2><p>{html.escape(desc)}</p><div class="tiles">{tiles}</div>
<div class="shot"><img src="{A}/img/{IMG[k]}-hd.webp"></div>
<p class="lesson"><b>The lesson:</b> {html.escape(LESSON[k])}</p></section>'''
keys = list(CASES)
pages = ''.join(f'<div class="page">{case(keys[i])}{case(keys[i+1])}<div class="foot">WayneFlow · wayne-flow.site · Real campaign data. Results vary.</div></div>' for i in range(0, 6, 2))
doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0 }}
* {{ box-sizing: border-box }} body {{ margin: 0; font-family: Inter, sans-serif; color: #0B1A3A }}
.page {{ width: 8.5in; height: 11in; padding: .55in .6in; position: relative; page-break-after: always; overflow: hidden }}
.cover {{ background: linear-gradient(160deg, #0B1A3A 0%, #12306E 60%, #1F6BFF 130%); color: #fff }}
.logo {{ height: 34px; filter: brightness(0) invert(1) }}
.kick {{ margin-top: 1.3in; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; color: #9CC1FF; font-weight: 700 }}
.cover h1 {{ font-family: 'Inter Display', Inter, sans-serif; font-size: 50px; line-height: 1.04; letter-spacing: -.03em; margin: 14px 0 0; font-weight: 800 }}
.cover h1 em {{ font-style: normal; color: #5FD3FF }}
.cover .sub {{ font-size: 19px; line-height: 1.5; color: #D5E3FF; max-width: 30em; margin-top: 22px }}
.big {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: .7in }}
.big div {{ border: 1px solid rgba(255,255,255,.2); border-radius: 14px; padding: 16px 18px; background: rgba(255,255,255,.06) }}
.big b {{ display: block; font-size: 30px; font-weight: 800 }} .big span {{ font-size: 13px; color: #B9CCF2 }}
.by {{ position: absolute; left: .6in; bottom: .6in; display: flex; align-items: center; gap: 14px; font-size: 14px; color: #D5E3FF }}
.by img {{ width: 52px; height: 52px; border-radius: 50%; border: 2px solid #fff; object-fit: cover }} .by img + img {{ margin-left: -20px }}
.by b {{ color: #fff; display: block; font-size: 15px }}
.case + .case {{ margin-top: .32in; padding-top: .3in; border-top: 1px solid #E3E9F5 }}
.ck {{ font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; color: #1556D6 }}
.case h2 {{ font-family: 'Inter Display', Inter, sans-serif; font-size: 25px; letter-spacing: -.02em; margin: 6px 0 6px; line-height: 1.15 }}
.case p {{ margin: 0; font-size: 13px; line-height: 1.55; color: #3E4C66 }}
.tiles {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 12px 0 }}
.t {{ background: #F2F6FD; border-radius: 10px; padding: 9px 11px }} .t b {{ display: block; font-size: 19px; color: #1F6BFF }} .t span {{ font-size: 11px; color: #5B6B85 }}
.t:last-child b {{ color: #0E8A4B }}
.shot {{ border: 1px solid #E3E9F5; border-radius: 10px; overflow: hidden; height: 1.55in; background: #fff }} .shot img {{ width: 100%; height: 100%; object-fit: cover; object-position: top }}
.lesson {{ margin-top: 10px !important; background: #FFF8E6; border-radius: 8px; padding: 8px 11px }}
.foot {{ position: absolute; bottom: .32in; left: .6in; right: .6in; font-size: 10px; color: #8A97AE; border-top: 1px solid #E3E9F5; padding-top: 8px }}
.how h2 {{ font-family: 'Inter Display', Inter, sans-serif; font-size: 30px; letter-spacing: -.02em; margin: 0 0 6px }}
.how > p {{ color: #3E4C66; font-size: 14px; margin: 0 0 18px }}
.steps {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px }}
.steps div {{ border: 1px solid #E3E9F5; border-radius: 12px; padding: 14px 16px }} .steps b {{ display: block; font-size: 15px; margin-bottom: 4px }} .steps span {{ font-size: 12.5px; color: #3E4C66; line-height: 1.5 }}
.steps i {{ font-style: normal; display: inline-grid; place-items: center; width: 22px; height: 22px; border-radius: 6px; background: #1F6BFF; color: #fff; font-size: 12px; font-weight: 800; margin-right: 8px }}
.rules {{ margin-top: 22px }} .rules h3 {{ font-size: 18px; margin: 0 0 8px }}
.rules li {{ font-size: 13px; color: #3E4C66; margin: 6px 0; line-height: 1.5 }}
.cta {{ margin-top: 26px; background: linear-gradient(120deg, #1F6BFF, #19B4E6); color: #fff; border-radius: 16px; padding: 22px 24px }}
.cta b {{ display: block; font-size: 22px }} .cta p {{ margin: 6px 0 12px; color: #E6F0FF; font-size: 14px }}
.cta a {{ display: inline-block; background: #fff; color: #1556D6; font-weight: 800; text-decoration: none; padding: 10px 18px; border-radius: 10px; font-size: 14px }}
</style></head><body>
<div class="page cover"><img class="logo" src="{A}/logo.png">
<div class="kick">The WayneFlow case study pack</div>
<h1>6 campaigns. 588,000 emails. <em>The real numbers.</em></h1>
<p class="sub">Six cold email and LinkedIn campaigns we ran in 2026, with the dashboard screenshot behind every number, and the lesson you can copy into your own outbound.</p>
<div class="big"><div><b>588,000</b><span>cold emails sent</span></div><div><b>3,400+</b><span>buyers asked to talk</span></div><div><b>$510K+</b><span>pipeline for clients</span></div></div>
<div class="by"><img src="{A}/team/asim-sq.webp"><img src="{A}/team/ali-sq.webp"><div><b>WayneFlow by Ali &amp; Asim</b>8 years in outbound · clients in the USA and Canada</div></div></div>
{pages}
<div class="page how"><h2>How every campaign was built</h2><p>The same four steps sit behind all six results.</p>
<div class="steps">
<div><b><i>1</i>Find the buyers</b><span>We list the decision makers who match the client's best customers and verify every email before anything is sent.</span></div>
<div><b><i>2</i>Protect the domain</b><span>We send from separate domains we set up and warm. The client's main domain is never touched.</span></div>
<div><b><i>3</i>Write emails people answer</b><span>Short, plain and about the buyer's problem. The client approves every email before it goes out.</span></div>
<div><b><i>4</i>Book the meeting</b><span>We reply, follow up and qualify. Interested buyers land on the client's calendar with a short brief.</span></div></div>
<div class="rules"><h3>Five rules you can use today</h3><ol>
<li><b>Never send cold email from your main domain.</b> Use a separate domain and inboxes, and warm them for about two weeks first.</li>
<li><b>Verify every list.</b> Our bounce rates stayed between 0.45% and about 3% because nothing went out unverified.</li>
<li><b>Turn open tracking off.</b> Tracking pixels push emails toward spam. Measure replies and booked meetings instead.</li>
<li><b>Keep emails under 100 words.</b> One problem, one short proof point, one easy question.</li>
<li><b>Follow up with something new.</b> Three to five emails, each adding a fact or a result, never "just bumping this".</li></ol></div>
<div class="cta"><b>Want numbers like these for your company?</b><p>Book a free 20-minute call. We will show you who we would target, the angle we would use and how many meetings to expect.</p><a href="{CAL}">Book a 20-minute call</a></div>
<div class="foot">WayneFlow · wayne-flow.site · Every number comes from a live campaign dashboard. These are real past campaigns, not a promise; your results depend on your offer and market.</div></div>
</body></html>'''
open('pack.html', 'w').write(doc)
