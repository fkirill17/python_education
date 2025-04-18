def sortedSquares(nums):
    sort_lst = []
    l, r = 0, len(nums) - 1
    while l < r:
        if abs(nums[l]) > abs(nums[r]):
            sort_lst.append(nums[l] ** 2)
            l += 1
        else:
            sort_lst.append(nums[r] ** 2)
            r -= 1
    return sort_lst[::-1]


print(sortedSquares([-4,-1,0,3,10]))  # Задача основана том, что модули чисел по бокам встрого выше, чем в центре