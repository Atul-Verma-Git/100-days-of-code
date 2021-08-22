class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        res = 0
        for i in word:
            if ord(prev) < ord(i):
                res +=  min(abs(ord(i) - ord(prev)), abs(ord(i)-ord(prev) - 26)) + 1
            elif ord(prev) == ord(i):
                res += 1
            else:
                res +=  min(abs(ord(prev) - ord(i)), abs(ord(prev)-ord(i) - 26)) + 1
            prev = i
        return res
        