def isPalindrome(x: int) -> bool:
    if x < 9:
        return True
    lst_1 = list(str(x))
    ln = len(lst_1)
    ctr = ln // 2
    if ln % 2 != 0:
        lst_1.pop(ctr)
    lst_2 = lst_1[:ctr]
    lst_1 = lst_1[ctr:]
    if lst_1 == lst_2[::-1]:
        return True
    return False


print(isPalindrome(7))
