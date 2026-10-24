class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = defaultdict(int)
        def recurse(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            if i > amount:
                return 0
            if i == amount:
                return 1
            numWays = 0
            for newJ in range(j, len(coins)):
                numWays += recurse(i+coins[newJ], newJ)
            self.memo[(i, j)] = numWays
            return numWays 
        return recurse(0, 0)

