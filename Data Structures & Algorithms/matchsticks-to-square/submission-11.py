class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.ans = False
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        def recurse(i, sides):
            if i == len(matchsticks):
                self.ans = True if sides[0] == sides[1] == sides[2] == sides[3] else self.ans
            else:
                for side in range(4):
                    if sides[side] > (sum(matchsticks) // 4):
                        break
                    sides[side] += matchsticks[i]
                    recurse(i+1, sides)
                    sides[side] -= matchsticks[i]
                    if sides[side] == 0:
                        break
        recurse(0, sides)
        return self.ans
