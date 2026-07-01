class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r != len(prices):
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP