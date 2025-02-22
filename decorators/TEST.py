def func(**kwargs):
    print(kwargs['a'])  # -> 1
    print(kwargs['b'])  # -> 2


dct = {'a': 1, 'b': 2}

print(func(**dct))
