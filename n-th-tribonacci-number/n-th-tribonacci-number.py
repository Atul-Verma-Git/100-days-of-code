class Solution:
    def tribonacci(self, n: int) -> int:
        output = [0,1,1]
        k = 2
        while k < n:
            output.append(output[k] + output[k-1] + output[k-2])
            k += 1
        return output[n]
        