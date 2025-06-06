string = b'hi!'
print(list(string))  # -> [104, 105, 33]
x = bytes([104, 105, 33])
print(x)  # -> b'hi!'
print(x.decode('utf-8'))  # -> hi!



