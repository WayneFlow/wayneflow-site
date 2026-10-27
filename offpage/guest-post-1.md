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
