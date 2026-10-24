class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftIndices = [-1] * len(heights)
        rightIndices = [len(heights)] * len(heights)

        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                leftIndices[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(len(heights)-1,-1,-1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                rightIndices[i] = stk[-1]
            stk.append(i)
        
        maxHeight = 0
        for i in range(len(leftIndices)):
            maxHeight = max(maxHeight, heights[i] * (rightIndices[i]-leftIndices[i]-1))
        return maxHeight

        

        



            
