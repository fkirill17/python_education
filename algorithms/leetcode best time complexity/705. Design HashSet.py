class MyHashSet(object):

    def __init__(self):
        self.hashset = set()  # Внимание

    def add(self, key):
        self.hashset.add(key)  # Внимание

    def remove(self, key):
        if key in self.hashset:
            self.hashset.remove(key)  # Внимание

    def contains(self, key):
        if key in self.hashset:
            return True
        return False


obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.remove(1)
param_3 = obj.contains(1)
param_4 = obj.contains(2)

print(param_3)  # -> False
print(param_4)  # -> True