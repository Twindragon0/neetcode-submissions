class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        def recurse(i, sides):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            else:
                for side in range(4):
                    if sides[side] > sum(matchsticks) // 4:
                        break
                    sides[side] += matchsticks[i]
                    if recurse(i+1, sides):
                        return True
                    sides[side] -= matchsticks[i]
                    if sides[side] == 0:
                        break
                return False
        return recurse(0, [0] * 4)
