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
