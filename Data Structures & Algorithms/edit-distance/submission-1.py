class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = defaultdict(int)
        def recurse(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            if i >= len(word1) and j >= len(word2):
                return 0
            elif i >= len(word1) and j < len(word2):
                return len(word2) - j
            elif i < len(word1) and j >= len(word2):
                return len(word1) - i
            elif word1[i] == word2[j]:
                self.memo[(i, j)] = recurse(i+1, j+1)
                return self.memo[(i, j)]
            else:
                self.memo[(i, j)] = min(1 + recurse(i+1, j+1), 1 + recurse(i+1, j), 1 + recurse(i, j+1))
                return self.memo[(i, j)]
        return recurse(0, 0)