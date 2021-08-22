class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        a = [0] * (2<<len(nums[0]))
        for i in nums:
            a[int(i,2)] = 1
        for i in range(len(a)):
            if a[i] == 0:
                s = i
                break
        res = ''
        for i in range(len(nums[0])):
            res = str(s%2)+res
            s = s//2
        return res