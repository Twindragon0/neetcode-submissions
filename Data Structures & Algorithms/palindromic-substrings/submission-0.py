class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                if j-i+1 <= 3:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    ans += 1
        return ans