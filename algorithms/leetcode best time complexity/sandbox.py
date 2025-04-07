class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):  # -> Вход
        self.stack_in.append(x)

    def pop(self):
        self.peek()  # Внимание
        return self.stack_out.pop()

    def peek(self):  # -> Выход
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Перемещение элементов из одного списка в другой
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out


q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.stack_in, '"stack_in"')  # -> [1, 2, 3] "stack_in"
print(q.stack_out, '"stack_out')  # -> [] "stack_out
q.pop()
print(q.peek(), '"peek"')  # -> 2 "peek"
print(q.stack_in, '"stack_in"')  # -> [] "stack_in"
print(q.stack_out, '"stack_out"')  # -> [3, 2] "stack_out"

