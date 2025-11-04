"""Scratch."""
from sys import maxsize

def max_subarray_sum(a: list[int]):
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def two_sum(nums: list[int], target: int):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(f"Max sum: {max_subarray_sum(lst)}")

    string = "radar"
    print(f"{string=} is_palindrome: {is_palindrome(string)}")

