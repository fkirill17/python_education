class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(10000)]

    def add(self, key):
        index = key % len(self.hashset)
        if key not in self.hashset[index]:
            self.hashset[index].append(key)

    def remove(self, key):
        index = key % len(self.hashset)
        if key in self.hashset[index]:
            self.hashset[index].remove(key)

    def contains(self, key):
        index = key % len(self.hashset)
        return key in self.hashset[index]


obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.remove(1)
param_3 = obj.contains(1)
param_4 = obj.contains(2)

print(param_3)  # -> False
print(param_4)  # -> True