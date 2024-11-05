class Person:
    name = 'Ivan'


print(dir(Person))  # Посмотреть атрибуты объекта
print(Person.__dict__)  # Состояние любых объектов хранится в словаре dict -> Вернулся read only словарь
print(Person.__dict__['name'])  # -> 'Ivan' Обращение к ключу словаря 'name'

# Мы не можем менять ключи этого словаря непосредственно через обращение к нему

# Person.__dict__['name'] = 'abc'  # TypeError: 'mappingproxy' object does not support item assignment

# Мы можем влиять на этот словарь либо через dot notation либо через функции getattr(), setattr(), delattr()

# Так как Python динамический язык, он позволяет добавлять новые свойства классам "на лету" через точку

Person.age = 23  # Создание нового атрибута класса

getattr(Person, 'name')  # -> 'Ivan' Получение значения атрибута
setattr(Person, 'dob', 123)  # Создание нового атрибута 'dob' - название атрибута, 123 - значение
delattr(Person, 'dob')  # Удаление атрибута


class Person:
    name = 'Ivan'

    def hello():  # Объявление метода класса
        print('Hello')


print(Person.__dict__['hello'])  # -> <function Person.hello at 0x000001715F9780E0>
print(Person.hello())  # -> 'Hello'
