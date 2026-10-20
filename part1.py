"""Binary-search membership after explicit sorting preprocessing."""


def binary(S, w):
    """S must be sorted in ascending order. Return whether w occurs."""
    left, right = 0, len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == w:
            return True
        elif S[mid] < w:
            left = mid + 1
        else:
            right = mid - 1
    return False


def prepare(values):
    """One-time O(n log n) preprocessing; not part of query time."""
    return sorted(values)


if __name__ == "__main__":
    S = prepare([33, 3, 40, 11, 21, 9, 16])
    print(binary(S, 21))  # True
    print(binary(S, 20))  # False
