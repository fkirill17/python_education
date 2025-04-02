import functools


def repeat(num):
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            for i in range(num):
                print(i)
                func(*args, **kwargs)
        return inner
    return outer


@repeat(3)
def my_func(a, b):
    """my_func"""
    print("Результат деления", a / b)


my_func(10, 2)

print(my_func.__doc__)
