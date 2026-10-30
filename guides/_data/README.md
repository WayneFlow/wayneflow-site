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
