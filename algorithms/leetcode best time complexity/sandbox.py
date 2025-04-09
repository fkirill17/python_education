def isPalindrome(x):
    if 10 > x > 0:
        return True
    st = str(x)
    return st == st[::-1]


print(isPalindrome(1))