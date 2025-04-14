def findMaxAverage(nums, k):
    if len(nums) == k:
        return float(sum(nums)) / k
    out = -10001
    summ = sum(nums[0:k])
    l, r = 0, k
    while r < len(nums):
        summ = (summ + nums[r] - nums[l])
        cur = float(summ) / 4
        out = max(cur, out)
        l += 1
        r += 1
    return out


print(findMaxAverage([3,3,4,3,0], 3 ))