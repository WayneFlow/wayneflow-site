#!/usr/bin/env python3
"""Build the free guide pages for Instagram reels.

Each reel gets one data file:  guides/_data/<slug>.json
Running this script makes:
  guides/<slug>.html   one page per reel keyword
  guides/index.html    the main "Free guides" page (newest first)
and adds every guide to sitemap.xml.

The page shell (head, nav, footer) is copied from a live blog post, and the
case study is copied from results.html, so guides always match the site.

Usage:  python3 tools/build_guides.py            (publish: skips drafts)
        python3 tools/build_guides.py --preview  (local check: includes drafts)
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "guides" / "_data"
OUT = ROOT / "guides"
SITE = "https://wayneflow.com"
CAL = "https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers"
REF_PAGE = ROOT / "blog" / "dns-records-for-cold-email.html"
RESULTS = ROOT / "results.html"

BLOCK_TYPES = {"h2", "h3", "p", "list", "steps", "prompt", "tip", "quote", "image", "table"}

GUIDE_CSS = """<style>
.g-badge{flex-wrap:wrap;display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;background:#EEF3FD;color:var(--blue-d,#1747B5);font-weight:700;font-size:14px}
.g-badge b{background:var(--blue,#2563EB);color:#fff;border-radius:999px;padding:2px 10px;letter-spacing:.04em}
.g-prompt{position:relative;margin:22px 0 26px;border-radius:16px;background:#0B1A3A;color:#E8EEFF;box-shadow:0 10px 30px rgba(11,26,58,.18)}
.g-prompt .g-ph{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid rgba(255,255,255,.12);font-size:13.5px;font-weight:700;letter-spacing:.02em}
.g-prompt button{appearance:none;border:0;border-radius:10px;padding:8px 14px;background:#fff;color:#0B1A3A;font:700 13px/1 inherit;cursor:pointer}
.g-prompt pre{margin:0;padding:16px 18px;white-space:pre-wrap;word-break:break-word;font:14.5px/1.65 ui-monospace,SFMono-Regular,Menlo,monospace;background:none;color:inherit}
.g-steps{counter-reset:s;list-style:none;padding:0!important;margin:0 0 24px}
.g-steps li{counter-increment:s;position:relative;padding:16px 18px 16px 62px!important;margin:0 0 12px!important;background:#fff;border-radius:14px;box-shadow:0 0 0 1px var(--line)}
.g-steps li:before{content:counter(s);position:absolute;left:16px;top:14px;width:32px;height:32px;border-radius:50%;background:var(--blue,#2563EB);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.g-tip{margin:22px 0 26px;padding:16px 18px;border-radius:14px;background:#F2FBE4;border:1px solid #D7EDB8;font-size:16.5px;line-height:1.7;color:#24410F}
.g-tip b{color:#173404}
.g-insider{margin:34px 0;padding:22px 24px;border-radius:18px;background:linear-gradient(135deg,#EEF4FF,#F2FBE4);border:1px solid #D9E6FB}
.g-insider .kicker{display:inline-block;margin-bottom:10px}
.g-insider p{margin:0 0 12px;font-size:17px;line-height:1.75;color:#26324D}
.g-insider a{font-weight:700}
.g-res{display:grid;gap:10px;margin:0 0 24px}
.g-res a{display:block;padding:14px 16px;border-radius:14px;background:#fff;box-shadow:0 0 0 1px var(--line);text-decoration:none}
.g-res a b{display:block;color:var(--text)}.g-res a span{font-size:14.5px;color:var(--muted)}
.g-hero-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
.g-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--gap,20px);margin-top:28px}
@media (max-width:1000px){.g-list{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.g-list{grid-template-columns:1fr}.g-prompt pre{font-size:13.5px}}
.g-kw{align-self:flex-start;display:inline-block;font-size:12.5px;font-weight:800;letter-spacing:.06em;color:var(--blue-d,#1747B5);background:#EEF3FD;border-radius:999px;padding:4px 10px}
.g-search{width:100%;max-width:520px;margin-top:22px;padding:14px 16px;border-radius:14px;border:1px solid var(--line);font:16px inherit;background:#fff}
</style>"""

COPY_JS = """<script>
document.querySelectorAll('.g-prompt button').forEach(function(b){b.addEventListener('click',function(){var t=b.closest('.g-prompt').querySelector('pre').innerText;var done=function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1600)};if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,done)}else{done()}})});
var gs=document.getElementById('g-search');if(gs){gs.addEventListener('input',function(){var q=gs.value.toLowerCase();document.querySelectorAll('.g-list .post-card').forEach(function(c){c.style.display=c.innerText.toLowerCase().indexOf(q)>-1?'':'none'})})}
</script>"""


def esc(s):
    return html.escape(str(s or ""), quote=True)


def inline(s):
    """Escape text, then allow **bold** and [label](url) links."""
    t = esc(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+|/[^\s)]*)\)",
               lambda m: f'<a href="{m.group(2)}"' + ('' if m.group(2).startswith('/') else ' target="_blank" rel="noopener"') + f'>{m.group(1)}</a>', t)
    return t


def anchor(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40]


def shell():
    """Split the reference blog post into reusable head-tail, top (nav) and bottom (footer)."""
    s = REF_PAGE.read_text(encoding="utf-8")
    head_start = s[: s.index("<title>")]
    after_title = s[s.index('<link rel="icon"'): s.index("</head>")]
    # drop page-specific structured data, keep org + website
    after_title = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"(BlogPosting|BreadcrumbList|FAQPage)".*?</script>\n?', "", after_title, flags=re.S)
    org = re.findall(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"(?:ProfessionalService|WebSite)".*?</script>', s, flags=re.S)
    body_start = s.index("<body")
    top = s[body_start: s.index("<main>") + len("<main>")]
    bottom = s[s.index("</main>"):]
    top = top.replace('data-page="blog"', 'data-page="guides"')
    bottom = bottom.replace('dataset.page="blog"', 'dataset.page="guides"').replace('a.dataset.p==="blog"', 'a.dataset.p==="guides"')
    return head_start, after_title, top, bottom


def meta(title, desc, url, typ="article", published=None):
    t, d = esc(title), esc(desc)
    out = [f"<title>{t}</title>",
           f'<meta name="description" content="{d}">',
           '<meta name="robots" content="index, follow, max-image-preview:large">',
           f'<link rel="canonical" href="{url}">',
           f'<meta property="og:type" content="{typ}">']
    if published:
        out.append(f'<meta property="article:published_time" content="{published}">')
    out += ['<meta property="og:site_name" content="WayneFlow">', '<meta property="og:locale" content="en_US">',
            f'<meta property="og:url" content="{url}">', f'<meta property="og:title" content="{t}">',
            f'<meta property="og:description" content="{d}">', f'<meta property="og:image" content="{SITE}/assets/og.jpg">',
            '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
            '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{t}">',
            f'<meta name="twitter:description" content="{d}">', f'<meta name="twitter:image" content="{SITE}/assets/og.jpg">',
            '<meta name="theme-color" content="#FFFFFF">']
    return "\n".join(out) + "\n"


def case_block(case_id):
    if not case_id:
        return ""
    s = RESULTS.read_text(encoding="utf-8")
    m = re.search(r'<article class="case[^"]*" id="%s">.*?</article>' % re.escape(case_id), s, flags=re.S)
    if not m:
        sys.exit(f"Case study {case_id} not found in results.html")
    block = m.group(0).replace(' flip"', '"')
    return block


def render_blocks(blocks, insider_html):
    out, toc = [], []
    half = max(1, len(blocks) // 2)
    for i, b in enumerate(blocks):
        t = b.get("type")
        if t not in BLOCK_TYPES:
            sys.exit(f"Unknown block type: {t}")
        if t in ("h2", "h3"):
            a = anchor(b["text"])
            if t == "h2":
                toc.append((a, b["text"]))
            out.append(f'<{t} id="{a}">{inline(b["text"])}</{t}>')
        elif t == "p":
            out.append(f"<p>{inline(b['text'])}</p>")
        elif t == "list":
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in b["items"]) + "</ul>")
        elif t == "steps":
            out.append('<ol class="g-steps">' + "".join(f"<li>{inline(x)}</li>" for x in b["items"]) + "</ol>")
        elif t == "prompt":
            out.append(f'<div class="g-prompt"><div class="g-ph"><span>{esc(b.get("label", "Copy this"))}</span><button type="button">Copy</button></div><pre>{esc(b["text"])}</pre></div>')
        elif t == "tip":
            out.append(f'<div class="g-tip"><b>{esc(b.get("label", "Pro tip"))}:</b> {inline(b["text"])}</div>')
        elif t == "quote":
            out.append(f"<blockquote>{inline(b['text'])}</blockquote>")
        elif t == "image":
            out.append(f'<p><img src="{esc(b["src"])}" alt="{esc(b.get("alt", ""))}" loading="lazy" style="width:100%;height:auto;border-radius:14px;box-shadow:0 0 0 1px var(--line)"></p>')
        elif t == "table":
            head = "".join(f"<th>{inline(c)}</th>" for c in b["head"])
            rows = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in b["rows"])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>")
        if i == half - 1 and insider_html:
            out.append(insider_html)
    return "\n".join(out), toc


def guide_page(g, sh):
    head_start, after_title, top, bottom = sh
    slug = g["slug"]
    url = f"{SITE}/guides/{slug}.html"
    title = g["title"]
    published = g["date"]
    nice_date = date.fromisoformat(published).strftime("%B %-d, %Y")
    insider = ""
    if g.get("insider"):
        insider = (f'<div class="g-insider"><span class="kicker">How we use this at WayneFlow</span>'
                   f'<p>{inline(g["insider"])}</p>'
                   f'<a href="{CAL}" target="_blank" rel="noopener">Want us to set this up for you? Book a free call →</a></div>')
    body, toc = render_blocks(g["blocks"], insider)

    res = ""
    if g.get("resources"):
        res = '<h2 id="resources">Links and tools</h2><div class="g-res">' + "".join(
            f'<a href="{esc(r["url"])}" target="_blank" rel="noopener"><b>{esc(r["name"])}</b><span>{esc(r.get("note", ""))}</span></a>' for r in g["resources"]) + "</div>"
        toc.append(("resources", "Links and tools"))

    faq_html, faq_ld = "", ""
    if g.get("faq"):
        faq_html = '<h2 id="faq">Quick answers</h2>' + "".join(f"<h3>{esc(f['q'])}</h3><p>{inline(f['a'])}</p>" for f in g["faq"])
        toc.append(("faq", "Quick answers"))
        faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\*\*|\[|\]\([^)]*\)", "", f["a"])}} for f in g["faq"]]}) + "</script>\n"

    art_ld = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": title, "description": g["description"],
        "mainEntityOfPage": url, "datePublished": published, "dateModified": published,
        "author": [{"@type": "Person", "name": "Syed Asim Hussain"}, {"@type": "Person", "name": "Syed Ali Hassan"}],
        "publisher": {"@id": f"{SITE}/#org"}, "image": f"{SITE}/assets/og.jpg"}) + "</script>\n"
    crumbs_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Free guides", "item": f"{SITE}/guides/"},
        {"@type": "ListItem", "position": 3, "name": title, "item": url}]}) + "</script>\n"

    toc_html = "".join(f'<a href="/guides/{slug}.html#{a}">{esc(t)}</a>' for a, t in toc)
    case_html = case_block(g.get("case"))
    case_sec = ""
    if case_html:
        case_sec = f'<section class="sec" style="padding-top:0"><div class="wrap">{case_html}</div></section>'

    kw = esc(g["keyword"].upper())
    page = (head_start + meta(title + " | WayneFlow", g["description"], url, "article", published) + after_title
            + art_ld + crumbs_ld + faq_ld + GUIDE_CSS + "\n</head>\n" + top + f"""
<section class="sec post">
  <div class="wrap">
    <div class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/guides/">Free guides</a><span>/</span><span>{esc(title)}</span></div>
    <header class="post-head"><span class="g-badge">You commented <b>{kw}</b></span><h1>{esc(title)}</h1><p class="lead">{inline(g["lead"])}</p>
      <div class="byline"><span class="author-photos"><img src="/assets/team/asim-sq.webp" alt="Syed Asim Hussain" width="44" height="44"><img src="/assets/team/ali-sq.webp" alt="Syed Ali Hassan" width="44" height="44"></span><div><b>By <a href="/about.html" style="color:inherit">Syed Asim Hussain &amp; Syed Ali Hassan</a></b><span>Published <time datetime="{published}">{nice_date}</time> · From our Instagram <a href="https://www.instagram.com/wayneflowagency/" target="_blank" rel="noopener" style="color:inherit">@wayneflowagency</a></span></div></div>
    </header>
    <div class="post-grid">
      <aside class="post-toc"><details><summary>On this page</summary>{toc_html}</details>
        <div class="toc-cta"><b>Rather have us do it?</b><p>2–5 sales calls every day, guaranteed.</p><a class="btn btn-primary btn-sm" href="{CAL}" target="_blank" rel="noopener">Talk to our founder</a></div>
        <a class="toc-pb" href="/free-cold-email-playbook.html"><img src="/assets/img/playbook-cover.webp" alt="Free cold email playbook" width="60" height="78" loading="lazy"><span><b>Free cold email playbook</b>35 pages · 7 real case studies</span></a></aside>
      <article class="post-body">
{body}
{res}
{faq_html}
        <div class="soft-cta"><h2>Want all of this done for you?</h2><p>Save the setup time. Our team finds your buyers, writes the emails, answers every reply and books qualified sales calls into your calendar. Talk to our founder for 20 minutes and you will leave with a plan, whether you work with us or not.</p><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a call with our founder</a></div>
      </article>
    </div>
  </div>
</section>
{case_sec}
<div class="wrap"><div class="band reveal"><div><h2>2–5 sales calls every day. Guaranteed.</h2><p>Liked this guide? This is a small piece of the system we run for our clients. Book a free 20-minute call and we will show you how it would work for your company.</p></div><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div></div>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Screenshot"><button type="button" aria-label="Close">✕</button><div><img alt=""><p></p></div></div>
""" + bottom.replace("</body>", COPY_JS + "\n</body>"))
    return page


def hub_page(guides, sh):
    head_start, after_title, top, bottom = sh
    url = f"{SITE}/guides/"
    cards = "".join(
        f'<a class="card post-card" href="/guides/{g["slug"]}.html"><span class="g-kw">{esc(g["keyword"].upper())}</span>'
        f'<h3>{esc(g["title"])}</h3><p>{esc(g["description"])}</p><span class="go">Open the free guide →</span></a>' for g in guides)
    title = "Free Cold Email Guides from Our Instagram | WayneFlow"
    desc = "Every free guide, prompt and template from the WayneFlow Instagram reels in one place. Commented a keyword? Find your guide here."
    return (head_start + meta(title, desc, url, "website") + after_title + GUIDE_CSS + "\n</head>\n" + top + f"""
<section class="sec post">
  <div class="wrap">
    <div class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span>Free guides</span></div>
    <header class="post-head"><span class="kicker">Free guides · {len(guides)} and counting</span><h1>Every free guide from our reels, in one place.</h1>
      <p class="lead">Commented a keyword on one of our Instagram reels? Your guide is here. New guides are added every day.</p>
      <input class="g-search" id="g-search" type="search" placeholder="Search by keyword, like CLAUDE" aria-label="Search guides">
      <div class="g-hero-cta"><a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Want it done for you? Book a call</a><a class="btn" href="/free-cold-email-playbook.html">Get the free 35-page playbook</a></div>
    </header>
    <div class="g-list">{cards}</div>
  </div>
</section>
<div class="wrap"><div class="band reveal"><div><h2>2–5 sales calls every day. Guaranteed.</h2><p>We find your buyers, write the emails, answer every reply and book qualified sales calls into your calendar.</p></div><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a></div></div>
""" + bottom.replace("</body>", COPY_JS + "\n</body>"))


def check(g, path):
    need = ["slug", "keyword", "title", "description", "lead", "date", "blocks"]
    miss = [k for k in need if not g.get(k)]
    if miss:
        sys.exit(f"{path.name}: missing {', '.join(miss)}")
    if not re.fullmatch(r"[a-z0-9-]+", g["slug"]):
        sys.exit(f"{path.name}: slug must be lowercase letters, numbers and dashes")
    if path.stem != g["slug"]:
        sys.exit(f"{path.name}: file name must match slug '{g['slug']}'")
    date.fromisoformat(g["date"])


def update_sitemap(guides):
    p = ROOT / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"\s*<url><loc>https://wayneflow\.com/guides/[^<]*</loc>.*?</url>", "", s)
    today = date.today().isoformat()
    add = [f'  <url><loc>{SITE}/guides/</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>']
    add += [f'  <url><loc>{SITE}/guides/{g["slug"]}.html</loc><lastmod>{g["date"]}</lastmod><priority>0.7</priority></url>' for g in guides]
    s = s.replace("</urlset>", "\n".join(add) + "\n</urlset>")
    p.write_text(s, encoding="utf-8")


def main():
    sh = shell()
    guides = []
    for path in sorted(DATA.glob("*.json")):
        g = json.loads(path.read_text(encoding="utf-8"))
        if g.get("draft") and "--preview" not in sys.argv:
            continue
        check(g, path)
        guides.append(g)
    guides.sort(key=lambda g: (g["date"], g["slug"]), reverse=True)
    for g in guides:
        (OUT / f"{g['slug']}.html").write_text(guide_page(g, sh), encoding="utf-8")
    (OUT / "index.html").write_text(hub_page(guides, sh), encoding="utf-8")
    update_sitemap(guides)
    print(f"Built {len(guides)} guide page(s) + guides/index.html")


if __name__ == "__main__":
    main()
