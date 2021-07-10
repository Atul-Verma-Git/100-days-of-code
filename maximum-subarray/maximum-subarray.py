class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -1e9
        sum = 0
        for _ in range(len(nums)):
            sum = max(sum + nums[_],nums[_])
            m = max(sum, m)
        return m   
                
                
        
        