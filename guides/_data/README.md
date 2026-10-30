# Guide data files

One JSON file per reel keyword: `<slug>.json` (slug = keyword in lowercase, e.g. `three.json` for THREE).
Run `python3 tools/build_guides.py` to build `/guides/<slug>.html`, `/guides/index.html` and the sitemap.
`"draft": true` keeps a guide off the live site (use `--preview` to build drafts locally).

Fields: slug, keyword, date (YYYY-MM-DD), title, description, lead, insider, case (case-01 ... from results.html), blocks, resources, faq.
Block types: h2, h3, p, list, steps, prompt, tip, quote, image, table. Text supports **bold** and [label](url).

## InstantDM status (used by the hourly checker)
- `"instantdm": "pending"`: guide page is live, the InstantDM automation still has to be made.
- `"instantdm": "live"`: automation made and turned on (add `"instantdm_flow": "<flow name>"`).
- `"instantdm": "skip"`: old reel, owner said not to make an automation.
- `"reel_status"`: optional note, e.g. "made 2026-10-30, not uploaded yet".

## Quality standard for every guide (read before writing one)
A guide must be genuinely useful on its own, even if the reader never hires us. Match the depth of math.json, well.json, dead.json and funnel.json:
- 20+ blocks. Explain **why** each step works, then **exactly how** to do it (steps, tables, templates, worked example with real numbers).
- Include at least: one worked example, one "common mistakes" or "problem finder" table, one copy-paste prompt, 3–4 FAQs.
- Every outside number must come from a real source found by web search that day (prefer the original report: Hunter, Instantly, Google, Microsoft). Name the source in the text and link it; add it to `resources`.
- Our own numbers only from results.html case studies. Never invent numbers, clients or results.
- Selling stays light: the insider box, the case study and the CTA (added automatically). No pitch inside the teaching blocks.
- Plain, simple English (short sentences; many readers are not native speakers).
- Check the math in every example before publishing.
