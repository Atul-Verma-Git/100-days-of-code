class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for j,i in enumerate(nums):
            if i in d.keys():
                return [d[i],j]
            d[target-i] = j
                