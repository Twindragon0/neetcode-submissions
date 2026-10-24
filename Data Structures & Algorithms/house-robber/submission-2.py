class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(2)] # 0 -> rob, 1 -> dont rob
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[0][i] = max(dp[1][i-1] + nums[i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1], dp[1][i-1])
        return max(dp[0][-1], dp[1][-1])
