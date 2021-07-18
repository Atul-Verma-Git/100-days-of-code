class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum( ( prices[idx+1]-prices[idx] ) for idx in range(len(prices)-1) if prices[idx] < prices[idx+1] )