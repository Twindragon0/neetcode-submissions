class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.memo = defaultdict(int)
        def recurse(i, curr):
            if i >= len(s):
                return 1 if curr == t else 0
            elif (i, curr) in self.memo:
                return self.memo[(i, curr)]
            else:
                self.memo[(i, curr)] = recurse(i+1, curr + s[i]) + recurse(i+1, curr)
                return self.memo[(i, curr)]
        return recurse(0, "")