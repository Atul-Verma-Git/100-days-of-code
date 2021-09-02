class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def Empty(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row, col
            return -1, -1
        
        def solve():
            row, col = Empty(board)
            if row == -1 and col == -1:
                return True
            for i in range(1,10):
                board[row][col] = str(i)
                if self.isValidSudoku(row,col,board):
                    if solve():
                        return True
                board[row][col] = '.'
            return False
   
        solve()

    def isValidSudoku(self,row,col, board):
        def check_horizontal(row, col, board):
            for i in range(9):
                if i == col:
                    continue
                if board[row][i] == board[row][col]:
                    return False
            return True
                    
            
        def check_vertical(row, col, board):
            for i in range(9):
                if i == row:
                    continue
                if board[i][col] == board[row][col]:
                    return False
            return True
            
        def check_square(row, col, board):
            r = row - row%3
            c = col - col%3
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if i == row and j == col:
                        continue
                    if board[i][j] == board[row][col]:
                        return False
            return True
        return check_horizontal(row, col, board) and check_vertical(row, col, board) and check_square(row, col, board)
        