def isPalindrome(x: int) -> bool:
    if 9 > x >= 0:
        return True
    lst_1 = list(str(x))
    ln = len(lst_1)
    center = ln // 2  # Определили центральный индекс
    if ln % 2 != 0:  # Нечетный случай
        lst_1.pop(center)
    lst_2 = lst_1[:center]
    lst_1 = lst_1[center:]
    if lst_1 == lst_2[::-1]:
        return True
    return False


print(isPalindrome(12321))

