def naive_majority_element(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    occur = {}
    for i in nums:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    for k, v in occur.items():
        if v > n/2:
            return k

def majority_element(nums):
    candidate = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1
    return candidate
