import asyncio
from pypdf import PdfReader, PdfWriter
A='file:///home/claude/site8/assets'
URL='https://wayneflow.com/free-cold-email-playbook.html?utm_source=preview-pdf&amp;utm_medium=pdf'
END=f'''<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:Letter;margin:0}}html{{-webkit-print-color-adjust:exact}}body{{margin:0;font-family:Inter,sans-serif}}
.c{{width:8.5in;height:11in;padding:.9in .8in;box-sizing:border-box;color:#fff;background:radial-gradient(circle at 85% 12%,rgba(95,211,255,.35),transparent 40%),linear-gradient(160deg,#0B1A3A,#12306E 62%,#1F6BFF 135%);display:flex;flex-direction:column;justify-content:center}}
.k{{letter-spacing:.18em;text-transform:uppercase;font-weight:800;color:#7DF0B1;font-size:13px}}h1{{font-size:46px;line-height:1.05;letter-spacing:-.03em;margin:14px 0}}p{{font-size:18px;line-height:1.55;color:#D5E3FF;max-width:30em}}
ul{{font-size:16px;color:#E2ECFF;line-height:1.9;padding-left:20px}}a.b{{display:inline-block;margin-top:26px;background:#fff;color:#1556D6;font-weight:800;text-decoration:none;padding:16px 26px;border-radius:14px;font-size:20px}}img{{width:150px;transform:rotate(-4deg);border-radius:8px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6);margin-bottom:24px}}</style></head><body><div class="c">
<img src="{A}/img/playbook-cover.webp"><div class="k">This was a preview</div><h1>Get the full 35-page playbook, free.</h1>
<p>You just read a few pages. The full playbook has all 17 chapters and 7 real case studies with dashboards:</p>
<ul><li>The exact Google Workspace setup and all four DNS records</li><li>The 3-week warmup schedule and the 10-minute daily health check</li><li>Building and verifying lists by hand</li><li>Real emails, follow-ups and the replies that book the call</li><li>U.S. and Canadian law, spam recovery and a 30-day launch calendar</li></ul>
<a class="b" href="{URL}">Get the full playbook free &rarr;</a><p style="font-size:14px;margin-top:14px">wayneflow.com/free-cold-email-playbook.html</p></div></body></html>'''
async def main():
    from playwright.async_api import async_playwright
    open('pv_end.html','w').write(END)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto('file:///home/claude/pdf_lm/pv_end.html'); await pg.wait_for_timeout(400)
        await pg.pdf(path='pv_end.pdf',format='Letter',print_background=True,prefer_css_page_size=True); await b.close()
    r=PdfReader('wayneflow-cold-email-playbook.pdf'); w=PdfWriter()
    for n in [1,2,3,4,5,11,12,13,17]: w.add_page(r.pages[n-1])
    w.append('pv_end.pdf')
    w.add_metadata({'/Title':'The WayneFlow Cold Email Playbook (Free Preview)','/Author':'WayneFlow by Ali & Asim'})
    w.write('wayneflow-cold-email-playbook-preview.pdf'); print(len(w.pages))
asyncio.run(main())
