class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        ans = 1
        freqs = defaultdict(int)
        while r < len(s):
            freqs[s[r]] += 1
            maxVal = max(freqs.values())
            sumExceptMax = sum(freqs.values()) - maxVal
            if sumExceptMax <= k:
                ans = max(ans, (r-l+1))
                r += 1
            else:
                freqs[s[l]] -= 1
                freqs[s[r]] -= 1
                l += 1
        return ans