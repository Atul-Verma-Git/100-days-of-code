class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(i,j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    return 1 + area(i+1, j) + area(i-1, j) + area(i,j-1) + area(i, j+1)
                else:
                    return 0
            else:
                return 0
        maxi = 0    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxi = max(maxi, area(i,j))
        return maxi
                    