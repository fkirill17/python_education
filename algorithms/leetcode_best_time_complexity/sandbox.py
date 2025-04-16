import collections


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):  # -> Вход
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())  # 4321

    def pop(self):
        return self.queue.popleft()

    def top(self):  # -> Выход
        return self.queue[0]

    def empty(self):
        return not self.queue


s = MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.queue)  # -> deque([3, 2, 1])
s.pop()
print(s.queue)  # -> deque([2, 1])
s.push(4)
print(s.queue)  # -> deque([4, 2, 1])