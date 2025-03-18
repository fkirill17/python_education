def maxProfit(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP


print(maxProfit([7,1,5,3,6,4]))
