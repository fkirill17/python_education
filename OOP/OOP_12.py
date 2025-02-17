class Person:
    age = 0

    def hello(self):
        print('Hello')


class Student(Person):
    pass


s = Student()
print(s.__dict__)  # -> {}
s.hello()  # -> 'Hello'

# Сначала Python ищет функцию в пространстве имен экземпляра, потом в пространстве имен дочернего класса,
# потом в пространстве имен родительского класса

# Все классы, которые мы создаём неявно наследуются от класса object

class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass


i7 = I7()
i5 = I5()

print(isinstance(i5, type(i7)))  # False так как i5 не является экземпляром класса I7
print(isinstance(i5, type(i5)))  # True так как i5 является экземпляром класса I5,

print(type(i5))  # -> <class '__main__.I5'> Ссылка на модуль, название класса
# type(i5) -> класс I5, из которого был создан экземпляр i5

print(isinstance(i5, IntelCpu))  # -> True - Является ли экземпляр i5 экземпляром класса IntelCpu?
print(isinstance(i7, IntelCpu))  # -> True - Является ли экземпляр i7 экземпляром класса IntelCpu?


class One:
    pass


class Two(One):
    pass


class Three(Two):
    pass


print(issubclass(Three, One))  # True так как Three и One лежат в одной цепочке наследований




