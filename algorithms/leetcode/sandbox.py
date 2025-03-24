def sum_func(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_func(nums[1:])


print(sum_func([2, 4, 6]))
