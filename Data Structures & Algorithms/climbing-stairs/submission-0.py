class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        numWays = [0] * (n+1)
        numWays[1] = 1
        numWays[2] = 1
        for i in range(n+1):
            if i == n:
                return numWays[i]
            if i+1 < n+1:
                numWays[i+1] += numWays[i]
            if i+2 < n+1:
                numWays[i+2] += numWays[i]
        