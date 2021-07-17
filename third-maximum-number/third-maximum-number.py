class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -1e11
        second = -1e11
        third = -1e11
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        for i in range(len(nums)):
            if nums[i] > third:
                third = nums[i]
                if third > second:
                    second , third = third, second
                    if second > first:
                        first, second = second , first
        return third
        
        