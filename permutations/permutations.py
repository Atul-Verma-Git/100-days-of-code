class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            num = nums.pop(0)
            temp = self.permute(nums)
            
            for t in temp:
                t.append(num)
            output.extend(temp)
            nums.append(num)
        
        return output
        