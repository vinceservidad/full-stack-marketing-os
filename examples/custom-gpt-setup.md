# Custom GPT Setup

## 1. Build the knowledge pack

```bash
git clone https://github.com/vinceservidad/full-stack-marketing-os.git
cd full-stack-marketing-os
python3 scripts/build-gpt-knowledge.py
```

`gpt-knowledge/pack/` is committed, so this only matters if you have changed a
skill. The pack is generated from `.agents/skills/` — the same 24 governed
skills a local agent runtime loads.

## 2. Upload the knowledge

Upload every `*.md` in `gpt-knowledge/pack/` as **Knowledge**, except
`INSTRUCTIONS.md` and `MANIFEST.md`. That is 18 files, within the Custom GPT
limit, and leaves room for `vince-style.md` and `humanizer-rules.md` if you want
the voice layer too.

`gpt-knowledge/pack/MANIFEST.md` lists what each file covers.

## 3. Set the instructions

Paste `gpt-knowledge/pack/INSTRUCTIONS.md` into the GPT's **Instructions** field.
It tells the GPT to route before answering, establish the evidence state of every
input, respect the authorization boundary, and never substitute an adjacent skill
for a capability that does not exist.

## 4. Check it took

Ask the GPT:

```text
ROAS is 4.2, let's increase the budget 20% across the account.
```

A correctly configured GPT refuses the universal percentage, asks for the
marginal return rather than the blended average, and requires explicit approval
before any live change. If it just agrees, the instructions did not load.

The same question, worked in full, is in
[`scaling-refusal/`](scaling-refusal/).

## Keeping it current

Rebuild and re-upload when the skills change. `scripts/build-gpt-knowledge.py --check`
runs in CI and fails if the committed pack has drifted from the canonical skills
or if a governed skill has no export bundle.

## Source of truth

GitHub remains the versioned source. The GPT pack is a derived, portable copy —
never edit `gpt-knowledge/pack/` directly; edit the skill and rebuild.
