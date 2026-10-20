# Assignment 2 Solutions

## Part 1: Binary Search

First, sort the numbers. Then check the middle element of the remaining search range.

- If it equals the target, return True.
- If it is smaller than the target, search the right half.
- If it is larger than the target, search the left half.
- If the range becomes empty, return False.

### Correctness

Initially, the search range contains every element. Because the list is sorted, each comparison safely removes the half that cannot contain the target. Therefore, the target stays in the remaining range if it exists. Finding a match returns True; an empty range means the target is absent.

The range shrinks every iteration, so the algorithm terminates.

### Time Complexity

Each iteration removes at least half the remaining elements, giving O(log n) search time and O(1) extra search space.

Sorting first takes O(n log n). Therefore, the complete operation takes O(n log n), while later searches take O(log n). This meets the requested bound only if preprocessing is allowed. Without preprocessing, searching arbitrary unsorted input requires O(n) time in the worst case.

## Part 2: Exponential Search

Check the first element, then check positions 1, 2, 4, 8, and so on. Stop when the checked value reaches or passes the target, or the position leaves the list. Use binary search within the resulting range.

Return a matching index, or -1 if the target is absent.

### Correctness

Because the list is sorted, any position before a checked value smaller than the target can be ruled out. When doubling stops, the remaining range contains the target if it exists.

Binary search safely narrows this range until a match is found or the range is empty. Doubling eventually reaches the end of the list, and binary search shrinks its range each iteration, so the algorithm terminates.

### Time Complexity

Let p be the target's insertion position: the number of elements smaller than the target.

Doubling and binary search each take O(1 + log(p + 1)) time. Extra space is O(1).

This can improve on searching the whole list when p is small. For a fixed p, the search takes O(1) time. However, worst-case time is still O(log n).

A small target value does not always mean a small position. Therefore, the assignment's requirement of better than O(log n) needs an additional assumption about the target's position. Simply saying the target value is much smaller than n does not guarantee this bound.

## Testing

Both programs passed tests covering empty lists, present and missing targets, duplicates, boundary values, and a large sorted list.
