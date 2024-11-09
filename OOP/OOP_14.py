class Person:
    def hello(self):
        print('I am Person')


class Student(Person):
    def hello(self):
        print('I am Student')


class Proffesor(Person):
    def hello(self):
        print('I am Proffesor')


class Someone(Student, Proffesor):
    pass


s = Someone()
s.hello()  # -> 'I am Student'


class Someone(Proffesor, Student):
    pass


s = Someone()
s.hello()  # -> 'I am Proffesor'

# Порядок, наследования при множественном наследовании имеет значение

print(s.__class__.mro())  # -> [<class '__main__.Someone'>, <class '__main__.Proffesor'>, <class '__main__.Student'>,
# <class '__main__.Person'>, <class 'object'>]

# Использование миксинов:

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            print('Food should be set')
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('I am Person')


class Student(FoodMixin, Person):
    food = 'Cheburek'

    def hello(self):
        print('I am Student')


s = Student()
s.get_food()  # -> 'I like Cheburek'
s.hello()  # -> 'I am Student'

# Миксин используем когда фичу нужно подмешать большому количеству не связанных родственными узами классов
# Любимую еду подмешиваем любым не связанным между собой классам
