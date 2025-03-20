def func(name, age):
    return f'Hey, {name}, your age: {age}'


dct = {'name': 'Alice', 'age': 24}

print(func(**dct))
