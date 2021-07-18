class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1,2]
        k = 1
        while k < n:
            output.append(output[k]+output[k-1])
            k += 1
        return output[n-1]