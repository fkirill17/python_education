def minCostToMoveChips(position):
    even = 0
    odd = 0
    for i in position:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)


print(minCostToMoveChips([2,2,2,3,3]))  # -> 2
