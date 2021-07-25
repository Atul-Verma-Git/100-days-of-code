class Solution:
    def getLucky(self, s: str, k: int) -> int:
        output = ""
        for i in s:
            output += str(ord(i)-ord('a')+1)
        i = 0
        res = 0
        while i < k:
            res = 0
            for j in output:
                res += int(j)
            output = str(res)
            i += 1
        return res