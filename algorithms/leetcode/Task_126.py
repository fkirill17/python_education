def maxProfit(prices):
    lst = []
    for idx in range(0, len(prices)):
        num = prices[idx]
        for idx2 in range(idx, len(prices)):
            num2 = prices[idx2]
            if num2 > num:
                lst.append(num2-num)
    if not lst:
        return 0
    return lst




print(maxProfit([7,1,5,3,6,4]))