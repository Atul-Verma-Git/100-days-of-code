class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            dp = [1] * (n) 
        else:
            dp = [1] * (m)
        
        print(dp)
        for i in range(max(m,n)-1):
            for j in range(min(m,n)):
                dp[j] = sum(dp[j:])
        return dp[0]
        