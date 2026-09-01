# Data Intake Manifest

Use this template when structured platform, analytics, commerce, or business-economics data is supplied to Marketing OS.

**Owner:** `$marketing-intake`  
**Measurement validity partner:** `$tracking-measurement`  
**Contract:** [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md)

## Decision scope

- Business objective:
- Decision to support:
- Primary owning skill after intake:
- Supporting skills:
- Required evidence level:
- Authorization boundary:

## Dataset register

Repeat this block for each delivered dataset.

### Dataset

- `dataset_id`:
- `contract_id`:
- `contract_version`:
- source system:
- source scope/account/property/store:
- source method: export / API / connector / query / report / manual file / other
- source generated at:
- represented period:
- timezone:
- currency:
- grain:
- primary key:
- row semantics:
- attribution basis:
- conversion/event definition:
- revenue basis:
- profit basis:
- freshness state:
- normalization state: received / profiled / mapped / validated-for-scope / degraded / rejected
- privacy/access restrictions:
- known limitations:

## Field lineage

| Normalized field | Source field(s) | Calculation / mapping | Notes |
|---|---|---|---|
|  |  |  |  |

## Quality checks

- [ ] source and scope identified
- [ ] dates and timezone identified
- [ ] currency identified for monetary fields
- [ ] grain and row semantics identified
- [ ] primary key tested or limitation recorded
- [ ] duplicates/missingness profiled
- [ ] conversion/event definitions recorded
- [ ] attribution basis recorded where applicable
- [ ] revenue/profit basis named
- [ ] derived metrics reproducible from base fields where practical
- [ ] within-source totals reconciled or gap explained
- [ ] cross-source differences preserved rather than force-matched
- [ ] mixed currencies handled explicitly
- [ ] partial/immature periods flagged
- [ ] direct customer PII removed when not required
- [ ] credentials/secrets absent

## Cross-source reconciliation

| Source / dataset | Metric | Basis | Period | Value | Reconciliation note |
|---|---|---|---|---:|---|
|  |  |  |  |  |  |

## Validity for the named decision

- Dataset validity state:
- What this evidence can support:
- What this evidence cannot support:
- Missing input that could reverse the decision:
- Required correction/additional extract, if any:

## Handoff

- Next owning skill:
- Decision-ready datasets:
- Degraded/rejected datasets:
- Open measurement questions:
- Exact status: intake recorded / mapping in progress / validated-for-scope / blocked
