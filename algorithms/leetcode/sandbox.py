def removeDuplicates(nums):
    l, r = 0, 1
    k = 0
    while r < len(nums):
        if nums[l] == nums[r]:
            nums.pop(r)
            nums.append(0)
        else:
            k += 1
            l = r
            r += 1
    return len(nums)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))