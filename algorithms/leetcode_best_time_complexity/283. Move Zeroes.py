def moveZeroes(nums):
    l, r = 0, len(nums)  # r - Указатель, который двигаем при перемещении элемента, используется для отсечения
    while l < r:
        if nums[l] == 0:
            nums.append(nums.pop(l))  # Перемещение элемента в конец списка
            r -= 1
        else:
            l += 1
    return nums


print(moveZeroes([0,1,0,3,12]))  # -> [1, 3, 12, 0, 0]
