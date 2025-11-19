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
    heapq.heapify(heap)
    largest2 = heap[-2:]
    product = largest2[0] * largest2[1]
    return product

def main(argv):
    nums = [int(x) for x in argv[1:]]
    print(f"slow_pairwise(nums): {slow_pairwise(nums)}")
    print(f"faster_pairwise1(nums): {faster_pairwise1(nums)}")
    print(f"heap_pairwise(nums): {heap_pairwise(nums)}")
    print(f"faster_pairwise_sorted(nums): {faster_pairwise_sorted(nums)}")
    print("Timings:")
    print(f"slow_pairwise(nums):\t\t{timeit.timeit(lambda: slow_pairwise(nums))}")
    print(
        f"faster_pairwise1(nums):\t\t"
        f"{timeit.timeit(lambda: faster_pairwise1(nums))}"
    )
    print(
        f"faster_pairwise_sorted(nums):\t"
        f"{timeit.timeit(lambda: faster_pairwise_sorted(nums))}"
    )
    print(f"heap_pairwise(nums):\t\t{timeit.timeit(lambda: heap_pairwise(nums))}")


if __name__ == "__main__":
    main(sys.argv)
