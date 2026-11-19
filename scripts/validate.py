import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "kaga-ult-build"
errors = []


def fail(msg):
    errors.append(msg)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail(f"{path.relative_to(ROOT)}: no frontmatter")
        return {}
    return dict(re.findall(r"^(\w[\w-]*):\s*(.+)$", m.group(1), re.M))


plugin = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
versions = {plugin["version"], market["metadata"]["version"], *(p["version"] for p in market["plugins"])}
if len(versions) != 1:
    fail(f"version mismatch across plugin.json and marketplace.json: {sorted(versions)}")

for rel in plugin.get("commands", []) + plugin.get("agents", []):
    if not (PLUGIN / rel).is_file():
        fail(f"plugin.json lists missing file {rel}")

for skill in sorted((PLUGIN / "skills").iterdir()):
    md = skill / "SKILL.md"
    if not md.is_file():
        fail(f"{skill.name}: no SKILL.md")
        continue
    fm = frontmatter(md)
    if fm.get("name") != skill.name:
        fail(f"{skill.name}: frontmatter name is {fm.get('name')!r}")
    if not fm.get("description"):
        fail(f"{skill.name}: empty description")
    for ref in set(re.findall(r"`references/([\w.-]+\.md)`", md.read_text(encoding="utf-8"))):
        if not (skill / "references" / ref).is_file():
            fail(f"{skill.name}: links missing references/{ref}")

for agent in sorted((PLUGIN / "agents").glob("*.md")):
    fm = frontmatter(agent)
    if fm.get("name") != agent.stem or not fm.get("description"):
        fail(f"agents/{agent.name}: name or description wrong")

tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
secret = re.compile(r"sk-[A-Za-z0-9_-]{24,}|ghp_[A-Za-z0-9]{30,}|github_pat_\w{40,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY")
for rel in filter(None, tracked):
    if rel.endswith("rates.yml"):
        fail(f"{rel} is tracked; it holds the real rate card")
    path = ROOT / rel
    if path.suffix not in {".md", ".json", ".yml", ".yaml", ".py", ".js", ".ts", ".sh", ".txt"}:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for n, line in enumerate(text.splitlines(), 1):
        if "\u2014" in line or "\u2013" in line:
            fail(f"{rel}:{n}: em or en dash")
        if secret.search(line):
            fail(f"{rel}:{n}: looks like a secret")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: v{versions.pop()}, {len(list((PLUGIN / 'skills').iterdir()))} skills, {len(list((PLUGIN / 'agents').glob('*.md')))} agents")
