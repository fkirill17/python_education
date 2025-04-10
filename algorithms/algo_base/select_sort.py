#TODO Указать в докстринге сложность алгоритма

def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] < smallest:
            smallest = arr[idx]
            smallest_idx = idx
    return smallest_idx


def selection_sort(arr):
    sort_arr = []
    for i in range(len(arr)):
        smallest_idx = find_smallest(arr)
        sort_arr.append(arr.pop(smallest_idx))  # Перемещение элементов из одного списка в другой
    return sort_arr


print(selection_sort([2, 3, 4, 5, 1, 10]))  # -> [1, 2, 3, 4, 5, 10]
