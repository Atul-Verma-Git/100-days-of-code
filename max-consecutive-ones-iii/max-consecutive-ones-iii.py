class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = 0
        i = 0
        j = 0
        zero = []
        while j < len(nums):
            if nums[j] == 1:
                j += 1
            else:
                if k == 0:
                    output = max(j - i, output)
                    i = j + 1
                    j += 1
                else:
                    if len(zero) < k:
                        zero.append(j)
                        j += 1
                    else:
                        output =  max(output, j - i)
                        x = zero.pop(0)
                        zero.append(j)
                        i = x + 1
                        j += 1
        return max(output, j - i)
                        
                    
            
        