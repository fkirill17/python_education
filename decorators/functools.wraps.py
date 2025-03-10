import functools


def repeat(num):
    def deco(func):
        @functools.wraps(func)  # Используем для сохранения метаданных декорируемой функции
        def wrapper(a, b):
            """Обёртка функции"""
            for i in range(0, num):
                func(a, b)
        return wrapper
    return deco


@repeat(3)
def my_func(a, b):
    """Документация"""
    p = a / b
    print("Результат деления", p)


my_func(10, 5)

# 1. Без @functools.wraps 2. С ним
print(my_func.__name__)  # -> 1. "wrapper" 2. "my_func"
print(my_func.__doc__)  # -> 1. "Обёртка функции" 2. "Документация"
