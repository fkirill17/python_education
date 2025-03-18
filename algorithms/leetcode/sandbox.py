def maxProfit(lst: list):
    l, r = 0, 1
    maxP = 0
    while r < len(lst):
        if lst[r] > lst[l]:
            profit = lst[r] - lst[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


print(maxProfit([7,1,5,3,6,4]))