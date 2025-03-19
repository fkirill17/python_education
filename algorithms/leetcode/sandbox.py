def removeElement(nums, val):
    k = 0
    for idx, num in enumerate(nums):
        if num == val:
            nums.pop(idx)
        else:
            k += 1
    print(nums)
    return k


print(removeElement([0,1,2,2,3,0,4,2], val=2))