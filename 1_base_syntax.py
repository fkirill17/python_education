"""
Базовый синтаксис
"""
# Докстринг

from typing import Callable  # Простой импорт

# TODO основные типы и структуры
types = [
    ...,  # Элипсис
    None,  # Ничто
    True, False, bool,  # Истина, Ложь, Булевы тип
    1, int,  # Целые числа
    1.1, float,  # Числа с плавающей точкой
    ' ', " ", str,  # Разные типы кавычек для включения их внутрь строки - print("'Hello World'") -> 'Hello World'
    """ """, str,  # Тройные кавычки для докстринга, многострочных строк, для комментариев
    f'',  # Добавляет переменные в строку - print(f'name {переменная}')
    r'', str,  # Позволяет игнорировать управляющие символы строк такие как \n и \t, используется в регулярках и path
    b'', bytes,  # Байтовая строка, Байт
    [], list,  # Список
    (), tuple,  # Кортеж
    {1, }, set,  # Множество неизменяемых объектов (Hash table)
    {1: "A"}, dict  # Словарь - КЛЮЧ неизменяемый тип данных (Hash table): ЗНАЧЕНИЕ любой тип данных
]

# TODO Основные операторы
_ = 1 + 2  # Сложение
_ = 1 - 2  # Вычитание
_ = 1 * 2  # Умножение
_ = 1 ** 2  # Возведение в степень
_ = 1 / 2  # Деление
_ = 1 // 2  # Целочисленное деление (10 // 3 = 3)
_ = 1 % 2  # Остаток от деления (10 % 3 = 1)
_ = 1 and 2  # Логический оператор И (Возвращает False если хотя-бы одно условие False)
_ = 1 or 2  # Логический оператор ИЛИ (Возвращает True если хотя-бы одно условие True)
_ = 1 > 2 | 1 >= 2 | 1 < 2 | 1 <= 2  # 1 больше 2 или 1 больше или равно 2 или 1 меньше 2 или 1 меньше или равно 2

# TODO Цикл for
for _ in types:  # Цикл ДЛЯ _ из types
    continue  # Досрочно переходит к следующей итерации

for _ in types:  # Цикл ДЛЯ _ из types
    break  # Досрочно завершает цикл
else:  # Необязательная инструкция, выполняемая после ШТАТНОГО завершения цикла (Когда цикл не был прерван через break)
    pass  # Инструкция которая НИЧЕГО не делает

# TODO Comprehensions
a = [i for i in types]  # Простое формирование списка
b = (i for i in types)  # ??? Создастся генератор
f = tuple(i for i in types)  # Формирование кортежа
c = {i for i in types if ...}  # Формирование множества с условием - "фильтром" if
g = {i if ... else b for i in types}  # Формирование множества с ветвлением (Если условие ИСТИНО добавляем i ИНАЧЕ b)
h = {i if ... else b for i in types if ...}  # "Фильтр" и ветвление (Сначала идёт фильтр, потом ветвление)
d = {str(i): i for i in types}  # Формирование словаря с преобразованием ключа в строку

# TODO цикл while
while a:  # Цикл пока а
    a.pop()  # Метод pop без аргумента удаляет последний элемент из списка

while a:  # Цикл пока а
    break  # Выход из цикла
else:  # Необязательная инструкция, выполняемая после ШТАТНОГО завершения цикла (Когда цикл не был прерван через break)
    pass  # Инструкция которая НИЧЕГО не делает


# TODO Присвоение, распаковка
def example_1():
    # При присвоении * позволяет собирать несколько значений в переменную:
    a, *b = [1, 2, 3, 4, 5]
    print(a)  # -> 1
    print(b)  # -> [2, 3, 4, 5]
    # Собираем центральные элементы
    a, *b, c = [10, 20, 30, 40, 50]
    print(a)  # 10
    print(b)  # [20, 30, 40]
    print(c)  # 50


def example_2():
    # При распаковке * достаёт значения из коллекции:
    a = [1, 2, 3]
    b = [4, 5, 6]
    merged = [*a, *b]
    print(merged)  # -> [1, 2, 3, 4, 5, 6]


def example_3():
    # Формирование списков, словарей, кортежей через переменные:
    a = 1
    b = 2
    c = 3
    d = 4
    list = [a, b, c, d]
    dict = {a: b, c: d}


def example_4():
    # Распаковка словарей с **
    def greet(name, age):
        print(f"Привет, {name}! Тебе {age} лет.")

    person = {"name": "Алиса", "age": 25}
    greet(**person)  # !!!


# TODO Срезы - Slice
my_list = [1, 2, 3][:]  # -> [1, 2, 3] - Копирование списка
my_list = [1, 2, 3][0:2]  # -> [1, 2] - Нарезка диапазона элементов (В срезах всегда используется полуоткрытый интервал)
my_list = [1, 2, 3][0:3:2]  # -> [1, 3] - Нарезка диапазона элементов с шагом 2 элемента
my_list = [1, 2, 3][::-1]  # -> [3, 2, 1] - Разворот списка
_ = {**{}}  # Распаковка словаря внутри другого словаря

# TODO Утверждение assert
x = 9
assert x > 10, 'Число меньше 10'  # -> AssertionError: Число меньше 10 (Код прекращает работу)
# Происходит проверка условия, если условие False, происходит ошибка AssertionError

"""При запуске Python с флагом -O (optimization) все assert будут игнорироваться:
Поэтому assert не должен использоваться для обработки ошибок в реальном коде — только для отладки!"""


def divide(a, b):
    assert b != 0, "Деление на ноль запрещено"
    return a / b


def func(text: str, space: str, action: Callable) -> None:
    if not text:
        return  # Оператор возврата
    """В передаче аргументов - : str это аннотации типов        
        Несколько типов в аннотации - : int | str 
        Аннотация list, tuple - list[int], tuple[any]
        Аннотация словаря dict[int, str]
        
        Когда аннотируем *args, то указываем тип данных, которые лежат внутри - *args: int
        Когда аннотируем **kwargs, то указываем тип данных, которые лежат в значениях - **kwargs: str
        
        После -> указывается тип данных, который возвращает функция"""

    print(space + action(text))  # ???
    func(text[1:], space + ' ', action)  # ???
    print(space + action(text))  # ???


# lambda функции
func('*', '', lambda text: ' '.join(i for i in text))


def func_2(*args, **kwargs): """*args - передача произвольного количества ПОЗИЦИОННЫХ аргуметнтов в функцию внутри tuple - func_2(1, 2, 3)
**kwargs - передача произвольного количества КЛЮЧЕВЫХ аргументов в функцию внутри dict - func_2(name="John", age=30)

!!! kwargs - словарь КЛЮЧ которого ВСЕГДА str

!!! Сначала передаём ПОЗИЦИОННЫЕ, затем КЛЮЧЕВЫЕ аргументы. Чтобы мы не могли поставить ключевой аргумент на место
позиционного аргумента, и не возникло путаницы"""


def func_3(myint: int, myint_2: int = 1): """

!!! Сначала в функцию передаются ОБЯЗАТЕЛЬНЫЕ аргументы БЕЗ default значения
Затем передаются НЕОБЯЗАТЕЛЬНЫЕ аргументы С default значением. Чтобы не возникло путаницы."""


def func_4(age: int, name: str, /): """

Все аргументы до / передаются ТОЛЬКО как ПОЗИЦИОННЫЕ - func_4(1, "John")
Если вызов будет - func_4(1, name = 'John') произойдет ошибка"""


def func_5(age: int, *, name: str): """

Все аргументы после * передаются ТОЛЬКО как КЛЮЧЕВЫЕ - func_5(1, name="John")
Если вызов будет - func_5(1, "John") произойдет ошибка"""


# TODO Декораторы
def decorator(multiplier: int):  # Приём ПАРАМЕТРОВ ДЕКОРАТОРА (5)
    def dec(func: typing.Callable):  # Приём ДЕКОРИРУЕМУОЙ ФУНКЦИИ f
        # Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:  # Обработка параметра декоратора
            multiplier += 1

        def wrap(*args, **kwargs):  # Приём АРГУМЕНТОВ декорируемой функции (2)
            for _ in range(multiplier):  # Цикл на основе диапазона, который формирует параметр декоратора
                # Генераторы (Видим yield - Значит это функция генератор)
                yield func(*args, **kwargs)  # В каждой итерации генерируем вызов функции f(2)

        return wrap

    return dec


@decorator(5)  # Синтексический сахар - декоратор с параметром, возвращает после себя функцию dec
def f(num: int) -> int:
    return num


deco = f(2)  # Вызов декорируемой функции и присвоение результата работы в переменную
# Результатом работы является генератор, который вызывает f(2), который был сформирован в цикле внутри wrap
#
# Итерация по генератору
for i in lst:
    print(i)  # 2 2 2 2 2

qwe = [*f(1)]  # ???

# TODO Условия
if i := d.get(''):  # Выражение в условии преобразуется в булевы тип -> bool(i := d.get(''))
    pass
elif not (q := d.get(1)):  # Дополнительное условие, выполняется если if False (Необязательный блок)
    # not - логическая инверсия
    pass
elif ...:  # Выполняется если предыдущий elif False (Количество блоков elif неограниченно)
    pass
else:  # Выполняется если все предыдущие условия False (Необязательный блок)
    pass

"""Оператор := полезен в ситуациях, когда вы хотите одновременно вычислить значение и использовать его сразу в выражении
без необходимости предварительного присваивания переменной.
!!! В списковых включениях его можно использовать только в условиях, но не в цикле"""

# match qwe:
#     case "1":
#         pass
#     case _:
#         pass


# TODO Исключения и их обработка
try:  # Код, который может вызвать исключение
    if ...:  # Условие для возбуждения ошибки
        raise ZeroDivisionError()  # Явное возбуждение ошибки, сразу перемещаемся в блок except ZeroDivisionError
except ZeroDivisionError as e:  # Отлавливаем ошибку, допускается несколько блоков except подряд
    pass
else:  # Код, который выполняется, если в блоке try не возникло ошибки (Необязательный блок)
    pass
finally:  # Код, который выполняется в любом случае (Необязательный блок)
    pass


# Можно создавать пользовательские ошибки: class MyCustomError(Exception)


# TODO Классы
class A:
    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def main(self) -> None:
        ...

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        super().main()
        print(self.test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'
