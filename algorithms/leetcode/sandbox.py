def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    while r >= l:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(searchInsert([1, 3, 6], 7))
