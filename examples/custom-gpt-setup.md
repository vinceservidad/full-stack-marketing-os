# Custom GPT Setup

## 1. Verify the generated pack

From the root of a Git checkout, with Git and Python 3 available:

```bash
python3 scripts/build-gpt-knowledge.py --check
```

The pack is committed. If canonical sources have changed, run
`python3 scripts/build-gpt-knowledge.py`, review the diff, and repeat the check.
The [manifest](../gpt-knowledge/pack/MANIFEST.md) lists the current upload files,
included sources, source hashes, and coverage limits.

## 2. Upload the knowledge and set instructions

Upload the numbered `*.md` files from `gpt-knowledge/pack/` as Knowledge. Do not
upload `INSTRUCTIONS.md` or `MANIFEST.md`. Paste only the instruction body below
the separator in [`INSTRUCTIONS.md`](../gpt-knowledge/pack/INSTRUCTIONS.md) into
the GPT's Instructions field. Check the current builder's file allowance before
adding optional voice material from `gpt-knowledge/`.

When refreshing an existing GPT, replace the previous pack files. Remove legacy
topic summaries and obsolete bundle versions so contradictory copies do not
remain in Knowledge. The documents in `docs/archive/gpt-knowledge-v1/` are not
current knowledge uploads.

## 3. Check retrieval and decision behavior

Ask a representative question, for example:

```text
ROAS is 4.2, let's increase the budget 20% across the account.
```

Inspect whether the response routes to `optimization-scaling`, preserves the
status of the supplied evidence, applies the current scaling readiness and
authorization gates, and avoids treating a universal percentage as a proven
rule. Review its source use against the owning skill and relevant contracts.

A good answer to one prompt is a smoke check, not proof of reliable retrieval,
better business decisions, or successful live-agent execution. A bad answer
does not by itself identify whether upload, retrieval, instructions, or model
behavior caused the problem. Record the actual output and investigate before
changing canonical rules.

## Source of truth and limits

The repository is the versioned source. The GPT pack is a derived knowledge
snapshot, not an installed agent runtime. It contains no live client evidence,
project context, tool access, or background execution. Current platform claims
still require the checks in `PLATFORM-CURRENCY.md`.

Generated-file checks verify source coverage and export integrity. A local
rebuild does not update an existing GPT; upload and saved-state verification
remain separate actions.
