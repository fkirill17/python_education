class Person:
    def create(self):
        self.name = 'Ivan'

    def display(self):
        print(self.name)


p = Person()
# p.display()  # -> AttributeError: 'Person' object has no attribute 'name'

p.create()  # -> Создали экземпляру атрибут name
p.display()  # -> 'Ivan'


class Person:
    def __init__(self, name):  # Метод init вызывается автоматически при вызове класса
        self.name = name

    def display(self):
        print(self.name)


p = Person(name='Ivan')  # Вызываем класс и передаём в метод __init__ аргумент
p.display()  # -> 'Ivan'

# Создание экземпляров классов состоит из 2 этапов
# 1. Когда вызываем класс, Python методом __new__ создаёт экземпляр класса
# 2. Метод __init__ присваивает созданному ранее экземпляру свойства на лету
