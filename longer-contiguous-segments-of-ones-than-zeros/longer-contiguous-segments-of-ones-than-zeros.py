class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l = list(s.split('0'))
        m = list(s.split('1'))
        max = 0
        max2 = 0
        for _ in range(len(l)):
            if len(l[_]) >= max:
                max = len(l[_])
        for _ in range(len(m)):
            if len(m[_]) >= max2:
                max2 = len(m[_])
        if max > max2:
            return True
        else:
            return False
