# Worked example: Shopify product page review

**Skill under test:** `$cro`
**Input:** [`fixtures/shopify-product-page.md`](fixtures/shopify-product-page.md)

Synthetic fixture. Nothing here is a performance claim about a real store, and no
figure below is a prediction of what a change would produce.

---

## Scope and primary business outcome

The primary business outcome is **qualified orders and the revenue behind them**, not
add-to-cart rate. Add-to-cart is a step metric used here for localization only —
improving it while checkout completion falls would be a loss.

**Read-only.** No page, theme, or app change has been made.

## Where the loss actually is

| Step | Rate | Sessions surviving (per 10,000) |
|---|---:|---:|
| Product page session | — | 10,000 |
| Add to cart | 4.1% | 410 |
| Cart → checkout | 62% | 254 |
| Checkout → order | 71% | 180 |

**97.7% of the total loss happens before the cart.** Cart and checkout together lose 56% of
those who reach the cart, which is worth attention later, but they operate on 4.1% of
traffic. The page itself is the constraint.

**The mobile/desktop split localizes it further:** 3.54% desktop against 1.31% mobile,
with mobile at 78% of sessions. Whatever is wrong is disproportionately wrong on the
device most people use.

## Findings

Each is a **hypothesis with the evidence behind it**, not a diagnosed cause. Heuristic
page review cannot establish causality — that is what the tests are for.

### F1 — The objection that decides the sale is answered 89% of the way down the page

34 of 214 reviews open with a variant of *"wasn't sure if it would irritate my
sensitive skin."* For 29 of them the worry resolved positively after purchase. That
is the dominant pre-purchase hesitation in the store's own customer language.

On the page, the only sensitivity signal is "Suitable for all skin types" inside a
38-word description, and the reviews carrying the real reassurance sit below a
"You may also like" block that **only 11% of sessions ever scroll to**.

**Evidence:** review theme counts (fixture), scroll depth 11%.
**Impact:** high — this is the largest documented objection meeting the lowest-visibility
part of the page.
**Confidence:** medium. Review authors are buyers; the people this objection actually
stopped never wrote a review. The evidence points at the objection, not at its size.

### F2 — Message scent breaks between the ad-side promise and a white-background bottle

Median time on page is 34 seconds. The first image is a white-background product shot
and the first text is a product title and price. Nothing above the fold states the
outcome the product delivers or who it is for.

**Impact:** high on mobile, where the fold is smallest and 78% of sessions land.
**Confidence:** low-medium. 34 seconds is consistent with a scent break, and equally
consistent with returning visitors who already know the product. **The fixture has no
new-versus-returning split for the page, so this cannot be separated.** Recorded as an
unknown, not resolved by assertion.

### F3 — Three accordions collapse the information that answers the remaining objections

"Ingredients" is opened by 19% of sessions. For a product whose main objection is
irritation, the ingredient list is decision information, not reference material.
"How to use" is collapsed too, while 9 reviews say they did not know it needed to be
kept out of sunlight — a post-purchase complaint that starts as a pre-purchase
uncertainty.

**Impact:** medium.
**Confidence:** medium.

### F4 — A real product problem is visible in the reviews and is not a page issue

22 reviews say the dropper dispenses too much. No page change fixes that. It is
recorded here so it reaches whoever owns packaging, and so nobody attempts to
A/B-test their way around it.

**Owner:** not `$cro`. Flagged and handed off.

### F5 — Quantity selector defaulting to 1 on a single-variant page

Minor. It occupies fold space on mobile and serves almost no one on a first purchase.
**Impact:** low. Listed because it is nearly free, not because it matters much.

## What is deliberately not concluded

- **No conversion-rate lift is estimated for any finding.** There is no test history and no session recordings in the fixture. A projected percentage here would be invented.
- **1.80% is not called "below benchmark."** No comparable benchmark was supplied, and a category average across different traffic mixes, price points, and brand strengths would not be evidence about this store.
- **Profitability of any change is not assessed.** COGS was not supplied.

## Prioritized tests

Ranked by expected business impact × confidence, and by reversibility.

| # | Hypothesis | Change | Primary metric | Stop rule |
|---|---|---|---|---|
| 1 | F1 — the sensitivity objection is suppressing add-to-cart | Move a sensitive-skin reassurance block, using verbatim review language, directly under the price. Do not paraphrase into a claim the reviews do not make. | Orders per session | No difference after 21 days or 400 orders per arm, whichever is later |
| 2 | F2 — above-the-fold scent break costs mobile sessions | Replace the first gallery image with one carrying the outcome and the audience; keep the white-background shot second | Mobile orders per session | Same as above; abandon if desktop degrades |
| 3 | F3 — collapsed accordions hide decision information | Expand "Ingredients" and "How to use" by default on mobile | Orders per session, accordion engagement as a secondary read | 21 days |
| 4 | F5 — quantity selector | Remove on first-purchase view | Orders per session | Ship-and-monitor; not worth an arm of its own |

**Run them sequentially, not concurrently.** Tests 1 and 2 both change what appears in
the first viewport; running them together makes neither result attributable.

**Sample-size reality check, before anyone starts:** at 24,310 sessions and 1.80%, the
page produces roughly 438 orders per month. A two-arm test detecting a 10% relative
change needs materially more than one month of traffic per arm. **Test 1 will take
longer than a month to read, and the stop rules above are written for the honest
duration rather than a convenient one.** Calling a winner early is the most likely way
this program produces a false result.

## Unknowns

| Unknown | Blocks |
|---|---|
| New versus returning split on the product page | Separating F2 from ordinary returning-visitor behavior |
| COGS | Whether any lift is worth its margin |
| Session recordings or heatmaps | Confirming where mobile attention actually stops |
| Traffic source mix | Whether the scent break is upstream in the ad, not on the page |
| Prior test history | Whether any of this has already been tried |

## What this example is for

The page has real problems, and a heuristic review could have produced a confident
list of them in a minute. What this output adds is the discipline around that list:
the loss is localized before it is explained, the largest finding comes from the
store's own customer language rather than a best-practice checklist, one finding is
handed to a different owner because no page change fixes it, and the test plan states
up front that it will take longer to read than the person asking probably wants.
