class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftHeights = []
        rightHeights = []
        stk = []
        for i, height in enumerate(heights):
            while stk and stk[-1][0] >= height:
                stk.pop()
            if stk:
                leftHeights.append(stk[-1][1])
            else:
                leftHeights.append(-1)
            stk.append([height, i])
        stk = []
        for i in range(len(heights)-1, -1, -1):
            while stk and stk[-1][0] >= heights[i]:
                stk.pop()
            if stk:
                rightHeights.insert(0, stk[-1][1])
            else:
                rightHeights.insert(0, len(heights))
            stk.append([heights[i], i])
        maxHeight = 0
        for i in range(len(heights)):
            maxHeight = max(maxHeight, heights[i]*((rightHeights[i]-1)-(leftHeights[i]+1)+1))
        return maxHeight