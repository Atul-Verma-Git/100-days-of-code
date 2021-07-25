class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {_:0 for _ in range(33)}
        for i in nums:
            if i > 0:
                for x in range(32):
                    i, num = divmod(i, 2)
                    d[x] += num
            else:
                d[32] += 1
                i = abs(i)
                for x in range(32):
                    i, num = divmod(i, 2)
                    d[x] += num
        
        output = 0
        for i in reversed(range(32)):
            output = 2 * (output) + (d[i] % 3)
        if d[32] % 3 != 0:
            return -output
        return output
            
            