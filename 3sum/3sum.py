class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        if len(nums) < 3:
            return output
        nums.sort()
        
        i = 0
        while i < len(nums)-2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and  nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1 
                    l += 1
            while nums[i] == nums[i+1] and i < len(nums)-2:
                i += 1
            i += 1
                    
        return output
        
            
        