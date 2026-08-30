# Archived: the hand-written GPT knowledge pack

These nine files were the Custom GPT export layer through v1.18.0. They are
superseded by `gpt-knowledge/pack/`, which is generated from the canonical
skills in `.agents/skills/`.

They are archived rather than deleted because they record what the export layer
used to claim. They should not be uploaded to a GPT.

**Why they were replaced:** hand-maintained, they fell behind the canonical
skills as the system grew from 9 topics to 24 governed skills. At the point of
replacement they totalled roughly 1,100 words against 40,000 in
`.agents/skills/`, and nine governed skills — `$affiliate-marketing`,
`$influencer-marketing`, `$lifecycle-marketing`, `$linkedin-ads`,
`$organic-social`, `$programmatic`, `$public-relations`, `$tiktok-ads`,
`$youtube-ads` — had no export representation at all. A GPT loaded with them was
not running this operating system.

`scripts/build-gpt-knowledge.py --check` now fails CI if a governed skill has no
export bundle, so the divergence cannot recur silently.

`vince-style.md` and `humanizer-rules.md` stayed in `gpt-knowledge/`: they are
voice and output-quality material, not derived from any skill.
