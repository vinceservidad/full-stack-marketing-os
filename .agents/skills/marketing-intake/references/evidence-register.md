# Evidence Register

One row per decision-relevant claim. The register records what is known and how — never what is assumed to be true.

## Evidence states

Ordered weakest to strongest. A state is never upgraded without the named artifact that justifies it.

| State | Meaning | May support |
|---|---|---|
| `asserted` | A person stated it; no artifact seen | Hypotheses and questions only |
| `documented` | Appears in a supplied document or screenshot | Provisional analysis, labeled |
| `observed` | Seen directly in a named source system | Analysis and recommendations, labeled by source |
| `reconciled` | Agrees with the business source of truth | Profitability and commercial conclusions |
| `verified` | Reconciled and independently confirmed, or experimentally established | Causal claims within the tested scope |
| `unknown` | Required but not supplied | Nothing — blocks dependent decisions |
| `contradicted` | Two sources disagree and the conflict is unresolved | Nothing — must be resolved or declared |

## Row fields

Claim; value; source system or person; artifact or export name; collection method; date range covered; evidence state; decisions it supports; what would change the state; date recorded.

## Rules

- A platform export is `observed` for platform behavior and no stronger for business outcome. Reaching `reconciled` requires agreement with the source of truth.
- A stakeholder restating a platform number is `asserted`, not `observed`. The artifact, not the confidence of the speaker, sets the state.
- `contradicted` outranks convenience. Do not silently pick the more favorable source; record both and the resolution method.
- A claim used in two decisions at different confidence levels is one row, not two.
- Absence of evidence is `unknown`, never a default, benchmark, or industry figure.
- Record the collection method where it changes interpretation: modeled versus observed conversions, sampled versus complete data, survey self-report versus behavior.

## Decision blocking

For each pending decision, list the rows it depends on and the weakest state among them. The weakest dependency governs the decision's confidence. If that state is `unknown` or `contradicted`, the decision is blocked and must be reported as blocked rather than answered with a caveat.
