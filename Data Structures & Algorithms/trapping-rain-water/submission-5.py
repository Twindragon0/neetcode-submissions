class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stk = []
        for i in range(len(height)):
            rightWall = height[i]
            while stk and height[stk[-1]] < rightWall:
                floor = height[stk.pop()]
                if stk:
                    res += (i - stk[-1] - 1) * (min(rightWall, height[stk[-1]]) - floor)
            stk.append(i)
        return res
            
