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
q.push(4)
print(q.pop())  # -> 2
print(q.pop())  # -> 3
print(q.pop())  # -> 4

