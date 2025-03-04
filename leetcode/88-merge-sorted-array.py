def merge(nums1, m,
          nums2, n) -> None:
    if n == 0:
        return
    end_idx = len(nums1) - 1
    while n > 0 and m > 0:
        if nums2[n-1] >= nums1[m-1]:
            nums1[end_idx] = nums2[n-1]
            n -= 1
        else:
            nums1[end_idx] = nums1[m-1]
            m -= 1
        end_idx -= 1
    while n > 0:
        nums1[end_idx] = nums2[n-1]
        n -= 1
        end_idx -= 1


def merge_gemini(nums1, m, nums2, n):
    """Gemini's version of merge arrays.

    Mostly the same as above, but maybe a little clearer
    """
    # Initialize 3 pointers:
    # - p1: Points to the last actual element in nums1 (index m-1)
    # - p2: Points to the last element in nums2 (index n-1)
    # - write_index: Points to the last position in nums1
    #   where we'll write the merged element (index m+n-1)
    p1 = m - 1
    p2 = n - 1
    write_index = m + n - 1

    # Iterate while there are elements in both arrays.
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            # if nums[p1] is larger, put it in write_index and decrement p1
            nums1[write_index] = nums1[p1]
            p1 -= p1
        else:
            # if numx[p2] is larger or equal, put it in write_index and decrement p2
            nums1[write_index] = nums2[p2]
            p2 -= 1
        # Always decrement write_index
        write_index -= 1

    # If there are remaining elements in nums2 (p2 >= 0), copy them to nums1
    # (handles the case where nums2 has larger elements than all of nums1)
    while p2 >= 0:
        nums1[write_index] = nums2[p2]
        p2 -= 1
        write_index -= 1
