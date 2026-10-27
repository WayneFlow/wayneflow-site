# WayneFlow blog writing brief (read fully)

## The company
WayneFlow ("WayneFlow by Ali & Asim") is a done-for-you B2B appointment setting agency. It runs cold email and LinkedIn outreach for U.S. B2B companies (agencies, B2B SaaS, construction software, professional services, founder/investor outreach) and books qualified sales appointments into clients' calendars. Offer: "25 qualified sales appointments a month. Guaranteed." (guarantee details are covered on a strategy call; never invent terms or prices). Booking link: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers
Site pages you may link to (relative links): results.html (case studies with live dashboards), process.html (4-step process), areas.html (all 50 states), book.html (book a call + FAQ), reviews.html.

## Real WayneFlow data (the ONLY first-party numbers you may use; never invent others)
- Totals: 588,000 emails sent, 12,900+ replies, 3,400+ interested buyers, 100+ calls/demos booked, 6 annual contracts signed, $510K+ pipeline generated.
- Agency client (Jun 1 to Oct 19, 2026): 82,671 emails sent, 76,081 people contacted, 2,429 replies (about 2.9% of emails; dashboard shows 3.19% reply rate), 2,146 positive/interested replies, bounce 1.64%. Pipeline $175,000.
- Construction software client: 162,073 emails sent, 158,322 contacted, 4,449 replies (2.81%), 31 sales-qualified demos held, 6 annual contracts signed, $15,000 in closed deals for the client. Bounce 2.87%.
- 5-day blitz (Sep 7 to 11, 2026): 96,408 emails in 5 days, 79,587 contacted, 1,095 replies, 115 interested, 25 calls booked, bounce 0.45%. Pipeline $62,500.
- Full quarter (Jan to Mar 2026): 236,545 emails, 118,387 contacted, 4,372 replies (3.69%), 1,061 interested, bounce 3.08%. Pipeline $100,000.
- Small pilot: 10,284 contacted, 417 replied (4%), 103 opportunities. Pipeline $150,000 is shown on site; prefer not to use it.
- LinkedIn (all time): 3,511 profile views, 1,375 invites, 351 accepted, 1,628 InMails, 154 replies (founders and angel investors). Pipeline $7,500.
- Practices: open tracking switched OFF on purpose (tracking pixels hurt deliverability; dashboards show 0 opens); separate secondary sending domains so the client's main domain is never at risk; lists verified before sending; emails sent weekdays in business hours in the prospect's time zone; reply rates 2.8% to 4% vs a typical ~1%; "pipeline" = value of qualified opportunities at clients' ~$2,500 average deal.

## Style: original U.S. B2B style
- American English and spelling. Confident, plain, specific. Short paragraphs (1 to 3 sentences). Concrete numbers, examples, checklists, mini case studies. Write like a senior practitioner who has run hundreds of campaigns, not a content farm. No fluff intros, no "In today's fast-paced world", no "delve", no em-dash overuse (use commas/periods instead; at most a few em dashes in the whole post), no emojis.
- "Sell without selling": teach so well the reader trusts us. Use WayneFlow's real numbers as proof inside the lessons ("In one of our campaigns..."). At most 2 soft mentions of working with WayneFlow in the body, plus ONE closing section (a calm, helpful invitation to book a strategy call, framed as "if you would rather have this done for you"). Never hype, never fake urgency.
- 100% accurate. Any industry fact, law or statistic that is not WayneFlow data must be verified with web search from a primary or highly reputable source (e.g. FTC, Google/Yahoo/Microsoft sender guidelines, BLS, Glassdoor/Indeed salary data, Gartner, HubSpot research) and linked inline with an <a href> to that source. If you cannot verify a number, do not use it. Never invent quotes, studies, clients or testimonials. Current date: October 2026.

## SEO requirements
- One primary keyword (given in your task) in: title, H1, first 100 words, one H2, meta description, and naturally throughout. Use related secondary keywords and natural questions Americans search.
- Length: 2,800 to 3,800 words of real substance.
- Structure: a short "Key takeaways" box near the top, then H2/H3 sections, at least one comparison table, at least one numbered checklist, a FAQ section with 5 to 7 questions (answers 40 to 80 words), then the closing section.
- 3 to 6 internal links to the site pages above with descriptive anchor text, plus 4 to 10 external links to authoritative sources.

## Output format (STRICT)
Write ONE file at the path given in your task. It must contain exactly:
1. First line: <script type="application/json" id="meta">{ JSON }</script> with keys: "title" (55 to 62 chars, includes keyword, ends with " | WayneFlow" counted in), "description" (140 to 158 chars), "h1", "excerpt" (1 to 2 sentences), "keyword", "readMinutes" (integer), "faq": [{"q":"...","a":"..."}] (same Q&As as the on-page FAQ, plain text).
2. Then the article body as an HTML fragment using ONLY: <p>, <h2 id="...">, <h3>, <ul>, <ol>, <li>, <strong>, <em>, <a href>, <blockquote>, <table><thead><tbody><tr><th><td>, and these wrappers:
   - Key takeaways: <div class="takeaways"><b>Key takeaways</b><ul>...</ul></div>
   - A highlighted WayneFlow data example: <div class="proof"><b>From our dashboards</b><p>...</p></div> (use 1 to 3 of these)
   - Closing: <div class="soft-cta"><h2 id="next-step">...</h2><p>...</p><p><a class="btn btn-primary" href="https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers" target="_blank" rel="noopener">Book a free strategy call</a></p></div>
   Do NOT include <h1>, <html>, <head>, <body>, <style>, inline styles, scripts (other than the meta line) or images.
   - FAQ: <h2 id="faq">Frequently asked questions</h2> then for each: <h3>question</h3><p>answer</p>
3. When done, reply with only: the file path, word count, and the list of external sources used.
