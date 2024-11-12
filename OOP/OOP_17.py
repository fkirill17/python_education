class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):  # Определять свойство name в дочернем классе не нужно, его мы унаследуем из родительского класса
    def __init__(self, name, surname):  # В __init__ метод дочернего класса нужно передать все нужные аргуметы
        super().__init__(name)  # Чтобы присвоить имя, нужно передать управление в __init__ родителя
        self.surname = surname


s = Student('John', 'Smith')
print(s.__dict__)  # -> {'name': 'John', 'surname': 'Smith'}

# 1. Хоть мы и вызываем метод родительского класса, он все равно остаётся связанным с объектом дочернего класса
# 2. Функция super() ищет определение метода вверх по дереву наследоввания, а не только в родительском классе
# 3. Порядок в котором мы вызываем super() имеет значение


class Person:
    def hello(self):
        print(f'Bound with -> {self}')


class Student(Person):
    def hello(self):
        print(f'Student_obj.hello() is called')
        super().hello()


s = Student()
s.hello()  # -> 'Student_obj.hello() is called' -> Bound with -> <__main__.Student object at 0x1e96922cec0>
print(hex(id(s)))  # -> 0x1e96922cec0

# Родительский метод связан с экземпляром класса и в аргумент self принимает словарь экземпляра, из которого был вызван
