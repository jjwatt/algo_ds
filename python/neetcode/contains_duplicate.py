
# My first solution.
# def has_duplicate(nums: list[int]) -> bool:
#     nums_set = set(nums)
#     return not len(nums) == len(nums_set)

# O(n^2) solution
# def has_duplicate(nums: list[int]) -> bool:
#     for i, num in enumerate(nums):
#         if num in nums[i+1:]:
#             return True
#     return False

# O(n) dict solution
def has_duplicate(nums: list[int]) -> bool:
    occur: dict[int, int] = {}
    for n in nums:
        occur[n] = 1 + occur.setdefault(n, 0)
    return any(v > 1 for v in occur.values())


if __name__ == "__main__":
    input: list[int] = [1, 2, 3, 3]
    print(f"input: {input}")
    output = has_duplicate(input)
    print(f"output: {output}")

    input = [1, 2, 3, 4]
    print(f"{input=}")
    output = has_duplicate(input)
    print(f"{output=}")
