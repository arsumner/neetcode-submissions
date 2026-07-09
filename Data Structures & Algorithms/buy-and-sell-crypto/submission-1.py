class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1, 0, -1):
            diff = prices[i] - min(prices[:i])
            profit = max(profit, diff)

        return profit
                
            

test = Solution()
t = test.maxProfit([10, 20, 15, 5])