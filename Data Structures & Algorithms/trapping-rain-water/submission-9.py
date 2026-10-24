class Solution:
    def trap(self, height: List[int]) -> int:
        left = 1
        right = len(height) - 2
        leftMax = height[0]
        rightMax = height[-1]
        res = 0
        while left <= right:
            if leftMax <= rightMax:
                res += max(leftMax - height[left], 0)
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                res += max(rightMax - height[right], 0)
                rightMax = max(rightMax, height[right])
                right -= 1
        return res

            
