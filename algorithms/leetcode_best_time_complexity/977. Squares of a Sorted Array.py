def sortedSquares(nums):
    l, r = 0, len(nums) - 1
    lst = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):  # Внимание
            lst.append(nums[l] ** 2)
            l += 1
        else:
            lst.append(nums[r] ** 2)
            r -= 1
    lst.reverse()
    return lst


print(sortedSquares([-4,-1,0,3,10]))  # Задача основана том, что модули чисел по бокам встрого выше, чем в центре
