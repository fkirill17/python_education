class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10 ** 4)]

    def add(self, key):
        index = key % 10000
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        index = key % 10000
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        index = key % 10000
        return key in self.buckets[index]