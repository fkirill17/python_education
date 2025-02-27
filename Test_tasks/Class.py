# Напишите стек, который поддерживает push, pop, top и get_min

class Stack:
    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, num):
        self.stack.append(num)
        if not self.min_num:
            self.min_num.append(num)
        if num < self.min_num[-1]:
            self.min_num.append(num)

    def pop(self):
        if not self.stack:
            return
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        if not self.stack:
            return None
        if self.min_num[-1] < self.stack[-1]:
            return self.min_num.pop()
        return self.min_num[-1]



a = Stack()

print(a.get_min(), 'get_num')

a.push(3)
a.push(4)
a.push(2)
a.push(5)
a.push(1)

a.pop()
print(a.get_min(), 'get_num')
a.pop()
print(a.get_min(), 'get_num')
a.pop()
print(a.get_min(), 'get_num')
a.pop()
print(a.get_min(), 'get_num')
a.pop()
print(a.get_min(), 'get_num')
a.pop()
print(a.get_min(), 'get_num')
