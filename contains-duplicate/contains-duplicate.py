class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                return True
            else:
                d[nums[i]] = True
        return False
        