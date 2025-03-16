class Person:
    name = 'Ivan'


p1 = Person()  # Вызов класса -> экземпляр класса
p2 = Person()

print(id(p1) == id(p2))  # -> False Разные объекты
print(type(p1))  # -> <class '__main__.Person'> Ссылка на модуль, название класса

# Мы создаём экземпляры классов, чтобы хранить разные значения в одних и тех же свойствах

# Свойства класса по умолчанию применяются для всех его экземпляров
print(p1.name)  # -> 'Ivan' Получили значение из глобального словаря класса
print(p2.name)  # -> 'Ivan'
print(Person.name)  # -> 'Ivan'
# Атрибуты класса ссылаются на один и тот же объект

print(p1.__dict__)  # -> {} Локальный словарь экземпляра пуст
print(p2.__dict__)  # -> {}
print(Person.__dict__)  # -> Значения глобального словаря

# Создание новых свойств объекта
p1.name = 'Oleg'
p2.name = 'Dima'
p2.age = 23

# Pyton ищет определение свойства name сначала в локальном словаре экземпляра и только потом в глобальном словаре класса
print(p1.__dict__)  # -> {'name': 'Oleg'} Так как мы переопределили name, вывелось name экземпляра
print(p2.__dict__)  # -> {'name': 'Dima', 'age': 24} Переопределили name и добавили age
print(Person.__dict__['name'])  # -> 'Ivan' атрибут name в классе Person остался неизменным

# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

# Свойства класса влияет на свойства его экземпляров
p1 = Person()
p2 = Person()
Person.name = 'abc'  # Переопределили значение свойства name в самом классе
print(p1.name)  # -> 'abc'
print(p2.name)  # -> 'abc'





