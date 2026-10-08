#!/usr/bin/env python3
"""Create a portable source/PDF ZIP without Git metadata or build files."""
import hashlib
import json
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
excluded = {'.git', '.lake', '__pycache__', 'build', 'dist'}
suffixes = ('.aux', '.bbl', '.bcf', '.blg', '.fdb_latexmk', '.fls', '.log',
            '.out', '.run.xml', '.synctex.gz', '.toc', '.lof', '.lot',
            '.olean', '.ilean', '.pyc')
files = [p for p in sorted(root.rglob('*')) if p.is_file()
         and not excluded.intersection(p.relative_to(root).parts)
         and p.relative_to(root).as_posix() != 'RELEASE-FILES.sha256.json'
         and not p.name.endswith(suffixes) and p.name != '.DS_Store']
# The historical verification log is public evidence, not a build intermediate.
log = root / 'formal/lean_verification.log'
if log.exists() and log not in files:
    files.append(log)
dist = root / 'dist'
dist.mkdir(exist_ok=True)
manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(files)}
manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + '\n'
archive = dist / 'gersten-counterexamples.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files):
        z.write(p, 'gersten-counterexamples/' + str(p.relative_to(root)))
    z.writestr('gersten-counterexamples/RELEASE-FILES.sha256.json', manifest_text)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
print(f'dist/{archive.name}: {len(files)} files')
print('SHA256:', hashlib.sha256(archive.read_bytes()).hexdigest())
