class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def populate(pos, unavailable):
            x, y = pos
            added = set()
            # right
            for col in range(y, n):
                if (x, col) not in unavailable:
                    added.add((x, col))
            # down
            for row in range(x, n):
                if (row, y) not in unavailable:
                    added.add((row, y))
            # left diag
            for i in range(n):
                row, col = x+i, y+i
                if row >= n or col >= n:
                    break
                if (row, col) not in unavailable:
                    added.add((row, col))
            # right diag
            for i in range(n):
                row, col = x+i, y-i
                if row >= n or col < 0:
                    break
                if (row, col) not in unavailable:
                    added.add((row, col))
            return added
        def recurse(i, curr, unavailable):
            if i >= n:
                self.ans.append(curr.copy())
            else:
                for j in range(n):
                    if (i, j) in unavailable:
                        continue
                    toAdd = populate((i, j), unavailable)
                    unavailable.update(toAdd)
                    newStr = ['.'] * n
                    newStr[j] = 'Q'
                    curr.append("".join(newStr))
                    recurse(i+1, curr, unavailable)
                    curr.pop(-1)
                    unavailable -= toAdd
            
        recurse(0, [], set())
        return self.ans
