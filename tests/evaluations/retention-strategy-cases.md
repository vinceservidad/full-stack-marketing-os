# Retention Strategy Behavioral Evaluations

These cases test `$retention-strategy` routing, evidence discipline, intervention fit, customer-choice boundaries, economics, and exact state.

| # | Case | Expected behavior |
|---:|---|---|
| 1 | User asks “reduce churn” with no definition | Require/label churn definition, cohort, window, and business model before a decision-grade intervention. |
| 2 | Cancellation survey says “too expensive” | Preserve as customer-stated evidence, not verified cause. Check pricing/value/fit/other evidence. |
| 3 | 80% of survey respondents select price but only 10% of cancellers answered | Report response coverage; do not treat 80% as prevalence across all churn. |
| 4 | Survey reason options changed last month | Do not compare reason shares as if definitions were stable. |
| 5 | Failed card customers are mixed with voluntary cancellations | Separate involuntary loss before intervention design. |
| 6 | Failed payment receives a 30% discount by default | Reject default discount; diagnose payment recovery mechanics first. |
| 7 | Customer cancelled after verified service outage | Route root defect to implementation/service owner before persuasion. |
| 8 | Product is still broken but user wants win-back ads/emails | Do not win back before the reason is resolved or explicitly changed. |
| 9 | Low activation precedes high churn | Route first-value barrier to `$activation`; retention strategy may treat it as upstream cause hypothesis. |
| 10 | Poor-fit acquisition cohort churns quickly | Route fit/qualification to `$icp-jtbd` and acquisition owner; do not trap poor-fit customers. |
| 11 | Team proposes exit discount to every canceller | Reject blanket treatment; segment by diagnosed reason and economics. |
| 12 | Team proposes hidden cancel link to lift retention | Reject as deceptive cancellation friction. |
| 13 | Team proposes five extra confirmation screens before cancel | Reject if material purpose is obstruction rather than necessary informed choice. |
| 14 | Customer unsubscribed from marketing but team wants win-back email | Honor suppression; do not create workaround contact. |
| 15 | Cancellation save accepted today | Do not call durable retention until continuing paid/value behavior is observed. |
| 16 | Card retry succeeds | Label payment recovered; do not automatically label durable retention. |
| 17 | Save offer delays cancellation by seven days, then customer cancels | Do not count as durable save. |
| 18 | Discounted renewals increase 20% but contribution drops | Do not call clean retention win; surface economics harm. |
| 19 | Renewal rises but refunds spike | Treat guardrail harm as failure/compromised result, not win. |
| 20 | Repeat purchase rises after earlier reorder reminders | Check pull-forward, stockpiling, later demand, returns, and contribution. |
| 21 | Ecommerce product is normally one-time purchase | State dedicated retention layer may not be decision-relevant rather than inventing repurchase. |
| 22 | Seasonal product customers have not repurchased off-season | Do not classify as churn without need-cycle evidence. |
| 23 | Subscription cancellation because project completed | Recognize no-longer-needs outcome; retention may be inappropriate. |
| 24 | Customer switches competitor | Investigate selection criteria; do not copy competitor or automatically undercut price. |
| 25 | Customer says “not using it” | Diagnose value, habit, fit, activation, and changed need rather than assuming reminder solves it. |
| 26 | Customer cancels after unexpected price increase | Pricing is a material commercial cause candidate; route price decision to `$pricing-monetization`. |
| 27 | User asks to redesign cancellation offer pricing | `$retention-strategy` owns eligibility/mechanism; `$pricing-monetization` owns commercial terms. |
| 28 | User asks for churn email subject lines | `$retention-strategy` owns reason/intervention objective; `$lifecycle-marketing` owns trigger/cadence; `$copywriting` owns words. |
| 29 | User asks only for cohort churn/LTV | Route primary ownership to `$retention-economics`, not retention strategy. |
| 30 | User asks why churn rose and what to do | Retention strategy owns diagnosis/intervention; retention economics supplies cohort evidence. |
| 31 | Exposed save-offer users retain better than unexposed | Do not infer causality without design; route causal validity to `$tracking-measurement`. |
| 32 | High-engagement customers retain more | Do not claim engagement causes retention from association alone. |
| 33 | Team excludes hard-to-save users after seeing results | Reject post-hoc eligibility/denominator gaming. |
| 34 | Team changes “saved” definition after results | Preserve predeclared definition; post-hoc redefinition invalidates comparison. |
| 35 | Team measures save rate only, not economics | Require realized continuation/economics and guardrails. |
| 36 | Team measures email clicks as retention | Reject diagnostic engagement as retained-value outcome. |
| 37 | Team measures coupon redemption as win-back success | Require realized return/continuation and economics beyond redemption. |
| 38 | Win-back customer buys once on 70% discount then disappears | Do not call durable win-back without downstream behavior/economics. |
| 39 | Recovered customers require repeated discounts every renewal | Surface discount dependency and contribution risk. |
| 40 | Cancellation survey has free-text complaints | Treat as research evidence; code with provenance and preserve contradictions. |
| 41 | A few vivid public reviews complain about support | Do not infer churn prevalence from review vividness. |
| 42 | Billing platform outage causes spike in churn metric | Diagnose involuntary/system cause before marketing intervention. |
| 43 | Measurement definition of active customer changed | Fix/reconcile definition before diagnosing retention behavior. |
| 44 | Product plan migration changes entitlements | Treat as possible cohort boundary and route commercial/product implications appropriately. |
| 45 | Activation journey changed mid-cohort | Preserve as cohort boundary/confounder when interpreting retention. |
| 46 | Team wants to contact cancelled customers forever | Require need-relevant timing, consent/suppression, and stopping rules. |
| 47 | Customer explicitly says do not contact | Suppress; retention objective cannot override preference. |
| 48 | Legal/contract cancellation right applies | Preserve the right; flag legal review if interpretation is material. |
| 49 | Customer can pause instead of cancel, and pause is genuinely available | May test pause when cause-compatible; disclose terms and measure eventual continuation. |
| 50 | Pause is offered but hidden fees continue | Reject misleading intervention; commercial exchange must remain legible. |
| 51 | Downgrade removes critical capability without clear disclosure | Reject as uninformed save; customer choice must be meaningful. |
| 52 | Support agent manually promises benefit not in policy | Do not institutionalize unsupported promise; route product/offer/policy truth. |
| 53 | Customer churn reason remains unknown | Preserve unknown/mixed state; do not force a reason or intervention. |
| 54 | Several causes interact | Preserve contributing causes; do not force single primary reason without support. |
| 55 | At-risk score comes from a model with no validation | Treat as hypothesis/provisional; do not automate intervention solely from score. |
| 56 | Risk model is accurate overall but weak for one segment | Segment evidence; do not apply universal threshold. |
| 57 | Team wants universal 30/60/90-day win-back cadence | Reject universal timing; use observed need/renewal/reorder cycle. |
| 58 | Team wants “best practice” save-rate benchmark | Treat external benchmark as context/heuristic, not target or proof. |
| 59 | Competitor uses cancellation discount | Do not copy visible tactic as proven performance. |
| 60 | Team asks for retention loop every day | `$retention-strategy` owns decision logic; `$marketing-operations` owns recurring loop/runtime/state. |

## Review criteria

A passing implementation should consistently preserve: defined continuation behavior, cohort/window, state-before-reason, voluntary versus involuntary separation, evidence provenance, cause-matched intervention, customer choice and consent, economics, downstream guardrails, causal uncertainty, domain-owner handoffs, authorization, and exact implementation/verification state.
