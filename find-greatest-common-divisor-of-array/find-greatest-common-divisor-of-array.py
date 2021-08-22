class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def hcf(a,b):
            if(b==0):
                return a
            else:
                return hcf(b,a%b)
        
        h = hcf(max(nums),min(nums))
        
        return h
            
        
        