# Memory and the code graph

Three memories, each with one job. A resume should read the smallest one that answers the question, not re-explore the repo.

| Layer | Holds | Read when |
|---|---|---|
| `~/.claude` memory | Who Kaga is, his standing rules | Loaded automatically |
| `docs/PROGRESS.md`, `DECISIONS.md`, `CREW-LOG.md` | Where the build is, what was settled and why | Session start, every phase boundary |
| `graphify-out/` | What the code is: files, symbols, imports, calls, clusters | Before any Glob, Grep, or Explore agent on a repo of 50+ source files |

The graph never replaces the docs: it knows what the code does, not why Kaga wanted it that way.

## Graphify

`graphifyy` on PyPI, CLI `graphify`, repo Graphify-Labs/graphify, Apache-2.0. Checked at v0.9.112 (17 Nov 2026).

- **What it does:** parses code with tree-sitter into a NetworkX graph plus a `GRAPH_REPORT.md`. Code is mapped offline with no API key and no telemetry. Docs, PDFs, and images need a semantic pass that sends them to the model.
- **What it saves:** the 71.5x figure is its own benchmark on a 52-file mixed corpus. An independent test measured about 5 to 10x on exploration. Under about 50 source files the graph adds structure, not savings, so skip it.
- **Status:** not installed. Installing it needs Kaga's yes, like any third-party tool.

### Set up, once per repo

```bash
pipx install graphifyy
graphify extract . --code-only
graphify claude install --project
graphify hook install
```

`pipx` runs once per machine. `claude install --project` writes project rules and a hook so Claude checks the graph before searching. `hook install` rebuilds the graph on every commit and branch checkout. Add `graphify-out/` to `.gitignore` unless Kaga wants it committed.

### Use

- **Session start:** read `docs/PROGRESS.md`, then `graphify-out/GRAPH_REPORT.md`.
- **Code questions:** `graphify query "<question>"`, `graphify path A B`, or `graphify explain <symbol>` first. Open a file only after the graph names it.
- **Delegating:** hand the agent the query result and the files it named, never "explore the repo". This replaces the Haiku repo-map sweep wherever a graph exists.
- **After `git pull`:** `graphify update .`. A stale graph lies: if a query names a file that is gone, rebuild before trusting anything else it says.

### Never

- Run the semantic pass on a client's docs or images without Kaga's yes. It sends them to a model and spends tokens once per file.
- Treat an `INFERRED` edge as fact for security or data access. Read the code.
- Put secrets in a query. Every query is logged locally to `~/.cache/graphify-queries.log`.
