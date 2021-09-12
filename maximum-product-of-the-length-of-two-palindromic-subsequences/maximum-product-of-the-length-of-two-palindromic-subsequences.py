class Solution:
    def maxProduct(self, s: str) -> int:
        def largestP(s):
            n = len(s)
            dp = [1] * n
            for j in range(1, len(s)):
                pre = dp[j]
                for i in reversed(range(0, j)):
                    tmp = dp[i]
                    if s[i] == s[j]:
                        dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                    else:
                        dp[i] = max(dp[i + 1], dp[i])
                    pre = tmp
            return dp[0]
        
        l = len(s)
        output = 1
        for i in range(1, (2**l)-1):
            r = ''
            m = ''
            for j in range(l):
                if i & (1<< j):
                    r += s[j]
                else:
                    m += s[j]
            print(largestP('mppdm'))
            output = max((largestP(r) * largestP(m)), output)
        return output
            
                    
                
            
                    
        