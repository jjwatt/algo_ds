def binsearch(haystack, needle):
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


def recbinsearch(haystack, needle):
    """Recursive binary search."""
    def rec(low, high):
        if low > high:
            # Didn't find needle
            return None
        mid = (low + high) // 2
        if haystack[mid] == needle:
            return mid
        if haystack[mid] < needle:
            # Search the right side
            return rec(mid + 1, high)
        if haystack[mid] > needle:
            # Search the left side
            return rec(low, mid - 1)
    return rec(0, len(haystack) - 1)



if __name__ == "__main__":
    tests = ((range(1, 11), 5),
             (range(1, 10), 8),
             (range(1, 10), 2),
             (range(10, 21), 16),
             (range(-5, 5), 4),
             (range(-10, 0), 5))
    breakpoint()
    for t in tests:
        res = binsearch(*t)
        if res:
            print(f"Found {t[1]} at index {res}")
        else:
            print(f"Could not find {t[1]} in {t[0]}")
