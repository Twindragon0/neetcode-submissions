class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.memo = defaultdict(int)
        def recurse(isAliceTurn, i, m):
            if i+2*m-1 >= len(piles) - 1:
                return (sum(piles[i:]), sum(piles[i:])) if isAliceTurn else (-sum(piles[i:]), 0)
            if (isAliceTurn, i, m) in self.memo:
                return self.memo[(isAliceTurn, i, m)]
            if isAliceTurn:
                maxVal = float("-inf")
                maxAlice = 0
                for x in range(1, min(len(piles)-i+1, 2*m + 1)):
                    res, y = recurse(False, i+x, max(m, x))
                    if sum(piles[i:i+x])+res > maxVal:
                        maxVal = sum(piles[i:i+x])+res
                        maxAlice = y+sum(piles[i:i+x])
                self.memo[(isAliceTurn, i, m)] = (maxVal, maxAlice)
                return (maxVal, maxAlice)
            else:
                minVal = float("inf")
                maxAlice = 0
                for x in range(1, min(len(piles)-i+1, 2*m + 1)):
                    res, y = recurse(True, i+x, max(m, x))
                    if -sum(piles[i:i+x])+res < minVal:
                        minVal = -sum(piles[i:i+x])+res
                        maxAlice = y
                self.memo[(isAliceTurn, i, m)] = (minVal, maxAlice)
                return (minVal, maxAlice)
        ans = recurse(True, 0, 1)
        return ans[1]
