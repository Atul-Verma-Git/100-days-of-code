class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            i = 0
            j = len(nums)-1
            mid = (i + j) // 2
            if (mid + 1 >= len(nums) or nums[mid] > nums[mid+1]) and (mid - 1 < 0 or nums[mid] > nums[mid-1]):
                return mid
            else:
                if nums[mid] < nums[mid-1] and mid != 0:
                    return self.findPeakElement(nums[:mid])
                elif nums[mid] < nums[mid+1] and mid != j:
                    return mid+1 + self.findPeakElement(nums[mid+1:])
                    
        