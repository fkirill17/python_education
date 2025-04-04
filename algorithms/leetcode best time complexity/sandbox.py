def add_item(item, x=[]):    # Изменяем список
    if item == 1:
        x.append(True)
    else:
        x.append(False)
    return x

print(add_item(2))  # [1, 2]  (ожидали [2], но список сохранился!)
print(add_item(3))  # [1, 2, 3]

print(add_item(1))  # [1]
print(add_item(3))