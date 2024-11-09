def second_outer(*aaa):
    print("second_outer")

    def outer(func):  # Передали функцию div
        print("outer")

        def inner(*args, **kwargs):
            a = aaa[0]
            while a:
                try:
                    print("second_outer")
                    return func(*args, **kwargs)
                except Exception as err:
                    print("Ошибка", err)
                    a -= 1
            return 'test_2'

        return inner

    return outer


def simple_deco(func):  # Передали inner
    print("simple_deco")

    def inner_2(*args, **kwargs):
        print("simple_deco_2")
        return func(*args, **kwargs)

    return inner_2


@simple_deco  # -> inner_2
@second_outer(5)  # -> outer(div) -> inner
def div(a, b):
    return a / b


print(div(5, 0))
