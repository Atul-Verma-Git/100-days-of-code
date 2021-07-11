class Solution:
    def isValid(self, s: str) -> bool:
        rev = { '(':')', '{':'}', '[':']'}
        a = []
        count = -1
        for _ in range(len(s)):
            if s[_] in rev.keys():
                a.append(s[_])
                count += 1
            else:
                if count < 0:
                    return False
                elif s[_] == rev[a.pop(count)]:
                    count -= 1
                else:
                    return False
        if len(a) != 0:
            return False
        return True
                
                
    
        
        