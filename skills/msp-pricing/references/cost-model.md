# {{COMPANY_NAME}} Pricing: Cost Model, Building Blocks, and Worked Examples

**Defaults you must review:** the costs, multipliers, and worked example below are one working
MSP's numbers in one market. See the "Setup Decisions" section of `../SKILL.md` before treating
any figure here as settled for your shop.

This is the detail behind the SKILL.md band logic. Read it to explain a number, revise the sheet, or
assemble a client's options. Everything is monthly USD unless noted.

## Contents
1. The cost formula
2. The building-block catalog (costs and prices)
3. The price formula (anchor, ladder, floor, start)
4. Standing decisions about the sheet
5. Value-factor logic
6. Worked example: three options for one client
7. On-site support: the open pricing decision

---

## 1. The Cost Formula

Loaded monthly cost for one recurring unit:

    loaded_cost = fixed_base + (labor_hours * remote_labor_rate)

Remote labor is about $40/hour and dominates most lines. On-site labor is about $80/hour. Neither is a
magic number anymore: both are built up from researched market wages (a decent L1 phone help desk tech
at ~$25/hr and a good field services tech at ~$32/hr), a 1.3x burden for taxes and benefits, and
delivery factors (escalation and tooling for remote; travel, utilization, and vehicle for on-site).
The build-up lands on $40 and $80, so existing prices are unchanged, but the basis is now transparent
and tunable. See `references/labor-rates.md` for the full research, sources, and the levers that
re-cost the whole sheet.

The monthly labor hours per block (1.0 for a workstation, 1.5 for a server, and so on) were checked
against industry support-load benchmarks; `references/support-hours.md` documents that research and the
per-line verdicts.

One real cost deliberately NOT in the loaded cost: payment processing (~3% of revenue). A fee on
revenue cannot be modeled as a fixed cost, so it lives in the pricing multipliers instead. See
section 3 and the standing decisions.

---

## 2. The Building-Block Catalog

**Recurring, per device:**

| Block | Fixed base | Labor hrs | Loaded cost | Anchor (1-yr) |
|-------|-----------|-----------|-------------|---------------|
| Workstation (account + computer user) | $10 | 1.0 | $50 | $140 |
| Account-only user (no managed machine) | $4 | 0.4 | $20 | $60 |
| Server | $15 | 1.5 | $75 | $210 |
| Mobile device | $12 | 0.5 | $32 | $90 |
| Network base fee | $0 | 0.5 | $20 | $60 |
| Firewall / router | $0 | 0.5 | $20 | $60 |
| Switch | $0 | 0.1 | $4 | $10 |
| Wireless access point | $0 | 0.1 | $4 | $10 |
| Camera | $0 | 0.1 | $4 | $10 |
| Printer (business-class, networked) | $0 | 0.3 | $12 | $40 |
| Special software | $0 | 1.0 | $40 | $110 |

A workstation line is a full user: a managed computer plus that person's support. An account-only line
is a user with a managed account but no managed machine (BYOD staff, 1099 contractors): identity
provisioning and deprovisioning, password and MFA support, account security monitoring, and license
management. It is lighter (0.4 hour versus 1.0) because there is no machine to maintain, landing at a
$60 anchor, about 43% of a full user. Set the per-client headcount to the sum of both: full users plus
account-only users. Endpoint agents (endpoint protection, MDM) do not apply to account-only users since
there is no managed endpoint; for heavy identity-security needs, raise the account-only labor or use
the security-pressure value factor.

(All anchors are the 2.703x value rounded up to the nearest $10; switch, WAP, and camera hold at $10
under the small-item exception. See standing decisions.)

**Per-endpoint add-ons (costs, loaded onto the device that uses them):**

| Add-on | Cost | Loaded onto |
|--------|------|-------------|
| Endpoint protection (plain tier by default; see msp-security Setup Decision 1) | $1.30 | essentially every managed workstation/server |
| ZTNA (secure access) | $7.00 | endpoints needing secure access |
| MDM (small business tier) | $5.00 | managed Macs (small business) |
| MDM (enterprise tier) | $7.00 | managed Macs (enterprise) |

**On-site support (per included hour):** loaded cost $80, anchor $220/hr (60% GM after fees), floor
$180/hr (50% GM after fees). Bundle a set number of hours into the monthly and describe them to the client as visits.

**One-time:** onboarding and migration, quoted from break-fix rates, always separate from the monthly.

---

## 3. The Price Formula

**Anchor (published 1-year price):**

    anchor = roundup_to_10(loaded_cost * STD_MULTIPLIER)
    STD_MULTIPLIER = 1 / (1 - PROC_FEE - 0.60) = 1 / 0.37 = ~2.703      (PROC_FEE = 0.03)

The multiplier delivers a 60% gross margin AFTER the 3% payment-processing fee that is baked into
every price (see standing decisions). Round up to the nearest $10. Before the fee decision this was a
flat 2.5x; the margin target has not changed, only what it survives.

**Contract ladder (reward for commitment, never breaks the floor):**

    price(years) = round(opening * (1 - 0.04 * (years - 1)))    for years 1..5
    where opening = the client's 1-year price: START when value factors apply, otherwise anchor

Each year beyond the first removes 4% of the opening price. Off the anchor, five years lands at
16% off, about a 53% gross
margin after fees. This is deliberately tuned: the anchor is a 60% margin and the floor is 50%, so the
ladder can only ever give away that 10-point gap. At 4% per year the deepest discount keeps a safety
buffer above the floor. Five percent per year (20% off at five years) is the hard ceiling, landing a
hair above the floor with no useful buffer.

**Minimum term and what clients see.** One year is the minimum term, so the 1-year price is the highest
number on any quote. There is no shorter or month-to-month rate. Clients are always shown a term
ladder topped by the 1-year price, with the longer terms presented beneath it (the standing set is
1, 2, 3, and 5 years; year 4 exists in the math but is not presented by default, set by
PRESENT_TERMS in the script). The configurator builds this client-facing ladder off the 1-year
opening price for that client (the START when value factors apply, otherwise the anchor), so the
1-year is always the highest figure and longer terms step down from it. Ladders appear on quotes
only; marketing carries no prices except the $1,000/month engagement minimum (example default).

**Floor (hard minimum):**

    floor = roundup_to_10(loaded_cost * FLOOR_MULTIPLIER)
    FLOOR_MULTIPLIER = 1 / (1 - PROC_FEE - 0.50) = 1 / 0.47 = ~2.128

The multiplier is a 50% gross margin after the payment fee. Anything below this needs owner sign-off.

**Start (opening ask):**

    start = roundup_to_5(anchor * (1 + total_value_uplift))    capped at anchor * 1.40

---

## 4. Standing Decisions About the Sheet

**Payment processing is baked into the multipliers (example default).** Clients pay by any
method with no surcharge, and {{COMPANY_NAME}} does not absorb the fee: a 3% processing cost (a
typical card-processing rate) is built into both multipliers (anchor 2.703x, floor 2.128x, from
1/(0.97-GM)). Never add a card fee or convenience fee line to a quote, and never offer a cash
discount. Assumes standard free deposits from your payment processor; the optional instant-deposit
fee (commonly around 1%) stays off. Small-item exception: switch, WAP, and camera anchors hold at
$10 rather than doubling to $20 over a ~$0.30 fee (57% GM after fees, above floor).

**"250.00% Margin" is mislabeled.** A 2.5x multiplier is a 60% gross margin / 150% markup, not a 250%
margin. The math the sheet performs is healthy; only the label is off. Renaming that column "2.5x
multiplier (60% GM)" would prevent confusion.

**Agent costs are not in the base cost.** Endpoint protection, ZTNA, and MDM are real
per-endpoint costs the Managed Services base does not capture. The configurator loads them on
demand. Folding at least endpoint protection into the standard workstation cost would make the
anchor honest by default.

**The contract ladder was re-tuned from 10% to 4% per year.** The original sheet discounted 10% per
year, which dropped the five-year price to a 33-36% gross margin, under the floor. The intent was to
reward commitment, not to sell thin. At 4% per year, every term from one to five years clears the 50%
floor while still giving a meaningful 16% discount at five years. The old five-year workstation price
was $78 (36% GM); the re-tuned one is about $118 (55% GM after fees, off the $140 anchor).

**Server labor raised from 1.0 to 1.5 hours.** The original sheet gave a server the same labor hour as
a workstation, setting the server anchor at only $140 against a market norm of about $200. Servers are
higher-touch (patching with maintenance windows, backup verification, tighter monitoring), so 1.5 hours
is the balanced estimate, putting loaded cost at $75 and the anchor at $210. Use 2.0 hours for a
server-heavy or high-availability client. See `references/support-hours.md` for the benchmarks.

**Managed Printer line (shipped example default).** Business-class networked printers only,
0.3 hr/month, $12 loaded, $40 anchor, $30 floor. Scope is by delivery channel: the monthly
covers everything remote-deliverable (connectivity, IP management, driver deployment, print
queues/spooler, scan-to-email and scan-to-folder config, firmware updates) plus vendor
liaison: you run warranty claims so the client never calls a printer vendor. Physical work
(repairs, swaps, installs) rides the client's on-site allowance or break-fix on-site rates.
No consumables, ever: no toner resale, no supplies management. Consumer-grade, inkjet, or
USB-attached printers get no monthly line, best-effort hourly only, flagged at onboarding
with a replacement recommendation under "you control the stack."

**Anchors are rounded up to $10.** $50 x 2.703 = $135.14 rounds to $140; $75 x 2.703 = $202.70 rounds
to $210. The small lines (switch, WAP, camera) are the exception noted above and hold at $10.

---

## 5. Value-Factor Logic

Value factors lift the opening ask above the anchor because the prospect's situation makes a stable,
secure environment worth more to them. They are additive, then capped at +40%.

| Factor | Uplift | Evidence required from discovery |
|--------|--------|----------------------------------|
| Compliance | +20% | Named regulated data: HIPAA, PCI, financial, legal |
| Downtime sensitive | +15% | A figure or clear story for the cost of an hour down |
| Security pressure | +12% | Cyber-insurance requirement or a recent incident |
| Power users | +12% | Specialized software, heavy workflows, high support volume |
| High pain | +8% | Acute pain, weak or absent incumbent, urgency |

Only flag what discovery surfaced. Respect the +40% cap: an opening more than 40% over your published
price reads as a shakedown.

---

## 6. Worked Example: Three Options for One Client

Acme Dental: 24 workstations, 5 mobile, 1 server, a small office of network gear, 25 users, considering
a 3-year term, HIPAA-regulated, schedule-dependent (downtime hurts). Three options assembled from
blocks (the JSON for this lives alongside the script as a template):

| Monthly | Lean | Recommended | Full Coverage |
|---------|------|-------------|---------------|
| Floor (walk-away) | $3,140 | $4,160 | $4,820 |
| Anchor (1-yr standard) | $3,980 | $5,130 | $6,110 |
| START (open here, internal) | $3,980 | $7,065 | $8,665 |
| Client 1-yr (highest) | $3,980 | $7,065 | $8,665 |
| Client 2-yr | $3,820 | $6,780 | $8,320 |
| Client 3-yr | $3,660 | $6,500 | $7,970 |
| Client 5-yr | $3,345 | $5,935 | $7,280 |

The first three rows are internal (where you walk away, your standard, and where you open). The four
Client rows are what goes on the quote: the term ladder, topped by the 1-year minimum term.

How to read it. Lead with Recommended (server, endpoint protection, secure access, a 2-hour monthly
on-site allowance, compliance and downtime factors flagged). Open at its START of $7,065. What the
client actually sees is a term ladder off that opening: 1 year $7,065 (the minimum term and highest
price), 2 years $6,780, 3 years $6,500, 5 years $5,935, about $237/user at the five-year rate, which
sits right in the $150-300 band for a compliance-driven client. Lean exists to be the responsible floor
of the conversation; Full Coverage exists to make Recommended look reasonable. Every margin on every
line stays in the mid-50s to low 60s after the payment fee, clear of the floor, even at the 3-year
discount.

The instinct to quote this client around $2,500 (a naive per-user ballpark of 25 x $100) would have
left well over $3,000/month on the table against any of the Recommended term prices. The defensible
number is far higher than the nervous number.

---

## 7. On-Site Support (example default)

The configurator prices included on-site hours at the standard anchor ($220/hr, 60% GM after fees) so a bundled
allowance holds the same margin as everything else and rides the same contract ladder.

On-site work beyond the included allowance bills per incident at the managed on-site rate on the
break-fix card (`break-fix-rates.md`), currently the same $220/hr. The old $120/hr retainer
courtesy rate is retired; it ran a 30% gross margin after the payment fee, well below the floor,
and no hourly work bills below the floor anymore. This closes what was previously the open
on-site pricing decision.
