class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                left = 0
            else:
                left = sum(nums[:i])
            if i == len(nums)-1:
                right = 0
            else:
                right = sum(nums[i+1:])
            if left == right:
                return i
        return -1
        
        