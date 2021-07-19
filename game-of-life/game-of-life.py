class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def ncount(board,i,j):
            count = 0
            c = len(board) -1
            d = len(board[0]) -1
            if i-1 >= 0:
                count += board[i-1][j]
                if j-1 >= 0:
                    count += board[i-1][j-1]
                if j+1 <= d:
                    count += board[i-1][j+1]
            if i+1 <= c:
                count += board[i+1][j]
                if j-1 >= 0:
                    count += board[i+1][j-1]
                if j+1 <= d:
                    count += board[i+1][j+1]
            if j-1 >= 0:
                count += board[i][j-1]
            if j+1 <= d:
                count += board[i][j+1]
            return count
        grid = y = [row[:] for row in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                b = ncount(grid,i,j)
                if b < 2:
                    board[i][j] = 0
                if b > 3:
                    board[i][j] = 0
                if b == 3:
                    board[i][j] = 1
            