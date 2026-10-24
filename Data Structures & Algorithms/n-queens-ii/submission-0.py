class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def recurse(i, available):
            if i == n:
                self.ans += 1
            else:
                for j in available[i]:
                    trimmed = []
                    # remove verticals
                    for row in range(i+1, n):
                        if j in available[row]:
                            available[row].remove(j)
                            trimmed.append((row, j))
                    # remove diagonals
                    for row in range(i+1, n):
                        diff = row-i
                        if j+diff in available[row]:
                            available[row].remove(j+diff)
                            trimmed.append((row, j+diff))
                        if j-diff in available[row]:
                            available[row].remove(j-diff)
                            trimmed.append((row, j-diff))
                    recurse(i+1, available)
                    for (row, col) in trimmed:
                        available[row].add(col)
        available = [set(el for el in range(n)) for _ in range(n)]
        recurse(0, available)
        return self.ans