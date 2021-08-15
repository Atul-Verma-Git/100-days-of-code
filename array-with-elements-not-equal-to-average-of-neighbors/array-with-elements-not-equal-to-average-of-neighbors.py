class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(2,len(nums)):
            if nums[i-1]-nums[i-2] == nums[i]- nums[i-1]:
                if i-3 < 0 or nums[i-2] - nums[i-3] != nums[i] - nums[i-2]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                else:
                    nums[i-1],nums[i-2] = nums[i-2],nums[i-1]
        return nums
        