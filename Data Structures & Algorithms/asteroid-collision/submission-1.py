class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        toWrite = 0
        for a in asteroids:
            if a > 0 or toWrite == 0:
                asteroids[toWrite] = a
                toWrite += 1
            else: # a < 0
                while True:
                    if toWrite == 0 or asteroids[toWrite - 1] < 0:
                        asteroids[toWrite] = a
                        toWrite += 1
                        break
                    elif abs(asteroids[toWrite - 1]) > abs(a):
                        break
                    elif abs(asteroids[toWrite - 1] == abs(a)):
                        toWrite -= 1
                        break
                    else:
                        toWrite -= 1
        return asteroids[:toWrite]            
