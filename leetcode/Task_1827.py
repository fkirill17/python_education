def func(name: int, age: int):
    print(name)
    print(age)

dct = {"name": "Alice", "age": 23}
func(**dct)

