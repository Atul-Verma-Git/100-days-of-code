class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dp = [i for i in range(1,n+1)]
        fact = 1
        for i in range(2,n):
            fact *= i
        output = ''
        k = k-1
        while k != 0:
            num , k = divmod(k, fact)
            output += str(dp[num])
            dp.pop(num)
            fact //= n-1
            n -= 1
        for i in range(len(dp)):
            output += str(dp[i])
        return output
        