def strStr(haystack, needle):
    if needle > haystack:
        return -1
    lst_1 = list(haystack)
    lst_2 = list(needle)
    ln_lst1 = len(lst_1) + 1
    ln_lst2 = len(lst_2)
    for idx in range(0, ln_lst1-ln_lst2):
        a = lst_1[idx:idx + ln_lst2]
        if a == lst_2:
            return idx
    return -1




print(strStr("abc", "c"))

