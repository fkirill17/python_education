from time import time
from random import choice


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


# Аргумент instance - экземпляр класса, из которого обратились к __get__
# Аргумент owner_class - класс из которого был создан экземпляр instance


class MyTime:
    epoch = Epoch()


m = MyTime()
print(m.epoch)  # -> 1731506533


class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, instance, owner_class):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rps = Choice('Rock', 'Paper', 'Scissor')



g = Game()


print(g.dice)  # -> 2
print(g.flip)  # -> 'Tails'
print(g.rps)  # -> 'Scissor'
