# Metric Definition Register

Metric names are not metric definitions. Two systems using the word "conversion" rarely count the same event. Define before comparing.

Use [`GLOSSARY.md`](../../../../GLOSSARY.md) as the canonical contract, and record client-specific variants here rather than redefining canonical terms.

## Define per metric

Name as used by the client; canonical glossary term; source system; exact event or record counted; counting rule (every versus one); value basis; inclusion and exclusion rules; attribution model and window; timezone; currency; known defects.

## Conversion architecture

**Google Ads.** Record each conversion goal, the conversion actions inside it, each action's Primary or Secondary status, which goal the campaign uses, counting setting, value setting, and attribution window. A Primary action influences bidding only when the campaign uses its containing goal. Reserve "Primary conversion action" for this setting; the main commercial result is the primary business outcome.

**Meta.** Record objective, conversion location, performance goal, dataset, optimization event, and attribution setting. Record whether reported conversions are modeled.

**Analytics and source of truth.** Record the equivalent definition in the analytics platform and in the business system, and whether the three agree.

## Cost and profit

Never record "profit" without its level and included costs.

| Field | Required detail |
|---|---|
| Revenue basis | Gross, net of discounts, net of refunds, with or without tax and shipping |
| Cost of goods sold | Included costs and whether landed |
| Variable costs | Fulfillment, payment fees, packaging, returns processing |
| Profit level | Gross, contribution after media, contribution after variable costs, operating |
| Discounts and refunds | Whether already deducted from the stated revenue basis |

Do not double-count a discount or refund already inside net revenue.

## Lifecycle and lead quality

For lead generation, define each stage — lead, marketing qualified, sales qualified, opportunity, customer — with its owning system, entry criteria, and typical lag. Keep funnel stage, awareness level, audience temperature, and lifecycle stage distinct. Record whether Customer Relationship Management outcomes are available and how they join to marketing source data.

## Comparability

Two metrics are comparable only when name, event, counting, value basis, attribution, window, timezone, and currency all match. Record any mismatch and either normalize it or declare the comparison invalid. Never resolve a mismatch by preferring the more favorable number.
