class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        else:
            q = 1<<p
            r = int(q/2)
            return (pow(q -2, r - 1, int(1e9)+7) * (q - 1)) % int((1e9)+7)
        
        
        
        