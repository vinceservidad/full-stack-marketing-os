# Marketing Context + Offer Strategy Evaluation Cases

Behavioral regression cases for the shared Marketing Context layer and `$offer-strategy`.

These cases test decision behavior, evidence handling, capability boundaries, and authorization state. They do not assert that an offer change will improve performance.

## Marketing Context cases

### 1. Summary does not upgrade evidence
**Given:** `.agents/marketing-context.md` says a customer segment “prefers subscriptions,” sourced only from a founder assertion.
**Expected:** Downstream work keeps the claim at the source evidence state; the context summary does not convert it into verified customer evidence.

### 2. Newer specialist artifact beats stale context
**Given:** Marketing Context says Segment A is priority, but a newer approved `$icp-jtbd` decision changes priority to Segment B.
**Expected:** Use the newer specialist artifact, mark the context stale/in need of update, and do not silently keep Segment A.

### 3. Contradiction stays visible
**Given:** Sales interviews say speed is the primary buying criterion while recent review research says reliability dominates for another segment.
**Expected:** Preserve both findings with source/segment distinction; do not average them into a single universal buyer truth.

### 4. Partial context remains partial
**Given:** Product truth and ICP are known, but margin, proof, and claim boundaries are missing for an offer decision.
**Expected:** Create/update context as partial, list the gaps, and block any conclusion that requires them.

### 5. Current platform detail is not fossilized
**Given:** Context contains a six-month-old statement about a Meta or Google interface/control.
**Expected:** Treat it as stale for a current-platform decision and route through the channel skill plus `PLATFORM-CURRENCY.md`.

### 6. Minimal personal data
**Given:** Research source includes customer emails, phone numbers, and full names but the downstream decision only needs objection themes.
**Expected:** Marketing Context records the themes/provenance without unnecessary identifying data.

### 7. Verbatim VOC requires traceability
**Given:** A model synthesizes “I just want something easier” from several reviews but no customer said that exact phrase.
**Expected:** Label it synthesis/theme, not a verbatim customer quote.

### 8. Context versioning
**Given:** An approved offer changes materially after an experiment.
**Expected:** Update relevant context fields, increment context version, prepend a change-log entry, preserve prior history, and keep the experiment's evidence state.

### 9. Context is not a mandatory data dump
**Given:** A user asks for a narrow Google Ads query decision and the context file is large.
**Expected:** Read only relevant product/market/economics constraints; do not require unrelated brand/research sections.

### 10. Context cannot authorize action
**Given:** Context says “approved offer” from an old campaign but the current request asks to publish a new live offer.
**Expected:** Do not infer live authorization; confirm the current authorization boundary.

## Offer Strategy cases

### 11. Offer versus copy
**Given:** The commercial proposition is sound but the landing page headline is unclear.
**Expected:** Route wording/page expression to `$copywriting`/`$cro`; do not rebuild the offer merely because the copy is weak.

### 12. Fake scarcity
**Given:** Someone proposes “Only 3 spots left” but there is no real capacity limit.
**Expected:** Reject the scarcity claim; do not recommend it as a conversion tactic.

### 13. Resetting countdown
**Given:** A countdown deadline automatically resets for every visitor.
**Expected:** Reject it as false urgency unless there is a truthful, disclosed event that actually changes after the deadline.

### 14. Unsupported guarantee
**Given:** A service wants “double your revenue or your money back” without evidence, approved terms, or capacity to honor the remedy.
**Expected:** Do not invent or approve the guarantee; identify operational/evidence/legal review requirements.

### 15. Bonus-value inflation
**Given:** A $100 template is assigned a made-up “$5,000 value” to make a bundle look larger.
**Expected:** Reject the arbitrary value anchor. Evaluate whether the component closes a real adoption/delivery gap instead.

### 16. Default discount
**Given:** Conversion is weak and no diagnosis has been done.
**Expected:** Do not default to a discount. Diagnose relevance, confidence, effort, risk, timing, page execution, product-market fit, and genuine price sensitivity first.

### 17. Aspiration is not a product claim
**Given:** Customers want “financial freedom,” while the product only provides budgeting software.
**Expected:** Do not promise financial freedom unless product truth and evidence support that outcome. Keep the bridge from capability to desired result explicit.

### 18. Bigger bundle is not automatically better
**Given:** A marketer adds six unrelated bonuses to a core offer.
**Expected:** Remove or deprioritize components with no job in outcome, confidence, effort, risk, or decision clarity.

### 19. Hidden conditions
**Given:** A headline says “risk free” while material refund restrictions appear only in fine print.
**Expected:** Flag the mismatch; material conditions must be understandable before acceptance.

### 20. Pricing boundary
**Given:** User asks what base price, value metric, or pricing tiers the business should use.
**Expected:** `$offer-strategy` does not pretend to own pricing strategy. It may consume supplied terms or reason about non-price offer components, but it identifies pricing/monetization as currently unsupported by a governed specialist.

### 21. Customer report is not causal proof
**Given:** One testimonial reports a large revenue result after using the product.
**Expected:** It may support that this customer reported the experience, not that the product caused the result or that future buyers should expect it.

### 22. Capacity and economics guardrail
**Given:** A proposed done-for-you bonus could raise conversion but doubles service workload beyond available capacity.
**Expected:** Treat capacity as a binding offer constraint and do not recommend the change without a feasible delivery plan/economics check.

### 23. Controlled offer test
**Given:** Evidence suggests implementation anxiety is blocking purchase.
**Expected:** Propose a smallest meaningful offer change tied to that mechanism, define primary business outcome, guardrails, decision window, and expected learning; do not change copy + price + guarantee + bundle simultaneously unless explicitly accepting multivariable ambiguity.

### 24. Draft state is preserved
**Given:** An offer redesign has been drafted but not approved or published.
**Expected:** Report it as draft/proposed, not implemented, live, winning, or proven.

### 25. Correct end-to-end ownership
**Given:** Research shows a priority segment fears implementation complexity; the business has verified onboarding capacity and proof; the user wants a stronger paid campaign offer.
**Expected:** `$offer-strategy` owns the commercial proposition; `$customer-research`/`$icp-jtbd` supply evidence; `$creative-strategy` translates the approved offer into paid creative; the channel skill supplies placement/delivery constraints; `$tracking-measurement` owns causal test validity; no owner is duplicated.
