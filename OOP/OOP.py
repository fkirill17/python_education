class Person:
    name = 'Ivan'


print(Person.name)  # -> 'Ivan' Вызов атрибута класса

print(Person.__name__)  # -> 'Person' Доступ к названию класса

print(dir(Person))  # Посмотреть доступные атрибуты класса

print(Person.__class__)  # -> 'type' потому что это пользовательский класс

# Чтобы создать экземпляр класса, нужно вызвать класс, вызов класса возвращает его объект

p = Person()  # Теперь p это экземпляр класса

print(p.__class__)  # -> '__main__.Person' Ссылка на модуль, название класса

print(type(p))  # -> '__main__.Person' Ссылка на модуль, название класса

print(p.__class__.__name__)  # -> 'Person' Вернулось название класса как строка

new_person = type(p)()  # Создался экземпляр того же типа, что и объект p

print(id(new_person) == id(p))  # -> False Два разных объекта
