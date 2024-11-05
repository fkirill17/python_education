name = 'Ivan'


class Person:
    name = 'Dima'

    def print_name(self):
        print(name)

    def print_name_self(self):
        print(self.name)

    @classmethod
    def change_name(cls, name):
        cls.name = name


p = Person()

p.print_name()  # -> 'Ivan'
p.print_name_self()  # -> 'Dima'

# Область видимости методов экземпляров не является вложенной в область видимости класса

p.name = 'Kirill'
print(p.__dict__)  # -> {'name': 'Kirill'} - Изменилось только свойство экземпляра
print(Person.name)  # -> 'Dima'

p.print_name_self()  # -> 'Kirill'

# Из экземпляра мы можем только читать свойства класса, но не менять их. @classmethod позволяет сделать это

p.change_name('Kirill')
print(Person.name)  # -> 'Kirill'


# Самый известный прием для использования методов классов - альтернативные __init__ методы

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls


p = Person('Kirill')

print(p.__dict__)  # -> {'name': 'Kirill'}

p = Person.from_file('text')


print(p.__dict__)  # -> {'name': 'Alena'}


class Config:
    name = 'Igor'


p = Person.from_obj(Config)

print(p.__dict__)  # -> {'name': 'Igor'}
