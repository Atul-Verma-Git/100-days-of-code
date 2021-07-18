class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        output = [0,1]
        if n == 0:
            return 0
        k = 2
        while k <= n:
            if (k) % 2 == 0:
                output.append(output[k//2])
                k += 1
            else:
                output.append(output[k//2] + output[(k//2)+1] )
                k += 1
        return max(output)
        