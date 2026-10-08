#!/usr/bin/env python3
"""Check the publication's metadata delta and preserved review artifacts.

This is a byte-preservation and source-consistency check. It does not rerun
Danus or certify the manuscript's mathematical arguments.
"""
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'evidence/publication/metadata-manifest.json'
HISTORICAL_MANIFEST = 'evidence/manuscript/review-manifest.json'
ALLOWED_CHANGES = {
    'paper/main.tex',
    'paper/preamble.tex',
    'paper/verification-scope.tex',
}
AUTHOR_LINE = '\\author{OpenAI}\n'
THANKS_LINE = (
    '\\thanks{The OpenAI byline is a user-requested attribution to preparation '
    'with ChatGPT/Codex; this is not an official OpenAI publication or '
    'institutional endorsement.}\n'
)
ATTRIBUTION_PARAGRAPH = (
    'The OpenAI byline was requested by the user to attribute the preparation\n'
    'of this consolidated article to ChatGPT/Codex. It does not identify an\n'
    'official OpenAI publication or institutional endorsement.\n\n'
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_file(relative):
    require(isinstance(relative, str), 'Artifact path is not a string')
    path = Path(relative)
    require(not path.is_absolute() and '..' not in path.parts,
            f'Artifact path leaves the repository: {relative}')
    result = (ROOT / path).resolve()
    require(result.is_relative_to(ROOT) and result.is_file(),
            f'Missing or non-local artifact: {relative}')
    return result


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_hash(relative, expected):
    require(isinstance(expected, str) and
            re.fullmatch(r'[0-9a-f]{64}', expected) is not None,
            f'Invalid SHA-256 entry: {relative}')
    data = local_file(relative).read_bytes()
    require(digest(data) == expected, f'SHA-256 mismatch: {relative}')
    return data


def check_metadata_delta(path, before_hash, current, reviewed_source):
    """Recover the old module by undoing only the permitted metadata edits."""
    if path == 'paper/main.tex':
        addition = AUTHOR_LINE + THANKS_LINE
        require(current.count(addition) == 1,
                'main.tex must contain the exact publication byline and note')
        restored = current.replace(addition, '', 1)
    elif path == 'paper/preamble.tex':
        require(current.count('pdfauthor={OpenAI}') == 1,
                'preamble.tex must set pdfauthor={OpenAI} exactly once')
        restored = current.replace('pdfauthor={OpenAI}', 'pdfauthor={}', 1)
    else:
        start = '\n% Begin input: verification-scope.tex\n'
        end = '\n% End input: verification-scope.tex\n'
        require(reviewed_source.count(start) == 1 and
                reviewed_source.count(end) == 1,
                'Cannot locate the historical authoring-scope module')
        restored = reviewed_source.split(start, 1)[1].split(end, 1)[0]
        heading, body = restored.split('\n', 1)
        require(current.startswith(heading + '\n') and current.endswith(body),
                'The historical verification-scope text was modified')
        inserted = current[len(heading) + 1:len(current) - len(body)]
        require(inserted == ATTRIBUTION_PARAGRAPH,
                'The added attribution paragraph differs from the publication note')
    require(digest(restored.encode('utf-8')) == before_hash,
            f'Changes exceed the permitted metadata transformation: {path}')
    return restored


def main():
    manifest = json.loads(local_file(MANIFEST).read_text(encoding='utf-8'))
    old = json.loads(check_hash(
        HISTORICAL_MANIFEST,
        manifest['historical_manifest_sha256']).decode('utf-8'))

    snapshot = manifest['historical_snapshot_files']
    require(isinstance(snapshot, dict) and snapshot,
            'Historical snapshot inventory is empty')
    require(HISTORICAL_MANIFEST in snapshot,
            'Historical manifest is absent from the snapshot inventory')
    for path, expected in snapshot.items():
        require(path.startswith('evidence/manuscript/') and
                path != 'evidence/manuscript/README.md',
                f'Unexpected historical snapshot path: {path}')
        check_hash(path, expected)

    reviewed = check_hash('evidence/manuscript/reviewed.tex',
                          old['source_sha256']).decode('utf-8')
    check_hash(manifest['historical_pdf_path'], old['pdf']['sha256'])
    changed = manifest['changed_modules']
    unchanged = manifest['unchanged_modules']
    require(set(changed) == ALLOWED_CHANGES,
            'Changed modules must be exactly the three attribution modules')
    require(not set(changed).intersection(unchanged),
            'A module is listed as both changed and unchanged')
    require(set(changed).union(unchanged) == set(old['modular_sources']),
            'Publication module inventory differs from the reviewed inventory')
    patch = []
    for path in sorted(changed):
        record = changed[path]
        require(record['before_sha256'] == old['modular_sources'][path],
                f'Incorrect historical module hash: {path}')
        require(record['before_sha256'] != record['after_sha256'],
                f'Module is incorrectly listed as changed: {path}')
        current = check_hash(path, record['after_sha256']).decode('utf-8')
        restored = check_metadata_delta(path, record['before_sha256'], current, reviewed)
        patch.extend(difflib.unified_diff(
            restored.splitlines(keepends=True), current.splitlines(keepends=True),
            fromfile='reviewed/' + path, tofile='publication/' + path))
    require(local_file('evidence/publication/metadata.patch').read_text(
        encoding='utf-8') == ''.join(patch),
        'Publication metadata.patch does not reproduce the exact source delta')
    for path, expected in unchanged.items():
        require(expected == old['modular_sources'][path],
                f'Unchanged module has a different historical hash: {path}')
        check_hash(path, expected)

    current_source = check_hash(manifest['current_source_path'],
                                manifest['current_source_sha256'])
    check_hash(manifest['current_pdf_path'], manifest['current_pdf_sha256'])
    build = ROOT / 'build'
    build.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='publication-check-', dir=build) as temporary:
        output = Path(temporary) / 'current.tex'
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/flatten_tex.py'),
             '--output', str(output)],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        require(result.returncode == 0,
                'Standalone-source expansion failed: ' + result.stderr.strip())
        require(output.read_bytes() == current_source,
                'Archived publication source differs from current TeX inputs')
    print(f'Publication: {len(snapshot)} preserved historical artifacts; '
          f'{len(unchanged)} unchanged modules; 3 metadata-only module changes.')
    print('Publication consistency checks passed; no mathematical review was rerun.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyError, TypeError, ValueError, OSError, subprocess.SubprocessError) as error:
        print(f'ERROR: publication consistency: {error}', file=sys.stderr)
        sys.exit(1)
