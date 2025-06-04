class MyIterator:
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.data):
            val = self.data[self.idx]
            self.idx += 1
            return val
        raise StopIteration

lst = [1,2]

obj = MyIterator(lst)

x = obj.__iter__()
print(x.__next__())
print(x.__next__())