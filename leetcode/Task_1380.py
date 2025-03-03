def luckyNumbers(matrix):
    lst = []
    for arr in matrix:
        lst.append(min(arr))
    l = len(lst) - 1
    while l > 0:
        if lst[l] < lst[l - 1]:
            lst.pop()
        else:
            lst.pop(l - 1)
        l -= 1
    return lst


matrix = [[7,8],[1,2]]

print(luckyNumbers(matrix))