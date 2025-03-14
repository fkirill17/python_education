# def climbStairs(n):
#     if n == 0:
#         return 0
#     lst = [0, 1]
#     x = 0
#     while True:
#         lst.append(lst[x + 0] + lst[x + 1])
#         x += 1
#         if x == n:
#             break
#     return lst[-1]

# Динамическое программирование
def climbStairs(n):
    if n <= 1:
        return 1
    a, b = 1, 1  # Два базовых случая
    for _ in range(n - 1):
        a, b = b, a + b  #Вычисляются все выражения справа, а потом одновременно присваиваются переменным слева.
    return b


print(climbStairs(4))
