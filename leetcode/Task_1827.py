def minOperations(nums):
    x = 0
    for idx in range(len(nums) - 1):
        while nums[idx] >= nums[idx + 1]:
            nums[idx + 1] += 1
            x += 1
    return x


print(minOperations([1,5,2,4,1]))
