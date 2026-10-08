#!/usr/bin/env python3
"""Check manuscript references, audit provenance, fact dependencies and Lean scope.

This standard-library-only check validates repository consistency. It does not
rerun Danus, evaluate mathematical arguments, or replace a TeX compilation.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)


def tex_check():
    entry = ROOT / 'paper/main.tex'
    require(entry.is_file(), 'Missing paper/main.tex')
    if not entry.is_file():
        return
    visited = set()
    contents = []

    def resolve(name, parent, suffix):
        p = Path(name)
        if not p.suffix:
            p = p.with_suffix(suffix)
        for base in (entry.parent, parent):
            candidate = (base / p).resolve()
            if candidate.is_file() and candidate.is_relative_to(ROOT):
                return candidate
        return None

    def read(path):
        if path in visited:
            return
        visited.add(path)
        text = uncomment(path.read_text(encoding='utf-8'))
        contents.append((path, text))
        for name in re.findall(r'\\(?:input|include)\s*\{([^{}]+)\}', text):
            if '#' in name:
                continue
            child = resolve(name, path.parent, '.tex')
            require(child is not None, f'Missing TeX input {name!r} in {path.name}')
            if child is not None:
                read(child)

    read(entry)
    text = '\n'.join(content for _, content in contents)
    labels = re.findall(r'\\label\s*\{([^{}]+)\}', text)
    labels = [x for x in labels if '#' not in x]
    repeated = [x for x, n in Counter(labels).items() if n > 1]
    require(not repeated, 'Duplicate labels: ' + ', '.join(repeated))
    refs = set()
    for group in re.findall(r'\\(?:ref|eqref|pageref|autoref|[cC]ref|[cC]pageref|nameref)\*?\s*\{([^{}]+)\}', text):
        refs.update(x.strip() for x in group.split(',') if '#' not in x)
    missing = refs - set(labels)
    require(not missing, 'Undefined labels: ' + ', '.join(sorted(missing)))
    bibkeys = re.findall(r'\\bibitem\s*(?:\[[^\]]*\])?\s*\{([^{}]+)\}', text)
    bibfiles = set()
    for path, content in contents:
        for group in re.findall(r'\\(?:bibliography|addbibresource)\s*(?:\[[^\]]*\])?\s*\{([^{}]+)\}', content):
            for name in group.split(','):
                b = resolve(name.strip(), path.parent, '.bib')
                require(b is not None, f'Missing bibliography {name!r}')
                if b:
                    bibfiles.add(b)
    for b in bibfiles:
        bibkeys.extend(re.findall(r'@(?!(?:comment|string|preamble)\b)\w+\s*\{\s*([^,\s]+)', b.read_text(encoding='utf-8'), re.I))
    repeated = [x for x, n in Counter(bibkeys).items() if n > 1]
    require(not repeated, 'Duplicate bibliography keys: ' + ', '.join(repeated))
    cites = set()
    for group in re.findall(r'\\(?:[a-zA-Z]*cite[a-zA-Z]*|nocite)\*?\s*(?:\[[^\]]*\]\s*)*\{([^{}]+)\}', text):
        cites.update(x.strip() for x in group.split(',') if '#' not in x and x.strip() != '*')
    missing = cites - set(bibkeys)
    require(not missing, 'Undefined bibliography keys: ' + ', '.join(sorted(missing)))
    print(f'TeX: {len(visited)} files, {len(labels)} labels, {len(bibkeys)} bibliography entries')


def evidence_check():
    index = json.loads((ROOT / 'evidence/danus/fact_index.json').read_text())
    ids = [item['fact_id'] for item in index]
    require(len(ids) == len(set(ids)), 'Duplicate Danus fact IDs')
    graph = {item['fact_id']: item['predecessors'] for item in index}
    for item in index:
        ident = item['fact_id']
        proof = ROOT / item['proof']
        verdict_file = ROOT / item['verification']
        require(proof.is_file(), f'Missing proof {ident}')
        if proof.is_file():
            require(sha256(proof) == item['sha256'], f'Proof hash mismatch {ident}')
        require(verdict_file.is_file(), f'Missing verification {ident}')
        if verdict_file.is_file():
            verdict = json.loads(verdict_file.read_text())
            require(verdict['fact_id'] == ident, f'Verification ID mismatch {ident}')
            require(verdict['verdict'] == item['verdict'] == 'correct', f'Unaccepted fact {ident}')
            require(not verdict['critical_errors'] and not verdict['gaps'], f'Unresolved verification {ident}')
        for dependency in item['predecessors']:
            require(dependency in graph, f'Missing predecessor {dependency} of {ident}')
    active, finished = set(), set()

    def visit(ident):
        if ident in active:
            ERRORS.append(f'Cyclic Danus dependency at {ident}')
            return
        if ident in finished or ident not in graph:
            return
        active.add(ident)
        for pred in graph[ident]:
            visit(pred)
        active.remove(ident)
        finished.add(ident)

    for ident in graph:
        visit(ident)
    origin = json.loads((ROOT / 'archive/origin_manifest.json').read_text())
    for item in origin['included_files']:
        file = ROOT / item['path']
        require(file.is_file(), f'Missing archived source {item["path"]}')
        if file.is_file():
            require(sha256(file) == item['sha256'], f'Archived source changed: {item["path"]}')
    provenance = json.loads((ROOT / 'formal/verification_manifest.json').read_text())
    lean = ROOT / 'formal/GerstenAudit.lean'
    require(sha256(lean) == provenance['source_sha256'], 'Historical Lean source hash mismatch')
    require(provenance['kernel_check_exit_code'] == 0, 'Historical Lean run failed')
    # Public evidence must not include host account paths or runtime instructions.
    private_path = re.compile(r'/' + r'(?:Users|home)/[^/\s]+|file:' + r'//')
    for base in ('evidence', 'archive', 'formal'):
        for file in (ROOT / base).rglob('*'):
            if file.is_file() and file.suffix in {'.md', '.json', '.tex', '.lean', '.log'}:
                require(not private_path.search(file.read_text(encoding='utf-8')),
                        f'Host-specific path in {file.relative_to(ROOT)}')
            require(file.name not in {'PROBLEM.md', 'TARGET.md', 'final_worker_status.json'},
                    f'Internal runtime file in public evidence: {file.relative_to(ROOT)}')
    print(f'Evidence: {len(index)} accepted facts, acyclic dependencies, {len(origin["included_files"])} unchanged original sources')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence-only', action='store_true')
    args = parser.parse_args()
    if not args.evidence_only:
        tex_check()
    evidence_check()
    if ERRORS:
        for error in ERRORS:
            print('ERROR:', error, file=sys.stderr)
        return 1
    print('Repository consistency checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
