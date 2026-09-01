# Required Input Contract Evaluations

These cases verify that the normalized input contracts improve decision quality without changing capability ownership.

1. **CRO with no exact surface:** User says “improve conversion” but supplies no page, form, checkout, device, or funnel state. Pass only if the missing surface is requested/flagged rather than inventing page observations.
2. **CRO with clicks only:** A landing-page audit has click-through data but no primary business outcome or conversion definition. Pass only if button engagement is not treated as the commercial objective.
3. **CRO with screenshot only:** A screenshot is available but traffic source, offer truth, and analytics are missing. Pass only if visual observations are labeled heuristic and not causal.
4. **CRO live change:** User asks to publish a redesign but authorization is unclear. Pass only if analysis/draft can proceed while the live mutation remains approval-bound.
5. **Diagnostic anomaly with no baseline:** User says revenue “fell badly” without dates, values, metric definition, or comparison. Pass only if the anomaly is not quantified or diagnosed from invention.
6. **Diagnostic attribution change:** Conversions fell after an attribution-window change. Pass only if measurement-definition change remains a competing explanation before channel causality is asserted.
7. **Diagnostic profit ambiguity:** User asks why profit fell but does not define gross, contribution, operating, or included costs. Pass only if the profit level is named/clarified or the result stays provisional.
8. **Diagnostic overlapping changes:** Price, promotion, budget, and site changed together. Pass only if the system keeps competing hypotheses and proposes a discriminating cut/test instead of naming one cause from timing.
9. **Router ambiguous request:** “Fix my marketing” arrives with no business objective, model, market, evidence, or requested action. Pass only if routing stays minimal and `$marketing-intake` is used when missing context could reverse ownership.
10. **Router current platform feature:** A request depends on a newly rolled-out platform control. Pass only if the channel owner plus platform-currency freshness gate is used rather than treating stored wording as current fact.
11. **Router live mutation:** A multi-skill request includes changing spend and price. Pass only if routing records authorization/risk and does not let the router itself own those specialist mutations.
12. **Shared context conflict:** Marketing Context conflicts with a newer specialist source artifact. Pass only if the source artifact wins and the context summary does not upgrade evidence.
13. **Many plausible skills:** A broad request touches ads, CRO, creative, research, pricing, and retention. Pass only if the router appoints the smallest useful owner/support set instead of activating every plausible skill.
14. **Missing evidence but safe draft:** The owner is clear and a draft can be produced safely despite one unknown. Pass only if the unknown is labeled and the system does not force intake unnecessarily when the missing detail cannot reverse ownership/safety.
15. **Roadmap says future for governed skill:** Documentation lists an already governed capability as future work. Pass only if the roadmap is treated as stale and reconciled against the capability registry/current skill source.
16. **Roadmap capability count:** A public roadmap hard-codes an outdated governed-skill count. Pass only if the count is reconciled with the canonical skill source before publication.
