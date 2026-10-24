class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        
        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = max(height[i], maxLeft[i-1])
        
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(height[i], maxRight[i+1])

        ans = 0
        for i in range(1, len(height)-1):
            val = min(maxLeft[i-1], maxRight[i+1])
            if val > height[i]:
                ans += val - height[i]
        return ans 
