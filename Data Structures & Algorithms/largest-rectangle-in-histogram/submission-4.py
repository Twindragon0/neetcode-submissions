class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxHeight = 0
        for i in range(len(heights)):
            left = i-1
            right = i+1
            leftIdx = -1
            rightIdx = len(heights)
            while left >= 0:
                if heights[left] >= heights[i]:
                    left -= 1
                else:
                    leftIdx = left
                    break
            while right < len(heights):
                if heights[right] >= heights[i]:
                    right += 1
                else:
                    rightIdx = right
                    break
            maxHeight = max(maxHeight, heights[i] * ((rightIdx - 1) - (leftIdx + 1) + 1))
        return maxHeight
