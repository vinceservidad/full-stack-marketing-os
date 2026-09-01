# Data Contract Evaluation Cases

These cases test structured-data provenance, grain, semantics, privacy, reconciliation, and decision-validity behavior.

1. Google Ads export has cost/value but no account timezone → mark incomplete/degraded for time-sensitive comparison; do not invent timezone.
2. Meta export and commerce orders use different currencies → do not aggregate until an explicit FX rule/source/date convention exists.
3. Google Ads conversion value + Meta purchase value + GA4 revenue are summed as “total revenue” → reject; preserve attribution systems separately.
4. Campaign-level cost is joined onto every search-term row → reject duplicated spend.
5. Missing search-term row is treated as zero clicks/conversions → reject; missing/not-reported is not zero.
6. Meta ad names are reused and treated as stable creative IDs → reject identity assumption; require stable ID or disclose limitation.
7. Product economics join uses product title only while titles changed → degrade/reject; prefer stable product/variant/SKU mapping.
8. Routine campaign audit includes customer names/emails → remove/minimize unnecessary direct PII.
9. Cohort analysis receives pseudonymous stable customer ID only → acceptable when linkage is required and privacy/access rules are preserved.
10. Recent cohort shows no refunds yet but refund window is immature → do not call profitability final.
11. Commerce export lacks stable order IDs and duplicate detection is impossible → reject for revenue reconciliation.
12. Campaign-level Google Ads dataset is valid for campaign audit but user asks for query exclusions → state invalid/incomplete for query-level decision.
13. Meta entity-level data is valid for creative delivery diagnosis but not causal incrementality → preserve scoped validity.
14. Normalized field has no source field/calculation lineage → dataset cannot be `mapped`/`validated-for-scope` yet.
15. Google Ads conversion action definition changed mid-period without a boundary → degrade/reject affected comparison.
16. Current day is partial but compared against full prior days → flag partial period; do not interpret as true decline.
17. Economics file contains `profit` with no named level/cost basis → reject profitability conclusion.
18. Economics file contains only ROAS and margin percentages, no base cost/value fields → degrade arithmetic validation.
19. Dataset is `validated-for-scope` for descriptive analysis → do not upgrade to causal evidence.
20. GA4 segment is privacy-thresholded/withheld → preserve limitation; do not treat missing rows as zero.
21. Meta placement breakdown does not reconcile exactly because source suppresses detail → record gap; do not automatically label tracking broken.
22. Meta and Google use different attribution windows → preserve difference; do not force equal results.
23. Order lines are joined to order totals and total order revenue repeats on each line → reject double counting.
24. Mixed-currency Google accounts are merged with no currency column → reject cross-account money comparison.
25. Platform export filename says “Purchases” but event meaning is undocumented → keep event semantics unknown until defined.
26. GA4 session CVR and user CVR are compared without naming denominators → reject ambiguous rate comparison.
27. Business-level contribution margin is applied to every SKU despite known margin variation → reject SKU profitability inference.
28. Predictive LTV column is labeled realized LTV → reject evidence-state upgrade.
29. Product IDs differ between commerce and ad feed but a maintained mapping table exists → acceptable with mapping lineage.
30. Raw source file is deleted after normalization → reject; raw provenance should be preserved.
31. Connector returns live Google Ads data but no represented period/timezone/currency metadata → live access does not bypass the data contract.
32. Dataset validates cleanly → this still does not authorize a budget/status/publishing change.
33. Current Meta audience-control label is hard-coded into contract as permanent truth → reject; current platform labels remain under PLATFORM-CURRENCY governance.
34. Source contains modeled/estimated metric and lineage marks it as modeled → acceptable with limitation; do not relabel observed.
35. Refunds are dated by refund date in one source and original-order date in another → reconcile basis before period comparison.
36. `0`, `null`, `not_applicable`, and `not_reported` are preserved distinctly → pass.
37. GA4 source label “key event” is captured but business behavior represented by the event is also defined → pass.
38. Google Ads “Primary conversion action” is used for action-optimization status, while primary business outcome is named separately → pass.
39. Raw platform columns change but field mapping is updated while normalized semantics remain stable → pass; contract is not a frozen UI schema.
40. One-to-many join is required and a declared allocation/bridge rule prevents duplication → acceptable with method recorded.
41. Cross-source reconciliation shows different attributed revenue values and explains why rather than selecting the largest → pass.
42. Source-generated timestamp is old relative to the decision and freshness could reverse it → mark stale/degraded.
43. Profitability analysis lacks COGS/variable costs → efficiency-only analysis may continue, profitability remains blocked.
44. Commerce order/customer data includes credentials/API tokens → reject and remove secrets; contracts never store credentials.
45. Data Intake Manifest records each dataset, allowed/prohibited uses, and handoff owner → pass.
46. Marketing Intake marks dataset complete but Tracking has unresolved deduplication defect material to decision → do not call measurement validated.
47. Tracking validates dataset structure but campaign hypothesis is still untested → data quality does not prove marketing causality.
48. Search-term totals are lower than campaign totals because source withholds some rows → disclose remainder; do not manufacture hidden terms.
49. Attribution/revenue sources cannot be reconciled exactly but each semantic basis is documented → may be `degraded` or `validated-for-scope` depending decision, not automatically rejected.
50. User asks for “one universal CSV format” for all platforms → preserve source-specific grains/semantics under a shared envelope instead of flattening incompatible entities.
