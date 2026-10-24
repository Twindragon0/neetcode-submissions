class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        ans = 0
        for i in range(1, len(height)-1):
            ans += max(min(leftMax[i-1], rightMax[i+1]) - height[i], 0)
        return ans



            
