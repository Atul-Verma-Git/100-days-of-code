class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one = 0
        two = len(nums) - 1
        while two > one and nums[two] == 2:
            two -= 1
        while one < two and nums[one] == 0:
            one += 1
        i = one
        while i <= two:
            if nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                while two > one and nums[two] == 2:
                    two -= 1
            if nums[i] == 0:
                nums[i], nums[one] = nums[one], nums[i]
                one += 1  
            
                
            i += 1
            
        