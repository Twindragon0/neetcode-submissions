class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        t = sum(nums) // 2
        dp = [[False] * len(nums) for _ in range(t)]
        for i in range(t):
            for j in range(len(nums)-1, -1, -1):
                if j+1 == len(nums):
                    dp[i][j] = True if (i+1)-nums[j] == 0 else False
                elif i-nums[j] >= 0:
                    dp[i][j] = dp[i-nums[j]][j+1] or dp[i][j+1]
                elif i-nums[j] == -1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[-1][0]
