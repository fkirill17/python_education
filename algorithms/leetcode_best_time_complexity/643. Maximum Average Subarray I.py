def findMaxAverage(nums, k):
    summ = 0
    for i in nums[0:k]:  # Первоначальное вычисление суммы элементов, далее на его основе реализуем скользящее окно
        summ += i
    out = summ
    l, r = 0, k
    while r < len(nums):
        summ = summ + nums[r] - nums[l]  # Ключевая формула скользящего окна
        if out < summ:  # Накопление максимума в summ
            out = summ
        l += 1
        r += 1
    return out / k


print(findMaxAverage([1,12,-5,-6,50,3], 4))  # -> 12.75
