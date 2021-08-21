class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        psum = 0
        nsum = 0
        m = 1e6
        ncount = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    ncount += 1
                    nsum += matrix[i][j]
                    if m > abs(matrix[i][j]):
                        m = abs(matrix[i][j])
                else:
                    psum += matrix[i][j]
                    if m > matrix[i][j]:
                        m = matrix[i][j]
        
        if ncount % 2 == 0:
            return psum + -(nsum)
        else:
            return psum + -(nsum) - (m *2)
                    
                    
                
        