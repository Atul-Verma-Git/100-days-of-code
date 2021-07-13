"""
nums = [2,3,1,2,4,3], sum = 0, output = [] min_length = infinity
sum = 2, output =[2] min_lenghth = infinity
sum = 5, output = [2,3] , min_length = infinity
sum = 6, output = [2,3,1],min_length = infinity
sum = 8, output = [2,3,1,2], min_length = 4
sum = 6, output = [3,1,2], min_length = 4
sum = 10, output= [3,1,2,4] min_length = 4
sum = 7, output = [1,2,4],min_length = 3
sum = 6, output =[2,4],min_length = 3
sum = 9, output = [2,4,3], minlength = 3
sum = 7, output = [4,3], inlength = 2


"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = []
        sum = 0
        min_length = float(inf)
        for i in range(len(nums)):
            sum = sum + nums[i]
            output.append(nums[i])
            if sum >= target:
                if len(output)==1:
                    return 1
                else:
                    while sum >= target:
                        min_length = min(min_length, len(output))
                        sum -= output[0]
                        del output[0]
        if min_length == float("inf"):
            return 0  
        return min_length
        
        
        