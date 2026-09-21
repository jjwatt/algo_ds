#!/usr/bin/env python3

# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume the input array always has a valid answer.


def wiggle_sort(nums: list[int]) -> None:
    arr = sorted(nums)
    n = len(nums)

    # Midpoint split: smaller half gets the extra element if n is odd.
    mid = (n - 1) // 2

    # Pointers to the end of each half.
    left = mid
    right = n - 1

    # Interleave backwards: odd positions take from the larger half,
    # even positions take from the smaller half.
    for i in range(n):
        if i % 2 == 1:
            nums[i] = arr[right]
            right -= 1
        else:
            nums[i] = arr[left]
            left -= 1


if __name__ == "__main__":
    input1 = [1, 5, 1, 1, 6, 4]
    print(f"{input1=}")
    wiggle_sort(input1)
    print(f"After wiggle_sort: {input1=}")
