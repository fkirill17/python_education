def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    idx1 = 0
    idx2 = 0
    lst = []
    while idx1 < len(nums1) and idx2 < len(nums2):
        if nums1[idx1] > nums2[idx2]:
            idx2 += 1
        elif nums1[idx1] < nums2[idx2]:
            idx1 += 1
        else:
            lst.append(nums1[idx1])
            idx1 += 1
            idx2 += 1
    return lst


print(intersect([2, 2], [1, 2, 2, 1]))  # -> [2, 2]
