class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name_demo(self):
        print('Код геттера')
        return self.name  # Геттер

    @name_demo.setter  # Названия декораторов и функций строго определено
    def name_demo(self, value):
        print('Код сеттера')
        self.name = value  # Сеттер


p = Person('Dima')

print(p.name_demo)  # -> 'Код геттера' -> 'Dima' p.name - это вызов функции геттера, вызов происходит без скобок
p.name_demo = 'Kirill'  # -> 'Код сеттера'

print(p.name_demo)  # -> 'Код геттера' -> 'Kirill'
print(p.name)  # -> 'Kirill' - обратились напрямую к свойству экземпляра

# Геттеры и сеттеры можно использовать как буферную зону, для полученя или редактирования атрибутов экземпляра класса
# Их так же можно применять для валидации значений, которые мы собираемся записать в атрибутах
