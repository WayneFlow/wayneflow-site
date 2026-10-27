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

*Syed Asim Hussain is co-founder of [WayneFlow](https://wayneflow.com), a B2B appointment setting agency that runs cold email, LinkedIn and X outreach for companies in the U.S. and Canada. He has spent 8 years in digital marketing and outbound.*
