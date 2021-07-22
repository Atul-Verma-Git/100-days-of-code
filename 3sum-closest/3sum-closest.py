class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums) -1
        i = 0
        output = nums[0]+nums[1]+nums[2]
        while i < len(nums)-2:
            k = i+1
            j = len(nums) -1
            while k < j:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(target - s) < abs (target- output):
                    output = s
                if s < target:
                    k += 1
                elif s > target:
                    j -= 1
            i += 1
        return output
                
            
        
            
        