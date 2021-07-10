class Solution:
    def romanToInt(self, s: str) -> int:
        s = '0' + s + '0'
        dictr = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, '0':0}
        sum = 0
        for _ in range(len(s)-1):
            if dictr[s[_]] < dictr[s[_+1]]:
                temp_sum = dictr[s[_+1]] - dictr[s[_]]
            elif dictr[s[_-1]] < dictr[s[_]]:
                sum = sum + temp_sum
            elif dictr[s[_]] >= dictr[s[_+1]]:
                sum += dictr[s[_]]
        
        return sum
                
            
            
        
        