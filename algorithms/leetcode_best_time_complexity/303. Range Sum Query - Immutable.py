class NumArray():

    def __init__(self, nums):
        self.prefixsum = []
        x = 0
        for num in nums:  # Создание листа с префиксными суммами за время O(n)
            x += num
            self.prefixsum.append(x)

    def sumRange(self, left, right):
        if left > 0:
            summ = self.prefixsum[right] - self.prefixsum[left - 1]  # Получение суммы диапазона за время O(1)
        else:
            summ = self.prefixsum[right]
        return summ


obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)
print(param_1)  # -> 1
print(param_2)  # -> -1
print(param_3)  # -> -3
