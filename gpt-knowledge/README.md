# GPT Knowledge Package

Export layer for running Full-Stack Marketing OS inside a Custom GPT. Canonical
executable skills live in [`.agents/skills/`](../.agents/skills/); authoritative
capability status is [`CAPABILITY-REGISTRY.md`](../CAPABILITY-REGISTRY.md).

## `pack/` — generated, do not edit

[`pack/`](pack/) holds 18 knowledge files compiled from all 24 governed skills,
their references, and the root contracts. It is built by
[`scripts/build-gpt-knowledge.py`](../scripts/build-gpt-knowledge.py) and
regenerated from canonical, never hand-edited.

```bash
python3 scripts/build-gpt-knowledge.py           # rebuild
python3 scripts/build-gpt-knowledge.py --check   # CI: fail on drift
```

CI fails if a generated file is edited by hand, **and if a governed skill has no
export bundle** — so a new skill cannot ship without reaching the GPT layer. That
second check is the one that matters: the previous hand-written pack had drifted
to roughly 1,100 words against 40,000 canonical, with nine governed skills
missing entirely. It is archived at
[`docs/archive/gpt-knowledge-v1/`](../docs/archive/gpt-knowledge-v1/).

## Setting up the GPT

1. Upload every `*.md` in `pack/` as **Knowledge**, except `INSTRUCTIONS.md` and `MANIFEST.md`.
2. Paste [`pack/INSTRUCTIONS.md`](pack/INSTRUCTIONS.md) into the GPT's **Instructions** field.
3. Optionally add [`vince-style.md`](vince-style.md) and [`humanizer-rules.md`](humanizer-rules.md) as Knowledge for voice and output quality.

[`pack/MANIFEST.md`](pack/MANIFEST.md) lists what each file covers.

## Hand-maintained files

`vince-style.md` and `humanizer-rules.md` are voice and output-quality material.
They are not derived from any skill and are not touched by the generator.

## Scope boundary

A file in this directory does not mean a governed specialist exists — though
since `pack/` is generated from `.agents/skills/`, its coverage now matches the
executable system by construction. `CAPABILITY-REGISTRY.md` remains
authoritative on what is governed, partially covered, or unsupported.
