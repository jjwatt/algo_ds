import copy
import heapq
import sys
import timeit


def slow_pairwise(nums):
    product = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = max(product, nums[i] * nums[j])
    return product


def recursive_pairwise(nums):
    def check_pairs(target, others):
        if not others:
            return 0
        product = target * others[0]
        max_of_rest = check_pairs(target, others[1:])
        return max(product, max_of_rest)
    if len(nums) < 2:
        return 0
    first = nums[0]
    rest = nums[1:]
    current_max = check_pairs(first, rest)
    remaining_max = recursive_pairwise(rest)
    return max(current_max, remaining_max)


def faster_pairwise1(nums):
    index1 = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[index1]:
            index1 = i
    index2 = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index1] and nums[i] > nums[index2]:
            index2 = i
    return nums[index1] * nums[index2]


def faster_pairwise_sorted(nums):
    largest2 = sorted(nums, reverse=True)[:2]
    product = largest2[0] * largest2[1]
    return product


def heap_pairwise(nums):
    heap = copy.copy(nums)
    while len(heap) > 2:
        heapq.heappop(heap)
    largest2 = heap[-2:]
    product = largest2[0] * largest2[1]
    return product


def main(argv):
    nums = [int(x) for x in argv[1:]]
    print(f"slow_pairwise(nums): {slow_pairwise(nums)}")
    print(f"faster_pairwise1(nums): {faster_pairwise1(nums)}")
    print(f"heap_pairwise(nums): {heap_pairwise(nums)}")
    print(f"faster_pairwise_sorted(nums): {faster_pairwise_sorted(nums)}")
    print(f"recursive_pairwise(nums): {recursive_pairwise(nums)}")

    print("Timings:")
    print(f"slow_pairwise(nums):\t\t"
          f"{timeit.timeit(lambda: slow_pairwise(nums))}")
    print(
        f"faster_pairwise1(nums):\t\t"
        f"{timeit.timeit(lambda: faster_pairwise1(nums))}"
    )
    print(
        f"faster_pairwise_sorted(nums):\t"
        f"{timeit.timeit(lambda: faster_pairwise_sorted(nums))}"
    )
    print(f"heap_pairwise(nums):\t\t"
          f"{timeit.timeit(lambda: heap_pairwise(nums))}")
    print(
        f"recursive_pairwise(nums):\t"
        f"{timeit.timeit(lambda: recursive_pairwise(nums))}"
    )


if __name__ == "__main__":
    main(sys.argv)
