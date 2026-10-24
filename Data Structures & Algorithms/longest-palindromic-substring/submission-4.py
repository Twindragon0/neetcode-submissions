class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = ""
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                if j-i+1 <= 3:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                        ans = ans if j-i+1 < len(ans) else s[i:j+1]
        return ans