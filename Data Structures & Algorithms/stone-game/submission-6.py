class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.memo = defaultdict(int)
        def recurse(lo, hi, isAliceTurn):
            if lo == hi:
                return piles[lo] if isAliceTurn else -piles[lo]
            elif (lo, hi, isAliceTurn) in self.memo:
                return self.memo[(lo, hi, isAliceTurn)]
            else:
                if isAliceTurn:
                    self.memo[(lo, hi, isAliceTurn)] = max(piles[lo] + recurse(lo+1, hi, False), piles[hi] + recurse(lo, hi-1, False))
                    return self.memo[(lo, hi, isAliceTurn)]
                else:
                    self.memo[(lo, hi, isAliceTurn)] = min(-piles[lo] + recurse(lo+1, hi, True), -piles[hi] + recurse(lo, hi-1, True))
                    return self.memo[(lo, hi, isAliceTurn)]
        ans = recurse(0, len(piles)-1, True)
        return True if ans > 0 else False
