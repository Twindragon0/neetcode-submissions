class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * amount
        for target in range(1, amount+1):
            for coin in coins:
                if target-coin == 0:
                    dp[target-1] = 1
                elif target-coin > 0:
                    dp[target-1] = min(dp[target-1], dp[target-coin-1]+1)
        if not dp:
            return 0
        elif dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]