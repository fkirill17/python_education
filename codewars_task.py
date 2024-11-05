# Вы придумали дизайн структуры данных, которая представляет алгебраический тип данных как пару элементов:

# class Cons:
#     def __init__(self, head, tail):
#         self.head = head
#         self.tail = tail
#
#     # Используя этот новый тип данных, мы можем легко построить список элементов. Например, список чисел:
#     #
#     # numbers = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, None)))))
#     #
#     # Каждая cons-ячейка содержит «значение» в своей голове, а в хвосте она содержит либо другую cons-ячейку,
#     # либо null. Мы знаем, что достигли конца структуры данных, когда хвост равен null
#     #
#     # Метод преобразования списка элементов вашего типа данных list в массив JS:
#
#     def to_array(self):
#         tail = self.tail
#         new_tail = (tail.to_array() if tail is not None else [])
#         return [self.head] + new_tail


# numbers = Cons(1, Cons(2, None))
#
# print(numbers.to_array())  # yields [1,2,3,4,5]


# Попросили добавить функционал в новый тип данных, добавить такие функции, как filter, map, reduce
#
# Итак, теперь вам нужно добавить:
# filter: создать новый алгебраический список, содержащий только те элементы, которые удовлетворяют предикатной функции.
# map: создать новый список, в котором каждый элемент является результатом применения функции, переданной аргументом.
# fromArray: дополнительный метод, который создает список из массива JS
#
# Для этого Kata определение Cons и прототипный/классовый метод toArray, to_array, into_vec уже загружены в вашу среду.
#
# Примеры использования:
#
# numbers = Cons.from_array([1, 2, 3, 4, 5])
# numbers.filter(lambda x: x % 2 == 0).to_array()  # yields [2,4]
# numbers.map(lambda x: x * x).to_array()  # yields [1,4,9,16,25]
#
# digits = Cons.from_array(["1", "2", "3", "4", "5"])
# integers = digits.map(int) \
#     .filter(lambda n: n > 3) \
#     .to_array()  # yields [4,5]


# Другими словами:
#
# Статический метод Cons.fromArray (или from_array, from_iter) создает Cons(1, Cons(2, Cons(3, Cons 4, Cons 5, null)))).
# Вышеуказанный фильтр создает новый список: Cons(2, Cons(4, null)).
# Также делает и вышеприведенная карта: Cons(1, Cos(4, Cons(9, Cons(16, Cons(25, null)))))

# 1. Создаю метод from_array, на вход которого принимается массив [1, 2, 3, 4, 5] ->
# Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, None)))))
#
# Для начала думаю разобрать на дебаггере функцию to_array
# Функция to_array основана на рекурсии


class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        # TODO: convert a Python list to an algebraic list.
        pass

    def filter(self, fn):
        # TODO: construct new algebraic list containing only elements
        #      that satisfy the predicate.
        pass

    def map(self, fn):
        # TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
        pass
