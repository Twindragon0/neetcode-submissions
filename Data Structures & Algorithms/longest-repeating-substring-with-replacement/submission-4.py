class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freqs = defaultdict(int)
        ans = 0
        maxVal = 0
        while r < len(s):
            freqs[s[r]] += 1
            if (r-l+1) - max(freqs[s[r]], maxVal) <= k:
                maxVal = max(freqs[s[r]], maxVal)
                ans = max(ans, r-l+1)
                r += 1
            else:
                freqs[s[l]] -= 1
                freqs[s[r]] -= 1
                l += 1
        return ans   