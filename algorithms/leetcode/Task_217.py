def containsDuplicate(nums):
    hash_table = set(nums)  # В set лежат всегда уникальные значения
    return len(nums) != len(hash_table)


print(containsDuplicate([1, 2, 3, 0]))
