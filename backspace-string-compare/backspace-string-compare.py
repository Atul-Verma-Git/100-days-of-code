class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def atulkafunction(s):
            atulkalist = []
            for i in s:
                if i == '#':
                    if atulkalist != []:
                        atulkalist = atulkalist[:-1]
                else:
                    atulkalist.append(i)
            return atulkalist
        
        return atulkafunction(s) == atulkafunction(t)
        