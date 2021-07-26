class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_horizontal(board):
            for i in range(9):
                d = {}
                for x in board[i]:
                    if x != '.':
                        if x in d.keys():
                            return False
                        d[x] = 1
            return True
                    
            
        def check_vertical(board):
            for i in range(9):
                d = {}
                for j in range(9): 
                    if board[j][i] != '.':
                        if board[j][i] in d.keys():
                            return False
                        d[board[j][i]] = 1
            return True
            
        def check_square(board):
            for i in [0,3,6]:
                for j in [0,3,6]:
                    d = {}
                    for x in range(3):
                        for y in range(3):
                            if board[i+x][j+y] != '.':
                                if board[i+x][j+y] in d.keys():
                                    return False
                                d[board[i+x][j+y]] = 1
            return True
        return check_horizontal(board) and check_vertical(board) and check_square(board)
                
            
        