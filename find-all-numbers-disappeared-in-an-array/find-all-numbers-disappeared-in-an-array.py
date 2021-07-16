class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            nums[temp] = -1 * abs(nums[temp])
        output = []
        for i,n in enumerate(nums):
            if n > 0:
                output.append(i+1)
        return output