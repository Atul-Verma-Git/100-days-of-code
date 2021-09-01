class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        
        if s != '' and p == '':
            return False
        
        if s == '' and p != '':
            if s == '' and (len(p) <= 1 or p[1] != '*'):
                return False
            else:
                return self.isMatch(s, p[2:])
        else:
            if s[0] == p[0] or p[0] == '.':
                if len(p) > 1:
                    if p[1] == '*':
                        if self.isMatch(s[1:],p) == True:
                            return True
                        else:
                            return self.isMatch(s,p[2:])
                    else:
                        return self.isMatch(s[1:],p[1:])
                else:
                    return self.isMatch(s[1:],p[1:])
            else:
                if s[0] != p[0] or p[0] != '.':
                    if len(p) > 1:
                        if p[1] == '*':
                            return self.isMatch(s,p[2:])    
                return False
                