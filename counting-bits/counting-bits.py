class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0,1]
        if n == 0:
            return [0]
        if n == 1:
            return output
        while len(output) <= n+1:
            l = len(output)
            for i in range(l):
                output.append(output[i] + 1)
                if len(output) == n+1:
                    return output
        
            
        