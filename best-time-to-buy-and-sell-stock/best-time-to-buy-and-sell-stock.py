class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if not p:
            return 0
        mp = 0
        minp = p[0]
        for i in range(1, len(p)):
            mp = max(mp, p[i] - minp)
            minp = min(p[i], minp)
        return mp
            
        