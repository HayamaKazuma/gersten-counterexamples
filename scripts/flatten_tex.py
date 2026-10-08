#!/usr/bin/env python3
"""Expand the manuscript's local TeX inputs into a standalone source file."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def flatten(entry):
    base = entry.parent.resolve()
    active = set()

    def expand(path):
        path = path.resolve()
        if path in active:
            raise ValueError(f'Cyclic TeX input: {path.name}')
        if not path.is_relative_to(base):
            raise ValueError('TeX input leaves the manuscript directory')
        active.add(path)
        text = path.read_text(encoding='utf-8')

        def include(match):
            name = Path(match.group(1))
            if not name.suffix:
                name = name.with_suffix('.tex')
            candidates = [base / name, path.parent / name]
            child = next((p for p in candidates if p.is_file()), None)
            if child is None:
                raise FileNotFoundError(name)
            rel = child.resolve().relative_to(base)
            return f'\n% Begin input: {rel}\n{expand(child)}\n% End input: {rel}\n'

        # Sources use literal input paths. Keep comments, including trailing
        # comments, without trying to expand commands inside them.
        lines = []
        for line in text.splitlines(keepends=True):
            comment_at = len(line)
            for offset, char in enumerate(line):
                if char != '%':
                    continue
                slash_count = 0
                previous = offset - 1
                while previous >= 0 and line[previous] == '\\':
                    slash_count += 1
                    previous -= 1
                if slash_count % 2 == 0:
                    comment_at = offset
                    break
            code, comment = line[:comment_at], line[comment_at:]
            lines.append(re.sub(r'\\(?:input|include)\s*\{([^{}]+)\}', include, code) + comment)
        active.remove(path)
        return ''.join(lines)

    return expand(entry)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entry', type=Path, default=ROOT / 'paper/main.tex')
    parser.add_argument('--output', type=Path, default=ROOT / 'build/gersten-counterexamples.tex')
    args = parser.parse_args()
    result = flatten(args.entry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding='utf-8')
    print(f'Wrote {args.output} ({len(result)} characters)')
