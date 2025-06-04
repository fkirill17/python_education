def isValid(s):
    dct = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    if len(s) % 2 != 0 or s[0] in dct:  # Если нечетное количество элементов или первый элемент закрывающая скобка
        return False
    stack = []
    for i in s:
        if i in dct and stack and stack[-1] == dct[i]:  # Если противоположная скобка лежит в последнем элементе стека
            stack.pop()  # Работа со стеком происходит через последний элемент
        else:
            stack.append(i)  # Работа со стеком
    return not stack


print(isValid('[()]'))
