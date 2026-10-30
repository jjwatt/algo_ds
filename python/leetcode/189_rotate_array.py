def rotate_extra_space(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than n
    new_nums = [0] * n
    for i in range(n):
        new_index = (i + k) % n
        new_nums[new_index] = nums[i]
    # Modify the original array
    for i in range(n):
        nums[i] = new_nums[i]


def rotate_reverse_subarrays(nums, k):
    n = len(nums)
    k = k % n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(0, n - 1)  # Reverse the whole array
    reverse(0, k - 1)  # Reverse the first k elements
    reverse(k, n - 1)  # Reverse the rest
