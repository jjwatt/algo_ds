def removeDuplicates(nums):
    """Remove duplicates from a sorted array in-place"""
    if not nums:
        return 0

    # Start slow at index 1 (first potential unique element)
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
