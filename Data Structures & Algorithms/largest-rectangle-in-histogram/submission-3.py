class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stk = []
        maxHeight = 0
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                height = heights[stk.pop()]
                width = i if not stk else (i-stk[-1]-1)
                maxHeight = max(maxHeight, height * width)
            stk.append(i)
        return maxHeight
