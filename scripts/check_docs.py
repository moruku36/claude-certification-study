"""Read-only local documentation checks; standard library, no network."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
markdown = list(ROOT.rglob('*.md'))
link_count = 0
for path in markdown:
    text = path.read_text(encoding='utf-8')
    if text.count('```') % 2:
        errors.append(f'{path.relative_to(ROOT)}: unclosed code fence')
    if text.count('<details>') != text.count('</details>'):
        errors.append(f'{path.relative_to(ROOT)}: unclosed details')
    if '\ufffd' in text:
        errors.append(f'{path.relative_to(ROOT)}: replacement character')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if re.match(r'https?://', link):
            continue
        if link.startswith('#'):
            continue
        target = (path.parent / unquote(link.split('#')[0])).resolve()
        link_count += 1
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing or outside-root link {link}')
    if re.search(r'(?:sk-ant-|gh[pousr]_)[A-Za-z0-9_-]{16,}', text):
        errors.append(f'{path.relative_to(ROOT)}: possible credential')

expected_weights = {
    'CCAO-F': [14,21,12,16,12,15,10],
    'CCAR-F': [27,18,20,20,15],
    'CCDV-F': [14.7,33.1,3.1,2.6,16.8,11,8.1,10.6],
    'CCAR-P': [17,13,19,16,14,14,7],
}
for lang in ('en','ja'):
    base = ROOT / 'docs' / lang
    for name in ('exam-facts','study-plan','coverage','concepts','labs','practice'):
        if not (base / f'{name}.md').exists():
            errors.append(f'missing {lang}/{name}')
    concepts=(base/'concepts.md').read_text(encoding='utf-8')
    labs=(base/'labs.md').read_text(encoding='utf-8')
    practice=(base/'practice.md').read_text(encoding='utf-8')
    if re.findall(r'^## (M\d\d)',concepts,re.M) != [f'M{i:02}' for i in range(1,11)]:
        errors.append(f'{lang}: concept IDs')
    if re.findall(r'^## (L\d\d)',labs,re.M) != [f'L{i:02}' for i in range(1,13)]:
        errors.append(f'{lang}: lab IDs')
    if re.findall(r'^## (Q\d\d)',practice,re.M) != [f'Q{i:02}' for i in range(1,31)]:
        errors.append(f'{lang}: question IDs')
    if practice.count('<details>') != 30:
        errors.append(f'{lang}: answer count')
    coverage=(base/'coverage.md').read_text(encoding='utf-8')
    for code,weights in expected_weights.items():
        section=coverage.split(f'## {code}\n',1)[1].split('\n## ',1)[0]
        actual=[float(x) for x in re.findall(r'\| ([\d.]+)% \|',section)]
        if actual != weights or abs(sum(actual)-100)>0.01:
            errors.append(f'{lang}/{code}: weight mismatch {actual}')
        for line in section.splitlines():
            if re.search(r'\| [\d.]+% \|',line):
                if not re.search(r'Q\d\d',line) or not re.search(r'M\d\d',line) or not re.search(r'L\d\d',line):
                    errors.append(f'{lang}/{code}: missing curriculum mapping')
sources=json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
if len({s['id'] for s in sources}) != len(sources):
    errors.append('duplicate source IDs')
if any(s['checked_on'] != '2026-10-13' for s in sources):
    errors.append('source checked dates differ')
index=json.loads((ROOT/'practice-index.json').read_text(encoding='utf-8'))
if len(index)!=30 or any(len(q['answer']) != q['select'] for q in index):
    errors.append('question index inconsistent')
for lang in ('en','ja'):
    text=(ROOT/'docs'/lang/'practice.md').read_text(encoding='utf-8')
    answers=re.findall(r'\*\*([ABCD]+)\*\*',text)
    if answers != [q['answer'] for q in index]:
        errors.append(f'{lang}: answer key differs')
print(f'Markdown files: {len(markdown)}; local links: {link_count}; sources: {len(sources)}')
print('Coverage: 27 domains, weights and bilingual mappings checked')
print('Curriculum: 10 concepts, 12 labs, 30 questions in each language')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('PASS: local docs checks (external HTTP checks are separate)')
