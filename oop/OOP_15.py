# Полиморфизм в Python это разное поведение одного и того же метода для разных классов
# Например: 1 + 1 -> 2, '1' + '1' -> '11'
# Оператор + является синтаксическим сахаром метода __add__

class Person:
    age = 1

    def __add__(self, value):  # Переопределили метод __add__
        self.age += 1
        print('value -', value)
        return self.age


p = Person()
print(p.__dict__)  # -> {} - Словарь экземпляра пуст, идём в словарь класса
print(Person.__dict__)  # -> {..., 'age': 1, '__add__': <function..., ...} - Взяли 'age' и '__add__'
print(p + 123)  # -> value - 123 -> 2 - Результатом работы __add__ явился p.age = 2, у экземпляра теперь свой 'age' = 2
print(p.__dict__)  # -> {'age': 2} - age теперь берём тут
print(p + 'abc')  # -> value - abc -> 3 - Перезаписали age экземпляра
print(p.__dict__)  # -> {'age': 3}


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):  # Переопределили метод __add__
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong object')

    def __eq__(self, room_obj):  # Переопределили метод __eq__
        if self.area == room_obj.area:
            return True
        return False


r1 = Room(3, 5)
r2 = Room(4, 7)
print(r1.__dict__)  # -> {'x': 3, 'y': 5, 'area': 15}
print(r2.__dict__)  # -> {'x': 4, 'y': 7, 'area': 28}
print(r1.area)  # -> 15
print(r2.area)  # -> 28
print(r1 + r2)  # -> 43
print(r1 == r2)  # -> False
