import argparse
import io
import json
import re
from pathlib import Path

CORRECTION = re.compile(
    r"\b(no|nope|don'?t|do not|stop|wrong|instead|again|still|why (did|is|are)|"
    r"not what|broken|doesn'?t work|isn'?t working|never|always|remember|"
    r"make sure|i said|i told|revert|undo|ugly|bland|generic|too (much|many|big|small)|"
    r"missing|forgot|cheap|expensive|budget|tokens?)\b",
    re.I,
)
NOISE_PREFIX = ("<command-", "<local-command", "Caveat:", "[Request interrupted", "<task-notification", "<bash-")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
SECRET = re.compile(
    r"(sk-(?:proj-|ant-)?[A-Za-z0-9_\-]{16,}|re_[A-Za-z0-9_]{16,}|AIza[0-9A-Za-z_\-]{30,}|xai-[A-Za-z0-9]{20,}|"
    r"gh[posur]_[A-Za-z0-9]{20,}|eyJ[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}|"
    r"(?:api[_-]?key|secret|token|password)\s*[:=]\s*\S{12,})",
    re.I,
)


def user_texts(entry):
    if entry.get("type") != "user":
        return []
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        blocks = [content]
    elif isinstance(content, list):
        blocks = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    else:
        return []
    out = []
    for text in blocks:
        text = REMINDER.sub("", text).strip()
        if text and not text.startswith(NOISE_PREFIX):
            out.append(SECRET.sub("[REDACTED]", re.sub(r"\s+", " ", text)))
    return out


def mine(root, exclude, limit, since=""):
    report = {}
    for session in sorted(root.glob("*/*.jsonl")):
        if session.stem in exclude:
            continue
        project = session.parent.name.split("projects-")[-1] or session.parent.name
        interrupts = 0
        seen = report.setdefault(project, {"messages": [], "interrupts": 0, "sessions": 0})
        seen["sessions"] += 1
        for line in io.open(session, encoding="utf-8", errors="ignore"):
            if "[Request interrupted" in line:
                interrupts += 1
            if '"type":"user"' not in line.replace(" ", ""):
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            for text in user_texts(entry):
                stamp = (entry.get("timestamp") or "")[:10]
                if since and stamp and stamp < since:
                    continue
                seen["messages"].append((stamp, bool(CORRECTION.search(text)), text[:limit]))
        seen["interrupts"] += interrupts
    return report


def render(report):
    lines = ["# History digest", ""]
    for project, data in sorted(report.items(), key=lambda kv: -len(kv[1]["messages"])):
        unique, dupes = [], set()
        for msg in data["messages"]:
            if msg[2] not in dupes:
                dupes.add(msg[2])
                unique.append(msg)
        flagged = sum(1 for m in unique if m[1])
        lines.append(f"## {project}")
        lines.append(f"sessions {data['sessions']}, messages {len(unique)}, corrections {flagged}, interrupts {data['interrupts']}")
        lines.append("")
        for stamp, is_correction, text in unique:
            lines.append(f"- {'[C] ' if is_correction else ''}{stamp} {text}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path.home() / ".claude" / "projects"))
    parser.add_argument("--out", required=True)
    parser.add_argument("--exclude", nargs="*", default=[])
    parser.add_argument("--limit", type=int, default=400)
    parser.add_argument("--since", default="")
    args = parser.parse_args()
    digest = render(mine(Path(args.root), set(args.exclude), args.limit, args.since))
    io.open(args.out, "w", encoding="utf-8").write(digest)
    print(f"wrote {args.out}, {len(digest)} chars")
