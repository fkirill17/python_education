def climbStairs(n):
    if n == 0:
        return 0
    lst = [0, 1]
    x = 0
    while True:
        lst.append(lst[x + 0] + lst[x + 1])
        x += 1
        if x == n:
            break
    return lst[-1]


print(climbStairs(4))


