class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def recurse(i, available, curr):
            if i == n:
                self.ans.append(["".join(el) for el in curr])
            else:
                for j in available[i]:
                    curr[i][j] = 'Q'
                    # trim the vertical, diags
                    trimmed = []
                    for row in range(i+1, n):
                        if j in available[row]:
                            available[row].remove(j)
                            trimmed.append((row, j))
                    for row in range(i+1, n):
                        toAdd = row-i
                        if j+toAdd in available[row]:
                            available[row].remove(j+toAdd)
                            trimmed.append((row, j+toAdd))
                        if j-toAdd in available[row]:
                            available[row].remove(j-toAdd)
                            trimmed.append((row, j-toAdd))
                    recurse(i+1, available, curr)
                    for (row, col) in trimmed:
                        available[row].add(col)
                    curr[i][j] = '.'
        
        curr = [['.' for _ in range(n)] for _ in range(n)]
        available = [set(el for el in range(n)) for _ in range(n)]
        recurse(0, available, curr)
        return self.ans
