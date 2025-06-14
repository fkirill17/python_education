import random

CNT = 3

CNT_LEETCODE = 35

CNT_QUESTION = 39

for i in range(CNT):
    print(f'Задача LeetCode {i + 1}: {random.randint(1, CNT_LEETCODE)}')
print('')
for j in range(CNT):
    print(f'Номер вопроса {j + 1}: {random.randint(1, CNT_QUESTION)}')