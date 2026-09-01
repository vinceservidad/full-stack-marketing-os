# Examples

This folder shows how Full-Stack Marketing OS is applied to realistic marketing decisions.

Examples are teaching artifacts. They demonstrate routing, evidence handling, diagnosis, prioritization, specialist handoffs, measurement, and final deliverables. They do **not** prove that the depicted strategy produced real-world results unless the example is explicitly labeled a verified public case study.

Read [`WORKED-EXAMPLE-STANDARD.md`](WORKED-EXAMPLE-STANDARD.md) before adding or materially changing a full walkthrough.

## Full worked examples

### Ecommerce growth diagnosis

[`ecommerce-growth/`](ecommerce-growth/)

Shows a multi-skill business diagnosis where spend increased while revenue flattened. The walkthrough preserves co-limiting constraints, separates channel and CRO ownership, names non-priorities, and delays scaling until economics/capacity are ready.

### Google Ads audit

[`google-ads-audit/`](google-ads-audit/)

Shows account, query, product, margin, attribution, and marginal-efficiency reasoning without blanket broad-match rules, one universal ROAS threshold, or automatic platform-recommendation acceptance.

### Meta Ads audit and creative testing

[`meta-ads/`](meta-ads/)

Shows how platform-attributed revenue, prospecting vs retargeting, CTR, landing-page quality, frequency, audience mix, creative IDs, and scaling readiness are separated instead of collapsed into one Meta ROAS verdict. It explicitly rejects undocumented “algorithm change” explanations and broad-vs-interest universal rules.

### DTC creative strategy

[`creative-strategy/`](creative-strategy/)

Shows synthetic customer evidence → JTBD → insight → angle → mechanic → concept → hook → visual direction → controlled test. Includes the governed 1080×1350 4:5 → centered 1080×1080 1:1 cross-crop production rule.

### Shopify CRO audit

[`shopify-cro/`](shopify-cro/)

Shows how stable add-to-cart behavior plus deteriorating mobile checkout completion leads to a focused checkout-friction investigation rather than a full-site redesign.

## What a full walkthrough contains

Each main walkthrough uses:

```text
README.md
input-evidence.md
decision-trace.md
final-output.md
```

- `README.md` explains the request, fictional/anonymized business, owner chain, and learning objective.
- `input-evidence.md` preserves what is observed, calculated, inferred, assumed, synthetic, or unknown.
- `decision-trace.md` is an auditable professional decision record. It is not private chain-of-thought.
- `final-output.md` shows the concise deliverable a user could actually receive.

## Example status labels

Every example must declare one of:

- **Synthetic worked example** — fictional business/data built to demonstrate the method.
- **Anonymized worked example** — real-work structure with identifying/confidential information removed.
- **Verified public case study** — real publishable evidence with appropriate permission where required.

Do not blur these categories.

## Compact / legacy examples

Some older files may remain as small demonstrations for areas not yet expanded into full walkthroughs, such as Custom GPT setup. These compact examples should not be mistaken for complete end-to-end case studies.

## Privacy and truth rules

Do not include:

- client-confidential information
- account access details or credentials
- personal data
- identifiable private customer data
- unverified performance claims
- invented testimonials presented as real
- fake live-state claims

Synthetic customer language must be labeled synthetic and must not be reused publicly as testimonial proof.

## Case-study boundary

**Worked example:** demonstrates how the system thinks and decides.

**Case study:** demonstrates what actually happened in reality.

A worked example can be synthetic. A case study requires evidence.
