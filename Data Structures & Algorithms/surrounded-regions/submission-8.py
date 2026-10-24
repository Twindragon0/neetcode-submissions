class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        for i in range(1, len(board)-1):
            for j in range(1, len(board[i])-1):
                if (i, j) not in visited and board[i][j] == "O":
                    isValid = True
                    curr = []
                    queue = deque()
                    visited.add((i, j))
                    queue.append((i, j))
                    while queue:
                        row, col = queue.popleft()
                        if (row-1 == 0 and board[row-1][col] == "O") or (row+1 == len(board)-1 and board[row+1][col] == "O") or (col-1 == 0 and board[row][col-1] == "O") or (col+1 == len(board[row])-1 and board[row][col+1] == "O"):
                            isValid = False
                        curr.append((row, col))
                        if row-1 > 0 and (row-1, col) not in visited and board[row-1][col] == "O":
                            visited.add((row-1, col))
                            queue.append((row-1, col))
                        if row+1 < len(board) - 1 and (row+1, col) not in visited and board[row+1][col] == "O":
                            visited.add((row+1, col))
                            queue.append((row+1, col))
                        if col-1 > 0 and (row, col-1) not in visited and board[row][col-1] == "O":
                            visited.add((row, col-1))
                            queue.append((row, col-1))
                        if col+1 < len(board[0]) - 1 and (row, col+1) not in visited and board[row][col+1] == "O":
                            visited.add((row, col+1))
                            queue.append((row, col+1))
                    if isValid:
                        for (r, c) in curr:
                            board[r][c] = "X"
                            



                        