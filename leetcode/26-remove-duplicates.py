def remove_duplicates(nums):
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


def remove_duplicates_set(nums):
    """Remove duplicates from an unsorted array in-place"""
    seen = set()
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] not in seen:
            seen.add(nums[read_index])
            nums[write_index] = nums[read_index]
            write_index += 1
    # Truncate list to remove remaining elements
    # del nums[write_index:]
    return write_index


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 4]
    breakpoint()
    n = remove_duplicates(nums)
    print(f"{nums=}")
    print(f"{n=}")
