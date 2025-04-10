def romanToInt(s):
    dct = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000}
    s = list(s)
    lst = []
    lst_2 = []
    for sym in s:
        lst.append(dct[sym])
    l, r = 0, 1
    while r < len(lst):
        if lst[l] < lst[r]:
            num = lst[r] - lst[l]
            lst_2.append(num)
            l += 2
            r += 2
        else:
            lst_2.append(lst[l])
            l += 1
            r += 1
    if l < len(lst):
        lst_2.append(lst[-1])
    return sum(lst_2)


print(romanToInt("MDIX"))