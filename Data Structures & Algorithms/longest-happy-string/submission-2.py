class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def recurse(max1, max2, max3, char1, char2, char3, use1, use2, use3):
            if max2 > max1:
                return recurse(max2, max1, max3, char2, char1, char3, use2, use1, use3)
            if max3 > max2:
                return recurse(max1, max3, max2, char1, char3, char2, use1, use3, use2)
            if max2 == 0:
                return min(2, max1) * char1
            if use1 != 2:
                return char1 + recurse(max1-1, max2, max3, char1, char2, char3, use1+1, 0, 0)
            if use2 != 2:
                return char2 + recurse(max1, max2-1, max3, char1, char2, char3, 0, use2+1, 0)
            return char3 + recurse(max1, max2, max3-1, char1, char2, char3, 0, 0, use3+1)
        return recurse(a, b, c, 'a', 'b', 'c', 0, 0, 0)
