from random import randint


def my_deco(exceptions: list[tuple[Exception, callable]]):
    def wrapper(func):
        def wrapper_1(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                for ex in exceptions:
                    if isinstance(e, ex[0]):
                        ex[1]()
                        raise e
        return wrapper_1

    return wrapper


def bar():
    print(1)


@my_deco([(KeyError, bar), (IndexError, lambda : print(2))])
def foo():
    if randint(1, 2) == 1:
        raise KeyError()
    else:
        raise IndexError()


foo()

# Напишите декоратор, который принимает в качестве аргумента список таплов исключений и callback'ов,
# который при исключении вызыввет соответсвующий callback
