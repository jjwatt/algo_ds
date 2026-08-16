

# def get_concatenation(nums: list[int]) -> list[int]:
#     return nums*2

## Iteration (2 passes)
# def get_concatenation(nums: list[int]) -> list[int]:
#     output = []
#     size = len(nums)
#     times = 2
#     for time in range(times):
#         for i in range(size):
#             output.append(nums[i])
#     return output


## Iteration (1 pass)
# ans, array of len 2n where
# ans[i] == nums[i] and ans[i + n] == nums[i]
def get_concatenation(nums: list[int]) -> list[int]:
    n: int = len(nums)
    # Initialize array twice as big as n.
    ans: list[int] = [0] * 2*n
    for i, _ in enumerate(nums):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans


if __name__ == "__main__":
    lst: list[int] = [1, 4, 1, 2]
    print(f"input list: {lst}")
    output = get_concatenation(lst)
    print(f"output list: {output}")
