class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for i in reversed(range(len(nums))):
            l = len(output)
            for j in range(l):
                temp = output[j][:]
                temp.insert(0,nums[i])
                output.append(temp)
            
        return output
        
        
            
        
            
        
        
        