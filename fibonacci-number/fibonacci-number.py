class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        output = [0, 1]
        k = 1
        while k < n:
            output.append(output[k]+output[k-1])
            k += 1
        return output[-1]
        