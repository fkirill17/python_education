""" Нужно отличать синтаксический сахар "декоратор", от паттерна проектирования.
Декоратор не изменяет функцию, которую он декорирует"""


def div(a, b):
    return a / b


# Любую функцию в питоне можно передать в переменую

my_var = div
print(type(my_var))  # <class 'function'>
print(my_var(1, 2))  # 0.5

# Функция может быть аргументом, а так же возвращаемым значением из другой функции

"""Задача, чтобы при каждом взаимодействии с функцией div высвечивалось рекламное сообщение"""


def outer():
    def div(a, b):
        return a / b

    return div


"""Функция outer, определяет внутри себя другую функцию div и возвращает ее в виде результата собственной работы"""

var = outer()  # Передали в переменную результат вызова outer
print(type(var))  # <class 'function'>
print(var(1, 2))  # В переменной var лежит вызов функции outher, которая возвращает функцию div (в var лежит div)
# и теперь к нему можно подставить аргументы

"""Пример простого декоратора (паттерн проектиования)"""


def outer(func):
    def inner(*args, **kwargs):  # Параметры inner передаются в функцию
        print("Рекламное сообщение")  # Дополнительный функционал
        return func(*args, **kwargs)  # Декорируемая функция, принимает паркаметры из inner

    return inner


def div(a, b):
    return a / b


var = outer(div)  # В функцию outer аргументом передаётся div, и outer возвращает вместо себя inner
print(var(1, 2))  # В var лежит функция inner, в которую мы покидываем параметры

"""Пример декоратора (синтаксический сахар)"""


def outer(func):
    def inner(*args, **kwargs):  # Благодаря args, kwargs можем передавать сюда функции с разным количеством аргументов
        print("Рекламное сообщение")
        return func(*args, **kwargs)

    return inner


@outer
def div(a, b):
    return a / b


print(div(1, 2))

"""Передача параметров в декоратор"""


def second_outer(param):  # Функция для передачи параметров
    def outer(func):
        def inner(*args, **kwargs):
            print(param)
            return func(*args, **kwargs)

        return inner

    return outer


@second_outer("Рекламное сообщение")  # Декоратор вернёт вместо себя outer и код будет работать как в примере выше
def div(a, b):
    return a / b


print(div(1, 2))
