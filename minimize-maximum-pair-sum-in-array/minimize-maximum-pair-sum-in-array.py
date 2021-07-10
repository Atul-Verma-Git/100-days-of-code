class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        for _ in range(len(nums)):
            if sums <= nums[_]+nums[len(nums)-_-1] :
                sums = nums[_]+nums[len(nums)-_-1]
            else:
                pass
        return sums