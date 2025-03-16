def isValid(s):
    open_to_close = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    stack = []

    for c in s:
        if c in open_to_close:  # Открывающая скобка?
            if not (stack and
                    (stack.pop() == open_to_close[c])):  # Стек пуст? И последний элемент стека != значение из словаря?
                return False
        else:  # Закрывающая скобка
            stack.append(c)  # Добавляем скобку в стек

    return not stack  # Если нет стека неявно вернется True


print(isValid("()()())"))
