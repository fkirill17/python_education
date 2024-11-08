class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Код геттера')
        return self._name

    @name.setter
    def name(self, value):
        print('Код сеттера')
        self._name = value

# Названия декораторов и функций строго определено


p = Person('Dima')

print(p.name)  # -> 'Код геттера' -> 'Dima' p.name - это вызов функции геттера, вызов происходит без скобок

p.name = 'Kirill'  # -> 'Код сеттера'
print(p.name)  # -> 'Код геттера' -> 'Kirill'
print(p._name)  # -> 'Kirill' - обратились напрямую к свойству экземпляра

# Геттеры и сеттеры можно использовать как буферную зону, для полученя или редактирования атрибутов экземпляра класса
# Их так же можно применять для валидации значений, которые мы собираемся записать в атрибутах
