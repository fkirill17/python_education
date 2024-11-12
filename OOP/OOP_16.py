# Любой алгоритм хэширования преобразует строку неопределенной длины в строку определенной длины

import hashlib

print(hashlib.md5('Kirill'.encode('utf-8')).hexdigest())  # ->  'e7c0b37a667cc5a8b904fb25558c7448'
print(hashlib.md5('Kirill '.encode('utf-8')).hexdigest())  # -> '57be4cc03e85b64230d45bdac0fd008a'
# Строки разной длины были преобразованы в хэш одинаковой длины

# Идентификация объекта словаря идет по хэшу ключа, поэтому ключи в словаре должны быть хэшируемыми объектами
# и не должны изменяться во время исполнения программы

# Объект является хэшируемым если у него есть метод __hash__ и метод __eq__


class Person:
    def __init__(self, name):
        self._name = name

    @property  # Свойство _name только для чтенеия. В процессе работы программы это свойство не будет меняется
    def name(self):
        return self._name

    def __hash__(self):  # Переопределили метод __hash__
        return hash(self._name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self._name == person_obj._name


p1 = Person('Ivan')
p2 = Person('Ivan')
p3 = Person('Oleg')
print(p1 == p2)  # -> True
print(p1 == p3)  # -> False
print(hash(p1))  # -> '3738245507588158695' Одинаковые хэши
print(hash(p2))  # -> '3738245507588158695' Одинаковые хэши

d = {p1: 'Ivanoff Ivan'}
print(d.get(p1))  # -> 'Ivanoff Ivan' Благодаря переопределению __hash__ и __eq__
# есть возможность использовать экземпляр как ключ в словаре

