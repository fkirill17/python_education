def merge(nums1, m, nums2, n):
    idx = 0
    while idx < len(nums2):
        nums1[m] = nums2[idx]
        idx += 1
        m += 1
        nums1.sort()
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))