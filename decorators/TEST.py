def outher(func):
    def inner(*args, **kwargs):
        print("Тестовое сообщение")
        return func(*args, **kwargs)

    return inner


@outher
def div(a, b):
    return a * b


print(div(6, 5))
