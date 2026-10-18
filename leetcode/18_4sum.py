#!/usr/bin/env python3


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    quadruplets: list[list[int]] = []

    for i in range(n - 3):
        # Skip duplicate values for the first element.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination pruning.
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate values for second element.
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Early termination pruning for second element.
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            # Two-pointer search for the remaining two elements.
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    output = four_sum(nums, target)
    print(f"{output=}")
