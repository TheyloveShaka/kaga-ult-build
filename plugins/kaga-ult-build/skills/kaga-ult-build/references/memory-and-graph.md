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
- **What it saves:** `graphify benchmark` prints 100x and more, but it measures against reading the whole repo, which nobody does. Tested on MyLand (484 files, 2026-11-19): tracing "how is a document encrypted before upload" cost about 2.5k tokens through the graph against about 8k by grep and read, roughly 3x, and the graph found the exact chain (`addDocument` to `addFile` L335 to `sealFile` in `src/crypto/file.ts`). Under about 50 source files, skip it.
- **Status:** installed on Kaga's machine 2026-11-19 in its own venv at `~/.graphify/venv`, with a `graphify` shim in `~/bin` (no pipx on this machine).

### Set up, once per repo

```bash
graphify update .
echo "graphify-out/" >> .git/info/exclude
```

`update` is the code-only build: tree-sitter, no model, about a minute for 500 files. Never use `graphify extract` for this: it runs the semantic pass with whatever API key the environment holds. Supabase migrations need the SQL extra (`pip install "graphifyy[sql]"` into the venv). `.git/info/exclude` keeps the output out of git without touching the client's `.gitignore`.

Two optional steps change the repo or its hooks, so Kaga runs them himself: `graphify hook install` (rebuild on every commit and checkout) and `graphify claude install --project` (writes a CLAUDE.md section and a hook so Claude checks the graph before searching).

### Use

- **Session start:** read `docs/PROGRESS.md`, then only the summary and core nodes of the report: `sed -n '/^## Summary/,/^## Graph Freshness/p;/^## God Nodes/,/^## Import Cycles/p' graphify-out/GRAPH_REPORT.md`. On MyLand that is 1.2 KB; the whole report is 45 KB.
- **Code questions:** `graphify query "<question>"` to find the entry symbol, then `graphify explain "<path>::<symbol>"` to walk the calls with file and line numbers. `query` output is capped at about 2k tokens and starts noisy (tests first); `explain` is where the precision is. Open a file only at the lines the graph names.
- **Ambiguous names:** the CLI lists the candidates; retry with `path::symbol`.
- **Delegating:** hand the agent the query result and the files it named, never "explore the repo". This replaces the Haiku repo-map sweep wherever a graph exists.
- **After `git pull` or a batch of edits:** `graphify update .` (seconds, cached). A stale graph lies: if a query names a file that is gone, rebuild before trusting anything else it says.

### Never

- Run the semantic pass on a client's docs or images without Kaga's yes. It sends them to a model and spends tokens once per file.
- Treat an `INFERRED` edge as fact for security or data access. Read the code.
- Put secrets in a query. Every query is logged locally to `~/.cache/graphify-queries.log`.
