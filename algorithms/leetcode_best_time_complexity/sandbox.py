class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.iterable):
            raise StopIteration
        val = self.iterable[self.index]
        self.index += 1
        return val


iterator = MyIterator([1,2,3,4,5])
print(iterator.__next__())
