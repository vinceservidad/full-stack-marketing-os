# GPT Knowledge Package

Portable Markdown knowledge generated from the canonical Marketing OS sources.
The [capability registry](../CAPABILITY-REGISTRY.md) defines governed, partial,
and unsupported coverage. A knowledge upload does not install executable skills
or establish that a GPT will retrieve and apply them correctly.

## Generated pack

[`pack/`](pack/) contains the numbered knowledge files, setup instructions, and
a source inventory with SHA-256 hashes. The generator includes every governed
skill and its Markdown support files, root governance contracts, and the complete
Markdown libraries in `frameworks/`, `playbooks/`, `workflows/`, and `templates/`.
See [the generated manifest](pack/MANIFEST.md) for current counts and exclusions.

Run the builder from a Git checkout with Git available. It selects tracked and
non-ignored untracked source files using Git's ignore rules, including local
exclude rules. Ignored scratch such as nested `work/` notes is never bundled or
hashed. A tracked file remains canonical even if a later ignore rule matches it;
non-ignored new files remain visible for review before staging. Archives without
their own Git checkout are refused; clone the repository before rebuilding.

```bash
python3 scripts/build-gpt-knowledge.py
python3 scripts/build-gpt-knowledge.py --check
python3 -m unittest discover -s tests -p 'test_gpt_knowledge.py' -v
```

Edit canonical sources, then regenerate and review the resulting diff. `--check`
compares content bytes and the full output tree, so it detects missing, modified,
or extra files, including nested files. Missing or duplicate skill assignments
and local Markdown links to material outside the export fail generation. Adding
a skill requires assigning it in the generator's `BUNDLES` list.

Source sections retain canonical prose and identify their repository paths.
Local Markdown links become source labels; external links and fenced examples
are preserved. Bare paths and URLs are not dependency discovery. Runtime scripts,
non-Markdown assets, local project context, client evidence, examples, evaluations,
and archived documents are outside the pack. These remain explicit limitations,
not implied capabilities.

## Custom GPT setup

Follow [the setup guide](../examples/custom-gpt-setup.md). Upload the numbered
Markdown files and use the instruction body from [`INSTRUCTIONS.md`](pack/INSTRUCTIONS.md).
Keep `MANIFEST.md` for source provenance; it is not an upload file. Rebuild and
replace uploaded files whenever canonical sources change.

The optional hand-maintained [`vince-style.md`](vince-style.md) and
[`humanizer-rules.md`](humanizer-rules.md) are voice guidance. They are not part
of the generated pack and do not override its governance. Check the current GPT
builder's upload allowance before adding optional files.

## Historical exports

The former hand-maintained topic summaries are preserved in
[`docs/archive/gpt-knowledge-v1/`](../docs/archive/gpt-knowledge-v1/). They are
historical material and should not be uploaded alongside the generated pack.
