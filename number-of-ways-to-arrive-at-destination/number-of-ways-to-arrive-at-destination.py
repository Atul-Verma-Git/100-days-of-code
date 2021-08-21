class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        mat = [[0] * n for _ in range(n)]
        for i,j,k in roads:
            mat[i][j]= mat[j][i] = k
        
        count = 0
        d = [float('inf')] * (n-1)
        d.append(0)
        c = [1] * n
        for i in reversed(range(n-1)):
            incount = 0
            for j in range(i,n):
                if mat[i][j] > 0:
                    if mat[i][j] + d[j] < d[i]:
                        d[i] = mat[i][j] + d[j]
                        incount = 1 * c[j]
                    elif mat[i][j] + d[j] == d[i]:
                        incount += 1 * c[j]
            c[i] = incount
        return c[0] % 1000000007
            
                
        

        