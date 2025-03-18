def removeDuplicates(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:
            nums.pop(r)
        else:
            l = r
            r += 1
    return len(nums)


print(removeDuplicates([1,1,2]))
