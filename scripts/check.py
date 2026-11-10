from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
names = 'define research analyze evaluate review validate plan investigate'.split()
errors = []
for name in names:
    f = root/'plugin'/'skills'/name/'SKILL.md'
    if not f.exists(): errors.append(f'missing {f}')
    else:
        s=f.read_text(encoding='utf8')
        if not s.startswith('---\n') or f'name: {name}\n' not in s or 'description:' not in s:
            errors.append(f'invalid metadata: {name}')
actual={p.parent.name for p in (root/'plugin'/'skills').glob('*/SKILL.md')}
if actual != set(names): errors.append(f'unexpected skill set: {actual ^ set(names)}')
print('PASS: eight skills and frontmatter present' if not errors else '\n'.join(errors))
sys.exit(bool(errors))
