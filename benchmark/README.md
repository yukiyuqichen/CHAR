# Data format benchmark

Why the variant→standard character maps are stored as **UTF-8 JSON, one entry
per line** (`char_converter/data/*.json`) rather than a compact text lexicon or
MessagePack.

**Short version: the choice is about maintainability, not performance.** The
benchmark below exists to *rule performance out* as a deciding factor — it
confirms that size and parse time do not meaningfully differ between the
sensible options, so the format can be picked purely on how easy the data is to
live with across the whole project. On that axis JSON wins (see
[Decision](#decision)).

The maps are loaded once per `CharConverter` construction
(`char_converter/converter.py`), and the data is identical across formats —
6,578 entries for `v2s`, 6,781 for `v2t`, each a `char → [char, ...]` mapping.

## How to reproduce

```bash
python benchmark/benchmark_formats.py
```

The script loads the current data, regenerates every other format from it into
a temp dir, verifies each round-trips back to the same dict, then times the
full **open-file + parse-into-dict** path (`timeit`, min of 7 samples ×
200 calls). It reports whether msgpack's C extension is active, because that
dominates the msgpack numbers (see below).

## Results

Python 3.11.7. `bytes` = on-disk size; `µs/load` = end-to-end read+parse,
lower is better. The shipped format is **json (utf-8, 1/line)**.

### With msgpack C extension (normal `pip install msgpack`)

| option | format | bytes | µs/load |
| --- | --- | ---: | ---: |
| v2s | json (ascii escapes) | 155,236 | 931 |
| v2s | **json (utf-8, 1/line)** | **107,927** | **1,240** |
| v2s | opencc lexicon (txt) | 54,781 | 1,192 |
| v2s | msgpack | 61,362 | 1,127 |
| v2t | json (ascii escapes) | 162,156 | 961 |
| v2t | **json (utf-8, 1/line)** | **112,720** | **1,265** |
| v2t | opencc lexicon (txt) | 57,311 | 1,223 |
| v2t | msgpack | 64,095 | 1,159 |

### With pure-Python msgpack fallback (e.g. some Anaconda builds)

| option | format | bytes | µs/load |
| --- | --- | ---: | ---: |
| v2s | json (ascii escapes) | 155,236 | 872 |
| v2s | **json (utf-8, 1/line)** | **107,927** | **1,176** |
| v2s | opencc lexicon (txt) | 54,781 | 1,186 |
| v2s | msgpack | 61,362 | **10,810** |
| v2t | json (ascii escapes) | 162,156 | 990 |
| v2t | **json (utf-8, 1/line)** | **112,720** | **1,257** |
| v2t | opencc lexicon (txt) | 57,311 | 1,257 |
| v2t | msgpack | 64,095 | **11,250** |

Absolute numbers vary by machine, but the relationships are stable.

## What the numbers say

The headline: at ~1 ms per load, the spread between JSON, the text lexicon and
C-extension msgpack is noise. Nobody constructs converters in a hot loop, and
even if they did, the difference is immaterial. **Treat size and speed as a
tie — decide on maintainability.** The details below are just the evidence for
that "tie".

* **Parse cost is format-insensitive at the top end.** UTF-8 JSON, the text
  lexicon and C-extension msgpack all land within ~10% of each other
  (~1.1–1.3 ms). The real work is allocating ~6,700 short `str`/`list` objects,
  which every format pays equally; the container syntax is noise next to that.

* **Size.** The text lexicon is smallest (~55 KB) and UTF-8 JSON is middling
  (~108 KB); ASCII-escaped JSON is largest (~155 KB) because every CJK
  character becomes a 6-byte `\uXXXX` escape. A ~50 KB spread over a file
  loaded once is not a decision criterion here.

* **ASCII-escaped JSON parses fastest** (~0.9 ms) despite being the largest
  file — CPython's C JSON decoder handles `\uXXXX` (plain ASCII bytes) slightly
  faster than decoding multi-byte UTF-8. We still prefer UTF-8 output because
  it is readable in a diff; the sub-0.3 ms cost is irrelevant.

* **msgpack is a dependency trap.** With the C extension it's competitive, but
  with the pure-Python fallback it is **~10× slower** (11 ms). It also forced a
  third-party runtime dependency — and, historically, dragged in `setuptools`
  at runtime to locate the data file.

## Decision

**UTF-8 JSON, one entry per line — chosen for maintainability.** With
performance and size ruled out as differentiators, the format is decided by how
easy the data is to maintain across the whole project:

* **One format every consumer reads natively — no build pipeline.** The table
  is used in three places: the Python package (`json.load`), the npm package
  (`import … assert { type: 'json' }`), and the browser demo
  (`fetch(...).then(r => r.json())`, which pulls the very same
  `char_converter/data/*.json` off GitHub Pages). JSON is the only format all
  three read with zero parsing code and zero conversion step. A binary or
  bespoke-text format would force a build pipeline to emit JSON for the two
  web consumers — added machinery to save ~50 KB nobody notices.

* **Zero runtime dependencies.** Loading is stdlib `json` on Python and native
  everywhere in JS; nothing to install, pin, or break on upgrade. (msgpack was
  a third-party dependency and historically pulled `setuptools` in at runtime
  to locate the data file.)

* **Human-readable, diffable data.** One `"before": ["after", …]` per line, so
  code review and `git diff` show exactly which mappings changed — impossible
  with binary msgpack, and lost with a single-line JSON blob.

The compact text lexicon is smaller and the ASCII JSON parses marginally
faster, but neither advantage is worth a second data format or a build step
across three consumers.

## Implementation note

The data is written one entry per line (`{\n"key": ["val"],\n…}`) purely for
readable diffs — it is still a single valid JSON object, so every consumer
loads it with an ordinary JSON parser and no special handling.
