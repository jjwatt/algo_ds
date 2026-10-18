#!/usr/bin/env python3


def two_sum_sorted(A: list[int], T: int) -> list[tuple[int, int]]:
    left = 0
    right = len(A) - 1
    pairs = []

    while left < right:
        current_sum = A[left] + A[right]

        if current_sum == T:
            pairs.append((A[left], A[right]))
            # Skip duplicates to keep pairs unique.
            while left < right and A[left] == A[left + 1]:
                left += 1
            while left < right and A[right] == A[right + 1]:
                right -= 1
            left += 1
            right -= 1
        elif current_sum < T:
            # Need a larger sum.
            left += 1
        else:
            # Need a smaller sum.
            right -= 1

    return pairs


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    pairs = two_sum_sorted(sorted(nums), target)
    print(f"{pairs=}")
    output = []
    for pair in pairs:
        output.append((nums.index(pair[0]), nums.index(pair[1])))
    print(f"{output=}")
