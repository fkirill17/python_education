"""Грокаем алгоритмы - примеры кода:"""


def sum_func(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_func(nums[1:])


print(sum_func([2, 4, 6]))


def len_func(nums):
    if not nums:
        return 0
    else:
        return 1 + len_func(nums[1:])


print(len_func([1, 2, 3]))
