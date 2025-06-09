def findMaxAverage(nums, k):
    l, r = 0, k
    total_sum = sum(nums[:k])  # Первоначальное вычисление суммы элементов, далее на его основе реализуем скользящее окно
    max_sum = total_sum
    while r < len(nums):
        actual_sum = total_sum - nums[l] + nums[r]  # Ключевая формула скользящего окна (Sliding Window)
        if actual_sum > max_sum:  # Накопление максимума
            max_sum = actual_sum
        r += 1
        l += 1
    return max_sum / k


print(findMaxAverage([1,12,-5,-6,50,3], 4))  # -> 12.75
