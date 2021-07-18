class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        count = 0
        while nums:
            if nums[0] == 1:
                del nums[0]
                count += 1
            else:
                del nums[0]
                output = max(output,count)
                count = 0
        return max(output,count)