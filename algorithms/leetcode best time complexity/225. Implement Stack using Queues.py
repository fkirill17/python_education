class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):  # -> Вход
        self.stack.append(x)

    def pop(self):
        if self.stack:
            x = self.stack.pop()
            return x

    def top(self):  # -> Выход
        if self.stack:
            return self.stack[-1]

    def empty(self):
        if self.stack:
            return False
        else:
            return True


obj = MyStack()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print([param_2, param_3, param_4])  # -> [5, None, True]
