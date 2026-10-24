class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt(x) = 2 * sqrt(x/4) = 2 * (x * 2^-2)^1/2
        def recurse(x):
            if x < 2:
                return x
            l = 2 * recurse(x // 4)
            r = l + 1
            return l if r*r > x else r
        return recurse(x)

