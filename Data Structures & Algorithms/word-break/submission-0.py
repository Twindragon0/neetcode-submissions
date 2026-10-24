class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                dp[i] = dp[i] or (s[:i+1].endswith(word) and (dp[i-len(word)] if i-len(word) >= 0 else True))
        return dp[-1]