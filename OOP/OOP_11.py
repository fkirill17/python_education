class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._fullname = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._fullname = None  # Когда вызываем сеттер - обнуляем кэш

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._fullname = None  # Когда вызываем сеттер - обнуляем кэш

    @property
    def full_name(self):
        if self._fullname is None:
            self._fullname = f'{self._name} {self._surname}'
        return self._fullname


p = Person('John', 'S')
print(p.__dict__)  # -> {..., '_fullname': None}
print(p.full_name)  # -> 'John Smith'

# После вызова метода full_name полное имя закэшировалось
print(p.__dict__)  # -> {..., '_fullname': 'John S'}

p.surname = 'J'  # Произвели редактирование - вызвали сеттер и обнулили кэш
print(p.__dict__)  # -> {..., '_fullname': None}
print(p.full_name)  # -> 'John J'

# После вызова метода full_name полное имя закэшировалось
print(p.__dict__)  # -> {..., '_fullname': 'John J'}

print(p.surname)
