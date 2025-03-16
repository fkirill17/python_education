class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name_demo(self):
        print('Код геттера')
        return self._name

    @name_demo.setter
    def name_demo(self, value):
        print('Код сеттера')
        self._name = value

# Названия декораторов и функций строго определено


p = Person('Dima')

print(p.name_demo)  # -> 'Код геттера' -> 'Dima' p.name - это вызов функции геттера, вызов происходит без скобок

p.name_demo = 'Kirill'  # -> 'Код сеттера'
print(p.name_demo)  # -> 'Код геттера' -> 'Kirill'
print(p.name_demo)  # -> 'Kirill' - обратились напрямую к свойству экземпляра

# Геттеры и сеттеры можно использовать как буферную зону, для полученя или редактирования атрибутов экземпляра класса
# Их так же можно применять для валидации значений, которые мы собираемся записать в атрибутах
