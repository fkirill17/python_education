import weakref
from weakref import WeakKeyDictionary

a = 123
b = a

print(id(a) == id(b))  # -> True
del a
print(b)  # -> 123

# Примеры работы сильных ссылок


class Person:
    pass


p = Person()

w = weakref.ref(p)
print(w)  # -> <weakref at 0x00000188D2CFD670; to 'Person' at 0x00000188D2C9B8C0>
print(w())  # -> <__main__.Person object at 0x0000025089E8B8C0>

del p
print(w)  # -> <weakref at 0x000001ED2B5DD670; dead>
print(w())  # -> None


class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()

v.x = 10
print(Vector.x._values.keyrefs())  # -> [<weakref at 0x000001EF61DBF920; to 'Vector' at 0x000001EF61DC78C0>]

del v
print(Vector.x._values.keyrefs())  # -> []


