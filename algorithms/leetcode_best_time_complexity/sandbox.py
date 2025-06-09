import copy

lst = [1,2,3,4,5,[1,2]]
coplst = copy.deepcopy(lst)


lst[-1].append(100)
print(coplst)