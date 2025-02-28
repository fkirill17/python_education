class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == [] and list2 == []:
            return []
        elif list1 == [] and list2 != []:
            return list2
        elif list1 != [] and list2 == []:
            return list1
        lst = []
        for x, y in zip(list1, list2):
            if x <= y:
                lst.append(x)
                lst.append(y)
            else:
                lst.append(y)
                lst.append(x)
        return lst


print(Solution().mergeTwoLists([1,2,4], [1,3,4]))
