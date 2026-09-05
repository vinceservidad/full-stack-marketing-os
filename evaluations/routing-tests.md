# Routing Evaluations

Routing is the system's entry point. A request sent to the wrong owner invalidates
every downstream decision, however good that skill's own method is. These cases
test the boundaries that are genuinely contestable — not the obvious ones.

Owner under test: `$marketing-router`, applying [`CAPABILITY-REGISTRY.md`](../CAPABILITY-REGISTRY.md) and the stateful [`marketing-decision-lifecycle.md`](../workflows/marketing-decision-lifecycle.md).

Naming the right skill is not sufficient. A case passes only on the stated
decision behavior; a response that lands on the right owner for a reason the
criterion excludes does not pass. Lifecycle stage and specialist owner are
separate dimensions: identifying `strategy`, `review`, or `optimize` does not
transfer the underlying decision to `$marketing-router` or `$growth-strategy`.

## 1. Creative test plan for Meta

**Prompt:** “Create a testing plan for Facebook ads.”

**Pass:** `$creative-strategy` owns the concept, angle, and test matrix; `$meta-ads` supports with placement and delivery constraints only. Evidence for the angles is requested rather than assumed. The lifecycle is not expanded into unrelated stages merely because the request says “plan.”

**Fail:** `$meta-ads` owns the creative decision, a test matrix is produced with invented customer language, or the router forces a full context → goal → strategy sequence without a decision-relevant reason.

## 2. Search campaign audit

**Prompt:** “Audit my Search campaign performance.”

**Pass:** `$google-ads` owns the bounded campaign review. The requested lifecycle work is `review`; if conversion definitions or other evidence capable of reversing the audit are missing, the response may step back to `context`/`$marketing-intake` for that blocker before the audit conclusion. Conversion goals, their included conversion actions, and Primary/Secondary status are separated before any efficiency conclusion.

**Fail:** The audit proceeds on platform ROAS alone, `$marketing-reporting` is appointed owner of a single-channel audit, or the lifecycle label is used to bypass the missing-definition gate.

## 3. Product page not converting

**Prompt:** “Why is my Shopify product page not converting?”

**Pass:** `$cro` owns. Measurement integrity is flagged as an unresolved dependency rather than assumed sound, and findings stay hypotheses until tested.

**Fail:** A heuristic page critique is presented as the diagnosed cause.

## 4. SEO content strategy

**Prompt:** “Create an SEO content strategy.”

**Pass:** The lifecycle stage is `strategy`, but `$seo` still owns the bounded domain strategy. `$copywriting` is engaged only for the words once the strategy exists. `$growth-strategy` joins only if the real decision is integrated business-level priority across opportunities rather than SEO strategy itself.

**Fail:** `$copywriting` owns the strategy, `$creative-strategy` is routed to because the request mentions content, or every `strategy` stage is automatically assigned to `$growth-strategy`.

## 5. Paid ad hook versus long-form copy

**Prompt:** “Write me ad hooks for a cold Meta audience, and a nurture email sequence for the people who click.”

**Pass:** The request is split: `$creative-strategy` owns the paid-ad hooks, `$copywriting` owns the email copy, `$lifecycle-marketing` owns the sequence logic and cadence. One owner is appointed for the final response.

**Fail:** A single skill claims both, or the copy boundary between paid-ad hooks and lifecycle copy is not observed.

## 6. YouTube format selection

**Prompt:** “Should I use bumper ads or skippable in-stream for a new product launch?”

**Pass:** `$youtube-ads` owns format and view-through measurement fit; `$google-ads` supplies the shared account and bidding layer only.

**Fail:** `$google-ads` owns the format decision because YouTube runs through Google Ads.

## 7. Cross-channel executive report

**Prompt:** “Build me one report for the board covering Google, Meta, and email.”

**Pass:** `$marketing-reporting` owns combining findings the channel skills already produced. It does not perform the underlying audits itself, and it states which inputs do not yet exist.

**Fail:** `$marketing-reporting` re-derives channel analysis, or the report is assembled from platform exports without reconciliation state.

## 8. Platforms disagree on revenue

**Prompt:** “Meta says £80k, Google says £70k, Shopify says £100k. Where is the missing revenue?”

**Pass:** `$tracking-measurement` owns. Overlapping attribution is not summed, and definitions, windows, and timezones are aligned before any conclusion.

**Fail:** The platform figures are added, or a channel skill owns the reconciliation.

## 9. Spend rose and sales fell

**Prompt:** “I increased spend last week and revenue went down. What happened?”

**Pass:** The current lifecycle stage is `review`. `$performance-diagnostics` owns; the channel skill supports; competing explanations are tested rather than one cause asserted. `$cro` joins only if landing evidence points to a site issue. The router does not restart completed strategy/planning stages unless the evidence shows those assumptions are now invalid.

**Fail:** A single cause is asserted, the channel skill owns the cross-channel diagnosis, or the system restarts the entire lifecycle without a decision-changing reason.

## 10. Budget increase request

**Prompt:** “ROAS is 4.2, let's increase the budget 20% across the account.”

**Pass:** The requested lifecycle stage is `optimize`. `$optimization-scaling` owns and applies its readiness, economics, and constraint gates. The universal percentage is rejected, and no live change is executed before the evidence gates and applicable authorization scope are satisfied. If decision-grade economics/source-of-truth evidence are missing, the work steps back to `context` rather than pretending the optimize stage is ready. A proposed review or test is not a live mutation.

**Fail:** The increase is endorsed on platform ROAS, a fixed percentage step is treated as safe, or the lifecycle stage is treated as permission to execute.

## 11. Lifetime value question

**Prompt:** “Is this customer segment worth acquiring at a higher cost?”

**Pass:** `$retention-economics` owns the lifetime-value and payback model; `$optimization-scaling` consumes the result and applies its own proof standard before any spend decision.

**Fail:** A scaling decision is made directly from a lifetime-value estimate without the scaling gates.

## 12. Dashboard build request

**Prompt:** “Build me a Looker Studio dashboard wired to our warehouse.”

**Pass:** The capability gap is named explicitly. Dashboard implementation and warehouse design have no governed specialist, and no adjacent skill is substituted for them. A lifecycle label such as `execute` does not manufacture an execution capability that the registry does not contain.

**Fail:** `$marketing-reporting` or `$tracking-measurement` is appointed owner of dashboard implementation, or lifecycle orchestration is used to hide the unsupported capability.

## 13. Escalating complaints on organic social

**Prompt:** “We're getting a wave of angry comments about a delayed shipment on Instagram, and a journalist just DM'd us.”

**Pass:** `$organic-social` owns routine community management; `$public-relations` owns the response once it escalates to media contact. Legal-exposure review is flagged rather than performed.

**Fail:** One skill handles both without the escalation boundary, or a public statement with liability exposure is drafted as final.

## 14. Affiliate who is also a creator

**Prompt:** “One of our affiliates has 40k followers and posts about us. How should we structure this?”

**Pass:** `$affiliate-marketing` owns commission structure and attribution integrity; `$influencer-marketing`'s disclosure discipline applies in addition to affiliate-link disclosure.

**Fail:** Only one disclosure regime is applied, or the partner is treated as a pure media buy.

## 15. Audit request with no economics

**Prompt:** “Audit my account and tell me if it's profitable. I don't have COGS to hand.”

**Pass:** `$marketing-intake` owns until the evidence state is recorded. Efficiency analysis may proceed labeled as such; the profitability conclusion stays blocked rather than estimated.

**Fail:** A benchmark margin is substituted, or profitability is concluded from ROAS.

## 16. Boosting an organic post

**Prompt:** “This TikTok did well organically — put money behind it.”

**Pass:** `$organic-social` owns the content read; the paid decision routes to `$tiktok-ads`, including the Spark Ads versus in-feed choice.

**Fail:** `$organic-social` owns the paid buy, or the organic result is treated as proof the paid version will perform.

## 17. Integrated growth priorities

**Prompt:** “Our objective, economics, and constraint evidence are ready. Which growth opportunities should we prioritize?”

**Pass:** The current lifecycle stage is `strategy`: context and goal are already satisfied by the prompt. `$growth-strategy` owns integrated priorities, opportunity cost, capacity, and non-priorities. Specialist decisions stay with their owners; paid-media scaling still requires `$optimization-scaling` gates. The router does not repeat intake or redefine the goal without a new blocker.

**Fail:** A generic channel checklist replaces the strategic choice, growth strategy directly authorizes a budget increase, or the system forces already-satisfied context/goal stages to run again.