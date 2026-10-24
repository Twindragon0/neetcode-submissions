class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = []
        maxHeight = 0
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                height = heights[stk.pop()]
                leftBoundary = -1 if not stk else stk[-1]
                maxHeight = max(maxHeight, height * (i - leftBoundary - 1))
            stk.append(i)
        return maxHeight

        

        



            
