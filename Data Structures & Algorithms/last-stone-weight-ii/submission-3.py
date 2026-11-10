class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        self.memo = defaultdict(int)
        def recurse(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            if j >= total / 2:
                return j - (sum(stones) - j)
            if i >= len(stones):
                return float("inf")
            self.memo[(i, j)] = min(recurse(i+1, stones[i] + j), recurse(i+1, j))
            return self.memo[(i, j)]
        return recurse(0, 0)
