class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkCol(board) and self.checkRows(board) and self.checkSquare(board)
    def checkCol(self, board):
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in nums:
                    return False
                else:
                    nums.add(board[row][col])
        return True

    def checkRows(self, board):
        for row in range(9):
            nums = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in nums:
                    return False
                else:
                    nums.add(board[row][col])
        return True

    def checkSquare(self, board):
        for squareRow in range(0, 9, 3):
            for squareCol in range(0, 9, 3):
                nums = set()
                for row in range(squareRow, squareRow+3):
                    for col in range(squareCol, squareCol+3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] in nums:
                            return False
                        else:
                            nums.add(board[row][col])
        return True
    
    



    

                