def twoSum(x: list, target: int):
    dct = {}
    for idx, num in enumerate(x):
        desire = target - num
        if desire in dct:
            return [dct[desire], idx]
        dct[num] = idx


print(twoSum([2, 7, 11, 15], 9))