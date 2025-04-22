def findMaxAverage(nums, k):
    l, r = 0, k
    first_sum = sum(nums[l:k])
    max_sum = 0
    while r < len(nums):
        curr_sum = first_sum + nums[r] - nums[l]
        max_sum = max(curr_sum, max_sum)
        l += 1
        r += 1
    return max_sum / k


print(findMaxAverage([1,12,-5,-6,50,3], 4))  # -> 12.75