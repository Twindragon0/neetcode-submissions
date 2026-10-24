class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height)-1]
        left = 1
        right = len(height) - 2
        ans = 0
        while left <= right:
            if leftMax <= rightMax:
                ans += max(leftMax - height[left],0)
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                ans += max(rightMax - height[right],0)
                rightMax = max(rightMax, height[right])
                right -= 1
        return ans

