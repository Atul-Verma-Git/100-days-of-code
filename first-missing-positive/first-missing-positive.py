class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        b = len(nums)
        while i < len(nums):
            if nums[i] < 1 or nums[i] > b:
                del nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if temp < len(nums):
                nums[temp] = -1 * abs(nums[temp])
        output = []
        for i,n in enumerate(nums):
            if n > 0:
                return i + 1
        return len(nums)+1
        
        