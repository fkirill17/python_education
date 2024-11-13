from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


c = MyTime()
print(c.epoch)  # -> 1731512168
# self: <__main__.Epoch object at ...>              - Дескриптор
# instance: <__main__.MyTime object at ...>         - Объект из которого обратились к дескриптору
# owner: <class '__main__.MyTime'>                  - Класс MyTime, экземпляром которого является instance

print(MyTime.epoch)  # -> 1731512168
# self: <__main__.Epoch object at ...>              - Дескриптор
# instance: None                                    -
# owner: <class '__main__.MyTime'>                  - Класс MyTime, экземпляром которого является instance

# Мы можем возвращать значения свойств если обращение идет из экземпляра
# и возвращать сам дескриптор, если обращение произошло через класс. Например, такое реализовано в @property


class Epoch:
    def __get__(self, instance, owner_class):
        if instance is None:  # Если вызов произошел из класса
            return self
        return int(time())  # Если вызов проищошел из экземпляра класса


class MyTime:
    epoch = Epoch()


c = MyTime()
print(c.epoch)  # -> 1731512100
print(MyTime.epoch)  # -> <__main__.Epoch object at 0x000001A3983BCE00>
