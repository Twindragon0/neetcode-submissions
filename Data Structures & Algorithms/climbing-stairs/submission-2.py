class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = defaultdict(int)
        def recurse(curr):
            if curr in self.memo:
                return self.memo[curr]
            if curr > n:
                return 0
            if curr == n:
                return 1
            self.memo[curr] = recurse(curr+1) + recurse(curr+2)
            return self.memo[curr]
        return recurse(0)