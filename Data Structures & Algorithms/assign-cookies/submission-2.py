class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        ans = 0
        j = 0
        i = 0
        while i < len(s):
            if j >= len(g):
                return ans
            if (s[i] >= g[j]):
                ans += 1
                i += 1
                j += 1
            else:
                i += 1
        return ans