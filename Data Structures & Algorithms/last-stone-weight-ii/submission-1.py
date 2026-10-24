class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.total = sum(stones) // 2
        self.memo = defaultdict(int)
        def recurse(i, curr):
            if (i, curr) in self.memo:
                return self.memo[(i, curr)]
            if curr >= self.total or i >= len(stones):
                return abs(curr - (sum(stones) - curr))
            self.memo[(i, curr)] = min(recurse(i+1, curr), recurse(i+1, curr + stones[i]))
            return self.memo[(i, curr)]
        return recurse(0, 0)
