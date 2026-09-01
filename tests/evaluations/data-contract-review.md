# Data Contract Evaluation Review

**Reviewed:** 2026-09-01  
**Result:** Pass

## Coverage reviewed

The 50 data-contract cases cover:

- source/provenance, date range, timezone, currency, freshness, and field lineage
- stable grain/key behavior and prevention of duplicated money/outcomes through joins
- missing vs zero vs not-applicable vs not-reported/withheld states
- Google Ads campaign/query/product semantics
- Meta campaign/ad set/ad/creative/audience/placement semantics
- commerce order vs line-item revenue/refund/product joins
- web-analytics session/user/event denominators and attribution
- business economics, named profit levels, LTV maturity, and capacity
- platform attribution vs analytics attribution vs commerce/accounting revenue
- raw vs normalized data preservation
- privacy minimization, pseudonymous IDs, and secret rejection
- scoped data validity vs causal evidence
- current-platform terminology remaining under PLATFORM-CURRENCY governance
- the boundary that a valid dataset does not authorize live mutation

## Behavioral result

Pass. The contract system consistently requires the shared dataset envelope, preserves source-specific semantics, prevents silent cross-source addition/flattening, and treats validity as decision-scoped.

The review found no case where:

- a missing field was silently invented;
- a missing row was automatically converted to zero;
- platform attribution was upgraded to verified business revenue;
- a one-to-many join was allowed to duplicate spend/revenue/conversions/orders;
- predictive/modelled evidence was relabeled realized;
- unnecessary direct customer PII or credentials were accepted as normal input;
- a clean dataset was treated as proof of causality or authorization for a live change.

## Architecture check

The canonical layer is:

```text
raw source
→ DATA-CONTRACTS.md envelope
→ source/domain contract
→ field lineage + normalized dataset
→ validation/reconciliation
→ scoped specialist decision
```

`$marketing-intake` owns completeness/provenance and the Data Intake Manifest. `$tracking-measurement` owns measurement/reconciliation validity where required. `$google-ads`, `$meta-ads`, `$performance-diagnostics`, and other specialist owners consume the data within the validated scope.

## Follow-up

Future connector/MCP work should reuse these contracts rather than inventing tool-specific marketing semantics. Connector actions may provide live data/access, but they must not bypass provenance, approval, rollback, or verification rules.
