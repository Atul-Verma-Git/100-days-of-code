class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''
        i = 0
        for i in range(len(s)):
            temp = self.pal(s, i, i)
            if len(temp) > len(output):
                output = temp
            temp = self.pal(s,i,i+1)
            if len(temp) > len(output):
                output = temp
        return output
            
        
        
    def pal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1 : r]
        
        
        
        