def merge(nums1, m, nums2, n):
    idx = 0
    while m < len(nums1):
        nums1[m] = nums2[idx]
        m += 1  # Указатель
        idx += 1  # Указатель
    nums1.sort()  # Внимание. Список изменяемый объект и к нему применимы методы
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
