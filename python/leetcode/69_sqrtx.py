def sqrt(x):
    low = 0
    high = x
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if mid*mid == x:
            return mid
        if mid*mid < x:
            low = mid + 1
            res = mid
        elif mid*mid > x:
            high = mid - 1
    return res

if __name__ == "__main__":
    tests = ((4, 2), (8, 2))
#    breakpoint()
    for (x, _) in tests:
        res = sqrt(x)
        print(f"{res=}")
