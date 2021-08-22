class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        temp = [0]
        for i in range(len(mat)):
            b = float('inf')
            retemp = {}
            for j in range(len(mat[0])):
                for k in range(len(temp)):
                    if temp[k] + mat[i][j] < target:
                        retemp[temp[k] + mat[i][j]] = True
                    elif b > temp[k] + mat[i][j]:
                        b = temp[k] + mat[i][j]
            retemp[b] = True
            temp = list(retemp)
        if b == 0:
            return 0
        m = float('inf')
        for i in temp:
            if abs(target - i) < m:
                m = abs(target - i)
        return m
            
                    
        