def moveZeroes(nums):
    l, r = 0, len(nums)
    while l < r:
        if not nums[l]:
            r -= 1
            nums.append(nums.pop(l))
        else:
            l += 1
    return nums



print(moveZeroes([0,1,0,3,12]))  # -> [1, 3, 12, 0, 0]