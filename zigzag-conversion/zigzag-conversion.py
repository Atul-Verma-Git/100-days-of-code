class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = [[] for _ in range(numRows)]
        counter = 0
        i = 0
        while counter < len(s):
            temp[i].append(s[counter])
            counter += 1
            i += 1
            if i == numRows:
                i -= 2
                while counter < len(s) and i > 0:
                    temp[i].append(s[counter])
                    counter += 1
                    i -= 1
        output = ''
        for i in temp:
            output += ''.join(i)
        return output
                    
                
                    
                
                
            
            
                
                
            
            
                
                
                
            
        