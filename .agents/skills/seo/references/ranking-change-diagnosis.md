# Ranking Change Diagnosis

Organic search has no experimental holdout in the way `$tracking-measurement` can design one for paid media — a page either ranks or does not, for everyone. Causal claims here rest on ruling out competing explanations, not on a controlled test, and should be graded accordingly on the causal evidence ladder (rarely above C2 for a single-site observation).

## Competing explanations to rule out, in order

1. **Algorithm update.** Check documented update timing against `PLATFORM-CURRENCY.md` and the change's date. A broad-core or targeted update affecting the page's category is the most common alternative explanation and must be checked first.
2. **Seasonality.** Compare against the same period in prior years, not only the immediately preceding period; organic search has strong annual patterns in many categories.
3. **Competitive entry or exit.** Check whether a competitor newly ranks or a previously ranking competitor dropped out, which can move position independent of anything the business did.
4. **Technical regression.** Check for an unrelated deploy, robots.txt change, redirect, or canonical change around the same date — including changes made by another team not aware of the SEO impact.
5. **Measurement change.** Check for a search-console property change, a tracking-code update, or a change in how a query is categorized before concluding traffic itself changed.
6. Only after the above are checked and ruled out or explicitly could not be ruled out: attribute the change, provisionally, to the specific content or technical action taken, and state the remaining uncertainty.

## Method

1. Restate the change precisely: which queries, pages, or page groups; ranking position, click-through rate, or traffic; absolute and relative magnitude; exact date range.
2. Check each competing explanation above against the same date range, in order, before considering the specific action a cause.
3. Where multiple concurrent changes exist (a content update and a technical deploy in the same week), state that isolation was not possible and do not select the more convenient explanation.
4. Report the surviving hypothesis with its evidence level, not as a confirmed cause, and state what evidence — typically a comparable, later, isolated change — would raise confidence.

## Rules

- Do not attribute a ranking change to a specific action without checking every competing explanation in order; a partial check is not a completed diagnosis.
- An algorithm update ruled in is not further explainable — do not speculate about the update's specific mechanism beyond what is officially documented; label anything beyond that as inference per `PLATFORM-CURRENCY.md`.
- Multiple concurrent changes with no way to isolate them is itself the correct finding; do not force a single-cause narrative onto ambiguous evidence.
- A single instance of a ranking change following an action is C1 at best (correlation, no control). Do not describe it in language that implies a higher evidence level.
