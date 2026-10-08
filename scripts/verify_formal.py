#!/usr/bin/env python3
"""Run the pinned Lean checker; retain a log and provenance under build/."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', default='lean', help='Lean 4.34.1 executable')
    args = parser.parse_args()
    source = ROOT / 'formal/GerstenAudit.lean'
    text = source.read_text(encoding='utf-8')
    # Source contains only simple non-nested comments; reject proof admissions.
    code = re.sub(r'/\-.*?\-/', '', text, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
        raise SystemExit('Forbidden admission or untrusted evaluation in formal source')
    executable = str(Path(args.lean).resolve()) if '/' in args.lean else args.lean
    version = subprocess.check_output([executable, '--version'], cwd=source.parent, text=True).strip()
    if not re.search(r'\b4\.34\.1\b', version):
        raise SystemExit(f'Expected Lean 4.34.1; received {version}')
    output = ROOT / 'build/formal'
    output.mkdir(parents=True, exist_ok=True)
    run = subprocess.run(
        [executable, '-o', str(output / 'GerstenAudit.olean'), source.name],
        cwd=source.parent, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    (output / 'lean.log').write_text(run.stdout, encoding='utf-8')
    manifest = {
        'version': version,
        'source': 'formal/GerstenAudit.lean',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'exit_code': run.returncode,
        'theorems': len(re.findall(r'^theorem\s+', code, re.M)),
        'scope': 'Polynomial identities and two natural-number inequalities only.',
        'end_to_end_K_theory_formalization': False,
    }
    (output / 'result.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(run.stdout, end='')
    print(f'Lean exit code: {run.returncode}; log: build/formal/lean.log')
    return run.returncode


if __name__ == '__main__':
    sys.exit(main())
