def removeElement(nums, val):
    k = 0  # Количество уникальных элементов
    idx = 0
    while idx < len(nums):
        if nums[idx] == val:
            nums.pop(idx)  # Когда делаем удаление по индексу, индекс не переносим
        else:
            idx += 1  # Когда удаления по индексу не было, двигаем индекс
            k += 1
    return k


print(removeElement([1, 2, 2, 1], val=1))
