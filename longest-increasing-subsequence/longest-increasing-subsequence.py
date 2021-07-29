class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        def helper(num):
            n = 1
            for i in range(len(dp)):
                if num < dp[i][1]:
                    n = max(n, 1 + dp[i][0])
            dp.append([n, num])
            
        i = len(nums) - 1
        while i >= 0:
            helper(nums[i])
            i -= 1
        return max(dp)[0]
            
            
        