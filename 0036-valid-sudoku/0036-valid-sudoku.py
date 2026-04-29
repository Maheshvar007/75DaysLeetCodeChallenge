class Solution(object):
    def isValidSudoku(self, board):
        seen = set()      
        for i in range(9):
            for j in range(9):
                val = board[i][j]           
                if val != '.':
                    if (val, i) in seen or (j, val) in seen or (i//3, j//3, val) in seen:
                        return False
                    
                    seen.add((val, i))          # row
                    seen.add((j, val))          # column
                    seen.add((i//3, j//3, val)) # box
        return True