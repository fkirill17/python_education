def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:  # Цикл пока l и r не поменяются местами
        mid = (r + l) // 2  # Поиск центрального элемента
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(searchInsert([1, 3, 6], 5))
