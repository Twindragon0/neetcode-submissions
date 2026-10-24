class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkCol(board) and self.checkSquare(board)
    def checkRow(self, board):
        seen = set()
        for row in board:
            for char in row:
                if char == ".":
                    continue
                elif char in seen:
                    return False
                else:
                    seen.add(char)
            seen = set()
        return True

    def checkCol(self, board):
        seen = set()
        for col_idx in range(9):
            for row_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                elif board[row_idx][col_idx] in seen:
                    return False
                else:
                    seen.add(board[row_idx][col_idx])
            seen = set()
        return True
    
    def checkSquare(self, board):
        seen = set()
        for i in range(0,9,3):
            for j in range(0,9,3):
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        if board[a][b] == ".":
                            continue
                        elif board[a][b] in seen:
                            return False
                        else:
                            seen.add(board[a][b])
                seen = set()
        return True

                