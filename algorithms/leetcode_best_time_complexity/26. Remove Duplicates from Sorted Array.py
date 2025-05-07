def removeDuplicates(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            r += 1
        else:
            nums.pop(r)
    return len(nums)


print(removeDuplicates([1,2,3,3,4,5,6]))
