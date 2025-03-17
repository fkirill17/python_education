def maxProfit(prices):
    l = 0
    r = len(prices) - 1
    maxP = 0
    while l < r:
        if prices[r] - prices[l] > maxP:
            maxP = prices[r] - prices[l]
        l -= 1
        r -= 1
    return maxP

print(maxProfit([7,1,5,3,6,4]))
