def mySqrt(x):
    n = x
    while n ** 2 > x:
        n = n // 2
        if n ** 2 == x:
            return n
    while n <= x:
        n = n + 1
        if n ** 2 > x:
            return n - 1


print(mySqrt(2))
