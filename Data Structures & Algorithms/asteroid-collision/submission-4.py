class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        toWrite = 0
        for a in asteroids:
            if a > 0:
                asteroids[toWrite] = a
                toWrite += 1
            else: # a < 0
                while True:
                    if toWrite == 0 or asteroids[toWrite-1] < 0:
                        asteroids[toWrite] = a
                        toWrite += 1
                        break
                    elif abs(a) < abs(asteroids[toWrite-1]):
                        break
                    elif abs(a) == abs(asteroids[toWrite-1]):
                        toWrite -= 1
                        break
                    else: # abs(a) > abs(stk[-1])
                        toWrite -= 1
        return asteroids[:toWrite]


