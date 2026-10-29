class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = defaultdict(int)
        def recurse(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if j+1 < len(p) and p[j+1] == '*':
                self.memo[(i, j)] = recurse(i, j+2)
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    self.memo[(i, j)] = self.memo[(i, j)] or recurse(i+1, j)
                return self.memo[(i, j)]
            else:
                if i < len(s) and (p[j] == "." or p[j] == s[i]):
                    self.memo[(i, j)] = recurse(i+1, j+1)
                    return self.memo[(i, j)]
                else:
                    self.memo[(i, j)] = False
                    return False
        return recurse(0, 0)