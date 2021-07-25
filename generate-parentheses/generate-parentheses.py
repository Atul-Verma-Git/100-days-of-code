class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = ['()']
        if n == 1:
            return output
        i = 2
        while i < n + 1:
            temp = []
            j = len(output)
            k = 0
            while k < j:
                for y,x in enumerate(output[k]):
                    if (y == 0 or y == len(output[k]) or x == ')') and (output[k][:y] + '()' + output[k][y:]) not in temp:
                        temp.append(output[k][:y] + '()' + output[k][y:])
                k += 1
            output = temp
            if i == n+1:
                return temp
            i += 1
        
            
        return output
        
        