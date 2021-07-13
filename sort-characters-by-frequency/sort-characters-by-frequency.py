class Solution:
    def frequencySort(self, s: str) -> str:
        output = {}
        for i in s:
            if i not in output.keys():
                output[i] = 1
            else:
                output[i] += 1
        l = [[i,j] for i, j in output.items()]
        l.sort(key = lambda x : x[1], reverse = True)
        c = ''
        for i in range(len(l)):
            c += l[i][0] * l[i][1]
        
        return c    
            
            