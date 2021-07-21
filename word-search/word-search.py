class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(grid,i,j,w):
            if w == "":
                return True
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or w[0] != grid[i][j]:
                return False
            p = grid[i][j]
            grid[i][j] = -1
            
            s = check(grid,i-1,j,w[1:]) or check(grid,i+1,j,w[1:]) or check(grid,i,j-1,w[1:]) or check(grid,i,j+1,w[1:])
            grid[i][j] = p
            return s
            
            
            
        r = len(board); c = len(board[0])
        for i in range(r):
            for j in range(c):
                grid = [_ for _ in board]
                if check(grid,i,j,word):
                    return True
        return False