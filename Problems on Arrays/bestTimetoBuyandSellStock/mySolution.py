def buyAndSellStock(prices):
    maxProfit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j]- prices[i]
            if (profit>0):
                maxProfit = max(profit, maxProfit)
    return maxProfit

prices = [7,6,4,3,1]
res = buyAndSellStock(prices)
print(res)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4868897/most-optimized-kadanes-algorithm-java-c-2yt85