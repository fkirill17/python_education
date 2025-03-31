def isValid(s):
    dct = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    if len(s) % 2 != 0:
        return False
    stack = []
    for i in s:
        if i in dct and stack and stack[-1] == dct[i]:
            stack.pop()
        else:
            stack.append(i)
    return not stack
