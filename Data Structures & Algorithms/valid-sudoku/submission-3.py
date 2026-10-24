class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        squareMap = defaultdict(list)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                # Add to row map
                if board[row][col] in rowMap[row]:
                    return False
                else:
                    rowMap[row].append(board[row][col])
                # Add to col map
                if board[row][col] in colMap[col]:
                    return False
                else:
                    colMap[col].append(board[row][col])
                # Add to square map
                if board[row][col] in squareMap[3*(row//3) + col//3]:
                    print(rowMap)
                    print(colMap)
                    print(squareMap)
                    return False
                else:
                    squareMap[3*(row//3) + col//3].append(board[row][col])
        print(rowMap)
        print(colMap)
        print(squareMap)
        return True
    
    
    



    

                