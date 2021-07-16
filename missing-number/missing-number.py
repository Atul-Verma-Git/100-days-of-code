"""
4 -> 0,1,2,3,4
[1,3,4,0]
if all negetive return 0
else return i+1
[-1,3,4,2] -> 1st iter
[-1,3,-4,2] -> 2nd iter
[-1,3,-4,-2] -> 3rd iter
[-1,-3,-4, -2]-> 4th iter
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n+1) )//2) - sum(nums)
                
        