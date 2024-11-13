from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


c = MyTime()
print(c.epoch)  # -> 1731512168
# self: <__main__.Epoch object at 0x000001D6DD3CC770>       - Дескриптор
# instance: <__main__.MyTime object at 0x000001D6DD3CC7A0>  - Объект из которого обратились к дескриптору
# owner: <class '__main__.MyTime'>                          - Класс MyTime, экземпляром которого является instance

print(MyTime.epoch)  # -> 1731512168
# self: <__main__.Epoch object at 0x000002ABC3EDC800>       - Дескриптор
# instance: None                                            - Объект из которого обратились к дескриптору
# owner: <class '__main__.MyTime'>                          - Класс MyTime, экземпляром которого является instance


# Такое поведение позволяет возвращать разные значения в зависимости от того откуда было вызвано свойство epoch
# Если есть instance это один вариант, если нет instance это второй вариант

# Мы можем возвращать значения свойств если обращение идет из экземпляра
# и возвращать сам экземпляр дескриптора если обращение произошло через класс. Такое поведение реализует @property


class Epoch:
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return int(time())


class MyTime:
    epoch = Epoch()


c = MyTime()
print(c.epoch)  # -> 1731512100
print(MyTime.epoch)  # -> <__main__.Epoch object at 0x000001A3983BCE00>
