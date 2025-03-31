def isPalindrome(x):
    if 0 <= x < 10:
        return True
    x = str(x)
    return x == x[::-1]



print(isPalindrome(11))
