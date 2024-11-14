class IntDescroptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescroptor()  # Дескриптор-1 Внутри создаётся словарь с ключем _values и при вызове __set__ делается запись
    y = IntDescroptor()  # Дескриптор-2


v1 = Vector()
v2 = Vector()

# В этих примерах мы вызываем метод __set__ для экземпляров x, y
v1.x = 1  # Обращаемся к методу дескриптора-1 set(self='Ссылка на дескриптор-1', instance='Ссылка на v1', value=1)
v1.y = 4  # Обращаемся к методу дескриптора-2 set(self='Ссылка на дескриптор-2', instance='Ссылка на v1', value=4)

v2.x = 14  # Обращаемся к методу дескриптора-1 set(self='Ссылка на дескриптор-1', instance='Ссылка на v2', value=14)
v2.y = 8  # Обращаемся к методу дескриптора-2 set(self='Ссылка на дескриптор-2', instance='Ссылка на v2', value=8)

print(v1.__dict__)  # -> {}
print(v2.__dict__)  # -> {}

# Словарь класса Vector
print(Vector.__dict__)  # -> {..., 'x': 'Ссылка на дескриптор-1', 'y': 'Ссылка на дескриптор-2', ...}

# Переходим по ключам x, y в словаре класса Vector, и видим словари самих дескрипторов
print(Vector.x.__dict__)  # -> {'_values': {'Ссылка на v1',: 1, 'Ссылка на v2': 14}}
print(Vector.y.__dict__)  # -> {'_values': {'Ссылка на y1',: 4, 'Ссылка на y2': 8}}

# В этих примерах мы вызываем метод __get__ для экземпляров x, y
print(v1.x)  # -> 1 Метод дескриптора-1 get(self='Ссылка на дескриптор-1', instance='Ссылка на v1', owner='Vector')
print(v1.y)  # -> 4 Метод дескриптора-2 get(self='Ссылка на дескриптор-2', instance='Ссылка на v1', owner='Vector')

print(v2.x)  # -> 14 Метод дескриптора-1 get(self='Ссылка на дескриптор-1', instance='Ссылка на v2', owner='Vector)
print(v2.y)  # -> 8 Метод дескриптора-2 get(self='Ссылка на дескриптор-2', instance='Ссылка на v2', owner='Vector)
