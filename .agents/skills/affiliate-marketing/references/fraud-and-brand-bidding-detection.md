# Fraud and Brand-Bidding Detection

Because affiliate commission is directly tied to a tracked action, this channel has a structurally higher incentive for gaming than most others in this system — the partner's payment depends on triggering the tracked event, not on genuinely influencing the customer.

## Common patterns

**Cookie stuffing.** A partner drops tracking cookies on users who never actually saw or clicked a genuine affiliate link — via hidden iframes, forced redirects, or browser-extension injection — so that a later, unrelated purchase is credited to them. Detect via unusually high click-to-cookie ratios, conversion patterns disconnected from any visible traffic source, or a partner's reported clicks that do not correspond to any real referral pattern.

**Brand bidding.** A partner bids on the business's own branded search terms, often outranking the business's own ad or landing in front of an organic result the business would have received for free, then captures commission on a sale that required no incremental effort from the partner. This both pays commission for a sale the business would likely have gotten anyway and can raise the business's own paid-search costs by adding a competing bidder on its own brand.

**Coupon-code leakage and poaching**, covered in [Attribution integrity](attribution-integrity.md), is a milder but far more common version of the same underlying problem: capturing credit for a purchase already in motion.

**Incentivized or fake traffic.** Traffic driven through pay-to-click schemes, bot networks, or explicitly incentivized clicks (users paid or rewarded to click, regardless of genuine interest) inflates click and sometimes conversion metrics without real customer intent behind them.

## Method

1. Screen partner-level metrics for anomalies before evaluating raw performance: unusually high conversion rate relative to category norms, a click pattern with no plausible traffic source, or a conversion rate that moves sharply with no corresponding change in the partner's actual promotional activity.
2. Establish and monitor an explicit brand-bidding policy: whether partners may bid on branded terms at all, and if so, under what restriction (exact match only, must not outrank the business's own ad, must use approved ad copy). Check actual bidding behavior against the stated policy, not just the policy's existence.
3. For a suspected cookie-stuffing pattern, cross-reference the partner's claimed traffic source against server-side or third-party verification where available, rather than accepting the network's or partner's self-reported numbers alone.
4. Treat an unexplained spike in any partner's volume as a screening trigger, not a success signal, until the anomaly is explained.

## Rules

- A brand-bidding violation is not a minor policy breach; it typically represents commission paid for demand the business already owned, and should be enforced (restrict, suspend, terminate) rather than tolerated for the sake of volume.
- Do not accept a partner's self-reported traffic source or promotional activity as sufficient verification for a flagged anomaly; require independent or platform-level confirmation where available.
- Do not treat a high-converting partner as automatically legitimate; a suspiciously high conversion rate relative to category norms is itself a fraud-screening signal, not proof of quality.
- Enforcement action (restrict, suspend, terminate) against a partner is a real relationship and revenue decision; state the evidence and confidence level supporting it explicitly rather than acting on a single ambiguous signal.
