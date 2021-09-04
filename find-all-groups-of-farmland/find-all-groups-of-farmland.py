class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        output = []
        def check(r,c):
            for i in range(r, len(land)):
                if land[i][c] == 1:
                    r_index = i
                else:
                    break
            for i in range(c, len(land[0])):
                if land[r][i] == 1:
                    c_index = i
                else:
                    break
            for i in range(r,r_index+1):
                for j in range(c,c_index+1):
                    land[i][j] = 0
            return r_index,c_index
        
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    x, y = check(i,j)
                    output.append([i,j,x,y])
        return output
                    
                    
                
                    