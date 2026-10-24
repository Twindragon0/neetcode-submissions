class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxHeight = 0
        for i in range(len(heights)):
            leftShortest = -1
            rightShortest = len(heights)
            left = i-1
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            if left >= 0:
                leftShortest = left
            right = i+1
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            if right < len(heights):
                rightShortest = right
            maxHeight = max(maxHeight, heights[i] * (rightShortest - leftShortest - 1))
        return maxHeight

        



            
