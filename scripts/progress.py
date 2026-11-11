"""Count TODO.md task checkboxes, print a progress bar, refresh the Progress line in the file."""
import re, sys, pathlib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # the bar uses block characters; Windows consoles default to cp1252

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "TODO.md")
text = path.read_text(encoding="utf-8")
tier = None
counts = {}
for line in text.splitlines():
    m = re.match(r"## (P\d)\b", line)
    if m:
        tier = m.group(1)
        continue
    if line.startswith("## "):
        tier = None
    m = re.match(r"- \[( |x)\] \*\*T\d+", line)
    if m and tier:
        done, total = counts.get(tier, (0, 0))
        counts[tier] = (done + (m.group(1) == "x"), total + 1)

done = sum(d for d, _ in counts.values())
total = sum(t for _, t in counts.values())
width = 30
filled = round(width * done / total) if total else 0
bar = "█" * filled + "░" * (width - filled)
tiers = " · ".join(f"{k} {d}/{t}" for k, (d, t) in sorted(counts.items()))
line = f"[{bar}] {done}/{total} ({100 * done // total}%) · {tiers}"
print(line)

marker = re.compile(r"(?m)^\*\*Progress:\*\* .*$")
new = f"**Progress:** {line}"
if marker.search(text):
    text = marker.sub(lambda _: new, text, count=1)
    path.write_text(text, encoding="utf-8", newline="")
