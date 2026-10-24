class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        dp = defaultdict(int)
        def recurse(i, turn):
            if i >= len(stoneValue):
                return 0
            if (i, turn) in dp:
                return dp[(i, turn)]
            totalVal = 0
            res = float("-inf") if turn == 0 else float("inf")
            for j in range(i, min((i+3), len(stoneValue))):
                totalVal += stoneValue[j]
                if turn == 0:
                    res = max(res, totalVal + recurse(j+1, 1))
                else:
                    res = min(res, recurse(j+1, 0) - totalVal)
            dp[(i, turn)] = res
            return res
        res = recurse(0,0)
        if res < 0:
            return "Bob"
        elif res > 0:
            return "Alice"
        else:
            return "Tie"