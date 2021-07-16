class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [float('inf')] * (len(nums) - 1)
        for i in range(len(nums)):
            j = i+1
            jump = 0
            while jump < nums[i] and j < len(nums):
                dp[j] = min(dp[i] + 1, dp[j])
                jump += 1
                j += 1
        return dp[-1]
                
        