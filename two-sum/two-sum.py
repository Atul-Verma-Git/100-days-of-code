class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        l = len(nums)
        for _ in range(l):
            b = target - nums[_]
            if nums[_] in d.keys():
                A = d[nums[_]]
                return [A ,_]
            d[b] = _
        