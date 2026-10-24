class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf")] * (len(cost)+1)
        dp[0], dp[1] = 0, 0
        for i in range(len(cost)):
            dp[i+1] = min(dp[i+1], dp[i] + cost[i])
            if i != len(cost)-1:
                dp[i+2] = min(dp[i+2], dp[i] + cost[i])
        return dp[-1]