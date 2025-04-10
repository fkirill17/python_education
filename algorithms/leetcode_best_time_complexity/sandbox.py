class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(10000)]

    def add(self, key):
        idx = key % len(self.hashset)
        if not self.hashset[idx]:
            self.hashset[idx].append(key)


    def remove(self, key):
        idx = key % len(self.hashset)
        if self.hashset[idx]:
            self.hashset[idx].remove(key)

    def contains(self, key):
        idx = key % len(self.hashset)
        return key in self.hashset[idx]


obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.remove(1)
param_3 = obj.contains(1)
param_4 = obj.contains(2)

print(param_3)  # -> False
print(param_4)  # -> True