def mergeTwoLists(list1, list2):
    if list1 == [] and list2 == []:
        return []
    list1 = list1 + list2
    for i in range(len(list1)):
        print()
        flag = False
        for idx in range(len(list1) - 1):
            if list1[idx] > list1[idx + 1]:
                list1[idx], list1[idx + 1] = list1[idx + 1], list1[idx]
                flag = True
        if not flag:
            break
    return list1
# Сделал сортировку пузырьком вместо, того чтобы сростить list1 и list2

print(mergeTwoLists([1, 2, 5], [1, 4, 5]))
