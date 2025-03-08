def searchInsert(nums, target):
    for idx, num in enumerate(nums):
        if num < target:
            continue
        if num == target:
            return idx
        if num > target:
            return idx
    return idx + 1





print(searchInsert([1,3,5,6], 7))