def func(n):
    while n // 3 == 0:
        n = n / 3
        if n == 1:
            return True

    return False

print(func(27))