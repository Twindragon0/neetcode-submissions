class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            while stk and height[i] > height[stk[-1]]:
                bottom = stk.pop()
                if stk:
                    left = stk[-1]
                    res += (i - left - 1) * (min(height[i], height[left]) - height[bottom])
            stk.append(i)
        return res

