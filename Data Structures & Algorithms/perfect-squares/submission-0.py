class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        currSquares = [1]
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            if i == (currSquares[-1]+1)**2:
                dp[i] = 1
                currSquares.append(currSquares[-1]+1)
            else:
                for num in currSquares:
                    dp[i] = min(dp[i], dp[i-num**2]+1)
        return dp[-1]