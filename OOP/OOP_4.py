class Person:
    def hello(*args):
        return 'Hello'


print(Person.hello)  # <function Person.hello - Ссылка на функцию hello

p = Person()
print(p.hello)  # -> <bound method Person.hello(Ссылка на функцию hello)of<__main__.Person object(Cсылка на экземпляр p)

print(Person.hello())  # -> 'Hello'
# print(p.hello())  # -> TypeError: Person.hello() takes 0 positional arguments but 1 was given


# При вызове метода у экземпляра класса, первым аргументом функция получает тот экземпляр класса с которым связан метод
print(Person.hello(p))  # -> 'Hello'

print(type(p.hello))  # -> <class 'method'>
print(type(Person.hello))  # -> <class 'function'>

print(id(p.hello) == id(Person.hello))  # -> False

print(p.__dict__)  # -> {}

# Методы это специальные классы, котрые объеденяют в себе функции класса и конкретный экземпляр класса


print(p.hello.__func__)  # -> <function Person.hello - Ссылка на функцию hello
print(p.hello.__self__)  # -> <__main__.Person object - Cсылка на экземпляр класса p

print(id(dir(Person.hello)) == (dir(p.hello)))  # False - у класса и у экземпляра класса разные атрибуты


class Person:
    def hello(self):  # Функция, которая учитывает, что её будут вывызвать из экземпляра
        return self


p = Person()
print(p.hello())  # -> <__main__.Person object - Cсылка на экземпляр класса p


class Person:
    def create(self):
        self.name = 'Ivan'


p = Person()
p.create()
print(p.__dict__)  # {'name': 'Ivan'}
