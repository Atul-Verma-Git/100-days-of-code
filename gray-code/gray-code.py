'''
n = 1 0, 1
n =2 -> 00 01 11 10
n = 3 -> 110 111 101 100
n = 4 -> 
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        output = [0,1]
        for _ in range(1,n):
            b = len(output)
            c = 2**_
            for __ in reversed(range(b)):
                output.append(c + output[__])
        return output
            
        
        