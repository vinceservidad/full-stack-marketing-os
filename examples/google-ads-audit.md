# Worked example: Google Ads audit

**Skill under test:** `$google-ads` (routed via `$marketing-router`, handed off to `$marketing-intake` first — see step 0)
**Inputs:** [`fixtures/google-ads-search-terms.csv`](fixtures/google-ads-search-terms.csv), [`fixtures/google-ads-conversion-setup.md`](fixtures/google-ads-conversion-setup.md)

Both fixtures are synthetic. No client data appears here, and nothing below is a
performance claim about any real account. This shows the shape and standard of the
output, and reproduces from the two files above.

---

## Step 0 — Intake, before any audit

The request arrives as "audit my account and tell me if it's profitable." COGS is
supplied as *"around 30%, I think"* with no artifact. Under `$marketing-intake`,
that is an **asserted** figure, not observed, and confidence in the speaker does
not upgrade it.

**Consequence, recorded before the audit starts:** efficiency analysis proceeds and
is labeled as such. The profitability question is **blocked**, not estimated from a
category benchmark.

---

## Scope

| | |
|---|---|
| Account | Single Google Ads account, UK, GBP |
| Period | Last 30 days |
| Campaigns | `Search - Brand`, `Search - Non-Brand` |
| Business source of truth | Shopify net revenue, £14,880 |
| Requested | Efficiency and scalability assessment |
| Excluded | Shopping and Performance Max (not present); profit conclusions (blocked, above) |

## Measurement status — **failed, and it gates everything below**

Three defects, in order of how much they distort the numbers.

**1. Purchases are double-counted.** `Purchase` (Google Ads tag) and `Purchase (GA4)`
are both Primary and both sit inside the `Purchases` conversion goal. One transaction
is counted twice, and its value twice.

**2. A £5 assigned-value newsletter signup is Primary inside the same goal.** Both
campaigns bid to `Maximize conversion value` against that goal, so bidding is being
steered toward email signups, and £5 of non-revenue is added to reported value for
each one.

**3. Reported value exceeds total business revenue.** Google Ads claims £17,094.50 of
conversion value in a period where the business made **£14,880 across all channels**.
Google Ads alone reports 114.9% of the whole company's revenue. Even before
apportioning any of it to organic, email, or direct, the figure is impossible.

> **Every efficiency number in this audit inherits these defects.** They are reported
> because the ratios between segments are still informative. No number here is
> reconciled, and none should be used to set a target or a budget until it is.

**Owner of the fix:** `$tracking-measurement`. This audit does not change tracking.

## Findings

### F1 — Brand and non-brand share one goal and one target, so brand is masking acquisition

| Segment | Cost | Reported value | Reported ROAS |
|---|---:|---:|---:|
| Brand | £527.00 | £12,867.00 | 24.4x |
| Non-brand | £2,841.81 | £4,227.50 | 1.49x |
| **Blended** | **£3,368.81** | **£17,094.50** | **5.07x** |

Both campaigns run `tROAS 600%` against the account-default goal. Blended performance
(507%) reads as a near-miss against target. It is two different businesses averaged
together: brand at 24.4x, which largely captures demand that already exists, and
non-brand acquisition at 1.49x.

**Evidence:** fixture search-terms export, segmented by campaign.
**Impact:** high — the number the account is optimized against is not the number that
describes new-customer acquisition.
**Confidence:** high on the split; the absolute values inherit the measurement defects.

### F2 — Non-brand acquisition is at best around break-even, and the real figure is worse

At the **asserted** 30% COGS, and taking the reported value at face value:

```
Non-brand reported value        £4,227.50
Gross margin at 30% COGS  ×0.70 £2,959.25
Media cost                     -£2,841.81
                                ---------
Contribution after media          £117.44
```

That is 2.8% of revenue, before fulfillment, payment fees, and refunds — none of
which were supplied. Since the reported value is inflated by F1's defects, the
true figure is below this, and plausibly negative.

**This is a sensitivity, not a conclusion.** It exists to show that the profitability
question is decision-relevant, not to answer it. It resolves when a COGS artifact and
the missing cost lines arrive.

**Confidence:** low on the absolute number; high that the answer is not "scale this."

### F3 — One query is genuinely irrelevant; the rest are not

`serum jobs london` (£39.10, 34 clicks, 0 conversions) is job-seeker intent. It cannot
convert. Negative it.

**Three queries that look like the same problem and are not:**

| Query | Cost | Conv | Why it stays |
|---|---:|---:|---|
| `how to use vitamin c serum` | £246.10 | 1 | Informational intent from a real buyer segment. Assisted value is unmeasurable while F1–F3 measurement defects stand. |
| `is vitamin c serum safe during pregnancy` | £66.70 | 0 | 58 clicks is far too small a sample to conclude anything. |
| `vitamin c serum boots` | £122.88 | 0 | Retailer-intent, but this is the competitor-set query a brand usually wants visibility on. A negative here is a coverage decision, not a cleanup. |

Per this skill's rules: **never add a negative solely because a query did not convert
in a small sample.** Consider intent, spend against allowable CPA, assisted value, and
protected coverage. Only `serum jobs london` clears that bar on this evidence.

### F4 — The best-performing non-brand query is a broad-match long-tail with no dedicated home

`best vitamin c serum for sensitive skin` — £241.06, 9 conversions, £742.50 value,
3.08x ROAS, against the non-brand average of 1.49x. It sits in a general `Serums` ad
group on broad match, so its landing experience and ad copy are generic.

**Confidence:** medium. Nine conversions is a signal, not a proven segment.

## Protected coverage

Do not reduce without a separate decision: all three brand queries (24.4x, and
defending brand terms from competitors), and `vitamin c serum for dark spots` — the
strongest specific-intent non-brand term at 3.03x.

## Prioritized actions

| # | Action | Owner | Reversible | Approval |
|---|---|---|---|---|
| 1 | Deduplicate `Purchase` / `Purchase (GA4)`; demote one to Secondary | `$tracking-measurement` | Yes | Required — changes bidding inputs |
| 2 | Remove `Newsletter signup` from the `Purchases` goal, or set its value to £0 | `$tracking-measurement` | Yes | Required |
| 3 | Reconcile corrected Google Ads value against Shopify by day | `$tracking-measurement` | Yes (read-only) | No |
| 4 | Split brand and non-brand onto separate conversion goals and separate targets | `$google-ads` | Yes | Required |
| 5 | Add `serum jobs london` as a campaign negative | `$google-ads` | Yes | Required |
| 6 | Supply a COGS artifact plus fulfillment, fees, and refund rate | Client | n/a | n/a |

**Nothing above has been executed.** Items 1–5 are drafts. Under this system a live
change needs the exact entity, current and proposed state, rationale, risk, a
rollback rule, and explicit approval.

## Tests

- **After actions 1–3 only:** re-measure for one full purchase cycle before changing any bid or budget. The corrected baseline is the deliverable, not an improvement.
- **F4:** move `best vitamin c serum for sensitive skin` into its own ad group with matched copy and a sensitive-skin landing page. Stop rule: no lift in qualified conversion rate after 200 clicks or 21 days, whichever is later.

## Unknowns

| Unknown | Blocks |
|---|---|
| COGS (asserted, no artifact) | Every profitability conclusion |
| Fulfillment, payment fees, refund rate | Contribution after media |
| Newsletter signup count in the period | Sizing the inflation in F1 |
| Non-Google channel contribution to the £14,880 | Reconciliation in action 3 |
| New versus returning customer split | Whether brand ROAS reflects acquisition at all |

## What this example is for

It demonstrates the failure mode this system is built to prevent: an account whose
blended 5.07x ROAS looks like a near-miss against target, where the measurement is
broken in three directions, brand is subsidizing acquisition that is roughly
break-even, and the profitability question cannot honestly be answered at all with
what was supplied.

An audit that reported "5.07x ROAS, slightly under target, tighten up the wasted
spend" would be wrong on every count while sounding useful.
