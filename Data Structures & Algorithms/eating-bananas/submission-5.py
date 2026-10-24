class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            kCandidate = (left + right) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/kCandidate)
            if totalHours > h:
                left = kCandidate + 1
            elif totalHours <= h:
                res = kCandidate
                right = kCandidate - 1
        return res

        
        

