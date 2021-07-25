class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        l = list(d.values())
        l.sort()
        if l[0] == l[-1]:
            return True
        return False
        