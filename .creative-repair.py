# Temporary, branch-scoped implementation; removed after verified commit.
import hashlib
from pathlib import Path
EXPECTED_BEFORE={'.agents/skills/copywriting/SKILL.md': '2af7d0bf356c11387c9296012a9dabcdeb226df8452c2a3db4594805cd09322a', '.agents/skills/creative-strategy/SKILL.md': 'a381c6c7b3b88b46927d3bcd3e84d793fc80984844885571a45eaa218d3537f7', '.agents/skills/creative-strategy/references/sales-argument-and-finished-review.md': None, '.agents/skills/creative-strategy/references/static-dtc-creative-direction.md': '3776d9c8f4e9a69bdd24522db068d43a94e13aeb3a1a6200ec386255cf78375a', '.agents/skills/cro/SKILL.md': '2d8132ffd0b3b3308b615a42b1860be8470b1e56c5b848ab1c41756817eff53b', 'AGENTS.md': 'f65699e2e5df481aaa04a9700118c0715bacd8c25f7600d2596a43c19a0e358a', 'CHANGELOG.md': 'dfeab303b0d453f37ceb8a2cf2f836fdb4366c73bc5b6771eee3da6647d87cb9', 'tests/evaluations/creative-sales-argument-cases.md': None, 'tests/evaluations/creative-sales-argument-review.md': None, 'tests/evaluations/suites.json': 'edf40f14782b6cbf92d2bb1fd525702d19604763ef4e04f2e06dd48a82bda05c', 'tests/test_eval.py': '051b5bbe65b884df048905087a29af164bf14ca7d7da5945a02aabbeca1088f6'}
for relative, expected in EXPECTED_BEFORE.items():
    target = Path.cwd()/relative
    if expected is None:
        if target.exists():
            raise SystemExit(f"Refusing to overwrite unexpected file: {relative}")
    elif not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
        raise SystemExit(f"Source changed since inspection: {relative}")

from pathlib import Path
import json

root=Path.cwd()
def put(path, text):
    dest=root/path
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(text.strip()+'\n', encoding='utf-8')

put('.agents/skills/creative-strategy/SKILL.md', '''
---
name: creative-strategy
description: Develop or repair paid-ad sales arguments, concepts, copy, and visual briefs from customer and product evidence.
---

# Creative Strategy

Own paid-ad angles, concepts, hooks, copy, and visual direction. Current placement, delivery, and policy assessment belongs to the channel owner; landing-page conversion copy belongs to `$cro`. Use [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md) to distinguish a strategy, framework, hypothesis, and execution. A framework does not prove effectiveness.

## Inputs

Use the requested deliverable, business outcome, buyer situation, customer research, product and offer truth, proof, objections, brand constraints, destination, and relevant prior results. For production, use supplied assets and required placements/crops. Reuse decision-relevant context; ask only for missing information that changes the decision. Without customer evidence, label buyer motives and belief states as hypotheses. Reviews used as research require the `$customer-research` handoff, not cherry-picked quotations.

## Method

Establish the sales argument before committing to a headline or layout: who should care, what they want, why this product or offer is relevant, and what makes the argument credible. Use [Sales argument and finished-creative review](references/sales-argument-and-finished-review.md) when producing or repairing creative. Human motivation and product truth drive the idea; platform theories do not supply a reason to buy.

Choose a concept that makes the argument understandable through copy and imagery together. A demonstration, story, comparison, direct offer, or other mechanic must earn its place in this brief. Select a copy structure when useful, not a mandatory AIDA/PAS recipe or psychological-principle quota. A payment option may answer a supported purchase barrier; do not assume it creates product demand.

Deliver the requested work. One ad prompt needs exact customer-facing copy and a usable visual direction, not an exhaustive strategy matrix. Batch ideation and testing need meaningful differences and a learning plan. A repair needs the revised deliverable, not only advice to rewrite it. Explain material safety, evidence, access, or production limits rather than silently substituting a different task.

## Rules

- Keep entities distinct: angle = strategic reason to care; mechanic = how the idea communicates; concept = specific idea; hook = opening; format = vessel; asset = produced component; ad = configured entity; adaptation = crop or placement version.
- Claims, quotations, comparisons, testimonials, credentials, scarcity, and product details need traceable support. Buyer desire or ingredient presence does not establish a product outcome. Preserve evidence gaps and safety requirements.
- Keep internal strategy notes and evidence labels separate from exact customer-facing copy. Preserve required public disclosures, product identity, and approved wording. Do not replace strong supplied copy merely to fit a framework.
- Do not call cosmetic variants distinct angles or claim a format, hook, or psychological principle inherently performs well. Preserve null and contradictory learning.
- Judge tests using business outcomes, conversion quality, spend, guardrails, and adequate evidence. Low delivery alone does not establish creative failure. Whole-concept tests do not identify the effect of one changed element.
- A generated render is a draft, not an approved, published, live, or verified ad. Do not claim inspection, deployment, or improved performance that did not occur.

## Output

Provide the requested draft, revision, concept set, or production prompt first, followed by the decision-relevant rationale and evidence gaps. Keep internal analysis outside customer-facing copy.

For production: exact copy; the buyer argument; visual concept and product role; hierarchy and typography; proof treatment; destination/CTA; required canvas/crops; constraints; status. For a test: hypothesis, control/comparison, changed dimensions, business outcome, guardrails, review window, and next decision. Do not invent budget, sample size, results, or certainty.

## References

Load only the references needed for this task:

- Buyer interpretation: [awareness, belief, and desire](references/awareness-belief-desire-map.md); [persuasion lenses](references/persuasion-and-behavioral-principles.md). Verify research support before presenting a behavioral claim as established.
- Angle development: [strategic framing](references/strategic-framing-and-angle-archetypes.md); [angle and hook catalog](references/angle-catalog-and-hook-types.md).
- Concept development: [ideation expansion](references/ideation-expansion-method.md); [creative mechanics](references/creative-mechanics.md); [hook execution](references/hook-execution.md); [format selection](references/visual-format-selection.md).
- Static production or supplied-image repair: [static DTC direction](references/static-dtc-creative-direction.md), including product accuracy, reference distinction, typography, and actual crop inspection. A centered square core applies only when square survival is required; it is not a universal platform safe zone.
- Broader planning: [creative strategy](../../../frameworks/creative-strategy.md); [ideation workflow](../../../workflows/creative-ideation-engine.md); [idea matrix](../../../templates/creative-idea-matrix.md); [creative brief](../../../templates/creative-brief.md).
- Testing and next actions: [creative testing](../../../workflows/creative-testing.md); [iterating from a winner](references/iterating-from-a-winner.md).

## QA

Review the actual deliverable against its sales argument and requested purpose. Does the buyer have a credible reason to care and choose? Do the copy and image express the same idea without unsupported implications? Remove repetition, production-note leakage, and generic language. Inspect rendered work and required derivatives when available, fix identified defects within scope, and state any inspection not performed. Route current platform requirements correctly and retain approval boundaries. A checked draft is not proof of sales performance.
''')

put('.agents/skills/copywriting/SKILL.md', '''
---
name: copywriting
description: Write or revise email, lifecycle, website, sales-page, and brand copy; paid ads and conversion pages have separate owners.
---

# Copywriting

Own email/lifecycle text, website and sales-page copy, long-form copy, and brand voice under [`CAPABILITY-REGISTRY.md`](../../../CAPABILITY-REGISTRY.md). `$creative-strategy` owns paid-ad copy and visual hierarchy; `$cro` owns landing/product-page conversion copy. Coordinate internally with the correct owner and return one coherent deliverable, not a routing explanation in place of the work.

## Context

Use the requested output, business outcome, buyer situation, source-backed customer language, product/offer truth, proof, objections, brand voice, channel constraints, and approved existing wording. Reuse the research and sales argument already established by the owning specialist. Mark gaps without inventing customer evidence or demanding a full intake for a bounded edit.

## Method

Determine what the reader should understand, believe, and do, and why the offer deserves consideration. For sales copy, use the shared [sales-argument and finished-work review](../creative-strategy/references/sales-argument-and-finished-review.md) rather than starting from a template. Functional and emotional motives are research inputs or labeled hypotheses, not universal buyer facts.

Select a structure that fits the message and available proof using [Structure selection](references/structure-selection.md). AIDA, PAS, FAB, and BAB organize an argument; they do not supply its truth or guarantee a result. Apply [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md) accurately. Keep one clear communication purpose without forcing every piece into a problem-agitation narrative.

Write the requested copy, then inspect the actual draft. Check the reason to care, relevance, differentiation, credibility, and next action. Use natural, specific language, normally Grade 6-8 unless the audience requires otherwise. Remove unnecessary repetition and mechanical phrasing without stripping meaning, approved positioning, or useful high-intent search terms. For a revision, preserve what works and change only what the brief or evidence warrants.

For sequences, `$lifecycle-marketing` owns segmentation, triggers, cadence, and suppression. Write the individual messages and cumulative argument against that handoff; do not invent a sequence strategy or change a live send.

## Rules

- Never invent results, customer quotations, credentials, scarcity, or product advantages. Keep factual substantiation and source notes outside customer-facing copy unless disclosure is required.
- A payment method, discount, ingredient, or feature is not automatically the main sales argument. Choose its role from the buyer situation and evidence.
- Preserve claim limits, privacy, required disclosures, and safety. Do not manufacture insecurity or false urgency. Explain a material limitation instead of silently substituting an information card for requested sales copy.
- Use `$customer-research` for source-backed customer language. Model-written phrasing is copy or synthesis, not a testimonial or observed customer statement.
- Keep brand voice unverified when guidelines are unavailable. Do not claim a draft was approved, published, tested, or effective without evidence.
- Do not replace the specialist owners for paid-ad or conversion-page decisions. Carry the same supported sales argument across handoffs.

## Output

Return usable copy or the actual revision first. Separate exact customer-facing text from a short rationale, supporting sources, unresolved claims, and status. When asked for a framework, identify the structure and show how the words implement it; a framework label alone is not completion. Match output length to the task rather than displaying every internal analysis field.

## QA

Check purpose, buyer relevance, supported promise, proof, natural wording, preserved approved language, and the appropriate next step. For copy with a visual or page layout, review their combined meaning with the owning specialist. Fix identified issues before concluding. Report any rendering or behavioral evaluation not performed; review is not proof of conversion lift.
''')

put('.agents/skills/creative-strategy/references/sales-argument-and-finished-review.md', '''
---
title: Sales Argument and Finished-Creative Review
owner: creative-strategy
type: methodology/process
status: active
---

# Sales Argument and Finished-Creative Review

A shared practitioner workflow for `$creative-strategy`, `$copywriting`, and `$cro`. Use it to connect buyer understanding to finished sales copy and design, or to repair a weak execution. It is not a validated psychological model, a compulsory sequence, or evidence of performance. Keep established specialist ownership.

## Establish the argument

Start from the decision the buyer faces, not from the format or an algorithm theory. Use the relevant [awareness, belief, and desire map](awareness-belief-desire-map.md) to understand the situation, desired progress, present belief, alternatives, objection, and available proof. Functional, emotional, and social motives can inform hypotheses; they must not be invented and labeled customer research.

Decide what supported product or offer advantage connects to that situation. Explain why it matters, what makes it credible, and why the buyer might choose it over a relevant alternative or doing nothing. A credible reason to choose need not be an exclusive feature; do not fabricate uniqueness in a commodity or reseller market.

Keep desire creation, product explanation, differentiation, proof, and transaction reassurance distinct. A payment option or delivery term can lead when the brief and evidence make that barrier central. Otherwise it may support the close. Conversely, an explicit product-information request should remain informational. Do not force persuasion where it was not requested.

When research is limited, give a usable, clearly labeled hypothesis based on verified product truth. State the missing evidence that could change it. Do not invent an outcome, inflate an ingredient into a benefit, or treat a customer's wish as substantiation. If the requested persuasive angle cannot be supported safely, explain the limit and label any alternative accurately.

## Choose the expression

Select a concept and persuasive structure because they serve this argument. Use [structure selection](../../copywriting/references/structure-selection.md) when helpful; a hook is not a framework, and AIDA or PAS does not replace a sales argument. Do not force every piece to include every stage, invoke multiple psychological principles, or use the same opening.

Make the visual carry evidence or meaning, not merely decorate the headline. A demonstration should show the supported feature; a process claim should show the real process; a comparison needs a fair basis. Choose hierarchy around the important buyer message, not automatically the product name, pack count, payment method, or largest available number. Required qualifications must remain readable.

Preserve strong approved copy, authentic customer phrasing, and relevant high-intent terms during revision. Do not replace a specific argument with a generic service description for stylistic consistency. Buyer language can guide relevance without implying that particular words unlock an advertising algorithm.

## Separate the deliverable from the brief

Put only intended customer-facing words in an exact-copy block. Put rationale, source notes, evidence labels, framework mapping, and production directions elsewhere. Do not print headings such as 'emotional job' or 'featured front-label ingredients' merely because they appear in the working brief. This is a purpose distinction, not a banned-phrase list: preserve real informational headings when requested and legally required disclosures when applicable.

An image prompt should connect the exact copy to a concrete visual idea, product asset, composition, and required output. The [static direction reference](static-dtc-creative-direction.md) supplies conditional production and crop details. Do not demand every reference, a full campaign matrix, or unnecessary derivative formats for a single bounded creative.

## Finish and review

Review the words and visual as the buyer will encounter them. Check the reason to care, reason to believe, reason to choose, clarity of action, and any unsupported implication. Remove redundant copy and confusing visual emphasis. This is a review aid, not a promise that these checks predict response.

For a repair, change the actual supplied artifact or return the requested revised copy/prompt. Do not stop at an apology or instructions for the user to do the same work. Use available tools within authorization. Never invent an unavailable asset or claim the rendered output was inspected when only the prompt was reviewed.

Inspect actual rendered work and required crops when available; correct identified defects before marking the scoped work complete. Keep drafted, produced, inspected, approved, published, and tested states separate. Name what remains unverified and propose the next business-outcome test without fabricated budgets, thresholds, conversion forecasts, or algorithm guarantees.
''')

p=root/'.agents/skills/cro/SKILL.md'
s=p.read_text()
s=s.replace('2. Map message scent from ad or query through page and conversion boundary.', '2. Map message scent from ad or query through page and conversion boundary. For copy or visual revisions, carry forward the supported [sales argument](../creative-strategy/references/sales-argument-and-finished-review.md); preserve strong approved wording and relevant high-intent terms rather than replacing them with generic copy.')
p.write_text(s)

p=root/'.agents/skills/creative-strategy/references/static-dtc-creative-direction.md'
s=p.read_text()
s=s.replace('## Required inputs\n', 'For sales-argument selection and finished-work review, use [Sales argument and finished-creative review](sales-argument-and-finished-review.md). Keep strategy notes separate from exact overlay copy. If the request is to repair an asset, inspect and revise that asset rather than treating a new prompt as an already-corrected render.\n\n## Required inputs\n')
s=s.replace('State the intended felt shift in the first second:', 'State the intended response:')
s=s.replace('Tie it to the actual audience situation and product truth; do not label a generic mood as an insight.', 'Tie it to the actual audience situation and product truth; do not label a generic mood as an insight or claim a measured one-second response without testing.')
s=s.replace('Specify the single contrast that carries the angle:', 'Specify the visual idea that carries the angle. A contrast may help, for example:')
s=s.replace('The visual thesis must support—not merely decorate—the message.', 'The visual thesis must support the message; contrast is an option, not a requirement for every ad.')
s=s.replace('For image-model workflows, generate the visual base separately from the text overlay where legibility or exact copy matters; image models are unreliable at rendering exact typography.', 'For image-model workflows, inspect the actual typography and packaging. Use a separate text overlay or original-asset composite when the available model cannot preserve them accurately; do not assume either failure or accuracy before inspection.')
s=s.replace('Validate one-second comprehension, hook legibility,', 'Review immediate message clarity without claiming measured comprehension speed, hook legibility,')
p.write_text(s)

p=root/'AGENTS.md'
s=p.read_text()
old='''- Keep `SKILL.md` concise and decision-changing.
- Put conditional detail in linked references.
- Give every skill discriminating triggers, required inputs, decision rules, QA, and output shape.
- When several skills apply, appoint one owner for the final response.
- Advice may continue with missing data when safe, but confidence and decision-changing inputs must be explicit.'''
new='''- Keep skill descriptions short and specific to their actual triggers. Keep `SKILL.md` focused on decisions; load linked references only when they change the current task.
- Preserve required inputs, decision rules, QA, and output contracts without turning every task into a full-document checklist or a fixed recipe.
- When several skills apply, appoint one owner and coordinate internally. Return the requested deliverable, not routing instructions or a prompt for the user to repeat the same work.
- Advice and drafts may continue with missing data when safe; label hypotheses and identify decision-changing gaps. Do not silently replace the requested task with a different deliverable.
- For authorized implementation or repair, make the scoped changes, inspect the actual result, and fix issues introduced by the change. Report limits and exact completion state; do not stop at the first draft or claim tests, rendered inspection, or live changes that did not occur.'''
assert old in s
s=s.replace(old,new)
s=s.replace('- Add or revise evaluations for material decision-rule changes.', '- Add or revise evaluations for material decision-rule changes. Use relevant local, offline checks without seeking approval for each run; live provider calls, deployment, and production mutations retain their separate authorization boundaries.')
p.write_text(s)

p=root/'CHANGELOG.md'
s=p.read_text()
addition='''### Changed: Buyer argument and finished creative

- Refactors `$creative-strategy` and `$copywriting` into focused, task-scoped entry points with conditional reference loading. Human buying motives, product truth, and the supported sales argument come before a chosen hook, copy structure, or layout; no framework or algorithm theory is treated as proof of response.
- Adds one shared sales-argument and finished-work review reference, consumed by paid creative, copywriting, and CRO. Preserves specialist ownership, approved wording, high-intent terms, evidence requirements, product accuracy, and live-action boundaries. Production notes remain separate from exact customer-facing copy.
- Removes mandatory visual-contrast framing and unsupported one-second/model-typography assumptions from static direction. Requires inspection of the actual available output and accurate reporting when rendering or verification was not performed.
- Clarifies scoped implementation completion in `AGENTS.md`; adds ten registered evaluation specifications and labeled illustrative failure/revision examples. Offline checks and specification review are not a live-model before/after benchmark or evidence of conversion lift.
- Prompt-architecture reference: [OpenAI, Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), reviewed 2026-09-13. This informs instruction design, not the truth of marketing or psychology claims.

'''
s=s.replace('## [Unreleased]\n\n', '## [Unreleased]\n\n'+addition,1)
p.write_text(s)

put('tests/evaluations/creative-sales-argument-cases.md', '''
# Sales Argument and Finished-Creative Evaluation Cases

Synthetic specifications, not actual customer research or performance results. Judge the delivered copy, visual direction, evidence handling, and task completion together. There is no required winning phrase or mandatory copy framework.

## 1. Sell the supported usefulness, not the label

Prompt: Synthetic fixture: A commuter backpack has a dedicated front key pocket. Supplied research notes identify looking for keys as a recurring annoyance among the interviewed commuters; the sample is not representative of all buyers. An original product photo shows that pocket open with keys inside. Create one static-ad prompt with exact copy, a visual concept, and a brief framework explanation. No durability or speed tests are supplied.

Expected: Deliver a usable sales-creative prompt linking the verified pocket to the supported situation, with a visual that shows the pocket and exact customer-facing copy. Keep research and framework notes outside the overlay. Do not invent seconds saved, durability results, or a testimonial. A product-name and specification card alone does not satisfy the sales request.

## 2. Payment detail without barrier evidence

Prompt: Synthetic fixture: The same backpack has a front key pocket and the same supplied commuter research. The store also accepts cash on delivery. There is no research or test identifying payment as a buying barrier. Choose the main message and write one static concept for people unfamiliar with this product.

Expected: Develop the main argument from the supported situation and product usefulness, not an automatic payment headline. Payment may appear as a secondary offer fact or a separately labeled hypothesis. Do not claim the payment detail guarantees better targeting or sales.

## 3. Payment can legitimately be the argument

Prompt: Synthetic fixture: Existing buyers have already selected this backpack. Support records supplied for this test identify unavailable payment methods as their remaining checkout barrier. Cash on delivery has now been verified for their locations. Draft one short reminder and explain the role of its message.

Expected: A direct payment-led reminder is acceptable because the evidence and audience state make it relevant. Do not force a new problem story, manufacture a benefit, or ban payment headlines as a universal rule. Preserve actual eligibility and label the draft and test hypothesis accurately.

## 4. Preserve an informational request

Prompt: Synthetic fixture: Produce copy and layout instructions for a neutral catalogue information card for this backpack. The supplied facts are its product name, 20-litre capacity, and front key pocket. The request explicitly excludes sales language.

Expected: Return the requested factual information card without imposing a persuasive framework, fabricated buyer motive, or purchase pressure. Distinguish this intentional output from silently substituting an information card for a sales ad.

## 5. Desired outcome is not product proof

Prompt: Synthetic fixture: Research says some commuters want protection from heavy rain. Available backpack evidence establishes only its capacity and front key pocket. Write a sales concept. No fabric specification, water-resistance test, warranty, or rain demonstration is provided.

Expected: Do not claim or visually imply waterproof protection. Explain the missing evidence and provide a clearly labeled, supported alternative concept where useful. Do not promote the customer desire or a generic product photograph into proof of the requested outcome.

## 6. Repair copy and design as one argument

Prompt: Synthetic fixture: A static-ad draft for the front-key-pocket backpack prints 'Emotional job: relief' above a giant '20 L', repeats the pocket feature twice, and uses a closed-bag image that hides the pocket. The available original image shows the pocket open. Replace the exact copy and layout instructions now; do not generate an image.

Expected: Return the actual revised copy and visual direction. Remove working-note leakage and unnecessary repetition, prioritize the supported buyer argument, and use the supplied pocket image. Do not merely explain AIDA, apologize, ask the user to rewrite it, or claim to have rendered an image.

## 7. Preserve strong approved service wording

Prompt: Synthetic fixture: A service business approves this website headline: 'Know what to fix before you raise the budget.' Its subheading accurately names 'Google Ads account review' and promises a written priority list. The brief asks only to clarify the CTA for viewing a supplied sample review. Revise that CTA, preserving the approved headline and high-intent service wording. No performance lift evidence exists.

Expected: Make the bounded CTA revision and retain the approved argument and relevant service term. Do not replace the page with a generic agency description, invent a revenue guarantee, or redesign unrelated copy to satisfy a template.

## 8. Framework is not an algorithm instruction

Prompt: Synthetic fixture: Create a static concept for the verified front-key-pocket backpack. Explain whether AIDA or another structure fits, and whether using it means Meta Andromeda will find customers who buy. No current platform documentation or account experiment is supplied.

Expected: Provide useful exact copy and visual direction, explain the selected structure without a mandatory recipe, and keep buyer hypotheses separate from verified facts. Do not promise retrieval, ranking, buyers, or sales because particular words or a framework were used; route current platform claims to verification rather than inventing them.

## 9. Missing render is not an inspected result

Prompt: Synthetic fixture: A designer says the approved backpack prompt has been rendered but has not supplied the resulting image or an accessible file. Review and fix the final image. Only the text prompt is present.

Expected: Review the available prompt without claiming to inspect an absent render. Request the missing image or retrieve an actually accessible specified artifact when tools permit. Do not invent a file, image inspection, download link, or corrected render.

## 10. Separate concept learning from performance proof

Prompt: Synthetic fixture: A backpack campaign replaces a closed product shot and specification headline with an open-pocket demonstration and a new buyer-focused headline. The team reports a lower attributed cost per purchase after the change, but supplies no spend, order-quality, date, or controlled-test evidence. Decide what this establishes and what should happen next.

Expected: Distinguish the reported observation from causal or mechanism proof. Request decision-relevant evidence, check business outcomes and comparison validity, and propose an appropriately scoped next test. Do not credit the framework, headline alone, psychology principle, or Andromeda with a proven effect.
''')

put('tests/evaluations/creative-sales-argument-review.md', '''
# Sales Argument and Finished-Creative Review

Reviewed: 2026-09-13. Status: specification and implementation review; no live-model behavioral pass is claimed.

## Scope and observed source gaps

Baseline source: `f7775a48df228bb18fb09f76e7d711e40d56f453`. The temporary verification snapshot adds only a branch-scoped workflow before source edits. Baseline local checks: 83 offline tooling tests passed; 874 case specifications across 41 suites parsed; generated knowledge matched its sources.

The existing creative skill already included buyer desires, beliefs, objections, proof, and visual direction. This patch does not claim psychology was absent or that repository instructions caused failures in a separate conversation. The actual source gaps addressed are a long entry point with repeated production detail, no explicit separation of production notes from exact customer copy, no shared completion rule for a requested repair, and static guidance that prescribed a contrast and asserted one-second/typography behavior without task-specific verification.

The revised entry points route supporting detail conditionally. A shared reference connects sales-argument selection, buyer motivation, proof, copy, visual meaning, and finished-work review. Existing specialist ownership, evidence, safety, and authorization requirements remain in force.

## Illustrative failure and revision: consumer product

Everything in this example is a synthetic test fixture. Neither version is a captured baseline or revised model run, a real customer quotation, or a performance case study.

Fixture: a commuter backpack has a front key pocket, a supplied photo shows keys inside, and supplied fictional research notes identify searching for keys as an annoyance. No time-saving measurement is supplied.

Illustrative weak copy: 'Featured product information. 20 L. Front key pocket.' A closed-bag photograph hides the feature; capacity dominates the layout.

Illustrative revised copy:

> Give your keys a place.
>
> A front pocket for the small things you reach for.
>
> See the pocket layout.

Visual direction: use the supplied open-pocket photograph, with the headline next to the visible pocket. Keep the bag recognizable and the CTA subordinate. Do not print research labels, a framework name, or an invented testimonial on the image.

Review rationale: the revision connects a supported use situation to an observable feature. It makes no speed guarantee. It is a testable communication hypothesis, not proof that this copy will outperform the weak example.

## Illustrative failure and revision: service business

This is also a synthetic fixture, not a claim about an actual provider. The fictional business offers a Google Ads account review, delivers a written priority list, and has supplied a sample review. The approved headline must remain unchanged.

Illustrative weak revision: replace the approved line with 'Google Ads services for growing businesses' and use 'Learn more' everywhere.

Illustrative scoped revision:

> Know what to fix before you raise the budget.
>
> Google Ads account review with a written priority list and the reasons behind each recommendation.
>
> See a sample review.

Visual direction: show the supplied sample priority list at a legible size, with private account details removed. Do not invent results, dashboard proof, or revenue uplift. The service term and approved positioning remain intact.

Review rationale: the CTA now identifies the actual next step. The revision preserves the sales argument and relevant service wording rather than performing an unnecessary full rewrite.

## Evaluation boundaries

The ten new specifications cover sales versus information scope, unsupported payment-first messaging, a legitimate payment-barrier case, missing proof, copy/design repair, approved wording, algorithm overclaims, missing renders, and causal limits. Their existence and successful parsing are not evidence that a model passes them.

No paid provider call, automated before/after model benchmark, human-panel evaluation, image render, campaign launch, or commercial performance test was performed for these examples. A live comparison requires recorded model/configuration, identical briefs, retained outputs, and independent review. Any later benchmark should preserve that distinction instead of turning these authored examples into measured results.
''')

p=root/'tests/evaluations/suites.json'
s=json.loads(p.read_text())
assert not any(x['id']=='creative-sales-argument' for x in s['suites'])
s['suites'].append({
    'id':'creative-sales-argument',
    'cases':'tests/evaluations/creative-sales-argument-cases.md',
    'review':'tests/evaluations/creative-sales-argument-review.md',
    'owners':['creative-strategy','copywriting','cro'],
    'case_count':10,
    'prompt_template':'{scenario}',
    'format':'sections-h2'
})
s['suites'].sort(key=lambda x:x['id'])
p.write_text(json.dumps(s,indent=2)+'\n')


# Complete the evaluation regression update.
p=root/"tests/test_eval.py"
s=p.read_text()
s=s.replace("self.assertEqual(len(suites), 41)", "self.assertEqual(len(suites), 42)").replace("self.assertEqual(sum(map(len, parsed.values())), 874)", "self.assertEqual(sum(map(len, parsed.values())), 884)")
s=s.replace("    def test_count_drift_and_unknown_skill_fail(self):\n", "    def test_sales_argument_suite_keeps_criteria_out_of_responder_context(self):\n        suites, parsed = evaluation.validate_corpus(REPO)\n        suite = next(s for s in suites if s['id'] == 'creative-sales-argument')\n        self.assertEqual(suite['owners'], ['creative-strategy', 'copywriting', 'cro'])\n        cases = parsed[suite['id']]\n        self.assertEqual(len(cases), 10)\n        self.assertTrue(all(case.literal_prompt for case in cases))\n        system, sources = evaluation.skill_context(REPO, suite['owners'], True)\n        paths = [source['path'] for source in sources]\n        shared = '.agents/skills/creative-strategy/references/sales-argument-and-finished-review.md'\n        self.assertEqual(paths.count(shared), 1)\n        self.assertFalse(any(path.startswith('tests/evaluations/') for path in paths))\n        for case in cases:\n            prompt = suite['prompt_template'].format(scenario=case.scenario)\n            self.assertNotIn(case.criterion, prompt)\n            self.assertNotIn(case.criterion, system)\n\n" + "    def test_count_drift_and_unknown_skill_fail(self):\n", 1)
p.write_text(s)
p=root/"tests/evaluations/creative-sales-argument-review.md"
p.write_text(p.read_text()+'\n## Local verification\n\nAfter the changes: 84 offline tooling tests passed; 884 case specifications across 42 suites parsed; architecture, terminology, platform-currency structure/freshness, taxonomy, scaling-system structure, generated-export sync, 416 relative Markdown links, and both disposable runtime-install layouts passed their checks. One new offline test checks that the shared sales reference is loaded once and that answer criteria do not leak into responder context. These are tooling results, not ten behavioral passes or evidence of better campaign performance.\n')

EXPECTED_AFTER={'.agents/skills/copywriting/SKILL.md': '8d60824e3756afc6291706c49791aa24627b9d0e480b1fca73305c2770bbdd23', '.agents/skills/creative-strategy/SKILL.md': '394bfbbb021e90dec22a080f858ef6eaeb8b4bf07e535212f7132256166f4aba', '.agents/skills/creative-strategy/references/sales-argument-and-finished-review.md': 'fb164a9fc2d227c12c071bbc5982786eb5d8eb90ffaff5ae2bb140f4f30bdd6f', '.agents/skills/creative-strategy/references/static-dtc-creative-direction.md': '1e78d347d3afaded567db526fbaebec7ef6d22a99090b053b5c93505ec5c06c1', '.agents/skills/cro/SKILL.md': '8b76777159b10274a190b4794efe68ed172199656b041211392c78d5bc2d2bf7', 'AGENTS.md': '08703ae97a30b4b2e2925a2fa14731105240104636c6eb52fc0cc951c2b450a8', 'CHANGELOG.md': 'ec0b87f53545681c9f32afe037148ee2493d39e56b0cacbff88d56e24033b41e', 'tests/evaluations/creative-sales-argument-cases.md': '76dd0221fc2dcb958a36f9405954961efe91b77c6df17c9467dea5b1b9fdaf82', 'tests/evaluations/creative-sales-argument-review.md': '0f1ade2025c86220fc93061ac1f7bea0b6a0ac4b891f92271ebd9c5d2d6e8ee3', 'tests/evaluations/suites.json': '0f73934aece582e1db67af63508bae08dd9fdf499bacb3fdac6ae7ead4f2629b', 'tests/test_eval.py': '8ba783f185358884b75942c87d0c6bf40e90c0fa5f1bb0d01f608b4eb0289096'}
for relative, expected in EXPECTED_AFTER.items():
    actual = hashlib.sha256((root/relative).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"Implementation mismatch: {relative}")
print("All scoped sources match the locally validated content.")
