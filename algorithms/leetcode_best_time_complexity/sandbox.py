def pivotIndex(nums):
    total_sum = sum(nums)
    l_sum = 0
    for idx, num in enumerate(nums):
        r_sum = total_sum - l_sum - num
        if r_sum == l_sum:
            return idx
        l_sum += num
    return -1


print(pivotIndex([1,7,3,6,5,6]))  # -> 3
