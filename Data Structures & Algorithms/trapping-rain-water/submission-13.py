class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            rightWall = height[i]
            while stk and rightWall > height[stk[-1]]:
                floor = height[stk.pop()]
                if stk:
                    leftWall = height[stk[-1]]
                    res += max((i - stk[-1]-1) * (min(leftWall, rightWall) - floor), 0)
            stk.append(i)
        return res



            
