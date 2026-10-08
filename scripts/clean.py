#!/usr/bin/env python3
"""Remove generated intermediates; preserve the checked-in manuscript PDF."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
for name in ('build', 'dist'):
    shutil.rmtree(root / name, ignore_errors=True)
suffixes = ('.aux', '.bbl', '.bcf', '.blg', '.fdb_latexmk', '.fls', '.log',
            '.out', '.run.xml', '.synctex.gz', '.toc', '.lof', '.lot')
for file in (root / 'paper').glob('*'):
    if file.is_file() and file.name.endswith(suffixes):
        file.unlink()
print('Removed build/, dist/, and TeX intermediates; retained manuscript PDF.')
