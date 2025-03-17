def twoSum(nums, target):
    known_numbers = {}
    for idx, num in enumerate(nums):
        desire = target - num
        if desire in known_numbers:
            return [known_numbers[desire], idx]
        known_numbers[num] = idx


print(twoSum([2, 7, 11, 15], 9))
