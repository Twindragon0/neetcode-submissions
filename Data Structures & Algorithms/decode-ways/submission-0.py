class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set(str(i) for i in range(1, 27))
        dp = [0] * len(s)
        dp[0] = 1 if s[0] in valid else 0
        for i in range(1, len(s)):
            dp[i] += dp[i-1] if s[i] in valid else 0
            if i == 1:
                dp[i] += 1 if s[i-1:i+1] in valid else 0
            else:
                dp[i] += dp[i-2] if s[i-1:i+1] in valid else 0
        return dp[-1]