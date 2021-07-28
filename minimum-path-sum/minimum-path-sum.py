class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        output = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        output[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < len(grid):
                    output[i+1][j] = min(output[i+1][j] , output[i][j] + grid[i+1][j])
                if j + 1 < len(grid[0]):
                    output[i][j+1] = min(output[i][j+1] , output[i][j] + grid[i][j+1])
        
        return output[-1][-1]
                
            
                  
        