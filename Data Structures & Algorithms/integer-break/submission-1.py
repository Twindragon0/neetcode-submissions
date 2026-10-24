class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        for k in range(2, n+1):
            numSecond = n - k * (n // k)
            numFirst = k - numSecond
            curr = 1
            if numFirst:
                curr *= (n // k) ** numFirst
            if numSecond:
                curr *= (n // k + 1) ** numSecond
            ans = max(ans, curr)
        return ans
