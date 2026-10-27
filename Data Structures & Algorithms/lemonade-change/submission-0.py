class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x, y, z, = 0, 0, 0
        for bill in bills:
            if bill == 5:
                x += 1
            elif bill == 10 and x >= 1:
                y += 1
                x -= 1
            elif bill == 20 and ((y >= 1 and x >= 1) or (x >= 3)):
                z += 1
                if y >= 1 and x >= 1:
                    y -= 1
                    x -= 1
                else:
                    x -= 3
            else:   
                return False
        return True