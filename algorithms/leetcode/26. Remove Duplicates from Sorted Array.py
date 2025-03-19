def removeDuplicates(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:  # Базовый случай
            nums.pop(r)  # Когда делаем удаление по индексу, индекс не переносим
        else:
            r += 1 # Когда удаления по индексу не было, двигаем индекс
            l = r
    return len(nums)


print(removeDuplicates([1,2,3,3,4,5,6]))
