# class Person:
#     def __init__(self, name, surname):
#         self._name = name  # свойство _name должно быть строкой
#         self._surname = surname  # свойство _surname должно быть строкой
#         self._fullname = None
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#         self._fullname = None  # Когда вызываем сеттер - обнуляем кэш
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#         self._fullname = None  # Когда вызываем сеттер - обнуляем кэш


# class StringD:
#     def __init__(self, value=0):
#         self._value = None
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self._value = value
#
#     def get(self):
#         return self._value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#
# p = Person('John', 'S')
#
# print(p.name.get())
# print(p.surname.get())

from time import time
from random import choice


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


# 2 аргумент, это экземпляр класса из которого происходит обращение к свойству
# 3 аргумент, это класс собственник


class MyTime:
    epoch = Epoch()


m = MyTime()
print(m.epoch)  # -> 1731506533


class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, instance, owner):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rps = Choice('Rock', 'Paper', 'Scissor')


g = Game()

print(g.dice)  # -> 2
print(g.flip)  # -> 'Tails'
print(g.rps)  # -> 'Scissor'
