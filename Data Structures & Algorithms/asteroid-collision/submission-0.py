class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            if asteroid > 0:
                stk.append(asteroid)
            else:
                while True:
                    if not stk or stk[-1] < 0:
                        stk.append(asteroid)
                        break
                    elif abs(stk[-1]) > abs(asteroid):
                        break
                    elif abs(stk[-1]) < abs(asteroid):
                        stk.pop()
                    else:
                        stk.pop()
                        break                
        return stk