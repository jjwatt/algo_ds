"""Scratch."""
import heapq
from sys import maxsize

def has_duplicate_set(nums: list[int]) -> bool:
    seen = set()
    for i in nums:
        if nums in seen:
            return True
        seen.add(i)
    return False

def has_duplicate_dict(nums: list[int]) -> bool:
    nums_freq = {}
    for i in nums:
        if i in nums_freq:
            nums_freq[i] += 1
        else:
            nums_freq[i] = 1
    for i in nums_freq.values():
        if i > 1:
            return True
    return False

def max_subarray_sum(a: list[int]):
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def two_sum(nums: list[int], target: int):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

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
    del nums[write_index:]
    return write_index


def group_anagrams(strs: list[str]) -> list[str]:
    anagrams = {}
    for s in strs:
        ss = str(sorted(s))
        if ss in anagrams:
            anagrams[ss].append(s)
        else:
            anagrams[ss] = [s]
    anagrams_list = []
    for k, v in anagrams.items():
        anagrams_list.append(v)
    return anagrams_list

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()
    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)
    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


def top_k_frequent_bucket_sort(
    nums: list[int], k: int
) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(f"Max sum: {max_subarray_sum(lst)}")

    string = "radar"
    print(f"{string=} is_palindrome: {is_palindrome(string)}")

    lst = [1, 2, 2, 3, 3, 3]
    k = 2
    res = top_k_frequent_bucket_sort(lst, k)
    print(f"{res=}")
