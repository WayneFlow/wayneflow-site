"""WayneFlow website tracking report -> PDF.
Usage: python3 make_report.py data.json out.pdf
data.json keys: title, period, generated, kpis{...}, daily[ {day,visitors,outside,leads,book_clicks,popups,popup_closed} ],
sources[[name,visitors]], countries[[name,visitors]], devices[[name,visitors]], pages[[page,views]],
leads[ {when,email,phone,country,device,source,intent,note} ], book_clicks[ {when,country,device,source,button} ],
insights[str], actions[str]
"""
import json, sys, base64, io, html
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

d = json.load(open(sys.argv[1])); out = sys.argv[2]
BLUE, DARK, GREEN, ORANGE, MUTED, LINE = '#1F63F0', '#0B1A3A', '#11865A', '#E8890C', '#5B6B86', '#E3E8F2'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#C9D2E3', 'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': MUTED})
def img(fig):
    b = io.BytesIO(); fig.savefig(b, format='png', dpi=200, bbox_inches='tight', transparent=True); plt.close(fig)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
def esc(x): return html.escape(str(x))

charts = {}
days = d.get('daily', [])
if days:
    lab = [x['day'][5:] for x in days]
    fig, ax = plt.subplots(figsize=(7.2, 1.85))
    ax.bar(lab, [x['visitors'] for x in days], color='#C9D8FB', label='All visitors', width=.6)
    ax.bar(lab, [x.get('outside', 0) for x in days], color=BLUE, label='Outside Pakistan', width=.6)
    for i, x in enumerate(days):
        ax.text(i, x['visitors'] + .4, str(x['visitors']), ha='center', color=DARK, fontsize=8)
    ax2 = ax.twinx(); ax2.plot(lab, [x['leads'] for x in days], color=GREEN, marker='o', lw=2, label='Emails')
    ax2.plot(lab, [x['book_clicks'] for x in days], color=ORANGE, marker='s', lw=2, label='Booking clicks')
    ax2.set_ylim(0, max(4, max([x['leads'] for x in days] + [x['book_clicks'] for x in days]) + 1)); ax2.spines['top'].set_visible(False)
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, frameon=False, ncol=4, loc='upper left', bbox_to_anchor=(0, 1.22), fontsize=8)
    charts['daily'] = img(fig)
def hbar(rows, color, key):
    if not rows: return
    rows = rows[:8][::-1]
    fig, ax = plt.subplots(figsize=(3.4, .32 * len(rows) + .4))
    ax.barh([r[0] for r in rows], [r[1] for r in rows], color=color, height=.6)
    for i, r in enumerate(rows): ax.text(r[1] + .2, i, str(r[1]), va='center', fontsize=8, color=DARK)
    ax.set_xticks([]); ax.spines['bottom'].set_visible(False)
    charts[key] = img(fig)
hbar(d.get('sources', []), BLUE, 'sources'); hbar(d.get('countries', []), '#5B8DFF', 'countries')
hbar(d.get('pages', []), '#7FA6F7', 'pages')
f = d.get('funnel')
if f:
    fig, ax = plt.subplots(figsize=(7.2, 1.45))
    names = [x[0] for x in f]; vals = [x[1] for x in f]
    cols = [BLUE, '#5B8DFF', ORANGE, GREEN][:len(f)]
    ax.barh(names[::-1], vals[::-1], color=cols[::-1], height=.62)
    for i, v in enumerate(vals[::-1]): ax.text(v + max(vals) * .01, i, str(v), va='center', fontsize=9, color=DARK, fontweight='bold')
    ax.set_xticks([]); ax.spines['bottom'].set_visible(False)
    charts['funnel'] = img(fig)

k = d['kpis']
kpi_html = ''.join(f'<div class="kpi {c}"><b>{esc(v)}</b><span>{esc(l)}</span>{("<i>"+esc(s)+"</i>") if s else ""}</div>' for l, v, s, c in k)
def table(rows, cols):
    if not rows: return '<p class="muted">None yet.</p>'
    th = ''.join(f'<th>{esc(c[1])}</th>' for c in cols)
    tr = ''.join('<tr>' + ''.join(f'<td class="{c[0]}">{esc(r.get(c[0], "") or "–")}</td>' for c in cols) + '</tr>' for r in rows)
    return f'<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
leads_t = table(d.get('leads', []), [('when', 'When (PKT)'), ('email', 'Email'), ('phone', 'Phone'), ('country', 'Country'), ('source', 'Came from'), ('intent', 'Intent')])
book_t = table(d.get('book_clicks', []), [('when', 'When (PKT)'), ('country', 'Country'), ('device', 'Device'), ('source', 'Came from'), ('button', 'Button')])
ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
ch = lambda key, cap: f'<figure><figcaption>{cap}</figcaption><img src="{charts[key]}"></figure>' if key in charts else ''

page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 14mm 13mm; }}
* {{ box-sizing: border-box; }} body {{ font-family: 'DejaVu Sans', Arial, sans-serif; color: {DARK}; font-size: 10.5px; margin: 0; }}
.top {{ background: linear-gradient(120deg,#0B1A3A,#1F4FD0); color: #fff; border-radius: 14px; padding: 18px 22px; display:flex; justify-content:space-between; align-items:flex-end; }}
.top h1 {{ margin: 0; font-size: 21px; }} .top p {{ margin: 4px 0 0; color: #C7D6FF; font-size: 11px; }} .top .r {{ text-align:right; font-size:10px; color:#C7D6FF }}
.kpis {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 12px 0; }}
.kpi {{ border: 1px solid {LINE}; border-radius: 12px; padding: 10px 12px; background: #F7F9FD; }}
.kpi b {{ display: block; font-size: 22px; color: {BLUE}; }} .kpi.g b {{ color: {GREEN}; }} .kpi.o b {{ color: {ORANGE}; }}
.kpi span {{ font-size: 10px; color: {MUTED}; font-weight: bold; text-transform: uppercase; letter-spacing: .03em; }} .kpi i {{ display:block; font-style:normal; font-size:9.5px; color:{MUTED}; margin-top:2px }}
h2 {{ font-size: 13.5px; margin: 14px 0 6px; padding-bottom: 4px; border-bottom: 2px solid {LINE}; }}
.box {{ border-radius: 12px; padding: 10px 14px; background: #EEF4FF; border-left: 4px solid {BLUE}; }} .box.g {{ background:#E8F6EF; border-color:{GREEN} }}
.box ul {{ margin: 4px 0; padding-left: 16px; }} .box li {{ margin: 3px 0; line-height: 1.45; }}
.grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
figure {{ margin: 0; break-inside: avoid; }} table {{ break-inside: avoid; }} figcaption {{ font-weight: bold; font-size: 10.5px; margin-bottom: 3px; }} figure img {{ width: 100%; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9.5px; }} th {{ text-align: left; background: #F1F4FA; color: {MUTED}; padding: 5px 6px; }}
td {{ padding: 5px 6px; border-bottom: 1px solid {LINE}; vertical-align: top; }} td.email {{ font-weight: bold; }} td.intent {{ font-weight:bold }}
.muted {{ color: {MUTED}; }} .foot {{ margin-top: 12px; color: {MUTED}; font-size: 9px; }} .pb {{ break-before: page; }}
</style></head><body>
<div class="top"><div><h1>{esc(d["title"])}</h1><p>{esc(d["period"])}</p></div><div class="r">WayneFlow · wayneflow.com<br>{esc(d["generated"])}</div></div>
<div class="kpis">{kpi_html}</div>
<h2>Bottom line</h2><div class="box">{ul(d.get("insights", []))}</div>
{ch("funnel", "From visit to booked call")}
{ch("daily", "Every day")}
<h2>Leads collected (emails and phone numbers)</h2>{leads_t}
<h2>Clicked "Book a call" (buying signal)</h2>{book_t}
<div style="break-inside:avoid">
<div class="grid2">{ch("sources", "Where visitors came from")}{ch("countries", "Countries")}</div></div>
<div class="grid2" style="margin-top:8px">{ch("pages", "Most viewed pages")}<div><figcaption>Devices and engagement</figcaption>{ul(d.get("engagement", []))}</div></div>
<h2>What to do next</h2><div class="box g">{ul(d.get("actions", []))}</div>
<p class="foot">{esc(d.get("footnote", ""))}</p>
</body></html>'''
open(out.replace('.pdf', '.html'), 'w').write(page)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.set_content(page, wait_until='load')
    pg.pdf(path=out, format='A4', print_background=True, margin={'top': '14mm', 'bottom': '14mm', 'left': '13mm', 'right': '13mm'}); b.close()
print('ok', out)
