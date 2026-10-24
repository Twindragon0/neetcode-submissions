class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                # Row case
                if board[row][col] in rowMap[row]:
                    return False
                else:
                    rowMap[row].add(board[row][col])
                # Row case
                if board[row][col] in colMap[col]:
                    return False
                else:
                    colMap[col].add(board[row][col])
                # square case
                if board[row][col] in squareMap[3*(row//3) + col//3]:
                    return False
                else:
                    squareMap[3*(row//3) + col//3].add(board[row][col])
        return True



    
    
    



    

                