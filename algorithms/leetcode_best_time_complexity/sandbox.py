x = 10  # глобальное пространство

def outer():
    y = 20  # нелокальное (enclosing)
    def inner():
        z = 30  # локальное
        print(x, y, z)
    inner()


outer()


