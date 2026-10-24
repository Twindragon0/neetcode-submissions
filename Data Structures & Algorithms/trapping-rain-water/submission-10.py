class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            rightWall = height[i]
            while stk and rightWall > height[stk[-1]]:
                floor = height[stk.pop()]
                if stk:
                    res += (i - stk[-1] - 1) * (min(height[stk[-1]], rightWall) - floor)
            stk.append(i)
        return res

            
