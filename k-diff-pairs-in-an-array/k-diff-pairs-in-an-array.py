class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        d = {}
        for i in nums:
            d.setdefault(i, 0)
            d[i] += 1
        for i in d.keys():
            if (k > 0 and i-k in d.keys()) or (k == 0 and d[i] > 1):
                count += 1
        return count
            
            
            