---
name: msp-pricing
description: >
  Use this skill whenever pricing or packaging a managed-services or break-fix engagement for
  your MSP: building a quote or proposal, deciding what to charge a prospect, assembling options
  for a client, working out a price band for negotiation, or sanity-checking margin on a deal.
  Triggers include "how much should we charge", "price this client", "put together options for",
  "what should I quote", "build a package for", "what's the floor on this deal", "per-user price",
  "how deep can we discount", "should this include on-site", or any mention of quoting devices,
  seats, servers, network gear, on-site visits, contract length, or monthly recurring revenue for
  an IT services deal. Also trigger when reviewing or revising the price sheet or the building
  blocks. Always load this skill before producing any number a client could see. Apply
  alongside msp-sales (value conversation), msp-brand (presentation), and msp-client-comms
  (price-increase letters).
---

# {{COMPANY_NAME}} Pricing

**Defaults you must review:** every dollar figure, margin, floor, anchor, and multiplier in this
skill is one working MSP's numbers in one market. Rebuild the cost model with your own labor
costs and license costs before quoting anything to a client. See `references/labor-rates.md` for
the wage research behind the loaded costs and the levers that re-cost the whole sheet, and
`references/support-hours.md` for the labor-hour assumptions behind every building block.

This skill is a configurator. It knows the building blocks {{COMPANY_NAME}} sells and what each
one costs, and it takes what you learn about a prospect and assembles a few custom options for
that specific client, each priced to protect margin. The options may look like tiers, but they
are built per client from set parts, and you sell them as "here is what I put together for you,"
not "here is our Gold plan."

The governing idea comes from an MSP industry pricing methodology (Package, Price, Profit) and
the trusted-advisor shift:
diagnose first, then prescribe. Cost-plus math is the floor under every number, never the answer.
Your costs tell you the lowest price you can survive on. The client's situation tells you the
highest price they will happily pay. The skill finds that ceiling and opens near it.

Apply this with `msp-sales` (the discovery that surfaces requirements and value factors, and the
conversation that delivers the number) and `msp-brand` (voice and formatting once a number reaches
the client).

---

## The Three Numbers

Every line, every option, resolves to a band with three reference points. Always compute all three.

1. **FLOOR**: the walk-away. Loaded cost times 2.128 (a 50% gross margin after the 3% payment
   fee). Never quote below this without owner sign-off. This is what stops fear-based discounting.

2. **ANCHOR**: the published standard. Loaded cost times 2.703, rounded up to the nearest $10 (a
   60% gross margin after the 3% payment fee). This is the honest, sustainable default and the
   basis of the contract ladder. Both multipliers carry the ~3% cost of accepting card payments,
   so clients pay however they like with no surcharge and no margin leak; see the cost model.

3. **START**: the opening ask. The anchor lifted by value factors specific to this prospect, capped
   at 40% over anchor so the first number is ambitious but not insulting.

You open at START, concede down the contract-length ladder, and stop at FLOOR. The realistic landing
is between the anchor and the contract price for the term they commit to.

Do not eyeball any of this. Run `scripts/price_quote.py`. See `references/cost-model.md` for the
math, the full building-block catalog with costs, and the standing decisions about the sheet. The
remote and on-site labor costs are built up from researched market wages (decent L1 phone tech, good
field tech) rather than flat guesses; `references/labor-rates.md` documents that research and the
levers that re-cost the sheet when wages or drive times change. The per-device labor-hour estimates
were checked against industry support-load benchmarks too; `references/support-hours.md` has that
research and the per-line verdicts (notably why a server is 1.5 hours, not 1.0).

---

## The Building Blocks

These are the set parts you assemble from. Full costs and prices are in `references/cost-model.md`;
this is the menu.

**Recurring, per user (monthly):** two kinds of user. A **workstation** is a full "account and
computer" user: a managed machine plus that person's support. An **account-only** user has a managed
account but no managed machine (BYOD staff and 1099 contractors): identity, password and MFA, account
security monitoring, and licensing. Account-only is lighter and priced well below a full user, so
support people who do not have a company computer without charging them like they do.

**Recurring, per device (monthly):** server, mobile device, network base fee, firewall or router,
switch, wireless access point, camera, printer (business-class, networked only), special software.

**Per-endpoint add-ons (load onto the devices that need them):** endpoint protection (at the tier
msp-security Setup Decision 1 sets; plain, non-EDR by default), ZTNA (secure access), MDM
small-business or MDM enterprise tier (Mac management). These are real costs;
loading them keeps the anchor honest instead of quietly eating margin. They do not apply to
account-only users, who have no managed endpoint.

**On-site support (monthly allowance):** a set number of on-site hours bundled into the monthly fee,
expressed to the client as visits ("about one visit a month"). The current sheet is remote-first, so
this is the block that lets you cover clients who need hands on site. On-site work beyond the
included allowance bills per incident at the managed on-site rate on the break-fix card
(`references/break-fix-rates.md`).

**One-time:** onboarding and migration, always quoted separately from the monthly using break-fix
rates. Never absorb the cost of moving a client onto your stack.

---

## How to Build and Price a Client's Options

**Step 1: Gather requirements, not guesses.** From discovery you need the headcount split (how many
full users with a company computer versus how many account-only BYOD or contractor users), device
counts (servers, mobile, and each kind of network device), the OS mix (any Macs to manage), the
security and compliance picture, and what on-site expectations they have. A wrong count quietly
breaks the margin, so ask rather than assume. The `msp-sales` discovery framework drives this.

**Step 2: Select blocks against the requirements.** Map what they need to the building blocks:

- Each user with a company computer is a workstation; each BYOD or 1099 contractor who only needs a
  managed, secured account is an account-only line. Set the per-client headcount to the sum of both.
- Macs in the fleet pull in an MDM block.
- A regulated industry or a cyber-insurance requirement pulls in ZTNA and the compliance value
  factor.
- A real need for hands on site pulls in an on-site allowance.
- Servers, cameras, special software: include only what they actually run.
- Endpoint protection belongs on essentially every managed computer (not account-only
  users).

**Step 3: Assemble two or three options.** Not standard tiers: options you built for this client.
A workable shape is a lean option (the minimum that responsibly covers them), a recommended option
(what a sensible owner in their situation should choose, and where you want them to land), and a
fuller option (everything that genuinely fits, which also makes the recommended one look reasonable).
Mark the recommended option so the configurator anchors on it. Keep the options honestly different in
what they include, never in response time.

**Step 4: Score value factors per option.** Flag a factor only when discovery actually surfaced it.
These lift the opening ask because the prospect's situation makes a stable, secure environment worth
more to them than the average client.

| Factor | Uplift | Flag it when |
|--------|--------|--------------|
| Compliance | +20% | Regulated data: healthcare/HIPAA, payment/PCI, financial, legal |
| Downtime sensitive | +15% | An hour of downtime is measurable lost revenue |
| Security pressure | +12% | A cyber-insurance mandate or a recent scare is driving the talk |
| Power users | +12% | Specialized software, heavy workflows, high support volume |
| High pain | +8% | Acute pain, weak or absent incumbent, urgency to move |

Manufacturing factors to inflate the number is transparent and costs the deal. The +40% cap keeps the
opening honest.

msp-security Tier 2 items (quoted per client) and security remediation projects found in an
assessment are priced here, as add-ons or SOW projects. Tier 1 baseline controls are part of the
managed fee and are never itemized as extras.

**Step 5: Run the configurator.** Write a small JSON file describing the client and the options,
then:

    python3 scripts/price_quote.py --packages client.json

It prices every option (floor, anchor, contract price for the term, opening START, per-user, margin
at every line) and prints a side-by-side. For a quick one-off check, the CLI flags work too:

    python3 scripts/price_quote.py --workstation 24 --mobile 5 --server 1 --users 25 \
        --years 3 --edr --ztna --onsite-hours 2 --compliance --downtime-sensitive

**Step 6: Present the options, then stop talking.** Lead with the recommended option, open at its
START, and let silence do its work. "For everything we set up here, it is $X a month." Full stop. If
they push back, ask a question before touching the price. Do not pre-discount, do not apologize for
the number. The contract ladder is how you reward a longer commitment, not a reflex give-away.

---

## Standards and Minimums (do not break without owner sign-off)

- **One year is the minimum term, so the 1-year price is the highest price you ever show.** There is
  no month-to-month or sub-year rate. Every quote presents a term ladder with the 1-year at the top,
  and longer terms (2, 3, and 5 years) stepping down beneath it. State this in plain words on the
  quote: the highest price shown is the one-year term, and committing longer locks in a lower
  monthly rate. Never let a client believe there is a cheaper short-term option, because there is
  not.
- **Marketing carries no prices.** The only public number, in marketing material of any kind, is
  the $1,000/month engagement minimum (example default; see msp-sales presentation rules).
  Anchors, ladders, and per-user figures appear only in quotes and live conversations, after
  discovery. Published package pricing invites price shopping and commoditization.
- **50% gross margin is the floor**, on every line and every option, including on-site, measured
  after the 3% payment-processing skim that is baked into the multipliers.
- **Payment processing is baked in.** Clients pay by any method with no surcharge; a 3% processing
  cost is built into every price. Never add a card fee or convenience fee line to a quote, and never
  offer a "cash discount" -- the price is the price.
- **The contract ladder never breaks the floor.** Each year of commitment beyond the first removes 4%
  of the client's 1-year opening price (the START when value factors apply, otherwise the anchor;
  this matches what price_quote.py actually computes), so a five-year deal is 16% off and still
  comfortably above the floor. The
  discount is a real incentive to commit, deliberately tuned so longer terms never push you into
  thin margin. (Five percent per year is the absolute ceiling; it would land the five-year price
  a hair above the floor with no useful buffer, so 4% is the standing choice.)
- **Engagement minimum is $1,000/month.** Below this a managed client costs more attention than it
  returns. Re-scope, raise it, or pass.
- **Response time never varies by option or by price.** Differentiate options by what is included and
  how proactive you are, never by how fast you answer. Every client gets your best response.
- **Onboarding and migration are billed separately**, always, at the managed-client rates on
  the break-fix card (`references/break-fix-rates.md`).
- **Onboarding fee waiver.** The onboarding SOW fee may be discounted 50 to 100% as a
  closing incentive, only when the client signs a Service Order with at least a
  one-year term on or before the SOW date, and only with the clawback in the Service
  Order (waived amount becomes due on early termination, except for Provider's
  uncured material breach). The fee is still quoted in full on the SOW; the waiver is
  a stated discount against it, never a silent absorption. Anything outside these
  conditions needs owner sign-off.
- **After-hours hourly work bills at 1.5x and holiday work at 2x.** This skill is the owning
  source for both multipliers; msp-legal (the MSA states them) and msp-helpdesk (the desk
  applies them) both defer here. Never invent or waive multipliers ad hoc. They multiply the
  hourly rates on the break-fix card (example default: managed $110 remote / $220 on-site,
  non-contract $150 remote / $220 on-site).
- **There is no retainer rate.** The old $120/hr on-site courtesy is retired everywhere. Managed
  clients get managed hourly rates, non-contract callers get non-contract rates, nothing bills
  below the floor.
- **Multi-year terms carry a 3% annual escalator** (example default). On each anniversary
  after year one, the monthly fee increases 3%, stated plainly in the Order so it is never a
  surprise letter. The ladder discount is real and so is wage drift; the escalator is what lets
  both be true.
- **Third-party licenses bill at cost plus 15%** (example default), presented as a single
  line covering procurement, license management, and vendor liaison. Never quote licenses at
  bare cost, and never break out the markup as its own line.
- **You control the stack.** Pricing assumes your tools. A client who insists on theirs is buying
  custom work: quote it higher or decline.

---

## Setup Decisions

Everything above is what the example MSP settled for its own shop. Settle each of these for yours
before this skill goes anywhere near a client:

- **Labor cost basis.** The example uses a $25/hr L1 remote wage, a $32/hr field tech wage, and a
  1.30x burden, landing at $40/hr remote and $80/hr on-site loaded cost. Rebuild this from your own
  hiring market and benefits package; see `references/labor-rates.md` for the levers.
- **Margin targets.** The example uses a 60% gross margin anchor and a 50% gross margin floor, both
  measured after a 3% payment-processing fee baked into the multipliers. Decide your own margin
  targets and processing-fee assumption.
- **Engagement minimum.** The example uses $1,000/month as the smallest managed-client fee it will
  accept. Set your own based on what a client actually costs you to service.
- **Contract ladder discount.** The example removes 4% of the opening price per year of commitment
  beyond the first (never more than 5%, which would erase the buffer above the floor). Decide your
  own ladder.
- **Annual escalator.** The example raises multi-year monthly fees 3% on each anniversary after year
  one. Decide your own, and make sure it is stated plainly in your contract paper.
- **Third-party license markup.** The example bills licenses at cost plus 15%. Decide your own
  markup and whether it covers procurement and vendor liaison the same way.
- **After-hours and holiday multipliers.** The example uses 1.5x after-hours and 2x holiday. These
  multipliers should match whatever your legal paper and helpdesk practice actually promise.
  Whatever you land on, it is a single owning source, not something restated inconsistently across
  skills.
- **Break-fix and hourly rate card.** The example uses $110/$150 remote and $220 on-site (managed
  vs. non-contract). Rebuild this card from your own loaded costs in
  `references/break-fix-rates.md`.
- **On-site allowance pricing.** The example prices bundled on-site hours at the standard anchor and
  rides the contract ladder like everything else. Decide whether that is the right model for your
  service area and drive times.
- **Support-hour assumptions per device.** The example's per-block labor hours (1.0 for a
  workstation, 1.5 for a server, and so on) reflect a reactive, early-stage shop with limited
  automation. Revisit these once you have your own ticket data; see `references/support-hours.md`.

Once you have settled these, re-run `scripts/price_quote.py` against a known client (for example
`scripts/client.template.json`) and check how far the band moved before quoting anything live.

---

## Output

For an internal decision, run the configurator and walk the user through the options in plain terms:
which to lead with, where to open, where the realistic landing sits, and where each floor is. Keep it
in the conversation; this is a working number, not a deliverable.

When a number is going into something the client will see (a quote or marketing), present the
**client-facing term ladder** the configurator produces: the 1-year price on top, clearly labeled as
the minimum term and the highest price, with 2, 3, and 5 years stepping down. Hand off to `msp-brand`
for voice and formatting and to `msp-sales` for the value framing. The client should always meet the
price wrapped in the outcome it buys, presented as options assembled for them, never as a naked
spreadsheet or a standard tier card. The internal band (floor and opening ask) stays internal.
