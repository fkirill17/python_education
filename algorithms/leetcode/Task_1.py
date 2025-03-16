def twoSum(nums, target):
    ln = len(nums)
    for i in range(0, ln):
        num = nums[i]
        for x in range(0, ln):
            if i == x:
                continue
            if nums[x] + num == target:
                return [i, x]


print(twoSum([2, 7, 11, 15], 9))
