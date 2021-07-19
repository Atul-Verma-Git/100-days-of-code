class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def rotate(i, j):
            l = len(matrix)
            temp = matrix[i][j]
            matrix[i][j] = matrix[l-j-1][i]
            matrix[l-j-1][i] = matrix[l-i-1][l-j-1]
            matrix[l-i-1][l-j-1] = matrix[j][l-i-1]
            matrix[j][l-i-1] = temp
            
        
        i = 0
        while i < (len(matrix) // 2) :
            j = i
            while j < len(matrix) - 1- i:
                rotate(i,j)
                j += 1
            i += 1
            
            
        
        
        