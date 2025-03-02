def minOperations(nums):
    x = 0
    for idx in range(len(nums) - 1):
        if nums[idx] >= nums[idx + 1]:
            diff = nums[idx] - nums[idx + 1] + 1
            nums[idx + 1] += diff
            x += diff
    return x


print(minOperations([1,5,2,4,1]))
