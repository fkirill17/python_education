class Person:
    def hello(self):
        print('Hello')

    @staticmethod
    def goodbye():
        print('Goodbye')


a = Person()
b = Person()

a.hello()  # -> 'Hello'
a.goodbye()  # -> 'Goodbye' В функции goodbye self отсутствует, но ошибка не возникла благодаря @staticmethod

print(id(a.hello) == id(b.hello))  # False
print(id(a.goodbye) == id(b.goodbye))  # True - Статический метод глобален для всех экземпляров класса

print(type(a.hello))  # <class 'method'>
print(type(a.goodbye))  # <class 'function'>

# Статические методы не принимают экземпляр класса и не имеют доступа к свойствам и методом классов и их экземпляров
