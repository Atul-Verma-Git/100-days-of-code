class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [True,True] + [False] * (len(nums)-1)
        count = 1
        for i in range(len(nums)):
            if dp[i + 1] == False:
                return False
            else:
                if i + nums[i] >= count:
                    jump = 0
                    j = i + 2
                    while j <= len(nums) and jump < nums[i]:
                        if dp[j] == False:
                            dp[j] = True
                            count += 1
                        jump += 1
                        j += 1
                        if dp[-1] == True:
                            return True
        return dp[-1]
        
                
        
        
        
                
        
        
                
        
        