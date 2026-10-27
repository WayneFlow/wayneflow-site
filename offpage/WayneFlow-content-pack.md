# What 588,000 cold emails taught us about reply rates in 2026

*By Syed Ali Hassan*

My co-founder and I have sent 588,000 cold emails for B2B clients, most of them in the U.S. and Canada. Those emails got 12,900+ replies. About 3,400 of the people who replied said some version of "yes, tell me more."

That's a lot of data on one question every founder asks before starting outbound: what reply rate should I expect?

The honest answer is that it depends on how you count, who you email, and how hard you push volume. Here's what our numbers showed, campaign by campaign.

## First, decide what "reply rate" means

This sounds boring. It's also the thing that confuses people most.

There are two ways to calculate a reply rate. You can divide replies by emails sent. Or you can divide replies by people contacted. If you run a three-step sequence, those two numbers can be far apart.

One of our agency clients ran from June 1 to October 19, 2026. We sent 82,671 emails to 76,081 people and got 2,429 replies. That's about 2.9% of emails sent. The sending dashboard shows 3.19%, because it divides by people contacted. Both numbers are correct. They answer different questions.

Our January to March 2026 campaign makes the gap bigger. 236,545 emails went to 118,387 people, about two emails per person. The 4,372 replies work out to 3.69% of people contacted, but only about 1.8% of emails sent.

So when someone on LinkedIn posts a screenshot of a 10% reply rate, ask two things. Per email or per person? And does that count "please remove me"?

My preference is to measure per person contacted. That number tells you how many humans engaged with your offer. Then track positive replies as their own number.

## The reply rates we actually see

Here are five campaigns side by side. All rates are replies divided by people contacted.

| Campaign | People contacted | Replies | Reply rate | Bounce rate |
|---|---|---|---|---|
| Small pilot | 10,284 | 417 | 4% | not tracked here |
| Full quarter, Jan to Mar 2026 | 118,387 | 4,372 | 3.69% | 3.08% |
| Agency client, Jun to Oct 2026 | 76,081 | 2,429 | 3.19% | 1.64% |
| Construction software client | 158,322 | 4,449 | 2.81% | 2.87% |
| 5-day blitz, Sep 2026 | 79,587 | 1,095 | about 1.4% | 0.45% |

Four of the five land between 2.8% and 4%. One sits well below. That outlier taught us the most, and I'll get to it.

## Lesson 1: Small, tight lists reply more

Our best reply rate came from our smallest campaign. A pilot of 10,284 contacts got 417 replies, about 4%. 103 of those became real opportunities.

That makes sense when you think about how the list gets built. A small list forces you to be picky. You choose one industry, one job title, one problem. The email can talk about that one person's actual week.

As a list grows, "close enough" contacts creep in. Each one drags the average down a little.

If you're starting out, build a list you can describe in one sentence. "Operations directors at commercial construction firms with 50 to 200 employees" is a list. "Decision-makers in construction" is a hope.

## Lesson 2: Volume buys meetings, and it costs you reply rate

In September 2026 we ran a 5-day blitz for a client. Between September 7 and 11, 96,408 emails went out to 79,587 people.

The reply rate was about 1.4%. That's far below everything else we run.

Now look at what came out the other end. 1,095 replies. 115 interested prospects. 25 calls booked. $62,500 in pipeline. All in five days.

Was it a bad campaign? I'd argue it did exactly what it was built for. When you go wide, you trade reply rate for speed. The client wanted calls on the calendar that month, and they got them.

The bounce rate was 0.45%, the lowest we've recorded. That list was verified hard before a single email went out, which is the only reason a send that big was safe.

The mistake is grading a blitz with the same yardstick as a narrow, hand-picked campaign. Decide which kind you're running before you look at the numbers.

## Lesson 3: Replies are not buyers

12,900+ replies sounds great on a slide. Here's the part people skip.

About 3,400 of those replies were interested buyers. Roughly 1 in 4. The rest were "not now," "wrong person," "take me off your list," and the occasional angry note.

The quarter campaign shows the same pattern. 4,372 replies, 1,061 interested. About 24%.

The 5-day blitz was harsher. 1,095 replies, 115 interested. About 1 in 10. That's the other cost of going wide.

So if you're building a forecast, don't stop at reply rate. Use the full chain:

1. People contacted
2. Reply rate
3. Share of replies that are interested
4. Share of interested prospects who book a call
5. Share of calls that turn into deals

In the blitz, 25 of 115 interested prospects booked a call. About 22%. Step 4 is where a lot of outbound programs leak money. Someone writes back "sure, send me some times," and nobody answers for two days. By then they've moved on.

## Lesson 4: Reply rate alone doesn't predict revenue

Our construction software client had a 2.81% reply rate. Not our highest. We sent 162,073 emails to 158,322 people and got 4,449 replies.

From that: 31 sales-qualified demos held, 6 annual contracts signed, and $15,000 in closed deals for the client so far.

Compare that with the agency client: a 3.19% reply rate and $175,000 in pipeline. Different market, different deal size, different sales cycle.

Construction software buyers move slowly. A 2.81% reply rate in that market is a good result. In a market of agency owners who live in their inbox, the same number would worry me.

Benchmarks are useful for spotting a broken campaign. They're close to useless for comparing two healthy campaigns in different industries.

## Lesson 5: Bounce rate is the quiet killer

Look at the bounce column again. 0.45%. 1.64%. 2.87%. 3.08%.

Every bounce tells the inbox provider you don't really know who you're emailing. Enough of them and your messages start landing in spam. Then your reply rate drops, and you blame the copy.

We verify every list before it goes out. Even so, contact data goes stale fast. People change jobs. Companies get bought. If a list has been sitting for a few weeks, verify it again before you hit send.

Gmail is clear about what it's watching. Its [email sender guidelines](https://support.google.com/a/answer/81126) tell senders to keep spam rates reported in Postmaster Tools below 0.10% and to avoid ever reaching 0.30%. Bounces and spam complaints are different things, but they usually come from the same root problem: emailing people who shouldn't be on your list.

## Lesson 6: Protect the domain that matters

Every campaign in this article ran on separate secondary sending domains. A client's main domain, the one their invoices and customer emails come from, never sends cold email.

It's a boring setup choice. It's also what lets you run a campaign like the 5-day blitz without putting the company's real inbox at risk.

If you're doing this yourself, buy a few domains that look close to your brand, set up SPF, DKIM and DMARC on each one, and warm them up before you send. Google requires all three for anyone sending 5,000 or more messages a day to Gmail accounts. Microsoft set similar [requirements for high-volume senders to Outlook.com](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) addresses, with enforcement starting May 5, 2025.

## Lesson 7: Send when people are at their desks

We send on weekdays, during business hours, in the prospect's time zone. That's the whole trick. No secret "Tuesday at 10:14 a.m." formula.

The reason is practical. A cold email that lands at 2 a.m. is buried under newer mail by the time the person wakes up. One that lands at 10 a.m. while they're working has a real chance of being read.

A list that covers the U.S. and Canada spans at least four time zones on the mainland alone. Most sending tools can schedule by the lead's location. Turn that on.

## Lesson 8: Turn off open tracking

Every one of our dashboards shows zero opens. We switched open tracking off on purpose.

Open tracking works by adding a tiny invisible image to each email. When the image loads, the tool logs an open. Spam filters know exactly what that looks like, and removing it gives them one less reason to treat you like a bulk sender.

The data isn't trustworthy anymore anyway. Apple says its [Mail Privacy Protection](https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios) "prevents senders from seeing if you've opened the email message they sent you." Once a big share of your opens are hidden or faked, the metric stops helping you make decisions.

Replies are the number that matters. Track those.

## How I'd read your reply rate in 2026

Based on 588,000 emails, here's how I'd judge a campaign, measured per person contacted:

- **Under 1%:** something is probably broken. Check deliverability first, then the list, then the copy.
- **1% to 2%:** normal for a wide, high-volume push like our blitz. Fine if interested replies are turning into calls.
- **2.8% to 4%:** where our targeted campaigns land.
- **Above 4%:** you either have a very tight list, a warm audience, or you're counting auto-replies.

The bigger point: treat reply rate as a health check. The goal is closed deals. A campaign with a 2.81% reply rate signed 6 annual contracts. Track the whole chain down to closed deals, and judge each campaign against the job it was built to do.

## A short checklist for your next campaign

1. Define reply rate as replies divided by people contacted, and write that down for your team.
2. Tag every reply: interested, not now, wrong person, remove.
3. Verify the list right before you send.
4. Send from secondary domains with SPF, DKIM and DMARC in place.
5. Turn off open tracking.
6. Schedule for weekday business hours in the lead's time zone.
7. Answer interested replies the same day.

None of this is clever. Most of it is the stuff people skip because it's tedious. In our experience, that's where the gap between a 1% campaign and a 3% campaign usually lives.

---

*Syed Ali Hassan is co-founder of [WayneFlow](https://wayne-flow.site), a B2B appointment setting agency that runs cold email, LinkedIn and X outreach for companies in the U.S. and Canada. He has spent 8 years in digital marketing and outbound.*
# We turned open tracking off. Here's what happened to deliverability

*By Syed Asim Hussain*

Every client dashboard we run shows the same number in the "opens" column: zero.

The first time a new client sees it, they usually email us. "Is the tracking broken?" Fair question. It looks broken.

It isn't. We switched open tracking off on purpose, across every campaign. This post explains why, what we track instead, and what our deliverability looks like with it off.

One thing up front, because I'd rather you trust the rest of this. We never ran a clean A/B test with tracking on in one group and off in another, same list, same copy, same week. So I can't tell you "turning off opens raised our reply rate by X%." Anyone who gives you that number from their own agency should show you how they isolated it.

What I can show you is how our campaigns perform with tracking off, across 588,000 emails, and why we're confident it was the right call.

## How open tracking works

When you turn on open tracking in a cold email tool, it adds a tiny invisible image to the bottom of every email. Usually it's a 1x1 pixel. Each recipient gets a unique image link.

When the email is opened and the image loads, the tool's server logs a hit. That hit becomes an "open" on your dashboard.

Simple. Here's the problem.

## Problem 1: The pixel is a spam signal

Spam filters read the code of every email, not only the words. A hidden image hosted on a third-party tracking server is one of the most common patterns in bulk mail.

Some sending tools load that image from a tracking domain shared by their customers unless you set up your own. That means your email can carry a link tied to whatever everyone else on that domain is sending.

A clean, plain-text email from a person to a person has no pixel. When your cold email looks like that, you've removed one reason for a filter to doubt it.

I won't pretend the pixel alone sends you to spam. Filters weigh a lot of signals. But when you're sending to people who have never heard of you, you want as few strikes against you as possible.

## Problem 2: The open data is unreliable

Start with Apple's Mail Privacy Protection. Here's how Apple describes it on its [support page](https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios): it "hides your IP address so senders can't link it to your other online activity or determine your exact location. It also prevents senders from seeing if you've opened the email message they sent you."

So for anyone using Apple Mail with the setting on, your open data can't tell you what you think it's telling you.

Corporate security tools muddy it further. Some scan links and images before a person ever sees the message, which can make an email look "opened" when no human has read it.

Put those together and the open rate on a cold campaign turns into a number you can't make decisions with. You end up rewriting subject lines based on noise.

Apple's page adds one detail worth knowing: Mail Privacy Protection "does not extend to links or email attachments." That doesn't mean you should start stuffing links into cold emails to get a cleaner signal. A link in a first-touch email is its own risk. My advice is to keep the first email plain.

## What we track instead

If you can't trust opens, you need other numbers. These are the ones on our dashboards:

1. **People contacted.** Not emails sent. Humans reached.
2. **Replies.** Any human response.
3. **Interested replies.** Someone asking for times, pricing or more details.
4. **Calls booked.** On the calendar, confirmed.
5. **Bounce rate.** Our early warning for list and deliverability problems.

Replies are the closest thing to an honest engagement signal you get in cold email. Someone read your message and cared enough to type back. No image proxy can fake that.

## What happened to deliverability

Here's how our campaigns look with tracking off. Reply rate here means replies divided by people contacted.

| Campaign | Emails sent | Reply rate | Bounce rate |
|---|---|---|---|
| 5-day blitz, Sep 7 to 11, 2026 | 96,408 | about 1.4% | 0.45% |
| Agency client, Jun 1 to Oct 19, 2026 | 82,671 | 3.19% | 1.64% |
| Construction software client | 162,073 | 2.81% | 2.87% |
| Full quarter, Jan to Mar 2026 | 236,545 | 3.69% | 3.08% |

Across all campaigns: 588,000 emails, 12,900+ replies, 3,400+ interested buyers, 100+ calls and demos booked.

A few things stand out to me.

**The blitz.** 96,408 emails in five days is a big push. It finished with a 0.45% bounce rate, 1,095 replies, 115 interested prospects and 25 calls booked. If our sending setup had a reputation problem, a campaign like that is where it would show up first. It didn't.

**The agency client.** 2,429 replies over about four and a half months, with 2,146 of them tagged positive or interested, and a 1.64% bounce rate. Steady results over a long run like that suggest the emails are reaching inboxes week after week.

**The targeted campaigns.** Most of our targeted work lands between 2.8% and 4% reply rate. You don't get replies from the spam folder, so a reply rate holding in that range is a decent sign the mail is landing.

Is all of that because of the missing pixel? No. Turning off open tracking is one piece of a setup. The other pieces matter at least as much, and I'll list them below. But I can say this plainly: after 588,000 emails with tracking off, we've never once wished we had the open data back.

## The rules got stricter, and that changes the math

In 2024 and 2025 the big inbox providers put their sender rules in writing. They don't mention tracking pixels, but they tell you how seriously they now take spam signals.

Here's a summary, pulled from each provider's own page:

| Provider | Applies to | Key requirements |
|---|---|---|
| [Google (Gmail)](https://support.google.com/a/answer/81126) | All senders | SPF or DKIM, valid forward and reverse DNS (PTR), TLS, spam rate in Postmaster Tools below 0.3% |
| Google (Gmail) | 5,000+ messages a day to Gmail | SPF, DKIM and DMARC (p=none is allowed), one-click unsubscribe for marketing and subscribed messages, visible unsubscribe link |
| [Yahoo](https://senders.yahooinc.com/best-practices/) | Bulk senders | SPF and DKIM, DMARC of at least p=none that passes, spam rate below 0.3%, one-click list-unsubscribe, honor unsubscribes within 2 days |
| [Microsoft (Outlook.com)](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) | Domains sending 5,000+ a day | SPF and DKIM must pass, DMARC of at least p=none aligned with SPF or DKIM; non-compliant mail rejected starting May 5, 2025 |

Gmail goes further in its best practices. It tells senders to keep their spam rate below 0.10% and to avoid ever reaching 0.30%.

Think about what 0.3% means. At 1,000 emails, three spam reports puts you at the line. Cold email has very little room for error now. Every small thing that makes your mail look less like a person writing to a person is worth removing.

One more rule that applies no matter which inbox you send to. In the U.S., the FTC's [CAN-SPAM compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) says the law "makes no exception for business-to-business email." You need accurate headers, an honest subject line, your physical postal address, and a clear way to opt out, and you must honor opt-outs within 10 business days.

## What we gave up

Being honest about the trade-offs matters, so here's what we lost.

**Subject line testing by open rate.** This used to be the standard way to test subject lines. We now test subject lines on reply rate and interested reply rate. It takes more volume to reach a clear answer, since replies are rarer than opens. We think it's worth it, because the answer is real.

**"Hot lead" alerts.** Some sales teams like seeing that a prospect opened an email five times so they can call them. With Apple hiding opens and security scanners creating fake ones, a lot of those alerts were wrong anyway. Reps were chasing ghosts.

**A comforting number.** A big open rate feels good on a weekly report. Zero looks scary. The fix is to agree on reply-based numbers with your team or your client before the campaign starts, so nobody panics when they see the opens column.

## The rest of the deliverability setup

Turning off the pixel won't save a campaign with a bad list or a burned domain. Here's the rest of what we do on every campaign:

1. **Separate secondary sending domains.** The client's main domain never sends cold email, so it's never at risk.
2. **SPF, DKIM and DMARC on every sending domain.** That covers the Google, Yahoo and Microsoft rules above.
3. **Verified lists.** Every list is checked before it goes out. Our bounce rates run from 0.45% to 3.08% across the campaigns above.
4. **Business-hours sending.** Weekdays, during working hours, in the prospect's time zone.
5. **Plain emails.** Short, written like a person, no tracking pixel.
6. **An easy way to opt out.** Required by law in the U.S. and good for your spam rate everywhere.

## If you want to try it

Turning off open tracking takes five minutes. Here's how I'd do it:

1. Open every active campaign in your sending tool and switch off open tracking. Check old templates and sequences too, since some tools set it per campaign.
2. Tell your team or client before they see the dashboard. Explain what you're tracking instead.
3. Set up reply tagging: interested, not now, wrong person, remove.
4. Pick your new weekly numbers: people contacted, replies, interested replies, calls booked, bounce rate.
5. Watch bounce rate and reply rate for the next few weeks. If both hold steady or improve, you have your answer for your own setup.

The zero in our opens column used to make clients nervous. Now it's usually the first thing we explain on a kickoff call, and by the end of the first month nobody asks about it anymore. They're too busy looking at replies.

---

*Syed Asim Hussain is co-founder of [WayneFlow](https://wayne-flow.site), a B2B appointment setting agency that runs cold email, LinkedIn and X outreach for companies in the U.S. and Canada. He has spent 8 years in digital marketing and outbound.*
# Community answers (Reddit / Quora)

Ready to adapt. Change the opening line to fit the thread, keep the numbers as they are. Post from a personal account (Ali or Asim). Only add a link if the thread asks for one.

---

## 1. "Is cold email dead in 2026?"

No, but lazy cold email is.

Quick disclosure: I run an appointment setting agency, so I'm biased, but I can at least show you real numbers.

Across our campaigns we've sent 588,000 cold emails. They got 12,900+ replies, and about 3,400 of those were people interested in talking. That turned into 100+ booked calls and demos and 6 annual contracts for clients. That's not a dead channel.

What did change is the rulebook. Google, Yahoo and Microsoft all published stricter sender rules in 2024 and 2025. Google tells senders to keep their spam complaint rate under 0.3%, ideally under 0.1%. Blast 10,000 generic emails from your main domain and you'll be in spam within a week.

What still works:

- Small, specific lists (one industry, one job title)
- Separate sending domains so your main domain stays safe
- Verified emails, so you're not bouncing
- Short, plain emails that sound like a person wrote them
- Sending on weekdays in the prospect's business hours

Our targeted campaigns usually land between 2.8% and 4% reply rate, counted as replies divided by people contacted. If you're getting under 1%, the channel probably isn't the problem. Check your list and your deliverability first.

---

## 2. "How many cold emails can I send per inbox per day?"

Short answer: fewer than you want to.

I run an appointment setting agency, so I deal with this every week.

My advice for a new inbox: start low, somewhere around 15 to 20 a day, and warm it up for a couple of weeks before any real campaign. Then increase slowly. I wouldn't push a single inbox much past 50 a day, even once it's healthy. If you need more volume, add more inboxes on separate secondary domains instead of pushing harder on one.

A few things matter more than the exact number:

- **Never use your main company domain.** Buy lookalike domains for outreach so your real inbox is never at risk.
- **Set up SPF, DKIM and DMARC** on every sending domain. Google requires all three once you send 5,000+ messages a day to Gmail accounts.
- **Verify your list.** Bounces hurt you faster than volume does. Our campaigns run from 0.45% to about 3% bounce rate, and the 0.45% one was also our biggest send: 96,408 emails in five days spread across many inboxes.
- **Watch the numbers.** If replies drop suddenly or bounces jump, slow down before you burn the domain.

Volume is a math problem. Inbox count times daily limit. Solve it by adding inboxes, not by pushing each one harder.

---

## 3. "Cold email vs LinkedIn outreach: which is better for B2B?"

They do different jobs. I use both.

Disclosure: I run an appointment setting agency that does both channels for clients.

Here are our real LinkedIn numbers, all time: 1,375 connection invites, 351 accepted (about 25%), 1,628 InMails, 154 replies. The audience was founders and angel investors, people who are hard to reach by email and spend real time on LinkedIn. That's where LinkedIn shines.

Email is a scale game. Across our email campaigns we've sent 588,000 emails, which got 12,900+ replies and 3,400+ interested buyers. You can't get that kind of volume on LinkedIn. The platform caps how many invites you can send, and accounts get restricted if you push.

How I'd decide:

- **Small, high-value audience** (founders, investors, C-suite at a few hundred companies): start with LinkedIn, back it up with email.
- **Larger market** (thousands of companies that fit): start with email, use LinkedIn to warm up your best prospects.
- **Selling to people who live in their inbox** (agency owners, ops managers): email.

The best results I've seen come from touching the same person on both. They see your name on LinkedIn, then your email feels familiar instead of cold.

---

## 4. "How do I get my first B2B clients?"

Start smaller than you think.

I run an appointment setting agency now, and the same thing works for new businesses as it does for our clients.

Step 1: talk to your network. Former coworkers, old clients, people who already trust you. Your first two or three clients almost always come from there.

Step 2: pick one narrow group. Not "small businesses." Something like "HVAC companies in Texas with 10 to 50 employees." You should be able to describe your list in one sentence.

Step 3: run a small cold email pilot. One of our pilots went to 10,284 contacts. 417 people replied (about 4%) and 103 became real opportunities. Small lists reply better because every email can speak to that person's actual problem.

Step 4: write like a human. Three to five sentences. Who you are, why you're emailing them specifically, one clear question. No attachments, no long pitch.

Step 5: answer replies fast. When someone says "sure, send me times," reply that day. A lot of first deals die because the founder waited two days.

Step 6: ask your first clients for a review the moment they're happy. Proof makes the next ten much easier.

It's slow at first. That's normal.

---

## 5. "Is cold email legal in the US and Canada?"

Short version: legal in the U.S. if you follow CAN-SPAM. Much stricter in Canada under CASL. Not legal advice, check with a lawyer for your situation.

For context, I run an appointment setting agency with clients in both countries, so we deal with this constantly.

**United States (CAN-SPAM).** You don't need prior consent. The FTC's guide says the law "makes no exception for business-to-business email," so B2B is covered. You need accurate "From" and header info, a subject line that matches the content, your valid physical postal address, a clear way to opt out, and you have to honor opt-outs within 10 business days. Each violating email can cost up to $53,088.

**Canada (CASL).** Consent is required, either express or implied. The CRTC lists three basics: get consent, identify yourself, include an unsubscribe. One form of implied consent is "conspicuous publication": the person published their email address publicly, didn't say they don't want unsolicited messages, and your message relates to their job. The CRTC is clear this is case by case and not a license to email any address you find. Keep records of where and when you found each address. Unsubscribes must be processed within 10 business days. Maximum penalties are $1 million per violation for individuals and $10 million for businesses.

If you email Canadians, build your list from public, role-relevant sources and document it.

---

## 6. "What's a good cold email reply rate?"

First question back: how are you counting it?

Disclosure: I run an appointment setting agency, and this is the question I get most.

Reply rate can mean replies divided by emails sent, or replies divided by people contacted. If you send a 3-step sequence, those are very different numbers. One of our campaigns had 4,372 replies from 118,387 people. That's 3.69% per person, but only about 1.8% of the 236,545 emails sent. I prefer per person.

Our real numbers, per person contacted:

- Small pilot: 4%
- Full quarter campaign: 3.69%
- Agency client: 3.19%
- Construction software client: 2.81%
- 5-day high-volume blitz: about 1.4%

So targeted campaigns for us land between 2.8% and 4%. Big volume pushes come in lower.

The more useful number is interested replies. Across 588,000 emails we got 12,900+ replies, and roughly 1 in 4 were interested. On the blitz it was closer to 1 in 10.

And reply rate doesn't predict revenue alone. The construction software campaign, our lowest targeted rate at 2.81%, led to 6 signed annual contracts.

Track the full chain: contacted, replied, interested, booked, closed.

---

## 7. "Should I hire an SDR or use an appointment setting agency?"

Depends on your stage. I'll give you both sides even though I'm biased.

Disclosure: I run an appointment setting agency.

**The SDR math.** Glassdoor currently puts average total pay for a U.S. sales development rep at around $104,700 a year, with base pay typically in the $57K to $73K range. On top of that you pay for tools, data, sending infrastructure, and your own time managing and training them. Then they need a few months to ramp before they're booking consistently.

**The agency math.** Pricing varies a lot. For reference, we charge $999 setup plus $1,500 a month for the full outbound system across cold email, LinkedIn and X. Any agency you consider should already have domains, tools, list building and copy figured out, and should be able to show you real campaign data.

When an SDR makes more sense:

- You have a proven offer and a sales leader to manage them
- Your sale needs deep product knowledge on the first call
- You want to build an internal team long term

When an agency makes more sense:

- You don't know yet which market responds best
- You want meetings in weeks, not after a hiring and ramp cycle
- Nobody on your team knows deliverability

A common path: start with an agency, learn what works, then hire SDRs to run the playbook in-house. Before you sign with any agency, ask to see their live dashboards. Testimonials are easy to collect.

---

## 8. "How do I keep my cold emails out of spam?"

Most spam problems come from setup, not copy.

I run an appointment setting agency. Across 588,000 emails, this is the checklist we follow:

1. **Use separate sending domains.** Never send cold email from your main company domain.
2. **Set up SPF, DKIM and DMARC** on every sending domain. Google, Yahoo and Microsoft all require these for bulk senders now.
3. **Warm up new inboxes** for a couple of weeks before sending campaigns.
4. **Keep daily volume per inbox low.** Add inboxes instead of pushing one harder.
5. **Verify your list** right before sending. Our bounce rates run from 0.45% to about 3%. Higher than that and you're asking for trouble.
6. **Turn off open tracking.** The tracking pixel is a bulk-mail signal, and Apple's Mail Privacy Protection hides opens anyway. All our dashboards show zero opens on purpose.
7. **Write plain emails.** Short, no images, no attachments, ideally no links in the first email.
8. **Send in business hours** in the prospect's time zone, on weekdays.
9. **Make opting out easy.** It's required by law in the U.S. and it keeps people from hitting "report spam" instead.

Google's guidelines say to keep your spam rate below 0.1% and never reach 0.3%. That's three complaints per 1,000 emails. Very little room for error, so get the setup right before you worry about the perfect subject line.
# YouTube video plans

Four long-form videos plus three Shorts cuts each. Presenter: Ali or Asim, on camera, with screen recordings of real WayneFlow dashboards for the proof moments. Never show client names, email addresses or lead data on screen. Blur anything that identifies a person or company.

Links used in descriptions:

- Website: https://wayne-flow.site (update to https://wayneflow.com after the move)
- Book a call: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers
- Results page: https://wayne-flow.site/results.html

---

## Video 1: Cold email deliverability in 2026

**Title:** Cold Email Deliverability in 2026: What Worked Across 588,000 Emails

**Target keyword:** cold email deliverability

**Length:** 12 to 14 minutes

### Hook (first 15 seconds, verbatim)

"We sent 96,408 cold emails in five days. The bounce rate was 0.45%. Twenty-five sales calls got booked. In this video I'll show you the exact setup behind that, and the three mistakes that put most cold emails in spam in 2026."

### Outline

- **0:00** Hook (above)
- **0:15** Who we are: two founders, 8 years each in outbound, 588,000 cold emails sent for B2B clients in the U.S. and Canada.
- **0:45** What changed: Google, Yahoo and Microsoft put their sender rules in writing. Show each official page on screen. Google: spam rate under 0.3%, ideally under 0.1%. 5,000+ a day to Gmail needs SPF, DKIM and DMARC. Microsoft started rejecting non-compliant high-volume mail on May 5, 2025.
- **2:30** Mistake 1: sending from your main domain. Why we use separate secondary domains for every client.
- **4:00** Mistake 2: dirty lists. Walk through bounce rates across our campaigns, from 0.45% to 3.08%. Every bounce is a signal you don't know who you're emailing.
- **5:45** Mistake 3: open tracking. How the pixel works. Apple Mail Privacy Protection quote on screen. Why our dashboards show zero opens.
- **7:30** The setup checklist: SPF, DKIM, DMARC, warmup, low daily volume per inbox, verified list, plain emails, easy opt-out.
- **9:30** Timing: weekdays, business hours, prospect's time zone. The U.S. and Canada span several time zones, so schedule by lead location.
- **10:30** How to know your deliverability is healthy without opens: reply rate per person contacted, bounce rate, sudden drops.
- **12:00** Recap and the one thing to fix this week.
- **12:45** Soft close: "If you'd rather have this built for you, the link's in the description."

### On-screen proof moments

1. **0:00 to 0:15:** Dashboard for the 5-day blitz (Sep 7 to 11, 2026): 96,408 emails sent, 79,587 contacted, 1,095 replies, 0.45% bounce.
2. **4:15:** Side-by-side bounce rates: blitz 0.45%, agency client 1.64%, construction software 2.87%, full quarter 3.08%.
3. **6:00:** Any campaign dashboard with the opens column at 0. Circle it.
4. **10:45:** Agency client dashboard (Jun 1 to Oct 19, 2026): 76,081 contacted, 2,429 replies, 3.19% reply rate, 1.64% bounce.
5. **12:00:** Totals card: 588,000 emails, 12,900+ replies, 3,400+ interested buyers, 100+ calls booked.

### Description

Cold email deliverability got stricter in 2024 and 2025. Here's the setup we use across 588,000 cold emails, including a 5-day campaign of 96,408 emails with a 0.45% bounce rate and 25 calls booked.

We cover the Google, Yahoo and Microsoft sender rules, why we never send from a client's main domain, why we turned open tracking off, and a checklist you can use today.

Sources mentioned:
- Google email sender guidelines: https://support.google.com/a/answer/81126
- Yahoo sender best practices: https://senders.yahooinc.com/best-practices/
- Microsoft Outlook.com high-volume sender requirements: https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730
- Apple Mail Privacy Protection: https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios

More case studies: https://wayne-flow.site/results.html
If you'd rather have us set it up, book a call: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers

### Shorts cuts

1. **"Why our dashboards show 0 opens"** (0:30): The pixel explained in one breath, Apple quote, zoom on the zero.
2. **"96,408 emails, 0.45% bounce"** (0:40): Blitz dashboard, then the one reason it was safe: list verified hard before sending.
3. **"Never send cold email from your main domain"** (0:30): One sentence on why, one sentence on what to do instead.

---

## Video 2: How to write a cold email

**Title:** How to Write a Cold Email That Gets Replies (Real Examples From 12,900+ Replies)

**Target keyword:** how to write a cold email

**Length:** 10 to 12 minutes

### Hook (first 15 seconds, verbatim)

"Most cold emails fail in the first line. Ours have pulled in more than 12,900 replies. I'm going to rewrite a bad cold email live, line by line, and show you exactly what we change and why."

### Outline

- **0:00** Hook (above)
- **0:15** The only job of a cold email is to get a reply. Closing happens later, on the call.
- **1:00** Show a typical bad cold email on screen (written by us as an example, not a real sender). Long intro, company history, three links, "hop on a call."
- **2:00** Rule 1: start with them. First line about their company or role, not about you.
- **3:15** Rule 2: one problem. Pick the single problem this person most likely has.
- **4:30** Rule 3: short. Three to five sentences. Read it out loud on camera to show how fast it is.
- **5:30** Rule 4: one easy question at the end. "Worth a quick chat?" beats "Book a 30-minute demo here."
- **6:30** Rule 5: plain text. No images, no tracking pixel, ideally no link in the first email.
- **7:30** The rewrite: final version on screen, side by side with the original.
- **8:30** Follow-ups: short, new angle each time, stop when they say stop.
- **9:30** How to judge your email: reply rate per person contacted, then interested replies. Show why 1 in 4 replies being interested is a realistic target.
- **10:30** Recap.
- **11:00** Soft close.

### On-screen proof moments

1. **0:05:** Totals card: 12,900+ replies, 3,400+ interested buyers.
2. **4:45:** Small pilot numbers: 10,284 contacted, 417 replies (4%), 103 opportunities. Point: tight list plus short email.
3. **9:30:** Funnel graphic: 588,000 emails, 12,900+ replies, 3,400+ interested, 100+ calls booked.
4. **9:50:** Construction software dashboard: 4,449 replies, 2.81% reply rate, 31 demos held, 6 annual contracts. Point: a good email to a slow market still wins.

### Description

How to write a cold email that people actually reply to. We rewrite a weak cold email live and explain every change, using lessons from 12,900+ replies across 588,000 B2B cold emails.

Inside: the first line that works, why shorter wins, the one question to end on, why we keep emails plain text, and how to write follow-ups that don't annoy people.

U.S. senders: make sure every email meets CAN-SPAM. FTC guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

See our results: https://wayne-flow.site/results.html
Book a call if you want us to write and run it for you: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers

### Shorts cuts

1. **"Delete your first line"** (0:30): Show a bad opener, cross it out, replace with a line about the prospect.
2. **"The 5-sentence cold email"** (0:45): Read the final rewrite out loud start to finish.
3. **"12,900 replies, only 1 in 4 interested"** (0:35): Why reply rate isn't the finish line.

---

## Video 3: Outsourced appointment setting vs hiring an SDR

**Title:** Outsourced Appointment Setting vs Hiring an SDR: The Real Cost in 2026

**Target keyword:** outsourced appointment setting

**Length:** 10 to 12 minutes

### Hook (first 15 seconds, verbatim)

"Glassdoor puts average total pay for a U.S. SDR at about $104,700 a year. That's before tools, data and the months it takes them to ramp. I run an appointment setting agency, so I'm biased. I'll show you the math anyway, and when hiring an SDR is the better call."

### Outline

- **0:00** Hook (above)
- **0:15** Disclosure and context: we run an agency, clients mostly in the U.S. and Canada.
- **0:45** The SDR cost: Glassdoor average total pay around $104,700, base typically $57K to $73K. Show the Glassdoor page on screen with the date. Note that figures change.
- **2:00** The hidden costs: sending tools, data, domains, management time, ramp time, turnover. (Talk through them as categories. Don't put made-up dollar amounts on screen.)
- **3:30** The agency cost: our pricing as one example, $999 setup plus $1,500 a month for cold email, LinkedIn and X. First-year total on screen: $18,999.
- **4:30** What you should get from any agency: domains, lists, copy, sending, reply handling, and real dashboards.
- **5:30** Proof: walk through two real campaigns.
- **7:30** When an SDR wins: proven offer, sales leader in place, complex product, long-term team building.
- **8:30** When an agency wins: still testing markets, need meetings fast, nobody knows deliverability.
- **9:30** The hybrid path: agency first to find what works, then hire SDRs to run the playbook.
- **10:15** Questions to ask any agency before you sign. Ask to see live dashboards. Testimonials alone prove very little.
- **11:00** Soft close.

### On-screen proof moments

1. **3:45:** Simple cost card: SDR average total pay (Glassdoor) about $104,700 per year vs agency example $18,999 first year. Label the SDR figure "pay only, excludes tools and management."
2. **5:45:** 5-day blitz dashboard: 96,408 emails, 1,095 replies, 115 interested, 25 calls booked, $62,500 pipeline.
3. **6:30:** Agency client dashboard: 82,671 emails, 2,429 replies, 3.19% reply rate, $175,000 pipeline.
4. **7:00:** Footnote on screen: "Pipeline = value of qualified opportunities at our clients' ~$2,500 average deal."

### Description

Outsourced appointment setting vs hiring an in-house SDR. We compare real costs, using Glassdoor salary data and our own agency pricing, and show real campaign dashboards so you can judge results.

Disclosure: we run WayneFlow, a B2B appointment setting agency. We cover when an SDR is the better choice too.

Salary source: Glassdoor, Sales Development Representative salaries (check current figures): https://www.glassdoor.com/Salaries/sales-development-representative-salary-SRCH_KO0,32.htm

Case studies with live dashboards: https://wayne-flow.site/results.html
Our process: https://wayne-flow.site/process.html
Book a strategy call: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers

### Shorts cuts

1. **"What an SDR really costs"** (0:40): Glassdoor number, then the list of costs that aren't in the salary.
2. **"5 days, 25 sales calls"** (0:30): Blitz dashboard walk-through.
3. **"Ask any agency this before you sign"** (0:35): "Show me a live dashboard." Why testimonials aren't enough.

---

## Video 4: Is cold email legal in Canada? (CASL)

**Title:** Is Cold Email Legal in Canada? CASL Explained for B2B Sellers

**Target keyword:** is cold email legal in Canada

**Length:** 9 to 11 minutes

### Hook (first 15 seconds, verbatim)

"Under Canada's anti-spam law, the maximum penalty for a business is $10 million per violation. Cold email to Canadians can still be legal, but the rules are very different from the U.S. Here's what the CRTC actually says, straight from their own FAQ."

### Outline

- **0:00** Hook (above)
- **0:15** Disclaimer: not legal advice. We run outbound for clients in the U.S. and Canada, and this is how we read the official guidance.
- **0:45** U.S. quick contrast: CAN-SPAM doesn't require prior consent, covers B2B, needs a physical address and opt-out, honor opt-outs within 10 business days.
- **2:00** CASL basics from the CRTC: three requirements. Get consent, identify yourself, include an unsubscribe.
- **3:00** Express vs implied consent. Explain both in plain words.
- **4:00** The conspicuous publication exemption: the address is published publicly, there's no "no unsolicited messages" statement next to it, and the message relates to the person's role. Show the CRTC FAQ text on screen.
- **5:30** What it doesn't allow: CRTC says it's not a broad license to email any address you find online. An address you can only get by querying a database isn't conspicuously published.
- **6:30** Records to keep, per the CRTC: where and how you found the address, when, whether it was conspicuous, whether there was a no-spam statement, and why your message fits their role.
- **7:30** Unsubscribe rules: link must work for at least 60 days, process requests within 10 business days.
- **8:15** Penalties: up to $1 million per violation for individuals, $10 million for businesses.
- **8:45** Practical checklist for B2B sellers emailing Canada.
- **9:45** Soft close.

### On-screen proof moments

This video is about rules, so proof moments are official pages, plus one WayneFlow screen:

1. **2:00:** CRTC FAQ page showing the three requirements.
2. **4:15:** CRTC FAQ text on conspicuous publication, highlighted.
3. **8:15:** CRTC penalty text, highlighted.
4. **8:45:** Our sourcing checklist as a simple on-screen graphic (where found, date, role match, no-spam statement check). Keep it generic, no client data.

### Description

Is cold email legal in Canada? Under CASL (Canada's Anti-Spam Legislation), you need consent, identification and an unsubscribe in every commercial message. We walk through express vs implied consent, the conspicuous publication exemption, the records you should keep, and the penalties, using the CRTC's own guidance.

Not legal advice. Talk to a Canadian lawyer about your specific situation.

Sources:
- CRTC, Frequently Asked Questions about CASL: https://crtc.gc.ca/eng/com500/faq500.htm
- FTC, CAN-SPAM Act compliance guide (U.S.): https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

We run cold email and LinkedIn outreach for B2B companies in the U.S. and Canada: https://wayne-flow.site
Book a call: https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers

### Shorts cuts

1. **"$10 million per violation"** (0:30): The CASL penalty number and why U.S. senders get caught out.
2. **"Found their email online? Read this first"** (0:45): Conspicuous publication in three plain conditions, plus the CRTC warning.
3. **"U.S. vs Canada cold email rules in 40 seconds"** (0:40): CAN-SPAM opt-out model vs CASL consent model.
# LinkedIn posts for the founders

12 posts. Each one is built on a single real number or lesson. Suggested author in brackets. No emojis, max 3 hashtags. Post as plain text; screenshots of the matching dashboard (with client details blurred) help.

---

## 1. The honest funnel [Ali]

588,000 cold emails.

12,900+ replies.

3,400+ interested buyers.

100+ calls and demos booked.

6 annual contracts signed.

That's our real funnel across every campaign Asim and I have run.

The step people skip is the jump from replies to interested. Only about 1 in 4 replies is someone who wants to talk. The rest are "not now," "wrong person" and "take me off your list."

So when you plan outbound, don't forecast from reply rate. Forecast from interested replies, then from calls booked.

Big numbers at the top of the funnel feel good. The bottom of the funnel pays the bills.

#coldemail #b2bsales

---

## 2. Zero opens, on purpose [Asim]

Every one of our client dashboards shows 0 opens.

New clients usually message us in week one asking if tracking is broken.

We turned it off on purpose.

Open tracking adds a tiny hidden image to every email. Spam filters know what that pattern looks like. And Apple's Mail Privacy Protection hides whether people opened your email anyway, so a lot of that data was wrong.

What we track instead: people contacted, replies, interested replies, calls booked, bounce rate.

A reply is the one number nobody can fake.

#emaildeliverability #coldemail

---

## 3. 5 days, 25 calls [Ali]

September 7 to 11 we ran a blitz for a client.

96,408 emails in five days.
79,587 people contacted.
1,095 replies.
115 interested.
25 calls booked.
$62,500 in pipeline.

The reply rate was only about 1.4%. That's well below our usual 2.8% to 4%.

It still did its job. The client needed meetings that month, so we traded reply rate for speed.

The thing that made it safe: the bounce rate was 0.45%, the lowest we've ever recorded. The list was verified hard before anything went out.

Go wide only when your list is clean.

#coldemail #outbound

---

## 4. Slow markets still pay [Asim]

Our construction software client had a 2.81% reply rate.

Not our best number. 162,073 emails, 4,449 replies.

But from that came 31 sales-qualified demos, 6 annual contracts, and $15,000 in closed deals so far.

Construction buyers move slowly. Budgets follow project seasons. A reply rate that would worry me with agency owners is a good result in that market.

If you sell into a slow industry, stop comparing your numbers to SaaS founders on LinkedIn. Compare this quarter to last quarter in your own market.

#b2bsales #construction

---

## 5. Two reply rates, both correct [Ali]

One of our campaigns shows a 3.19% reply rate on the dashboard.

I could also tell you it's 2.9%.

Both are true. 82,671 emails went to 76,081 people and got 2,429 replies. Divide by emails and you get 2.9%. Divide by people and you get 3.19%.

On a three-step sequence the gap gets bigger. Our January to March campaign was 3.69% per person and about 1.8% per email.

So when someone shows you a reply rate, ask how they counted it. We count per person. It tells you how many humans actually engaged.

#coldemail #salesmetrics

---

## 6. Start small [Asim]

Our best reply rate came from our smallest campaign.

10,284 contacts. 417 replies. About 4%. 103 real opportunities.

Small lists force you to be picky. One industry. One job title. One problem you know they have. The email can talk about their actual week.

As lists grow, "close enough" contacts sneak in, and each one drags the average down.

If you're starting outbound, build a list you can describe in one sentence. Run that first. Scale after you see replies, and only add the next segment once the first one is booking calls.

#coldemail #startups

---

## 7. What LinkedIn did for us [Ali]

Our LinkedIn numbers, all time:

3,511 profile views.
1,375 connection invites.
351 accepted.
1,628 InMails.
154 replies.

The audience was founders and angel investors. People who barely read cold email but do check LinkedIn.

That's the lesson. LinkedIn is great for a small, high-value list. Email is how you reach thousands. We use both, and the best results come when someone sees your name on LinkedIn before your email lands.

Pick the channel your buyer actually lives in. For most B2B markets, that means running both and watching which one books more calls.

#linkedin #outbound

---

## 8. The bounce column [Asim]

Four campaigns, four bounce rates:

0.45%. 1.64%. 2.87%. 3.08%.

Every bounce tells Gmail or Outlook you don't really know who you're emailing. Enough of them and your messages slide into spam. Then reply rates drop and everyone blames the copy.

We verify every list before it goes out. Even then, data goes stale. People change jobs. Companies get bought.

If your list has been sitting for a few weeks, verify it again. It costs a little. A burned domain costs a lot more.

#emaildeliverability #coldemail

---

## 9. Never risk the main domain [Ali]

Rule we've never broken: a client's main domain does not send cold email.

Every campaign runs on separate secondary domains. Set up with SPF, DKIM and DMARC. Warmed up before the first real send.

Why it matters: your main domain carries your invoices, your customer support, your proposals. If cold outreach damages its reputation, all of that starts landing in spam too.

It's the most boring part of our setup. It's also the reason we could send 96,408 emails in five days for one client without putting their real inbox at risk.

#coldemail #emaildeliverability

---

## 10. What "pipeline" means on our site [Asim]

Our site says $510K+ in pipeline generated.

Here's exactly what that means, because agencies love vague numbers.

Pipeline is the value of qualified opportunities we created, based on our clients' average deal of about $2,500. It's not closed revenue.

Closed revenue is a smaller number, and it's the client's sales team that closes it. For example, our construction software client signed 6 annual contracts worth $15,000 in closed deals so far.

If an agency shows you a pipeline number, ask how they define it. If they can't tell you in one sentence, be careful.

#b2bsales #agencylife

---

## 11. Where outbound leaks money [Ali]

In one campaign, 115 people said they were interested.

25 booked a call.

That's about 22%. And this is the step where most outbound programs lose money.

Someone writes back "sure, send me some times." Then the founder is busy, or the SDR is out, and nobody answers for two days. By then the prospect has moved on.

Fixes that cost nothing:

Reply to interested leads the same day.
Send two or three specific times, not "when works for you?"
Follow up once if they go quiet.

You already paid to get the yes. Don't lose it in the inbox.

#sales #outbound

---

## 12. Send when they're at their desk [Asim]

People ask us for the best time to send cold email.

Our answer is boring: weekdays, business hours, in the prospect's time zone.

An email that lands at 2 a.m. is buried under a pile of newer messages by the time they wake up. One that lands at 10 a.m. has a real shot.

Most of our clients sell across the U.S. and Canada. That's at least four time zones on the mainland. If you send everything at 9 a.m. Eastern, your West Coast list gets it at 6 a.m.

Turn on "send in lead's time zone" in your tool. It's one setting.

#coldemail #b2bsales
# Outreach emails

Final versions. Replace everything in [brackets]. Send from a founder's personal inbox, plain text, no tracking. Keep the follow-up in the same thread. One follow-up only, 5 to 7 days after the first email.

---

## 1. List-inclusion pitch

For authors of "best appointment setting agencies" or "best lead generation agencies" lists.

**Subject:** [List title] question

Hi [Name],

I read your list of [list title]. The section on [specific agency or point they made] was useful, especially [one detail].

I'm Ali, co-founder of WayneFlow. We run cold email, LinkedIn and X outreach for B2B companies, mostly in the U.S. and Canada.

If you update the list, I'd like to be considered. Some numbers you can check:

- 588,000 cold emails sent, 12,900+ replies, 100+ calls and demos booked
- One client: 96,408 emails in 5 days, 25 calls booked, 0.45% bounce rate
- A construction software client: 31 demos held, 6 annual contracts signed

Our case studies include screenshots of the live campaign dashboards: https://wayne-flow.site/results.html

Pricing is public too, if that helps your readers compare: $999 setup and $1,500 a month.

Happy to answer any questions or jump on a short call with you.

Thanks,
Syed Ali Hassan
Co-founder, WayneFlow
https://wayne-flow.site

### Follow-up

**Subject:** Re: [List title] question

Hi [Name],

Quick follow-up on this. If it helps, I can send dashboard screenshots for any of the numbers above, or a short write-up in whatever format you use for each listing.

No worries if the list isn't being updated right now.

Ali

---

## 2. Guest post pitch

For editors of B2B sales, marketing or SaaS blogs.

**Subject:** Guest post idea: what 588,000 cold emails showed us

Hi [Name],

I've been reading [blog name] for a while. Your post on [specific post title] made me rethink [one specific thing].

I'm Ali, co-founder of WayneFlow, a B2B appointment setting agency. My co-founder and I have each spent 8 years in outbound.

I'd like to write an original post for your readers. Two ideas:

1. **What 588,000 cold emails taught us about reply rates in 2026.** Real campaign data, including why our smallest list got a 4% reply rate and our biggest send got about 1.4%, and why both were fine.
2. **We turned open tracking off. Here's what happened to deliverability.** Why every dashboard we run shows zero opens, what we track instead, and the Google, Yahoo and Microsoft sender rules, linked to the official pages.

Both are 1,600 to 2,000 words, written for your site only, no sales pitch in the body. One short author bio at the end.

Would either work for you? Happy to follow your guidelines on length, links and format.

Thanks,
Syed Ali Hassan
Co-founder, WayneFlow

### Follow-up

**Subject:** Re: Guest post idea: what 588,000 cold emails showed us

Hi [Name],

Following up on this. If neither topic fits, I'm happy to pitch something closer to what your readers are asking about right now. Cold email legality in Canada (CASL) and outsourced appointment setting vs hiring an SDR are two I can cover with real numbers.

Ali

---

## 3. Podcast guest pitch

For hosts of B2B sales, agency or founder podcasts.

**Subject:** Guest idea for [Podcast name]: cold email in 2026

Hi [Name],

I listened to your episode with [guest name]. The part about [specific moment] stuck with me.

I'm Asim, co-founder of WayneFlow. We run outbound for B2B companies in the U.S. and Canada. Across our campaigns we've sent 588,000 cold emails and booked 100+ calls and demos for clients.

A few things I could talk about with real numbers behind them:

- Why we turned open tracking off on every campaign, and what we track instead
- A 5-day campaign: 96,408 emails, 115 interested prospects, 25 calls booked
- Why a 2.81% reply rate led to 6 annual contracts for a construction software client
- What changed when Google, Yahoo and Microsoft tightened their sender rules

I'll keep it practical. Your listeners should be able to fix something in their own outreach the same day.

Would that be a fit? Happy to work around your recording schedule.

Thanks,
Syed Asim Hussain
Co-founder, WayneFlow
https://wayne-flow.site

### Follow-up

**Subject:** Re: Guest idea for [Podcast name]: cold email in 2026

Hi [Name],

Bumping this in case it got buried. If it helps you decide, I can send a one-page outline of the episode with three or four questions you could ask.

Asim

---

## 4. Client review request (Clutch)

For happy clients only. Send after a good result, like a closed deal or a strong month.

**Subject:** Small favor?

Hi [Client first name],

Glad to see [specific result, e.g. "the 6 contracts signed this quarter"]. That was a good one.

Would you be open to leaving us a short review on Clutch? It helps other founders decide whether to work with us. It shouldn't take long.

Here's the link: [Clutch review link]

If it's easier, reply with a few honest lines about what worked and what could be better, and I'll help you get it into their format.

Either way, thanks for trusting us with your outreach.

Ali

### Follow-up

**Subject:** Re: Small favor?

Hi [Client first name],

Gentle nudge on the Clutch review. Totally fine if now's a busy time. The link is here whenever you have a few minutes: [Clutch review link]

Thanks again,
Ali
