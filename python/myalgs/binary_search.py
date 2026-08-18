import bisect
from collections.abc import Sequence
from typing import Protocol


class SupportsLessThan(Protocol):
    def __lt__(self, other: "SupportsLessThan", /) -> bool: ...


def pythonic_binsearch[T: SupportsLessThan](
    haystack: Sequence[T], needle: T
) -> int | None:
    index = bisect.bisect_left(haystack, needle)
    if index != len(haystack) and haystack[index] == needle:
        return index
    return None


def binsearch[T: SupportsLessThan](haystack: Sequence[T], needle: T) -> int | None:
    high = len(haystack) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if haystack[mid] == needle:
            return mid
        if haystack[mid] < needle:
            # Search the right side
            low = mid + 1
        elif haystack[mid] > needle:
            # Search the left side
            high = mid - 1
    return None


def recbinsearch[T: SupportsLessThan](haystack: Sequence[T], needle: T) -> int | None:
    """Recursive binary search."""

    def rec(low: int, high: int) -> T | None:
        if low > high:
            # Didn't find needle
            return None
        mid = (low + high) // 2
        if haystack[mid] == needle:
            return mid
        if haystack[mid] < needle:
            # Search the right side
            return rec(mid + 1, high)
        else:
            # Search the left side
            return rec(low, mid - 1)

    return rec(0, len(haystack) - 1)


if __name__ == "__main__":
    tests = (
        (range(1, 11), 5),
        (range(1, 10), 8),
        (range(1, 10), 2),
        (range(10, 21), 16),
        (range(-5, 5), 4),
        (range(-10, 0), 5),
    )
    # breakpoint()
    for t in tests:
        # res = binsearch(*t)
        res = recbinsearch(*t)
        if res:
            print(f"Found {t[1]} at index {res}")
        else:
            print(f"Could not find {t[1]} in {t[0]}")

    for t in tests:
        res = pythonic_binsearch(*t)
        if res:
            print(f"Found {t[1]} at index {res}")
        else:
            print(f"Could not find {t[1]} in {t[0]}")
