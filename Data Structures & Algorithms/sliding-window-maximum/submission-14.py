class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMax = [0] * len(nums)
        rightMax = [0] * len(nums)
        for i in range(0, len(nums), k):
            leftMax[i] = nums[i]
            for j in range(i+1, min(i+k, n)):
                leftMax[j] = max(leftMax[j-1], nums[j])
        
        for i in range(0, len(nums), k):
            end = min(i+k-1, n-1)
            rightMax[end] = nums[end]
            for j in range(end-1, i-1, -1):
                rightMax[j] = max(rightMax[j+1], nums[j])

        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(rightMax[i], leftMax[i+k-1]))
        return ans
        
