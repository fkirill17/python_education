class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x):  # -> Вход
        self.queue.append(x)

    def pop(self):
        if self.queue:
            r = self.queue.pop(0)
        return r

    def peek(self):  # -> Выход
        if self.queue:
            return self.queue[0]

    def empty(self):
        if self.queue:
            return False
        else:
            return True


obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print([param_2, param_3, param_4])  # -> [1, None, True]
