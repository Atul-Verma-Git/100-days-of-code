class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def col_max(i):
            j = 0
            maxi = 0
            while j < len(matrix):
                maxi = max(matrix[j][i], maxi)
                j += 1
            return maxi
        col = []
        for i in range(len(matrix[0])):
            col.append(col_max(i))
        row = []
        for i in matrix:
            row.append(min(i))
        
        
        output = []
        for i in row:
            for j in col:
                if i == j:
                    output.append(i)
        return output
                
            
            
        
            
                    