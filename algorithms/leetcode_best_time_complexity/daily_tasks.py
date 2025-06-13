import random

CNT_TASKS = 3

SOL_CNT = 34

for i in range(CNT_TASKS):
    print(f'Задача {i + 1}: {random.randint(1, SOL_CNT)}')