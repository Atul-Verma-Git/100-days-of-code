class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_smallest(nums):
            i = 0
            j = len(nums) - 1
            if nums[i] < nums[j]:
                return 0
            while i <= j :
                if i == j:
                    return i
                mid = (i + j + 1) // 2
                if (mid-1 < 0 or nums[mid] < nums[mid - 1]) and (mid+1 >= len(nums) or nums[mid] < nums[mid+1]) :
                    return mid
                else:
                    if nums[mid] > nums[j]:
                        i = mid
                    else:
                        j = mid
        
        def search(target, nums):
            i = 0
            j = len(nums) - 1
            while i <= j :
                mid = (i + j + 1) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target > nums[mid]:
                        i = mid + 1
                    else:
                        j = mid - 1
            return -1
        
        
        i = find_smallest(nums)
        print(i)
        
        if target > nums[-1]:
            return search(target,nums[:i])
        else:
            b = search(target,nums[i:])
            if b == -1:
                return -1
            return b+i
        
            
                    
            
        
                
                
                    
                
        
        