'''
[0,0,1,1,1,2,2,3,3,4]
 i j
[0, _ , 1,1]
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i += 1
                j += 1
        
            
            