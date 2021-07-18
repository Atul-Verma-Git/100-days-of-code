class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 1e6
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit