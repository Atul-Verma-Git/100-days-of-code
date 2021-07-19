class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        def check(i,j,fresh):
            r = len(grid)
            c = len(grid[0])
            if i-1 >= 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rotten.append([i-1,j])
                    fresh -= 1    
            if i+1 < r:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rotten.append([i+1,j])
                    fresh -= 1
            if j-1 >= 0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    rotten.append([i,j-1])
                    fresh -= 1
            if j+1 < c:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    rotten.append([i,j+1])
                    fresh -= 1
            return fresh
                
        
        
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append([i,j])
        time = 0
        while fresh > 0 and rotten:
            time += 1
            c = len(rotten)
            i = 0
            while i<c:
                a,b = rotten.pop(0)
                fresh = check(a,b,fresh)
                i += 1
    
        if fresh <= 0:
            return time
        return -1
                
                
            
            
        
        
        
                
        