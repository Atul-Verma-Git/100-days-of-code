class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = 1
        m = 0
        l = list(d.keys())
        for i in l:
            if i in d.keys():
                x = i
                count = d[i]
                while True:
                    if x + 1 in d.keys():
                        count += d[x+1]
                        del d[x+1]
                        x += 1
                    else:
                        m = max(count, m)
                        d[i] = count
                        break
        return m