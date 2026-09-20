# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number for
# every element in nums.

# The next greater number of a number x is the first greater number to
# its traversing-order next in the array, which means you could search
# circularly to find its next greater number. If it doesn't exist,
# return -1 for this number.


def next_greater_elments(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(2 * n):
        curr = nums[i % n]
        while stack and nums[stack[-1]] < curr:
            prev_idx = stack.pop()
            ans[prev_idx] = curr

        # Only push during the first pass.
        if i < n:
            stack.append(i)
    return ans


def main():
    input = [1, 2, 3, 4, 3]
    output = next_greater_elments(input)
    print(f"{output=}")


if __name__ == "__main__":
    main()
