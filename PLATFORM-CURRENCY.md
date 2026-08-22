# Platform Currency Contract

Marketing platforms change faster than stable marketing principles. This contract keeps the Marketing OS current without pretending to know undocumented auction or recommendation-system internals.

## Evidence states

- **Officially documented:** supported by a current first-party Google or Meta source, with a verification date.
- **Account-visible:** directly observed in the relevant account or interface, with account scope and observation date.
- **Experimentally observed:** supported by a defined test or controlled comparison; state design and limitations.
- **Inferred:** a plausible explanation supported by evidence but not isolated or officially documented.
- **Unknown:** not verified, unavailable, or undisclosed.

Never describe a rumor, community report, correlation, or platform recommendation as an algorithm change. Separate product availability, default behavior, eligibility, recommended practice, and measured business impact.

## Freshness gates

| Change class | Examples | Maximum registry age | Required action when stale |
|---|---|---:|---|
| High-change | AI/automation features, campaign creation defaults, bidding or audience controls, reporting availability, experiments, interface labels | 30 days | Recheck official documentation before making a current-state claim or configuration recommendation. Confirm account visibility before an account-specific plan. |
| Medium-change | Setup workflows, policy wording, attribution options, standard reports | 90 days | Recheck first-party documentation when the detail affects the decision. |
| Stable concept | Economics, evidence states, causal inference, experiment design | 180 days | Review for conceptual or regulatory changes; do not replace with platform slogans. |

Always perform a live first-party check regardless of age when the user asks for the latest/current behavior, a documented capability may determine spend or measurement, the account contradicts the registry, or a live mutation is being proposed.

## Source rules

1. Prefer first-party product help, developer documentation, release notes, and account-visible evidence.
2. Record the source URL, page title, verification date, and the exact claim supported.
3. Treat marketing claims and platform case studies as vendor evidence, not guaranteed outcomes.
4. Do not infer access from documentation: rollouts can depend on account, country, objective, inventory, permissions, or experiment enrollment.
5. Preserve the stable strategic concept in `GLOSSARY.md`; map the current interface label separately.
6. When a material label, control, eligibility rule, or reporting capability changes, update the relevant platform registry, skill decision rules, evaluation case, and `CHANGELOG.md` together.

## Response contract

For a platform-current answer, report:

1. **Verified as of:** date and scope.
2. **Officially documented:** supported product behavior.
3. **Account-visible:** what was actually observed, or `not checked`.
4. **Business implication:** a recommendation, distinct from the platform claim.
5. **Unknowns:** undisclosed mechanics, rollout uncertainty, or missing account evidence.
6. **Status:** advice only, draft, saved, published, processing, or live-verified.

The OS can be current to its verification standard; it cannot guarantee knowledge of undisclosed algorithms or changes released after the latest verification.
