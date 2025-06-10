def climbStairs(n):
    if n == 1:
        return 1
    prev = 1
    act = 1
    for i in range(n - 1):
        act = act + prev
        prev = act - prev
    return act


climbStairs(10)
