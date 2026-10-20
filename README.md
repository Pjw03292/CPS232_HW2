# CPS 232 - Fall 2026 - Assignment 2

## Group members

- Patrick Williams
- Sean Sanpietro
- Tyler Knoop

## Files and running

Requires Python 3; no additional packages.

```text
python part1.py
python part2.py
python -m unittest -v
```

On Windows, use `py` instead of `python` if needed. Run these commands from this folder.

Expected example output:

```text
True
False
8 was found at index 2
```

The first two lines come from Part 1; the third comes from Part 2.
See SOLUTIONS.md for the algorithms, correctness proofs, complexity, and limitations.

## Algorithm assumptions

Part 1 uses O(n log n) sorting preprocessing followed by O(log n) membership queries. Part 2 uses exponential search, taking O(1 + log(p + 1)) time, where p is the target’s insertion position. Detailed assumptions, correctness proofs, and complexity analysis are provided in SOLUTIONS.md.
