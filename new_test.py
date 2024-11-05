# def removeElement(nums, val):
#     for idx, i in enumerate(nums):
#         if i == val:
#             a = nums.pop(idx)
#             nums.append(a)
#     for idx, i in enumerate(nums):
#         if i == val:
#             a = nums.pop(idx)
#             nums.append(a)
#     return nums
#
# print(removeElement(nums = [3, 2, 2, 2, 3], val = 2))


# def removeElement(nums, val):
#     for idx, i in enumerate(nums):
#         if len(nums) == 1:
#             return nums
#         if i == val:
#             a = nums.pop(idx)
#             nums.append(a)
#         if nums[idx - 1] == val:
#             a = nums.pop(idx - 1)
#             nums.append(a)
#     x = 0
#     for idx, i in enumerate(nums):
#         if i == val:
#             x = idx
#             break
#
#     return x, nums

# def removeElement(nums, val):
#     lenght = len(nums) - 1
#     for idx, i in enumerate(nums):
#         if nums[lenght] == val:
#             lenght -= 1
#         if nums[idx] == val:
#             nums[lenght], nums[idx] = nums[idx], nums[lenght]
#             lenght -= 1
#         if nums[idx-1] == val:
#             nums[lenght], nums[idx-1] = nums[idx-1], nums[lenght]
#             lenght -= 1
#     return nums


def removeElement(nums, val):
    k = 0
    for idx, i in enumerate(nums):
        if i != val:
            nums[idx], nums[k] = nums[k], nums[idx]
            k += 1
    return nums


print(removeElement(nums = [0,1,2,2,3,0,4,2,3], val = 2))