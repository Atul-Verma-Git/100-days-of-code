class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        a=[]
        for _ in range(len(s)-2):
            if s[_] != s[_+1] and s[_]!= s[_+2] and s[_+1]!= s[_+2]:
                if s[_:_+2] not in a:
                    a.append(s[_:_+3])
        return len(a)

