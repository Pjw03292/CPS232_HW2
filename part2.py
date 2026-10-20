"""Exponential search in a sorted, random-access list."""


def search(a, target):
    """Return a matching index or -1. Input must be sorted ascending."""
    if not a:
        return -1
    if a[0] == target:
        return 0
    if a[0] > target:
        return -1

    bound = 1
    # Double the position until we reach or pass the target.
    while bound < len(a) and a[bound] < target:
        bound *= 2

    left = bound // 2
    right = min(bound, len(a) - 1)
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 20, 30, 45, 60]
    target = 8
    index = search(numbers, target)
    if index != -1:
        print(f"{target} was found at index {index}")
    else:
        print(f"{target} was not found")
