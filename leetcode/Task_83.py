def deleteDuplicates(head):
    lst = []
    for idx, num in enumerate(head):
        if not lst:
            lst.append(num)
            continue
        if num == lst[-1]:
            continue
        else:
            lst.append(num)
    return lst



print(deleteDuplicates([1, 1, 2, 2, 3, 3,3 ]))
