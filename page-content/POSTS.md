# Clyve page: first two posts (DRAFTS, nothing posted)

Rule: every statement below maps to evidence in the claims log. No stats, no "most brands", no outcome promises.

---

## Post 1 · Pinned "Start here" (multi-image post, 8 slides)

Files: `start-here/slide-01.png` ... `slide-08.png` (2160×2700, 4:5)

**Caption**

What is GTM engineering, and what does Clyve do with it?

GTM engineering is building automated revenue systems. Clyve does it for brands: audit first, then build.

8 slides, with sources on the definition slides. If you want an audit, DM us.

**Sources to put in the first comment** (links in comments, per your platform rules)
- https://www.clay.com/blog/gtm-engineering
- https://www.topo.io/glossary/gtm-engineer

**Claims log**

| # | Statement | Evidence |
|---|---|---|
| 1 | "Brands don't have a content problem. They have a go-to-market system problem." | Akul's approved About text (opinion) |
| 2 | "Facts live in a few heads. Content gets made by hand. That is a system problem. And systems can be engineered." | Opinion, labelled as the problem framing |
| 3 | "GTM engineering is the practice of building automated revenue systems using AI, data enrichment, and workflow automation." | Clay, verbatim, fetched 17 Nov 2026: clay.com/blog/gtm-engineering. NOTE: Clay is a vendor, so the slide names the source |
| 4 | Four things GTM engineers build (CRM/enrichment/outreach integrations; scripts that clean and de-duplicate lead data; automated outbound playbooks; product-usage signals to sales reps) | Topo glossary, fetched 17 Nov 2026: "API Integration", "Data Hygiene Automation", "Tool Configuration", "PLG Signals". Paraphrased, source printed on slide. Topo is also a vendor |
| 5 | "Find and fix revenue bottlenecks." | Clay: "GTM engineers find and fix revenue bottlenecks." |
| 6 | "Clay says it coined the title in 2023" | Clay: "Clay coined the term in 2023". Attributed to Clay, not asserted as fact |
| 7 | "act like an internal product team for the go-to-market organization" | Clay: "At Clay, our GTM engineers act like an internal product team that serves our GTM organization." Slide says "Its GTM engineers", meaning Clay's |
| 8 | "Audit first: map how your go-to-market runs today. Then build the system." | Clyve's offer path (Akul's locked positioning) |
| 9 | "Our own posts go through a claims log and a source check" | Drafts end with a claims log (docs/how-it-works.md); `automation/freshness.py` morning_check |
| 10 | "Build logs ... every week on this page" | COMMITMENT, not a fact. Keep only if Akul will post weekly |

Removed per Akul: his name, ContentOps, AI visibility.

---

## Post 2 · Build log 01 (single image)

File: `build-log-1/card.png`

**Caption**

Build log 01: how Clyve runs its own content.

Clyve runs its own content on a system. Ours has 7 steps, from reading what is working to a human pressing post. Along the way: the 14-day plan is checked in code, every draft ends with a claims log, drafts are linted, sources are re-read the morning a post goes out, and an image card is not rendered if it shows a number the draft does not contain.

Next in this series: the claims log, with a real example.

**Claims log**

| # | Statement | Evidence |
|---|---|---|
| 1 | Step 1: reads what is working on LinkedIn and Instagram | `docs/how-it-works.md` "Trend read": headless Claude session reads LinkedIn + Instagram, read-only |
| 2 | Step 2: plans the next 14 days, rules checked in code | `docs/how-it-works.md` "Rolling 14-day blocks"; `automation/blocks.py:210 validate_block` |
| 3 | Step 3: every draft ends with a claims log | `docs/how-it-works.md`: "Every draft ends with a claims log, the placeholders..." |
| 4 | Step 4: lint the draft | `automation/lint.py` `check()` |
| 5 | Step 5: sources re-read the morning a post goes out | `automation/freshness.py:57` `morning_check` re-runs `draft.verify`; docs/how-it-works.md:116. PARTLY: it warns, never blocks or skips. "Each claim" not verified, so caption says "sources" |
| 6 | Step 6: an image card is not rendered if it shows a number the draft lacks | `automation/assets.py:125-130`, log at :178. PARTLY: applies to single-image cards only, not carousel slides (:170 has no such gate) |
| 7 | Step 7: a human posts it | README: "you do the posting" |

(Removed an inferred "why" clause from the caption: the reason for adding the checks is not documented.)

---

## Not yet posted (needs real data)
- Answer Anatomy (frozen prompt run on real assistants, dates and raw answers saved)
- Claims-log walkthrough (use a real log from `weeks/`, check it has nothing private)
