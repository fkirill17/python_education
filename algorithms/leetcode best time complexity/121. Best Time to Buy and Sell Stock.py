def maxProfit(prices):
    l, r = 0, 1  # Индексы указателей
    maxP = 0
    while r < len(prices):  # Цикл пока правый указатель внутри списка
        if prices[r] > prices[l]:  # Как бы базовый случай (когда гарантирован хоть какой-то профит)
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)  # Накопление максимального значения
        else:
            l = r  # Иногда левый указатель ставим на место правого
        r += 1  # Всегда правый указатель сдвигаем на 1 ступень вправо
    return maxP


print(maxProfit([7, 1, 5, 3, 6, 4]))
