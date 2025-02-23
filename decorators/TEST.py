x = 9
assert x > 10, 'Число меньше 10'  # -> AssertionError: Число меньше 10 (Код прекращает работу)


def divide(a, b):
    assert b != 0, "Деление на ноль запрещено"
    return a / b

