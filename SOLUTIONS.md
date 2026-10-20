# Algorithms, correctness, and complexity

All logarithms below are base 2. Complexity assumes constant-time comparisons and random access to list elements, as is customary for this analysis. The algorithms do not check sortedness during each query because that check would take O(n).

## Part 1: membership in a set

### Input condition and preprocessing

Binary search requires sorted input. Because the problem gives arbitrary natural numbers, `prepare(values)` explicitly sorts them first. Sorting takes O(n log n) worst-case time and the Python implementation uses O(n) additional storage. Once this is done, each call to `binary(S, w)` takes O(log(n + 1)) worst-case time and O(1) auxiliary space.

Thus, the requested O(log n) bound holds for the SEARCH QUERY after preprocessing. It does not hold for the complete one-off operation starting from arbitrary unsorted input. This distinction is essential, not an implementation detail.

If no preprocessing or indexed representation is allowed, exact membership in an arbitrary unsorted array requires inspecting all n elements in the worst case. Suppose a search returns False while leaving a position unread. An input with w at that unread position is indistinguishable from the input examined by the search, so the answer could be wrong. Consequently the worst-case lower bound is Omega(n) element inspections. An O(log n) total solution is unavailable in this input model. Instructor clarification is needed about whether preprocessing is intended.

### Algorithm

1. Sort the input once using `prepare`.
2. Set left = 0 and right = n - 1.
3. While left <= right, compute mid = (left + right) // 2.
4. If S[mid] = w, return True.
5. If S[mid] < w, set left = mid + 1; otherwise set right = mid - 1.
6. Return False if the interval becomes empty.

### Correctness proof

Loop invariant: if w occurs in S and the algorithm has not returned, some occurrence of w lies between left and right, inclusive.

Initialization: the initial interval contains the entire sorted list, so it contains any occurrence of w.

Maintenance: if S[mid] = w, True is correct. If S[mid] < w, every element at or before mid is smaller than w, so discarding those positions preserves the invariant. If S[mid] > w, every element at or after mid is greater than w, so discarding those positions also preserves it.

Termination: each unsuccessful iteration removes mid and at least half the current interval, so the interval strictly shrinks. If the algorithm finds w, it correctly returns True. Otherwise left > right, so no candidate positions remain. By the invariant, w does not occur, and False is correct. This also handles an empty input.

### Query-time proof

An interval of m elements has at most floor(m/2) elements after an unsuccessful iteration. After k such iterations, at most floor(n/2^k) remain. For n >= 1, k = floor(log n) + 1 makes this number zero. Each iteration performs constant work, giving O(log(n + 1)) worst-case query time (usually written O(log n) for n >= 2). Best-case query time is O(1).

## Part 2: exponential search

### Algorithm

Input is an ascending sorted list. The function returns a matching index, or -1 if the target is absent. Duplicates are allowed; the returned match need not be the first.

1. Handle the empty list, a match at index 0, and a target below the first element.
2. Probe indices 1, 2, 4, 8, ... by doubling bound until a probe reaches/passes the target value or leaves the list.
3. Binary-search the inclusive interval [bound // 2, min(bound, n - 1)].
4. Return a matching index or -1.

The original `bound = 2` has been corrected to `bound *= 2`; otherwise the probing loop can fail to terminate.

### Correctness proof

The initial checks are correct: an empty list has no match; equality at index 0 is a match; and if the first value exceeds the target, sortedness rules out every element.

During the doubling phase, every probe that causes another doubling has a value smaller than the target. All preceding elements are therefore also too small. When doubling stops, either bound is outside the list or a[bound] >= target. If a match exists, it must lie in the interval from bound // 2 to min(bound, n - 1), inclusive. This interval may include an already rejected lower endpoint, which is harmless. If the loop never doubled, index 0 has already been checked, and the interval still includes every possible remaining match.

The binary-search phase maintains the invariant that any remaining match lies in [left, right]. Sortedness justifies discarding the lower portion when a[mid] < target and the upper portion when a[mid] > target. Equality returns a correct index. The interval strictly shrinks, so the phase terminates; an empty interval proves absence and justifies -1. Doubling also terminates because bound grows until it reaches the finite list length or the target bracket.

### Complexity and the meaning of a small target

Let p be the insertion position of the target: the number of elements strictly smaller than it, with 0 <= p <= n. Doubling uses O(log(p + 1)) probes. The final interval has O(p + 1) positions, so binary search also uses O(log(p + 1)) comparisons. Including the initial checks, total time is O(1 + log(p + 1)), and auxiliary space is O(1). Worst-case time remains O(log(n + 1)).

This can improve the search cost when the target is near the beginning. However, even p much smaller than n does not by itself guarantee an asymptotically strictly better bound: if p = sqrt(n), log p = (1/2) log n, which is still Theta(log n). If p is bounded independently of n, the time is O(1); if p is at most a fixed power of log n, it is O(log log n).

The assignment says that the target NUMBER i is much smaller than n. A small value does not generally imply a small position in an arbitrary sorted list of numbers. For example, a list may contain many negative numbers followed by the small positive target, or many duplicates smaller than it.

With the ADDITIONAL assumption that the list contains distinct nonnegative integers, a target i has insertion position p <= i. Exponential search then takes O(1 + log(i + 1)) time. This is strictly better asymptotically than log n when log(i + 1) = o(log n), for example for fixed i or i bounded by a fixed power of log n. Merely i/n -> 0 is not enough: i = floor(sqrt(n)) still gives a Theta(log n) bound.

Therefore, exponential search is the supplied improved algorithm under a small-position assumption (or the distinct nonnegative-integer assumption plus an appropriately small i). The literal statement does not provide enough conditions to guarantee a strictly sublogarithmic worst-case search. Those assumptions must be confirmed rather than silently asserted.

## Validation

`test_searches.py` compares results with Python membership on all nondecreasing lists of lengths 0 through 7 over six values, for eight possible targets per list. This covers empty input, duplicates, negative numbers, boundary matches, and absent targets. Additional tests cover unsorted input preprocessing and a 10,000-element list with targets inside and outside its range.
