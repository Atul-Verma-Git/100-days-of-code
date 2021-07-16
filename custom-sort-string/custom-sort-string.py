class Solution:
    def customSortString(self, order: str, str: str) -> str:
        o = list(order)
        s = list(str)
        output = ''
        for i in o:
            if i in s:
                while i in s:
                    output += i
                    s.remove(i)
        s = "".join(s)
        output += s
        return output
            
        