"""Leetcode 27 Remove element from list."""


def remove_element(nums: list[int], val: int) -> int:
    """Remove value from list."""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow


def do_example(nums: list[int], val: int):
    """Do example."""
    print(f"\tInput: {nums}")
    res = remove_element(nums, val)
    print(f"\tOutput: {res}")
    print(f"\tnums: {nums}")


if __name__ == "__main__":
    ex1_nums = [3, 2, 2, 3]
    ex1_val = 3
    print("Example 1:")
    do_example(ex1_nums, ex1_val)
    ex2_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    ex2_val = 2
    print("Example 2:")
    do_example(ex2_nums, ex2_val)
