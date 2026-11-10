# alfred-pydocs

An Alfred workflow for Python tooling docs. Type a keyword and a code or a few words, see what it
is, and press Enter to open its docs. ⌘C copies the code.

| keyword | searches | example |
| --- | --- | --- |
| `ruff` | ruff rules | `ruff TID251`, `ruff line too long` |
| `ty` | ty rules | `ty unresolved-import` |
| `pyright` | pyright rules (`report*` settings) | `pyright optional member` |
| `pep` | PEPs | `pep 8`, `pep type hints` |
| `py` | all of the above | `py typing` |

Install: download `alfred-pydocs.alfredworkflow` from the
[latest release](https://github.com/NorthIsUp/alfred-pydocs/releases/latest) and open it.

The index is built on first use and rebuilt weekly: ruff and ty rules from the installed tools
(falling back to `mise exec <tool>@latest`, then `uvx`), pyright rules from its config schema, and
PEPs from `peps.python.org/api/peps.json`. A source that's unavailable is skipped.

Built from [template-alfred-workflow-rs](https://github.com/NorthIsUp/template-alfred-workflow-rs)
on [we-love-alfred](https://github.com/NorthIsUp/north/tree/main/crates/we-love-alfred); everything
but the build lives in `workflow/workflow.toml`.

## Develop

```sh
mise install
mise run test
mise run install     # build dist/alfred-pydocs.alfredworkflow and open it in Alfred
```

Release: `mise run bump-patch`, commit, push to `main`. CI tags and attaches the workflow.
