class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if needle == haystack or needle == '':
            return 0
        for i in range(len(haystack)-l+1):
            if needle[0] == haystack[i]:
                if haystack[i: i+l] == needle:
                    return i
        return -1
        