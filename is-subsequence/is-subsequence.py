class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in s:
            flag = 1
            while j < len(t):
                if i == t[j]:
                    j += 1
                    flag = 0
                    break
                else:
                    j += 1
            if flag == 1:
                return False
        return True
                
        