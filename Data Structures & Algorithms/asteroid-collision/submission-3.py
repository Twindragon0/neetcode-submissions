class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            if a > 0:
                stk.append(a)
            else: # a < 0
                while True:
                    if not stk or stk[-1] < 0:
                        stk.append(a)
                        break
                    elif abs(a) < abs(stk[-1]):
                        break
                    elif abs(a) == abs(stk[-1]):
                        stk.pop()
                        break
                    else: # abs(a) > abs(stk[-1])
                        stk.pop()
        return stk


