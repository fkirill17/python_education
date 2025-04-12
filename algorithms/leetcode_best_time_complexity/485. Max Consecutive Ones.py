def findMaxConsecutiveOnes(nums):
    streak = 0
    diff = 0
    for num in nums:
        if num:
            streak += 1  # Накопление streak
        else:
            diff = max(diff, streak)  # Переменная хранит в себе максимальный предыдущий streak
            streak = 0  # Обнуленние streak
    return max(diff, streak)  # Если актульный streak больше предыдущего, возвращаем его


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  # -> 3
