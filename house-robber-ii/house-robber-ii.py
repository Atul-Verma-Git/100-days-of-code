class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr(nums):
            l = len(nums)
            first = 0
            sec = 0
            for i in range(l):
                first, sec = sec, max(sec, first + nums[i])
            return sec 
        return max(nums[0] + hr(nums[2:-1]),hr(nums[1:]))
            
            
                
            
        
            
        
        
            