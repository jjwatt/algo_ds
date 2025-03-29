def removeDuplicates2(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return len(nums)

    # Start the slow pointer at index 2 (allowing 2 of the first element)
    slow = 2
    for fast in range(2, len(nums)):
        # Compare with the element TWO positions back
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 5]
    breakpoint()
    n = removeDuplicates2(nums)
