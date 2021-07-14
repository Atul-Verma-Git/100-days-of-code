class Solution:
    def longestDecomposition(self, text: str) -> int:
        def check(str):
            j = len(str)-1
            while True:
                if str[0] == str[j]:
                    if str[0:(len(str) - j)] == str[j:]:
                        return str[(len(str) - j):j]
                j -= 1
                if j <= 0:
                    return str
        count = 0
        b = text
        while True:
            if b == '':
                return count
            c = check(b)
            if len(b) == 1:
                return count+1
            elif len(c) == len(b):
                return count+1
            elif len(c) != len(b):
                count += 2
                b = c
            