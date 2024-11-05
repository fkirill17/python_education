def second_outer(*aaa):  # Функция для передачи параметров
    def outer(func):
        def inner(*args, **kwargs):
            a = aaa[0]
            while a:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print("Ошибка", err)
                    a -= 1

        return inner
    return outer


@second_outer(5)  # Декоратор вернёт вместо себя outer и код будет работать как в примере выше
def div(a, b):
    return a / b


print(div(1, 0))
