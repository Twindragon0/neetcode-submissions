class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in range(2)] # top=dont have, bottom=have
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i])
        return max(dp[0][len(prices)-1], dp[1][len(prices)-1])

