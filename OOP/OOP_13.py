class Person:
    age = 0

    def hello(self):
        print('Hello')


class Student(Person):
    def hello(self):  # Происходит перегрузка метода
        print('Hello am student')


s = Student()
print(s.__dict__)  # -> {}
s.hello()  # -> 'Hello am student'

# Вся суть перегрузки методов в том, как Python находит атрибуты в пространстве имен
# Python не находит в экземпляре метода hello, но зато находит этот метод в классе Student и сразу выполняет его
# если бы в классе Student не было этого метода, то выполнится метод из класса Person


class Student(Person):
    def goodbye(self):  # Происходит расширение функциональности
        print('Goodbye')


s = Student()
s.hello()  # -> 'Hello'
s.goodbye()  # -> Goodbye


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello {self.name}')


class Student(Person):
    pass


s = Student('Ivan')  # Дочерний класс наследует все методы класса родителя
print(s.__dict__)  # -> {'name': 'Ivan'}
print(s.hello())  # -> 'Hello Ivan' - В self был передан тот экземпляр класса, который вызвал этот метод

# Основная идея - порядок разрешения имён. Если Python находит в дочернем классе такой же метод,
# как и в родительском - это перегрузка методов. Если в дочернем классе, находится метод, которого нет в родительском,
# это расширение функциональности
