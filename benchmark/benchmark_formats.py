"""Benchmark data-format choices for the variant->standard character maps.

Measures end-to-end "read file + parse into a dict" cost for the same mapping
stored in four formats, plus the on-disk size of each. Run from the repo root:

    python benchmark/benchmark_formats.py

The current data lives in char_converter/data/*.json (UTF-8, one entry per
line); the other representations are generated from it into a temp dir for
comparison.

Notes
-----
* Parse cost dominates over I/O here: building ~6,700 short str/list objects
  is the real work, and it is the same regardless of format.
* msgpack speed depends entirely on whether its C extension is installed.
  A plain `pip install msgpack` ships it; some environments (e.g. certain
  Anaconda builds) fall back to a pure-Python implementation that is ~10x
  slower. The script reports which one is active.
* Read the whole file then split; iterating a file object line by line
  (`for line in f`) is measurably slower for the text/lexicon format.
"""

import json
import os
import statistics
import sys
import tempfile
import timeit

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, 'char_converter', 'data')
OPTIONS = ['v2s', 'v2t']
NUMBER = 200   # timed calls per sample
REPEAT = 7     # samples; the minimum is reported (least noise)

try:
    import msgpack
    _HAS_C_EXT = False
    try:
        from msgpack import _cmsgpack  # noqa: F401
        _HAS_C_EXT = True
    except Exception:
        pass
except ImportError:
    msgpack = None
    _HAS_C_EXT = False


def load_source(opt):
    """Load the current on-disk JSON data into a dict (the reference data)."""
    with open(os.path.join(DATA, f'{opt}.json'), encoding='utf-8') as f:
        return json.load(f)


# ---- writers: produce each format from a dict -------------------------------

def write_json_ascii(d, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f)  # ensure_ascii=True -> \uXXXX escapes


def write_json_utf8_lines(d, path):
    body = ',\n'.join(
        json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False)
        for k, v in d.items()
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write('{\n' + body + '\n}\n')


def write_lexicon(d, path):
    with open(path, 'w', encoding='utf-8') as f:
        for k, v in d.items():
            f.write(k + '\t' + ' '.join(v) + '\n')


def write_msgpack(d, path):
    with open(path, 'wb') as f:
        f.write(msgpack.packb(d, use_bin_type=True))


# ---- loaders: read file + parse (end-to-end, matches real usage) ------------

def load_json_any(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_lexicon(path):
    mapping = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.read().rstrip('\n').split('\n'):
            if not line:
                continue
            k, _, rest = line.partition('\t')
            mapping[k] = rest.split(' ')
    return mapping


def load_msgpack(path):
    with open(path, 'rb') as f:
        return msgpack.unpack(f, raw=False)


def bench(fn):
    fn()  # warm the OS page cache
    return min(timeit.repeat(fn, number=NUMBER, repeat=REPEAT)) / NUMBER * 1e6


def main():
    print(f"Python {sys.version.split()[0]}")
    if msgpack:
        print(f"msgpack {'.'.join(map(str, msgpack.version))} "
              f"(C extension: {'yes' if _HAS_C_EXT else 'NO -> pure-Python fallback'})")
    else:
        print("msgpack not installed -> skipping that format")
    print(f"timeit: min of {REPEAT} samples x {NUMBER} calls, end-to-end read+parse\n")

    formats = [
        ('json (ascii escapes)', '.json',    write_json_ascii,      load_json_any),
        ('json (utf-8, 1/line)', '.json',    write_json_utf8_lines, load_json_any),
        ('opencc lexicon (txt)', '.txt',     write_lexicon,         load_lexicon),
    ]
    if msgpack:
        formats.append(('msgpack',          '.msgpack', write_msgpack,  load_msgpack))

    header = f"{'option':6} {'format':24} {'bytes':>8} {'us/load':>9}"
    print(header)
    print('-' * len(header))
    with tempfile.TemporaryDirectory() as tmp:
        for opt in OPTIONS:
            ref = load_source(opt)
            for idx, (name, ext, writer, loader) in enumerate(formats):
                path = os.path.join(tmp, f'{opt}_{idx}{ext}')
                writer(ref, path)
                assert loader(path) == ref, f"roundtrip mismatch: {opt} {name}"
                size = os.path.getsize(path)
                us = bench(lambda p=path, l=loader: l(p))
                print(f"{opt:6} {name:24} {size:>8} {us:>9.1f}")
            print()


if __name__ == '__main__':
    main()
