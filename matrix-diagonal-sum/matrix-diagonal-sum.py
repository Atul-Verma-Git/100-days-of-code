class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        l = len(mat)
        for i in range(l):
            s += mat[i][i] + mat[i][l-1-i]
        if l %2 != 0:
            s -= mat[l//2][l//2]
        return s
            
        