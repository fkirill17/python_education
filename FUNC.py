def func_1(*args: int, **kwargs: str) -> None:
    print(args)  # -> (1, 2, 3, 4)
    print(kwargs)  # -> {'name': 'John'}
    return None
    # Аннотации для (*args: int) - Лист интов
    # *args - это ПОЗИЦИОННЫЕ аргументы
    # В первую очередь передаём ПОЗИЦИНОННЫЙ аргумент, затем КЛЮЧЕВОЙ аргумент
    # Аннотации для (**kwargs: int) - словарь со значениями int
    # В **kwargs КЛЮЧИ всегда str и это КЛЮЧЕВЫЕ аргументы
    # В аннотациях может быть указано несколько типов через | (x: int | float)

lst = (1, 2, 3, 4)
dct = {'name': 'John'}

func_1(1, 2, 3, 4, name='John')  # Передача произвольного количества ПОЗИЦИОННЫХ и КЛЮЧЕВЫХ аргументов
func_1(*lst, **dct)  # Распаковка list, dict в ПОЗИЦИОННЫЕ и КЛЮЧЕВЫЕ аргументы


def func_2(x: int, y: int = 3) -> None:
    print(x, y)
    # Сначала в функцию передаются ОБЯЗАТЕЛЬНЫЕ аргументы - x, затем НЕОБЯЗАТЕЛЬНЫЕ - y с default значением через =

func_2(1)  # -> 1 3
func_2(x=1, y=4)  # -> 1 4
# ПОЗИЦИОННЫЕ аргументы можно передавать как КЛЮЧЕВЫЕ


def func_3(age: int, name: str, /) -> None:
    pass
    # Аргументы ДО / ТОЛЬКО ПОЗИЦИОННЫЕ
    # Аргументы ПОСЛЕ / ПОЗИЦИОННЫЕ и КЛЮЧЕВЫЕ

func_3(23, name='Alice')  # -> TypeError: func_3() got some positional-only arguments passed as keyword arguments: 'name'
func_3(23, 'Alice')  # -> Передача ПОЗИЦИОННЫХ аргументов


def func_4(*, age: int, name: str) -> None:
    pass
    # Аргументы ДО * ПОЗИЦИОННЫЕ и КЛЮЧЕВЫЕ
    # Аргументы ПОСЛЕ * ТОЛЬКО как КЛЮЧЕВЫЕ

func_4(23, name='Alice')  # -> TypeError: func_4() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
func_4(age=23, name='Alice')  # -> Передача КЛЮЧЕВЫХ аргументов


def func_5(id: int, *, age: int, name: str):
